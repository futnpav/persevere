import concurrent.futures
import time
# import dis
import asyncio
import sys
# # from numpy import array
# from util import dumb_add
# from typing import Final
import inspect
import types
import json
import threading
import queue
from dataclasses import dataclass
import pprint
import functools
import collections

# Function to perform a CPU-bound task
# def compute_factorial(n):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# def main():
#     numbers = [500, 600, 700, 800]

#     # Using ProcessPoolExecutor to compute factorials concurrently
#     start_time = time.time()

#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         futures = [executor.submit(compute_factorial, num) for num in numbers]
#         for future in concurrent.futures.as_completed(futures):
#             pass
#             # print(f"Factorial computed for number: {numbers[futures.index(future)]}:{str(future.result())}")

#     end_time = time.time()
#     # print(f"Computed all factorials in {end_time - start_time:.2f} seconds")

# if __name__ == "__main__":
#     main()

# class Counter:
# 	def __init__(self, n):
# 		self.current = 1
# 		self.n = n
# 	def __iter__(self):
# 		current = 1
# 		while current <= self.n:
# 			yield current
# 			current += 1
			

# 	# def __next__(self):
# 	# 	if self.current > self.n:
# 	# 		raise StopIteration
# 	# 	yield self.current
# 	# 	self.current += 1
        
# c = Counter(5)

# for i in c:
# 	print(i)

# def gen():
#     yield 5

# g = gen()
# print("a")

# class nothing:
# 	def __init__(self):
# 		self.n = 1
        
# 	def __next__(self):
# 		raise StopIteration
        
# 	def __iter__(self):
# 		return self
        
# nil = nothing()

# for x in nil:
#   print(x)

    
# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1

# counter = count_up_to(5)

# for i in counter:
#     print(i)

# def greeter():
# 	name = yield "Hello! What is your name?"
# 	yield f"Nice to meet you, {name}"

# g = greeter()
# print(next(g))          # "Hello! What is your name?"
# print(g.send("Jerry"))  # "Nice to meet you, Jerry"

# print(next(g))
# print(g.sene("Paul"))

# def my_generator():
#   yield 1
#   yield 2
#   yield 3

# g = my_generator()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def child():
#     yield 1
#     yield 2
#     return "done"

# def parent():
#     result = yield from child()
#     print("child returned:", result)

# def counter(n):
#     i = 0
#     while i < n:
#         yield f"this is the {i+1} time seeing you"
#         i += 1

# for i in counter(5):
#     print(i)

# def dump(gen, label):
#     f = gen.gi_frame
#     print(f"\n--- {label} ---")
#     print("gen:", gen)
#     print("gi_running:", gen.gi_running)
#     print("gi_yieldfrom:", gen.gi_yieldfrom)
#     if f is None:
#         print("gi_frame: None (generator is finished)")
#         return
#     print("f_lineno:", f.f_lineno)
#     print("f_lasti:", f.f_lasti)
#     print("f_locals:", f.f_locals)

# g = iter(Counter(5))
# dump(g, "just reated (not started)")

# print("next:", next(g))   # yields 1
# dump(g, "after yielding 1")

# print("next:", next(g))   # yields 2
# dump(g, "after yielding 2")

# def child():
#     first = yield "First Child Name: "
#     yield f"first child is {first}"
#     second = yield "Second Child Name: "
#     yield f"second child is {second}"
#     return f"{first} and {second} only"

# def parent():
#     result = yield from child()
#     print("child returned:", result)

# p = iter(parent())
# print(next(p))
# print(p.send("Tom"))
# print(next(p))
# print(p.send("Jerry"))
# try:
#     next(p)
# except StopIteration:
#     pass

# for i in p:
#     # print("hello")
#     print(i)

# my_gen = (n for n in range(10))

# for i in my_gen:
#     print(i)



# class natural_gen:
#     def __init__(self, max = 20):
#         self.max = max

#     def __iter__(self):
#         i = 0
#         while i < self.max:
#             yield i
#             i += 1

# class skipper:
#     def __init__(self, max = 100, by = 3):
#         self.n_gen = natural_gen(max)
#         self.by = by

#     def __iter__(self):
#         return (i for i in self.n_gen if i % self.by == 0)

# s = skipper(7, 100)

