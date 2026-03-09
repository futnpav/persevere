import math
import collections
import functools

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

"""
Section I
Q1: print 1, 2, 3 and 1, 2, 3, 4, 5
Parameter acc is initialized as an empty list and stored in the __defaults__ in the function object 
of flatten. As list is mutable the append operation has been made to the same default list across 
all calls 
Fix:
"""
def flatten(lst, acc=None):
    if acc == None:
        acc = []
    for x in lst:
        if isinstance(x, list):
            flatten(x, acc)
        else:
            acc.append(x)
    return acc

"""
Q2: print {d:[1,2]}
setdefault() only sets default value to the same key once. The second call simply return the list
the first call sets.
Fix:
"""
d = {}
d["a"] = [1]
d["a"] = [2]
print(d)
"""
Q3: print "All zero"
it is not accurate as any tests whether any element in the list is truable. It returns False when none
of the element is truable, not necessarily "All zero"
Fix:
"""
nums = [0, 0, 0]
if any(n != 0 for n in nums):
    print("Has non-zero")
else:
    print("All zero")
"""
Q4:
Same with Q1
"""
"""
Q5: Judging from the code it seems the developer wants to make a sorted copy of original list. In this
case the builtin sorted() is the right function to use.
Fix: 
"""
nums = [3, 1, 2]
result = sorted(nums)
print(result)
"""
Q6: -5//2 is equivalent to math.floor(-5/2), which returns -3. This is probably not the intended result.
If the developer wants to apply negative to rounded the division of 5/2, one might use: 
"""
print(-(5/2))
"""
Q7: the first prints [(1, 4), (2, 5), (3, 6)] and the second []. The zip object z is depleted after the 
first call to create the list object list(z).
"""
z = zip([1,2,3], [4,5,6])
print(list(z))
print(list(z))
"""
Q8: print False. Float point numbers needs to be compared with a given precision. 
Fix:
"""
print(round(0.1+0.2,1) == 0.3)
"""
Q9: Raise NameError on print(x). Python treats x as a local variable in f as it reads x = 5 during
compilation. However, at run time, print(x) attempts to read x before it is assigned to a value. 
Fix: If we intent f() to set global x to 5
"""
x = 10

def f():
    global x
    print(x)
    x = 5

f()
"""
Q10: keys() returns a view object of the keys in a dict, and it updates with the dict. In the example, 
if key "a" is removed then the list(d.keys())[0] will returns "b". It is always safer to use the key
name directly. Or we create snapshot of the dict keys so that it doesn't change with the dict.
Fix: 
"""
d = {"a":1, "b":2, "c":3}
key_snapshot = list(d.keys())
del d["a"]
print(key_snapshot[0])
"""
Section II

Q1:
def unique(lst):
   return list(set(lst))
Verdict: acceptable with notes. It returns a list without duplicates but doesn't retain order
Fix: 
"""
def unique(lst):
   return list(dict.fromkeys(lst))
"""
Q2:
def safe_get(d, key):
   try:
      return d[key]
   except:
      return None
Reject: It supresses all error without screening, which makes debug very difficult. 
Fix: if we know the type of value the dict stores, we shall use defaultdict. If not, we shall only
void the errors we know but let other errors propagate. 
"""
def safe_get(d, key):
   try:
      return d[key]
   except KeyError:
      return None
"""
Q3:
def is_sorted(lst):
   return lst == sorted(lst)
Verdict: accept. It is even better if it provides comments specifying it allows duplicates
"""
"""
Q4:
def add_user(users=[], name=""):
    users.append(name)
    return users
verdict: reject. mutable type used as default value for parameters. In this case the function keeps 
users in the same default list across funciton invocations where developers expect the function to
create a new list for each call if the users parameter is omitted. 
Fix:
"""
def add_user(users=None, name=""):
    if users is None:
        users = []
    users.append(name)
    return users
"""
Q5: Reject: not testing if nums is empty, which cause Divisionbyzero error
Fix:
"""
def average(nums):
    if not nums or not len(nums):
        return 0
    return sum(nums)/len(nums)

"""
Hopefully last drill before go!!!
Q1:
"""
records = [
   {"age": "30"},
   {"age": 25},
   {"age": None},
   {"age": "unknown"},
   {}
]
def normalize_data(records):
   result = []
   for record in records:
      if "age" not in record:
         continue
      try:
         tmp_age = int(record["age"])
      except (TypeError, ValueError):
         continue
      result.append(tmp_age)
   return result
"""
Q2:
"""
values = ["true", "False", "YES", "no", 1, 0, True, None, "asdfasdf"]
def normalize_bool(value):
   if isinstance(value, bool):
      return value
   if isinstance(value, int) and value in (0, 1):
      return bool(value)
   if isinstance(value, str):
      if value.lower() in ("true", "yes"):
         return True
      elif value.lower() in ("false", "no"):
         return False
   return None

bool_values = [b for value in values if (b := normalize_bool(value)) is not None]
print(bool_values)
"""
Q3:
"""
records = [
   {"id": 1, "score": "90"},
   {"id": 2, "score": None},
   {"id": 3, "score": "invalid"},
   {"id": 4, "score": "85"}
]
def normalize_records2(records):
   result = []
   for record in records:
      normalized_score = None
      if "score" not in record:
         continue
      score = record.get("score")
      if score is None:
         continue
      try:
         score = int(score)
      except (ValueError,TypeError):
         continue
      if score is not None:
         result.append({"id":record["id"], "score":score})
   return result
