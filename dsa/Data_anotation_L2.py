"""
Q1:
class A:
    def f(x, y):
        return x, y

a = A()

A.f(1, 2)
# returns 1, 2
a.f(1, 2)
# too many parameters, expecting 2
A.f(a, 2)
# returns a, 2
a.f(2)
# returns a, 2

Q2:
def cache_result(x, cache={}):
    if x in cache:
        return cache[x]
    cache[x] = x * 2
    return cache[x]

The code works in the sense it serves the purpose of the function, 1) double 
x and 2) caches results to avoid recalculation for the same x. However, this
function depends on a special feature how Python handles parameters with default
values, which may cause confusions. I accept this implmentation with the 
aforementioned note. Good implementation shall rely on well accepted coding
practice to reflect intention of the code as explicitly as possible. It is more 
graceful to implement caching feature with decorators. See implementation as follows. 

Note: This demonstrate intends to show how to make the implementation explicitly 
reflects the purpose of the code. Function wise one can use the existing lru_cache
decorator in the built-in module functools to achieve the same goal.
def cache_by_dict(func):
   cache = {}
   def wrapper(*args, **kwargs):
      x = args[0]
      if x in cache:
         return cache[x]
      cache[x] = func(*args, **kwargs)
      return cache[x]
   return wrapper

@cache_by_dict
def double(x):
   return x * 2

Q3:
This function contains a silent bug. It uses the builtin function sum as a name of
a local variable, which will shadow the function in the scope of the function. Any call
to the builtin sum function won't work and hard to debug. It is better rename it to my_sum
or _sum. This function however will work as expected, as it doesn't call the builtin sum
in the function body. 
print(count([1, 2, 3]) # will print 3
print(sum([1, 2, 3])) # will print 6


Q4:
This function will not work as expected as set in python only remove duplicates but won't
preserve order. Consider the following fix.
def unique_preserve_order(lst):
    return list(dict.fromkeys(lst))

Q5:
This function has a bug as it causes confussion when it returns 0 - caller can't tell
whether the function is in an erronous state or it is given 0 as an input. To make 
exception handling more effective, programmer shall
1. provide clear cause and description of the exception
2. only catch exceptions that it handle and let other unexpected exceptions propagate

def read_int(prompt):
    while True:
        s = input(prompt)
        if s.strip() == "":
            return None
        try:
            return int(s)
        except ValueError:
            print("Please enter a valid integer (or press Enter to skip).")

Q6:
This problem requires a function to normalizes python data records, which 
is widely needed prior to data serialization or message exchange. My 
implement fulfils the following features. It 
1. checks if input records are in a correct format and drops those in 
   incompatible format; 
2. checks if values in the data record have the correct type and in a 
   compatible range;
3. tries to fix records with incompatible values and drops those can't be
   fixed;
4. puts all acceptable or fixed records in a new list "cleaned", and the error
   messages for those dropped records in "errors"; and 
5. returns both lists to complete.

Note: Judging from the requirement that put all error messages in a list and 
   returns it to the caller, I believe it is not the interest of this function
   to catch and raise all exceptions in-place. Instead the user of this function
   expect to extract useful data and look into the errors separately. As such I 
   let the function log all errors in the errors list without raise any exceptions
   that requires immediate handling by the caller. 

records = [
  {"id": "001", "active": "true",  "score": "9"},
  {"id": 2,     "active": True,    "score": 10},
  {"id": "x3",  "active": "FALSE", "score": None},
  {"active": "true", "score": "7"}
]

def normalize_records(lst):
   def parse_bool(v):
      _truable = {True, 1, "1", "true", "yes"}
      _falsable = {False, 0, "0", "false", "no"}
      converted = v
      if isinstance(v, str):
         converted = v.strip().lower()
     
      if converted in _truable:
         return True
      elif converted in _falsable:
         return False
      else:
         raise ValueError("Incompatible value for casting to bool")
   
   _keys = ("id", "active", "score")
   cleaned = []
   errors = []
   if not isinstance(lst, list):
      errors.append("the input data is not a list")
      return cleaned, errors
   for i, r in enumerate(lst):
      if not isinstance(r, dict):
         errors.append(f"Row {i}: Not a dictionary")
         continue
      cr = {}
      for k in _keys:
         if k not in r.keys():
            errors.append(f"Row {i}: key {k} is missing")
            break
         try:
            if k == "id" or k == "score":
               cr[k] = int(r[k])
            else:
               cr[k] = parse_bool(r[k])
         except (TypeError, ValueError):
            errors.append(f"Row {i}: {k}:{r[k]}: wrong type or invalid value")
            break
      if(len(cr) == len(_keys)):
         cleaned.append(cr)
   return cleaned, errors
         
cleaned, errors = normalize_records(records)
print(cleaned)
print(errors)

Q7:
This function devides a list into chucks of whole k number of elements (use of 
range(0, len(lst)-k,k) clearly excludes remainders that don't make whole k). However, it fails
when the list has exactly multiple of k elements, in which case it misses the last chuck. 
For instance, if len(lst) is 8 and k is 4, it only appends [0:4] to out, missing [4:8]. It
works well when the length of the list is not multiple of k. E.g., len(lst) is 8 and k is 3,
it produces [[0:3],[3:6]]. The following function fixes the issue and append all chuck of k
elements sequentially to the list out. 
def chunks(lst, k):

    out = []
    for i in range(0, len(lst), k):
      if len(s := lst[i:i+k]) == k:
         out.append(s)
    return out

Q8:
from concurrent.futures import ProcessPoolExecutor

def task(x):
    return x * x

with ProcessPoolExecutor() as ex:
    futures = [ex.submit(task, i) for i in range(5)]
    print([f.result() for f in futures])

This is a very common mistake in concurrent execution. Every new process will rename the file 
where it is launched and execute it again. In this example each new process will re-execute the 
code section that launched it. To fix this bug, we need to use the name test to protect code 
section that shall only be executed in main process/thread, as shown below.

if __name__ == "__main__":
   with ProcessPoolExecutor() as ex:
      futures = [ex.submit(task, i) for i in range(5)]
      print([f.result() for f in futures])

Q9:
First prints 5, and second prints 100. 
If D is a data descriptor, both print 100 

Q10:
This function filfuls the requirement as it calcuates and return the result of a / b under
normal circumstances, and returns None shall error occur. It is acceptable but it will be
better if the function could reveal more details when it encoutners error for debug. Please
consider the following revision. 

err_str = ""
def safe_divide(a, b):
   global err_str
   try:
      return a / b
   except ZeroDivisionError:
      err_str = "Division by Zero"
      return None
   except (TypeError, ValueError):
      err_str = f"a:{a} or b:{b} is of wrong type or value"
      return None
   except:
      err_str = f"a:{a}/b:{b} caused an unexpected error"
      return None

Q11:
This function returns the expected value but it has the following issues:
1. it doesn't check the input list so it will run into errors if list is either invalid or 
has no or only one element.
2. It alters the input list which might be an undesirable side effect. 
3. If the largest number is duplicated, it actually returns the largest number

Here is the improved version. Note that this function raises exception should error occur, 
but won't catch or reraise the excections that python throws by default, instead all 
exceptions are expected to be handled by the caller. 

def second_largest(nums):
   if not isinstance(nums, list):
      raise TypeError("Please provide a list for this function")
   dedup = list(set(nums))
   if len(dedup) <= 1:
      raise ValueError(f"the list has {len(dedup)} distinctive numbers")
   return sorted(dedup)[-2]

Q12:
This funcion may catch beginner by surprise for it produces 
[1] 
[1, 1] 
[1, 1, 1] 
instead of the anticipated
[1]
[1]
[1]

The reason hides in the way how python constructs the function object when it reads "def". During 
construction when it puts default values into a tuple. If the default value is a mutable one, for 
instance a list in this case, python will keep appending into the same default list created during 
construction instead of creating a new one. This issue only affect mutable default value though - 
immutable default values continue to work in the way as we expected. Assignment to a parameter with
immutable default value will trigger python to treat it as a local variable and bind it to the new 
value in the function frame, and its scope of use is within the function call. 

"""