# for i in s:
    # print(i)

# def multi_of(n):
#     def by(m):
#         print(f"by {m}")
#         return n * m
#     return by

# threes = multi_of(3)

# print(threes(100))

# l = [x for x in range(5) if x % 2 == 0]
# print(l)

# g = {"a": 1}
# l = {"b": 2}

# print(locals())

# discount_rate = 0.10  # module-level (global)

# def price_with_discount(amount_cents):
#     global discount_rate
#     print("configured discount:", discount_rate)  # looks local because of the assignment below
#     discount_rate = 0.20  # assignment makes 'discount_rate' local in this function
#     return int(amount_cents * (1 - discount_rate))
# price_with_discount(10)

# x = 10
# def outer():
#     exec("""global x\nx+=1\nprint(x)""")

# outer()


# module level (GLOBAL)

# g = "global g"

# def outer():
#     e = "enclosing e"
#     def inner():
#         return e
#     return inner


# f = outer()
# outer()


# dis.dis(outer)


# queue = []
# condition = asyncio.Condition()


# async def consumer():
#     async with condition:
#         while not queue: # condition not met
#             print("Consumer waiting...")
#             await condition.wait() # releases lock & sleeps


# item = queue.pop(0)
# print("Consumer got:", item)


# async def producer():
#     await asyncio.sleep(1)
#     async with condition:
#         queue.append("apple")
#         print("Producer added item")
#         condition.notify() # wake one waiter


# async def main():
#     await asyncio.gather(consumer(), producer())


# asyncio.run(main())

# print(dumb_add(2, 4))
# print(sys.path)

# print(__name__)
# print(__package__)

# PI: Final[float] = 3.1415926
# PI = 4

# print(sys.path)
# sys.path.append('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages')


# a = array([
#     [ 1,  2,  3,  4],
#     [ 5,  6,  7,  8],
#     [ 9, 10, 11, 12],
#     [13, 14, 15, 16]
#     ])


# print(a[:2, :2])

# b = array([1, 2, 3, 4])
# c = [1, 2, 3, 4]
# # print(b[:2]) 
# s = a[2:, 2:]
# # print(a[2:, 2:])

# print(a[..., 2:])
# print(a.shape)
# print(b[(1,2)])

# print(id(a))
# print(id(s))

# def f_pass():
#     pass

# def f_ellipsis():
#     ...

# dis.dis(f_pass)
# dis.dis(f_ellipsis)

# print(sys.executable)
# print(sys.path)

# e = "global"

# class outer:
#     e = "enclosing"

#     class C:
#         def f(self):
#             frame = inspect.currentframe()
#             return frame   # captured from outer()

# y = 1

# class A:
#    x = y

# class B(A):
#    z = 10

#    def output(self):
#       print(z)

# b = B()
# b.output()

# print(sys.modules[B.__module__].__dict__["y"])
# print(B.__name__)
# B.__name__ = "D"
# print(B.__name__)
# print(b.output.__class__.__mro__)


# def greet(self):
#    return f"Hello, I am {self.name}"

# class Person:
#    def __init__(self, name):
#          self.name = name

# p = Person("Alice")
# # Manually bind the standalone function to the instance 'p'
# p.say_hello = types.MethodType(greet, p) # this puts greet in the dict of instance p
# # p.say_hello = greet
# print(p.say_hello())  # Output: Hello, I am Alice

# print(__name__)
# print(__package__)
# print(sys.path)

# gen = (x**2 for x in range(10))

# def outer():
#    x = 10
#    def inner():
#       nonlocal x
#       print(x)
#       x = 20
#    inner()
#    print(x)

# outer()

# print(0 and 1 )
# print(i := int("dd"))
# print(isinstance(i, int))
# records = [
#     {"id": 1, "score": "85"},
#     {"id": 2, "score": None},
#     {"id": 3, "score": "invalid"},
#     {"id": 4, "score": "92"}
# ]
# def cleanse_data(rs):
#    sum = n = 0
#    clean = list()
#    for r in rs:
#       try:
#          r["score"] = int(r["score"])
#          clean.append(r)
#          sum += r["score"]
#          n += 1
#       except:
#          continue
#    return clean, round(sum/n, 2)