"""
Q4:
"""
records = [
   {"id":1, "name":"Alice"},
   {"name":"Bob"},
   {"id":3},
]
def check_missing_keys(records):
   output = []
   expected_keys = ("id", "name")
   for rid, record in enumerate(records):
      for key in expected_keys:
         if key not in record.keys():
            output.append((rid, f"missing {key}"))
   return output
"""
Q5:
"""
data = [
   {"user":{"id":"1"}},
   {"user":{"id":2}},
   {"user":{}},
   {}
]
def extract_valid_id(data):
   result = []
   for user_item in data:
      user = user_item.get("user")
      if not isinstance(user, dict):
         continue
      id = user.get("id")
      try:
         id = int(id)
      except (TypeError, ValueError):
         continue
      result.append(id)
   return result
"""
Q6:
"""
records = [
   {"id":1},
   {"id":2},
   {"id":1},
   {"id":3},
   {"id":2}
]
def get_duplicated_id(records):
   unique_ids = set()
   duplicates = set()
   for record in records:
      if (rid := record.get("id")) is None:
         continue
      if rid not in unique_ids:
         unique_ids.add(rid)
      else:
         duplicates.add(rid)
   return list(duplicates)

print(get_duplicated_id(records))
"""
Q7: 
"""
nums = [1,3,5,3,2,5]
def first_duplicate(nums):
   seen = set()
   for num in nums:
      if num in seen:
         return num
      else:
         seen.add(num)
   return None
"""
Q8:
"""
nums = [3,1,3,2,1,4]
def remove_duplicate(nums):
   return list(dict.fromkeys(nums))
"""
Q9:
"""
import json
rows = [
   '{"x":1}',
   '{"x":"2"}',
   '{"x":01}',
   '{"y":3}'
]
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

def extract_int(rows):
   result = []
   for r in rows:
      try:
         obj = json.loads(r)
      except json.JSONDecodeError:
         continue
      data = obj.get("x")
      try:
         data = int(data)
      except (TypeError, ValueError):
         continue
      result.append(data)
   return result

"""
Q10:
"""
# safe_lookup({"a":1}, "a") → 1
# safe_lookup({"a":1}, "b") → None
# safe_lookup(None, "a") → None

def safe_lookup(data, key):
   if isinstance(data, dict):
      return data.get(key)
   return None
"""
Q11:
Explanation: my function handles numbers in str or other types that can be casted to float. 
Choosing float over int as the result of average is usually expected to be a float unless
explicitly requesting flooring or ceiling
"""
nums = [10,20,30]

def safe_average(nums):
   if not nums:
      return None
   valid_nums = []
   for num in nums:
      try:
         valid_num = float(num)
      except (TypeError, ValueError):
         continue
      valid_nums.append(valid_num)
   if not valid_nums:
      return None
   return sum(valid_nums)/len(valid_nums)
"""
Q12:
"""
nums = [-5,-2,-9]

def safe_max(nums):
   if not nums:
      return None
   return functools.reduce(lambda x, y: x if x > y else y, nums)
"""
Q13:
"""
def chunk(lst, chunk_size):
   if not lst:
      return None
   if chunk_size <= 0:
      raise ValueError("invalid chunk_size:{chunk_size}")
   if len(lst) < chunk_size:
      return []
   result = []
   chunked = 0
   while len(lst) - chunked >= chunk_size:
      result.append(lst[chunked:chunked+chunk_size])
      chunked += chunk_size
   return result
"""
Q14:
It prints [{"x":1},{"x":3}]. I don't know what interviewer expect me to say here...
"""
"""
Q15:
It prints [1,2] and {'id':2} I don't know what interviewer expect me to say here either...
"""
"""
3 harder ones
Q1:
"""
records = [
   {"id":1},
   {"id":2},
   {"id":1},
   {"id":3},
   {"id":2},
   {"id":2}
]
def first_duplicate(records):
   if not records:
      return []
   result = []
   seen = set()
   added = set()
   for inx, r in enumerate(records):
      if not isinstance(r, dict):
         continue
      rid = r.get("id")
      if rid is None:
         continue
      if rid not in seen:
         seen.add(rid)
      else:
         if rid not in added:
            result.append((rid, inx))
            added.add(rid)
   return result
"""
Q2:
I don't think there is a way to exactly detect duplicates without storing all the 
data we need to test. To mitigate this problem, I would go after two directions, namely
sampling and compression, or conbination of the two. With sampling I might create a pool
for storing a decent size of consequtive samples to test the frequency of duplicates and 
another pool for storing decent size of randomly selected samples with posistions as the 
stream flows in to test the data in a bigger picture. Depending on the characteristics of
the data we may also consider scaling the number down into a smaller range to increase 
the size of data for detection. Additionally we can also test the distribution of the data
to assess the likelihood for collision, e.g. evenly dividing the value space into segments
and check the hit rate of the number in each segment.  
"""
"""
Q3
"""
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
   result = []
   for r in records:
      if not isinstance(r, dict):
         continue
      rid = r.get("id")
      try:
         rid = int(rid)
      except (TypeError, ValueError):
         continue
      result.append(rid)
   return list(dict.fromkeys(result))
