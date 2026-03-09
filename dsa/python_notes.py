"""
A systematical understanding on python file execution.
Starting CPython with Python /users/me/myfile.py
Preparation and compilation
01. OS starts Python interpreter process
02. main in CPython is called with argv[0] = "python" and argv[1] = "/users/me/myfile.py"
03. CPython initializes the Python runtime:
    a. Memory & runtime core
        - object allocator
        - garbage collector
        - reference counting
        - internal singletons (None, True, False, NotImplemented, Ellipsis)
    b. Built-in types: int, float, str, list, dict, set, tuple, type, object, Exception, etc.
    c. the built-in module: built-in functions (print, len, range, etc.) and exceptions.
04. create and populate the sys module, e.g. sys.argv, sys.path, sys.modules, etc.
    sys.path contains the script path (/users/me), stdlib locations, and site-packages.
05. import site module (unless python -S)
    adds site-packages, loads .pth files, and performs other site-specific initialization.
06. create the __main__ module object, with __name__ = "__main__", and set it as the current module.
    Modules have a global namespace __dict__ and name. The module object is added to 
    sys.modules["__main__"].
07. read the source file /users/me/myfile.py, compile it into a code object (in bytecode (.pyc), and
    execute it in __main__ globals
Note: Compilation of functions can be tricky here. It first scans the function body for binding operations, 
    e.g. x = 20, import x, or for x in ... and then mark these names as local (later retrieved by loadfast).
    Then it scans for free varibles, and mark them as enclosing (later retrived by loadderef). Variables 
    with the same name follows LEGB rule, smaller scope shadows larger ones. 
Note: How Python finds source file
    Python loads the entry script by the path to the file, sets it as the entry module and names it __main__.
    The __package__ in of the main module is None. Other scripts are imported by packages and file name, e.g.
    import my_package.my_script. Import support relative lookup, namely . .. and ... Relative lookup needs
    __package__ for look up, as a result it doesn't work in the main module (__package__ being None)
Note: How a child process is spawn(Windows) or forked(Linux/MacOS)
    1. Start a new Python interpreter process that reloads the same Python file, rename the __name__ global
    to "__mp_main__", to prevent code under "if __name__ == '__main__'" from being executed in the child
    process.
    2. The target function are then pickled and sent to the child process, which will be the entry point of
    the child process. 
Execution
08. Prior to executing bytecode, Python creates a Frame Object for the main module, which provides the 
    execution context. The frame object includes the evaluaion stack, the instruction pointer, and reference 
    to Locals, Globals, and Built-ins dictionaries. Evaluation stack holds 1) intermediate results, 
    2) function arguments, 3) return values and 4) Loop/Exception State. Python creates a new frame for
    every scoped block, namely modules, class bodies, and functions before executing their bytecode
    Frames are kept in the call stack with which python controls the flow of execution. A frame
    is popped from the call stack after execution.
    Use inspect.currentframe().f_locals check the internals in a frame object. 
09. The outcome of execution of a class definition is a class object hold all names defined in it in its 
    __dict__, and outcome of a function definition execution is a function object. Different from class
    object, function objects hold a reference to globals besides those defined in it.

Creation of class object
10. All classes are instances of the type 'type', which is the default metaclass. Metaclass decides how a 
    class is created. E.g. if type is the metaclass, python calls type("classname", bases, namespace) to 
    create it. Metaclasses can also be a subclass of type, which implements 
    __prepare__, __new__ and __init__ to create the class object. 
    1. calls __prepare__(mcls, name, bases, **kw): -> {} to create the temp namespace (__dict__)
    2. execute free statements (not in methods) in the class body and collect class level variables, functions,
        child classes, etc. in __dict__
    3. calls __new__(mcls, name, bases, ns, **kw): -> cls to create the class object, setting important 
        class attributes such as __bases__, __mro__, __name__, __qualname__, __slots__, 
        __classcell__, and __module__. It also makes __dict__ a readonly view of the class dictionary 
        (the mapping proxy), so that the class can't be modified by directly modifying __dict__. Always 
        update class / instance with a bound name, e.g. instance.attribute = "new value"
    4. calls __init__(cls, name, bases, ns, **kw): -> cls to initialize the class object
Note: Inheritance related varibles such as __bases__, __mro__, __base__ are set by __new__ in the metaclass.
    __bases__ keep immediate base class only. MRO search starts with __bases__ of the calling class / instance
    all the way up the inheritance hierachy using C3 linearization.
Instantiation
    1. calls __call__(cls, *args, **kwargs): in the metaclass, in which in turn calls:
        on the class:
            a. __new__(cls, *a, **k): -> instance obj to create the instance obj
            b. __init__(self): -> instance obj to initilize the instance obj
Callable instance
    Class that implements dunder __call__ are callable class. __call__ is called when an class instance is
    directly invoked by instance()
Creation of function object
    Upon reading "def" Python calls the opcode MAKE_FUNCTION/types.FunctionType taking the compiled Code 
    Object of the function and the current environment to create the function object, which includes
        __code__: compiled function code (the instructions)
        __globals__: the refernece to module's global dict
        __closure__: the tuple holding references to the cell ojects that wrap the free variable (varibles
                    defined in outer functions but accessed by inner functions)
        __defaults__: the tuple holding default value of parametres
    The function objects for standalone functions and functions inside a class are literally the same during 
    construction.
Reference:
    Stage	            Internal Function (C-API)	Signature (Conceptual)
    Compilation         compile                     (source, filename, mode) -> code (bytecode object)
    Code Creation	    PyCode_New()	            (argcount, posonlyargcount, kwonlyargcount, nlocals, 
                                                    stacksize, flags, code, consts(literal values), names, 
                                                    varnames, filename, name, qualname, firstlineno, lnotab)
                                                    -> code object
    Function Creation	PyFunction_New()	        (code_object, globals_dict) -> function object
Note:
    Source code strings can also be compiled to bytecode on-the-fly by compile() or types.CodeType
Comparing default attributes of class objects and function objects
    Attribute	FO	CO	Purpose
    __globals__	Yes	No	Pointer to the module's __dict__. Functions need this for LOAD_GLOBAL.
    __dict__	Yes	Yes	Stores custom attributes assigned to the object.
    __module__	Yes Yes	A string name used for introspection and pickling.
    __name__	Yes	Yes	The name given in the definition (e.g., "my_func").
    __qualname__Yes	Yes	The "path" to the object (e.g., "MyClass.my_method").
    __closure__	Yes	No	Tuple of cells for non-local variables (if applicable).
    __code__	Yes	No	The compiled bytecode instructions.
    __mro__	    No	Yes	The Method Resolution Order (tuple of parent classes).
    __bases__	No	Yes	Tuple of immediate parent classes.
    __weakref__	Yes	Yes	
Note:
    The easily notable difference made by function objects is the possession of __globals__, __closure__. 
    When constructing the frame objects at function invocation, python puts the __glabal__ that the funtion
    object holds in itself in the frame object. This gives function object the freedom to be executed in 
    different context. Name resolution within functions is also screened at compilation depending on how a
    name is referenced, which results in different load op code to speed up look up. For an unbound name, 
    compiler generates LOAD_FAST if one assigned in the function body, LOAD_DEREF if declared nonlocal, or
    LOAD_GLOBAL if declare global. In a class body, accessing a name is always bound and mostly retrieved
    by LOAD_NAME. Search order is class namespace -> globals -> builtins. 

Ways to customize the execution context of a function object
    types.FunctionType(code, globals, name=None, argdefs=None, closure=None)
        from types import FunctionType
        # 1. Compile source code into a code object
        code_obj = compile("def f(x): return x + 1", "<string>", "exec")
        # 2. Extract the actual function's code object from constants
        func_code = code_obj.co_consts[0] 
        # 3. Create the function object manually
        my_dynamic_func = FunctionType(func_code, globals(), "my_dynamic_func") #customize global
        my_dynamic_func = FunctionType(..., argdefs=...) #customize default arguments
        my_dynamic_func = FunctionType(..., closure=...) #customize closure
    Functions that are bound with an instance become methods, which is accessed in the dotted form, 
    e.g. instance.method. 
    Binding can be customized as shown below. 
        import types

        def greet(self):
            return f"Hello, I am {self.name}"

        class Person:
            def __init__(self, name):
                self.name = name

        p = Person("Alice")
        # Manually bind the standalone function to the instance 'p'
        p.say_hello = types.MethodType(greet, p) # this puts greet in the dict of instance p
        print(p.say_hello())  # as the method is bound to p, no need to passing p to say_hello here

Instance Method Involcation (Dot access) - (Name resolution & invocation):
    p = Person()
    p.name()
    1.  p.__getattribute__("name"): This is called first. It orchestrates the following logic:
    2.  Check Class Hierarchy for Data Descriptors: 
        Python looks in Person and its bases for a name attribute that has both __get__ and __set__ 
        (e.g., a @property).
        If found: Call Person.name.__get__(p, Person) and return immediately. Otherwise,
    3.  Check Instance Dictionary: Look in p.__dict__['name'].
        If found: Return the value. (Note: This is why instance data "shadows" normal methods/non-data 
        descriptors). Otherwise, 
    4.  Check Class Hierarchy for Non-Data Descriptors / Values: Look in Person and its bases for name.
        If found:
            If it has __get__ (non-data descriptor: function/method, staticmethod, or classmethod), call 
            Person.name.__get__(p, Person).
            If it has no __get__ (a simple class variable), return it as-is.
    5.  p.__getattr__("name"): If steps 2, 3, and 4 all fail, Python calls this as a last resort. 
        If this isn't defined or raises an error, AttributeError is thrown.
    6.  Binding logic is inside __get__: 
        Note that @staticmethod and @classmethod are descriptor decorators and implement different 
        binding beheaviour in their __get__
            function.__get__ returns a bound method (links to p).
            classmethod.__get__ returns a bound method (links to Person).
            staticmethod.__get__ returns the underlying function (no binding).
    7.  Upto this point name resolution and binding is done, then it comes execution invoked by the 
        paranthesis operator (), which calls __call__ on the function object obtained in the previous
        steps, in which calls tp_call / vector_call. From this point python builds the frame object, push
        the frame in the call stack, and execute the method code in the frame. Pop the frame after 
        execution. 

Other specifics
Equality vs Identical
Equality is tested based on value, implemented by __eq__. Identity is esentially based on memory address. 

Hashable
    Hashable is the key property that decides whether one can be put in dictionary keys or sets. Sets 
    internally are hash tables. __hash__ and __eq__ are the default dunder methods for all objects. 
    However, for those who overwrite __eq__, python will set __hass__ to None, making it unable to 
    be hash keys or set elements. All collection classes rewrite __eq__ and hence non-hashable, 
    such as list, dict, set, etc. Custom classes are hashable by default, unless one's __eq__ is 
    rewritten. The default __eq__ actually checks identity. In python hash tables, __eq__ is user 
    to test whether same hash is a result of hash collision or same / equal elements.


Asyncio, multithreading, multiprocessing:
    Asincio implements a event loop inside the main thread to mimic multitasking and depends entirely 
    on the developers to coordinate execution among tasks, no time-slicing, no preemption. Asyncid 
    allows to send a task to a real OS thread via 
    run_in_executor() (asyncio.get_running_loop().run_in_executor()).
    Key points about Asyncio: await, asyncio.create_task()(run task immediately), await asyncio.gather(), 
    asyncio.TaskGroup() (tasks run immediately, calling thread awaits behind the scene (being blocked)), 
    asyncio.future (similar with yield in some sense, but code after future.set_result(v) is effectively
    discarded), asynio.lock(), asyncio.semaphore, asyncio.event, and asyncio.condition

Multithreading creates real OS level threads that are all guarded by GIL (CPU mutex), allowing only one
thread to execute at any given time. OS coordinates sharing CPU time among threads.
Multiprocessing spawn/fork interpreter processes at the OS level, which harnesses true parallelism of 
multiprocessor systems. Python parallelism via multiprocessing is costier than those languages support
real parallel multithreading such as Java. Note that each new process will re-enter the module where it
is launched with a new name (usually __mp_main__), without protection of if __name__ == "__main__", the
launching code will be re-executed and the application will crash. 

Decorators

    def my_modifier(func):
        def wrapper(*args, **kwargs):
            # things to do before calling func
            ...
            result = func(args, **kwargs)
            # things to do after calling func
            ...
            return result

    @my_modifier
    def my_func(p1, p2):
        ...

    # calling
    my_func(1, 2)

    def my_modifier(n):
    def my_modifier_inner(func):
        def wrapper():
            # things to do before calling func
            ...
            result = func(args, **kwargs)
            # things to do after calling func
            ...
            return result
        return wrapper
    return my_modifier_inner

    @my_modifier(1)
    def my_func():
    return "Hello Linus"

Note: Decorators can be chained, executing from the one immediately above the function being decorated 
upwards

Some popular decorators:

@staticmethod, @classmethod

@dataclass:
    automatically adds __init__, __repr__, and __eq__
    it doesn't allow class properties with mutable default value (ValueError) 
    Solution field(default_factory=contructor of the field)
    id_list: list = field(default_factory=list) instead of id_list: list = []

exec / eval
    global, local = {"__builtins__":{}}, {}
    exec(code, global, local)
    Python executes the code like calling a function - it builds a frame for it, passing the global 
    and local to the frame, and then put the frame in the call stack. if global and local parameters
    are omitted, the result of globals() and locals() in the current execution context are passed to
    the frame. As per the function signiture enclosing access is not supported. Developers can utilize
    the global and local parameter to customize the execution context for exec, limiting it access to
    certain builtins and variables. e.g. setting global to {"__builtins__":{}} to prevent the exec 
    from accessing the builtin function. Exec adds its only local vars to local, which is accessible 
    after exec. Please note the python __builtins__ is always sent to exec, even if we pass a empty 
    global to it. We have to explicitly set {"__builtins__":{}} in the parameter global to remove
    builtins.
    eval: single line, return the result of evaluation
    exec: multiline, doesn't return

Context manager (with callable that returns a resource obj[ as obj_name]: )
    __enter__(self) -> [resource handle], returns the resource handle
    __exit__(self, exc_type, exc_val, exc_tb) -> bool, called on exit or occurance of exceptions, 
    giving developer the chance to clean up (close resource handle) or handles exceptions in 
    __exit__. Those exc_* parameters capture exceptions information should any be raised in the
    code block inside the "with as". __exit__ returns True to indicates normal exit, False indicates
    exit with error and propagate exc parameters.

Iterable, Iterator and Generator
    Iterable has Iterator has Generator
    Iterable: __iter__
    Iterator: __iter__ and __next__, raises StopIteration
    Generator: __iter__ and __next__, raises StopIteration, and supports send(), throw():caller calls
    gen.throw(Exception) to cause the gen to raise the exception passed in for handling (except) and/or
    clean up (finally) inside gen. If handle, gen is able to continue yielding, and close():similar 
    with throw, only that it raises the dictated GeneratorExit exception and put the gen in an exhausted
    state.
    Generators are usually created by yield, or comprehension in (), e.g. (n for n in range(4))

Important modules:

pprint.pprint()

pickle:
    pickle.dump(obj:object, f:File) -> None
    pickle.load(f:File) -> python_object

Itertools:
    itertools.count(start, step), itertools.cycle(lst:list), itertools.combinations(i:iterable, n:int) 
    # n: number of the elements in each combination tuple
    itertools.chain(*iterables) -> itertools.chain # an iterable

functools:
- @singledispatch: basically breaks down case switch into individual functions. Note these functions
    only takes type for registration.
@functools.singledispatch
    def handle_error(error):
        raise NotImplemented(f"Can't handle this error {error}")
    @handle_error.register(TypeError)
    def _(error):
        print(f"handling TypeError: {error}")
    @handle_error.register(ValueError)
    def _(error):
        print(f"handling ValueError: {error}")

    handle_error(TypeError("wrong type"))

- @singledispatchmethod: similar with partialmethod, this works with class method.

- @total_ordering: enabling classes that have __eq__ and __lt__ to do >, >=, <=

- caching: keep items being cached in dict, hence requiring hashable, @lru_catch, @catch, 
@cached_property
    @lru_cache(maxsize=128, typed=False) # maxsize: the size of cache. typed: if typed == True, 
    items of different types are cached separately and both type and value are tested for 
    cache hitting. 
        @lru_cache
        def my_func(*args) -> any
        managing cache by:
        my_func.cache_info()
        my_func.cache_parameters()
        my_func.cache_clear() 
    @cache # alias to @lru_cache(None), set maxsize to unlimited
    @cached_property # wraps a method in a non-data descriptor, and puts the result in the instanse's
    __dict__ on its first invocation. 
    @cached_property
    def costy_calculation(self):
        return costy_result
    Note: developers need to figure out the way to invalidate the stale value of cached_property
    in the instanse's __dict__. One good way is to decorate all attributes with @property that 
    the cached_property depends on, and invalidate the cache_property e.g. 
    del self.__dict__[cached_property] in the setter and deleter of those depending attributes.
- partial, partialmethod, reduce
    partial creates a shortcut for a function with the parameter being assigned to a value
        def func(param:int):
            ...
        pf5 = partial(func, 5)
        pf5()
    partialmethod creates a shortcup for a class method
        class my_class:
            def method(self, param:int):
            ...
            pm5 = partialmethod(method, 5)
        mc = my_class()
        mc.pm5()
- reduce(f:function, i:iterable[, initializer])->the type f returns 
Note: f can only take two parameters, and each iteration i feeds f two consequtive items from the start
to the end. If initilizer is present, it is fed into f followed by the first element in i, and then
process repeats with result of 1st iteration and 2nd item, ... till the end.
- partial with reduce, magic
factorial = functools.partial(functools.reduce, lambda x, y:x*y)
print(factorial(range(1,30)))

collectons:
- namedtuple:
    Book = namedtuple("book", ["title", "author", "year"])
    bnw = Book("Brave New World", "Aldous Huxley", 1931)
    both bnw[1] and bnw.author work
    bnw_dict = bnw._asdict()
- deque: pop and append from both end quickly (though in big O pop/append from the head still O(n) for 
large deque)
    dq = deque(iterable[, maxlen])
    dq.append(1), dq.appendleft(1), dq.pop(1), dq.popleft(1)
- Counter(i:iterable|mapping|keyword args) -> Counter: count the repetition of each element and pair 
the items and their number of repetition repetition as key:value in the dictionary, from the most 
repeated to the least. Counter objects have a dict interface without raising KeyError (returns
0 on non-exist key). Counter([1,2,3,3,2])|Counter(a=2,b=3)|Counter({"a":2,"b":3})
    Counter().elements() -> iterable: returns a new iterable in which it resequences the original
    by the number of repetition [1, 3, 2, 3, 2] -> [1, 3, 3, 2, 2]
    Trick:
    list(collections.Counter(x=5).elements()) -> ["x", "x", "x", "x", "x"]
    Connter().most_common(3) -> list of tuples of the top 3 repeated items in the Counter object
    Counter().total() -> int: Counter(a=2,b=3).total() -> 5
OrderedDict(i:iterable): ordering is builtin for python after 3.7, but OrderDict can keep a tuple in
top:
    OrderedDict(i).move_to_end("item 3", last=False)
- ChainMap(d1, d2)->ChainMap: very confusing indeed, {**d1, **d2} is far clearer
    ChainMap object manages references to d1 and d2. In key search, it searchs from left to right, so
    d1 shadows d2. Assignment/deletion are always made to d1, even when the wanted key is in d2 only. 
    Updates are actually made to the original dicts.
- UserDict, UserList, UserString: wrapper class of those types, keeping a type instance in its class
attribute: data. Developers can customise beheaviors to these type by modifying the dunder methods.

- defaultdict(default_factory) -> collections.defaultdict
    Trick:
    def infinite_dict()
        return defaultdict(infinite_dict)
    id = defaultdict(default_factory=infinite_dict)

- inspect: check the stack of frame objects

Builtins:
@property # wraps the getter, setter, and deletor methods in a data discriptor object, and present
function invocation as property accesses. 
@property
def balance(self):
    return self._balance
@balance.setter
def balance(self, v):
    self._balance = v
@balance.deleter
def balance(self):
    self._balance = 0

any(i:iterable) -> bool # common parameters list or comprehension e.g. any([1, 2, 3]), 
any(n for n in range(2)), or any(n % 2 == 0 for n in range(19))
all(iterable) -> bool

enumerate(i:iterable, start:int=1) -> index:int, next(i):any

timeit:
timeit.timeit(code:str|code:function, repeat_times:int) -> seconds:float

Common Errors caught in the phase of execution:
Phase 1: Compilation (Pre-Stack). 
Lexical Analysis & Parsing ->abstract syntax tree & bytecode .pyc:
- SyntaxError: wrong syntax
- IndentationError: wrong indentation
Phase 2: Module/Class Frame Execution -> creates the main frame __main__, and subsequently
frames for executing imported modules, class definition, code passed to exec/eval. No frames
created for functions here yet - objects are created for each function instead
- ImportError: During importing modules, trying to import a non-exist module
- NameError: During accessing thru name, trying to access a global name not defined
Phase 3: Function Frame Creation (The Handshake). Python creates a frame for each function
at call time (function invocation). All frames in phase 2 and 3 are managed by the call stack
- TypeError: function parameter mismatch between definition and invocation
Phase 4: Active Frame Evaluation (Runtime Execution)
- AttributeError: During dot access, instance/class.non-exist_attributes
- IndexError: During accessing thru index, trying to access index not in range
- KeyError: During accessing thru key, trying to access a non-exist key
- NotImplementedError: Use to prevent abstract methods being called
- StopIteration: During iterating a iterator/generator, trying to call next on an exhausted one
- ValueError / TypeError: int("10") vs int("ten") or int([1]), 5 + "5"
- UnboundLocalError: read before assignment to local var
"""