# ls, s = cleanse_data(records)
# lst = [1, 2, 1, 4, 7, 2, 0, 1]
# # 
# def remove_duplicates(lst):
#    return list(dict.fromkeys(lst))

# print(remove_duplicates(lst))

# print(d := dict.fromkeys(lst, [x*x for x in lst]))

# print(list(d))

# a = {1:"a", 2:"b"}
# b = {2:"c", 3:"d"}

# print({**a, **b})

# def cache_by_dict(func):
#    cache = {}
#    def wrapper(x):
#       if x in cache:
#          print("hit")
#          return cache[x]
#       cache[x] = func(x)
#       return cache[x]
#    return wrapper

# @cache_by_dict
# def double(x):
#    return x * 2

# print(double(99))
# print(double(99))

# print(True.__str__())

# records = [
#   {"id": "001", "active": "true",  "score": "9"},
#   {"id": 2,     "active": True,    "score": 10},
#   {"id": "3",  "active": "FALSE", "score": 0},
#   {"active": "true", "score": "7"}
# ]

# def normalize_records(lst):
#    def parse_bool(v):
#       _truable = {True, 1, "1", "true", "yes"}
#       _falsable = {False, 0, "0", "false", "no"}
#       converted = v
#       if isinstance(v, str):
#          converted = v.strip().lower()
     
#       if converted in _truable:
#          return True
#       elif converted in _falsable:
#          return False
#       else:
#          raise ValueError("Incompatible value for casting to bool")
   
#    _keys = {"id", "active", "score"}
#    cleaned = []
#    errors = []
#    if not isinstance(lst, list):
#       errors.append("the input data is not a list")
#       return cleaned, errors
#    for i, r in enumerate(lst):
#       if not isinstance(r, dict):
#          errors.append(f"Row {i}: Not a dictionary")
#          continue
#       cr = {}
#       for k in _keys:
#          if k not in r.keys():
#             errors.append(f"Row {i}: key {k} is missing")
#             break
#          try:
#             if k == "id" or k == "score":
#                cr[k] = int(r[k])
#             else:
#                cr[k] = parse_bool(r[k])
#          except (TypeError, ValueError):
#             errors.append({f"Row {i}: {k}:{r[k]}: wrong type or invalid value"})
#             break
#          except:
#             errors.append({f"Row {i}: {k}:{r[k]}: unexpected error during casting"})
#             break
#       if(len(cr) == len(_keys)):
#          cleaned.append(cr)
#    return cleaned, errors
         
# cleaned, errors = normalize_records(records)
# print(cleaned)
# print(errors)
         

         

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# print(bool("TRUE"))

# l = [1, 2, 3, 4, 5, 6]

# def chunks(lst, k):
#     out = []
#     for i in range(0, len(lst)-k+1, k):
#       if(i+k-1<len(lst)):
#          out.append(lst[i:i+k])
#     return out

# print(chunks(l, 2))


# def task(x):
#     return x * x

# with concurrent.futures.ProcessPoolExecutor() as ex:
#     futures = [ex.submit(task, i) for i in range(5)]
#     print([f.result() for f in futures])

# def producer(queue):
#    for i in range(5):
#       item = f"item-{i}"
#       print(f"Producing {item}")
#       queue.put(item)
#       time.sleep(2)
#    queue.put(None)

# def consumer(queue):
#    while True:
#       item = queue.get()
#       if item is None:
#          break
#       print(f"Consuming {item}")


# def main():
   # q = queue.Queue()
   # producer_thread = threading.Thread(target=producer, args=(q,))
   # consumer_thread = threading.Thread(target=consumer, args=(q,))

   # producer_thread.start()
   # consumer_thread.start()

   # producer_thread.join()
   # consumer_thread.join()
   # with concurrent.futures.ProcessPoolExecutor() as ex:
   #    futures = [ex.submit(task, i) for i in range(5)]
   #    print([f.result() for f in futures])


# if __name__ == "__main__":
   # main()

# class D:
#     def __get__(self, obj, owner):
#         return 100
    
#     def __set__(self, obj, value):
#          obj._value = value

# class C:
#     x = D()

# c = C()
# c.__dict__['x'] = 5
# print(c.__dict__)
# print(type(c.x))
# print(C.x)

# def safe_divide(a, b):
#    try:
#       return a / b
#    except Exception as e:
#       raise e
#    finally:
#       return None
   
