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
Function/method invocation
    Step	Action	                Logic / C-Signature
    Start	Access p.name	        p.__getattribute__('name')
    Check 1	Data Descriptor?	    Checks if Person.name has __set__ (e.g., a @property). If yes, call 
                                    its __get__.
    Check 2	Instance Dict?	        Checks p.__dict__['name']. If found, return it.
    Check 3	Non-Data Descriptor?	Checks Person.__dict__['name']. If it's a function, call 
                                    func.__get__(p, Person).
    Check 4	Class Dict?	            If no __get__, return the raw value from Person.__dict__.
    Fail	Not found?	            Call p.__getattr__('name'). Fail raises exception
            Bind                    Python calls __get__ on the returned object. In __get__ python call 
                                    types.Method type to bind the method with the instance. 
                                    After binding the calling the method e.g. p.say_hello() doesn't 
                                    require passing instance reference as a parametre.
            execution               call __call__ on the instance which calls tp_call / vector_call to execute 
                                    the method, which begins with creation of a Frame object.

Name resolution:
    Access to a bound name follows MRO, via object's __getattributes__, __getattr__, and __get__ the name
    refers to a function. __get__ binds the function to an instance. 
    Access to an unbound name in a function follows LEGB, and searching starting from __dict__ in the 
    scope where the name is defined outwards scope by scope along the russian doll all the way to the 
    module __dict__. If still not found, search __globals__ and finally __builtins__. 
    Python allows unresolved names during creation of function/class object, taking those unresolved names
    as global names. Name resolution exceptions are thrown at run time. 

Other specifics
Equality vs Identical
Equality is tested based on value, implemented by __eq__. Identity is esentially based on memory address. 

Hashable
Hashable is the key property that decides whether one can be put in dictionary keys or sets. Sets internally
are hash tables. __hash__ and __eq__ are the default dunder methods for all objects. However, for those 
who overwrite __eq__, python will set __hass__ to None, making it unable to be hash keys or set elements. All
collection classes rewrite __eq__ and hence non-hashable, such as list, dict, set, etc. Custom classes are
hashable by default, unless one's __eq__ is rewritten. The default __eq__ actually checks identity. In python
hash tables, __eq__ is user to test whether same hash is a result of hash collision or same / equal elements.

Descriptor
When resolving x below 
c = C()
c.x
1. Let type(c) be C. Search C (and its MRO) for attribute "x".
2. If found and it is a data descriptor, call __get__ immediately and return result.
3. Otherwise, check c.__dict__ for "x". If present, return that.
4. Otherwise, if found on class and it is a non-data descriptor, call __get__.
5. Otherwise, return class attribute as-is.

Dataclass:
__init__, __repr__, __eq__
it doesn't allow class properties with mutable default value (ValueError)

Asyncio:

"""