# print(safe_divide(2, 1))

# print(bool(""))

# def add(x, p=""):
#    p+=str(x)
#    return p

# print(add)
# add(1)

# nums = [2, 2, 4]

# def second_largest(nums):
#    if not isinstance(nums, list):
#       raise TypeError("Please provide a list for this function")
#    dedup = list(set(nums))
#    if len(dedup) <= 1:
#       raise ValueError(f"the list has {len(dedup)} distinctive numbers")
#    return sorted(dedup)[-2]

# print(second_largest(nums))

# def cache_by_dict(func):
#    cache = {}
#    def wrapper(*args, **kwargs):
#       x = args[0]
#       if x in cache:
#          return cache[x]
#       cache[x] = func(*args, **kwargs)
#       return cache[x]
#    return wrapper

# @cache_by_dict
# def double(x):
#    return x * 2

# print(double(5))

# def chunks(lst, k):
#    if not isinstance(lst, list):
#       raise TypeError("lst is not a valid list")
#    if k < 1:
#       raise ValueError(f"k:{k} is not valid")
#    out = []
#    for i in range(0, len(lst), k):
#       if len(s := lst[i:i+k]) == k:
#          out.append(s)
#    return out

# print([0]*3)
# import time

# def expensive():
#     time.sleep(1)
#     return 99

# # d = {"a": 1}
# d = {}
# x = d.get("a", expensive())
# print(x)

# class Box:
#    items: list = ["class"]
#    def __init__(self):
#       self.items = ["instance"]
   

# b = Box()
# print(b.items[0])
# print(Box.items[0])

# async def work():
#     await asyncio.sleep(0.1)
#     return 5

# async def main():
#     x = work()
#     r = await x
#     print(r)

# asyncio.run(main())

# nums = [0, 1, 2, 3, 4]
# print(list(filter(lambda x: x % 2, nums)))
# print(list(filter(lambda x: x % 2 == 0, nums)))

# grid = [[0]*3]*3
# grid[0][1] = 9
# print(grid)

# async def fetch_data(id, sleep_time):
#    print(f"Coroutine {id} stating to fetch data")
#    await asyncio.sleep(sleep_time)
#    return {"id": id, "data":f"Sample data from coroutine {id}"}

# async def main():
#    tasks = []
#    async with asyncio.TaskGroup() as tg:
#       for i, sleep_time in enumerate([2,1,3], start=1):
#          task = tg.create_task(fetch_data(i, sleep_time))
#          # tasks.append(task)

#    print("tasks launched")

   # results = [task.result() for task in tasks]

   # for result in results:
   #    print(f"Received result: {result}")

# print("see if this reenters")

# async def fetch_data(id, sleep_time):
#    print(f"Coroutine {id} starting to fetch data.")
#    await asyncio.sleep(sleep_time)
#    return {"id": id, "data":f"Sample data from coroutine {id}"}

# async def main():
#    task1 = asyncio.create_task(fetch_data(1, 2))
#    task2 = asyncio.create_task(fetch_data(2, 3))
#    task3 = asyncio.create_task(fetch_data(3, 1))

#    print("tasks launched")

   # result1 = await task1
   # result2 = await task2
   # result3 = await task3

   # print(result1, result2, result3)

# async def set_future_result(future, value):
#    print("started thread")
#    await asyncio.sleep(10)
#    future.set_result(value)
#    await asyncio.sleep(10)
#    print(f"Set the future's result to: {value}")
#    return 100

# async def main():
#    loop = asyncio.get_running_loop()
#    future = loop.create_future()
#    print("about to create task")
#    asyncio.create_task(set_future_result(future, "Future result is ready"))

#    result = await future
#    print(f"Received the future's result: {result}")

# print("good")
# asyncio.run(main())

# print("good")

# def timer(func):
#    def wrapper(*args, **kwargs):
#       start_time = time.time()
#       result = func(*args, **kwargs)
#       end_time = time.time()
#       print(f"Function {func.__name__!r} took: {end_time - start_time:.4f} sec")
#       return result
#    return wrapper

# def example_function(n):
#    return f"The sum is {sum(range(n))}"


# # ef = example_function
# print(timer(example_function)(1000))

# def demo_exec():
#    code = """def greet(name):
#    print(locals())
#    return f"Hello, {name}\"
# print(locals())
# abc = 'abc'"""

   # local_scope, global_scope = {"addr":"eastwood"}, {}
   # exec(code)
   # print(local_scope["greet"]("Jerry"))
   # print(locals())
   # print(global_scope["abc"])

# demo_exec()
# good = "good"
# code = """def greet(name):
#    print('ab')
#    return f"Hello, {name}\"
# # global abcd
# abcd = 'abcd'
# # print(a)
# print(good)
# print(locals)"""

# local_scope, global_scope = {"a":1}, {"a":2}
# global_scope = {}
# exec(code)
# print(local_scope["greet"]("Tom"))
# print(local_scope["abcd"])

# from functools import cached_property

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     @property
#     def radius(self):
#         return self._radius

#     @radius.setter
#     def radius(self, value):
#         self._radius = value
#         # Manually clear the cache when radius is updated
#         if 'area' in self.__dict__:
#             del self.__dict__['area']

#     @cached_property
#     def area(self):
#         print("--- Calculating Area ---")
#         return 3.14 * (self._radius ** 2)


# c = Circle(2)
# print(c.area)
# print(c.area)
# c.radius = 10
# print(c.area)
# print(c.area)

# def triadd(x, y):
#     print(x, y)
#     return x+y
# a = [2, 4, 6, 8, 10]
# r = functools.reduce(triadd, a, 100)
# print(r)

# factorial = functools.partial(functools.reduce, lambda x, y:x*y)
# print(factorial(range(1,30)))

# @functools.singledispatch
# def handle_error(error_code):
#     raise NotImplemented(f"Can't handle this error {error_code}")
# @handle_error.register(int)
# def _(error):
#     print(f"handling TypeError: {error}")
# @handle_error.register(str)
# def _(error):
#     print(f"handling ValueError: {error}")

# handle_error("a")

# c = collections.Counter({"cats":4,"dogs":8})
# print(c["dogs"])
# print(list(c.elements()))
# print(c.total())

# od = collections.OrderedDict({"a":2,"b":3})
# od.move_to_end("a")
# print(od)
# print("".join(od))

# i = collections.Counter([1, 3, 2, 3, 2]).elements()
# print(list(i))

# def infinite_dict():
#    return collections.defaultdict(infinite_dict)

# dd = collections.defaultdict(infinite_dict)

# dd["first"]["second"]["third"] = 4
# pprint.pprint(dd)

# d1 = {"a":1, "b":2}
# d2 = {"b":3, "c":4}

# pprint.pprint(cm:=collections.ChainMap(d1,d2))
# pprint.pprint({**d1, **d2})
# print(cm["c"])
# del cm["c"]

# print(int([1]))

# class my_class:
#    def init(self):
#       self.v = 5

#    def get_me(self):
#       return self

# if []:
#    print("true")
# else:
#    print("false")

# import json
# data = '{"x": 01}'
# json.loads(data)

# print(-(5//2))
# print(int(-5/2))

# data = [
#    {"user":{"id":"1"}},
#    {"user":{"id":2}},
#    {"user":{}},
#    {}
# ]
# def extract_valid_id(data):
#    result = []
#    for user_item in data:
#       if "user" in user_item:
#          if "id" in user_item["user"]:
#             try:
#                valid_id = int(user_item["user"]["id"])
#             except (TypeError, ValueError):
#                continue
#             result.append(valid_id)
#    return result

# print(extract_valid_id(data))

# records = [
#    {"id":1},
#    {"id":2},
#    {"id":1},
#    {"id":3},
#    {"id":2}
# ]
# def get_duplicated_id(records):
#    unique_ids = set()
#    duplicates = set()
#    for record in records:
#       if record["id"] not in unique_ids:
#          unique_ids.add(record["id"])
#       else:
#          duplicates.add(record["id"])
#    return list(duplicates)

# print(get_duplicated_id(records))

# print(int(01))

# rows = [
#    '{"x":1}',
#    '{"x":"2"}',
#    '{"x":01}',
#    '{"y":3}'
# ]

# def extract_int(rows):
#    result = []
#    for row in rows:
#       left, right = row.replace("{","").replace("}","").split(":")
#       if left not in ("'x'", '"x"'):
#          continue
#       if right[0] == "0":
#          continue
#       if right[0:1] in ("'0", '"0'):
#          continue
#       try:
#          valid_int = int(right.strip("'").strip('"'))
#       except ValueError:
#          continue
#       result.append(valid_int)
#    return result

# print(extract_int(rows))

# obj = {"a":2,"b":4}

# def safe_lookup(data, key):
#    if isinstance(data, dict):
#       return data.get(key)
#    return None
# print(safe_lookup({},"c"))

# nums = [10,20,3.2]

# def safe_average(nums):
#    if not nums:
#       return None
#    valid_nums = []
#    for num in nums:
#       if isinstance(num, int) or isinstance(num, float):
#          valid_nums.append(int(num))
#       elif isinstance(num, str):
#          try:
#             valid_int = int(num)
#          except (ValueError, TypeError):
#             continue
#          valid_nums.append(valid_int)
#    if len(valid_nums):
#       return functools.reduce(lambda x, y: x + y, valid_nums) // len(valid_nums)
#    return None

# print(safe_average(nums))

# nums = [-5,-2,-9]

# def safe_max(nums):
#    if not nums:
#       return None
#    return functools.reduce(lambda x, y: x if x > y else y, nums)

# print(safe_max(nums))

# def chunk(lst, chunk_size):
#    if not lst:
#       return None
#    if len(lst) < chunk_size:
#       return None
#    result = []
#    chunked = 0
#    while len(lst) - chunked >= chunk_size:
#       result.append(lst[chunked:chunked+chunk_size])
#       chunked += chunk_size
#    return result

# print(chunk([1,2,3,4,5,6,7], 3))

# rows = [{"x":1}, {"x":2}, {"x":3}]

# for r in rows:
#    print("entered")
#    if r["x"] == 2:
#       rows.remove(r)

# print(rows)

# items = [{"id":1}, {"id":2}]

# ids = []
# for i in items:
#    ids.append(i["id"])

# print(ids)
# print(i)

# values = ["true", "False", "YES", "no", 1, 0, True, None, "asdfasdf"]

# def normalize_bool(value):
#    if value is None:
#       return False
#    if isinstance(value, bool):
#       return value
#    if isinstance(value, int) and value in (0, 1):
#       return bool(value)
#    if isinstance(value, str):
#       if value.lower() in ("true", "yes"):
#          return True
#       elif value.lower() in ("false", "no"):
#          return False
#    return None

# bool_values = [b for value in values if (b := normalize_bool(value)) is not None]
# print(bool_values)

# rows = [
#    '{"x":1}',
#    '{"x":"2"}',
#    '{"x":01}',
#    '{"y":3}'
# ]
# def extract_int(rows):
#    result = []
#    for r in rows:
#       try:
#          obj = json.loads(r)
#       except json.JSONDecodeError:
#          continue
#       if not (data := obj.get("x")):
#          continue
#       try:
#          data = int(data)
#       except (TypeError, ValueError):
#          continue
#       result.append(data)
#    return result

# print(extract_int(rows))

records = [
   {"id":"001"},
   {"id":1},
   {"id":"1"},
   {"id":"x"},
   {"id":None},
   {},
   {"id":"002"},
   {"id":2}
]
def normalize_id(records):
   if not records:
      return []
   raw_result = []
   seen = set()
   for r in records:
      if not isinstance(r, dict):
         continue
      id = r.get("id")
      try:
         id = int(id)
      except (TypeError, ValueError):
         continue
      if id not in seen:
         seen.add(id)
      else:
         raw_result.append(id)
   return list(dict.fromkeys(raw_result))

print(normalize_id(records))

# records = [
#    {"id":1},
#    {"id":2},
#    {"id":1},
#    {"id":3},
#    {"id":2},
#    {"id":2}
# ]
# def first_duplicate(records):
#    if not records:
#       return []
#    result = []
#    seen = set()
#    added = set()
#    duplicate = []
#    for inx, r in enumerate(records):
#       if not isinstance(r, dict):
#          continue
#       id = r.get("id")
#       if id not in seen:
#          seen.add(id)
#       else:
#          if id not in added:
#             result.append((id, inx))
#             added.add(id)
#    return result

# print(first_duplicate(records))