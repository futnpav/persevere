"""
Task Set 1
Task 1A:
This is a very typical mistake working with container classes such as list, array, etc. What the code sniplet 
does is to create a new list and then append 1 to it every time f() is called. Instead of returning [1], 
[1, 1, [1,1,1], it returns [1], [1], [1], because the function creates a new list everytime on invocation. 
To use the function to append to an existing list, we need to create a list and then pass the list to the 
function as a parameter to make sure each time the function appends value to the same list. 
Task 1B
The time coomplexity for this function is n to the power of 2. The cost may be acceptable for a very small data
set but definitely not for large sets. If testing duplicity is the only goal it is much quick to use a 
dicdtionary. We can use the value in the list as the key to the dictioanry inserting (lst[n], 1) to the dictionary
and then compare the length of the two (lst and the new dictioary) after insertion. The new approach is much
quicker as it reduce the time complexity from O(n to the power of 2) to O(n), it does introduce extra space
complixity of O(n).
Task Set 2
In the large extent both functions work. However, neither funciton checks the type of the parameter s which will
result in exception of a wrong type is passed to the function. Semantically function #1 is more preferred
as it tests the string "as it is", rather than testing a modified version of the string as in #2. Performance
wise #2 has a slight edge as it test half the string length, but the time complexity is still considered O(n). I 
would suggest to take function #2, replacing 
s = s.lower().replace(" ", "")
with
if isinstance(s, str):
   return False
Task set 3
This json object doesn't including sufficient information for the recipient to reconstruct the list. The sender
needs to serialize all the needed data and include it in the json object. 
Task set 4
This function doesn't check the type of a and b neither does it check whether b is non-zero. Python by default 
stores float in 16 digits. It may also worth specifying the precision of the result. 
Task set 5
please give answer and explanation
Task set 6
taking the example in Task 1B, for each element in outer iteration, lst[i] == list[j] will be tested len(lst)
times in the worst case. Similarly in the worst case the outer iteration will loop len(lst) times. The total 
times of iteration of the two nested loops in the worst case is n to the power of 2. 
Mini Mock:
Q1:
List stores its elements sequentially in a continuous space. what list.pop(0) does involves two actions, which are 1) to return the first element and then 2) remove it from the list. As list store elements in a continuous space, it will fill up "holes" after deletion by shifting element after the hole forwards to make its internal storage space continuous agian. The shifting is not required for removing an element from the end. As a result, the time complexity of list.pop(0) is O(n) (due to shifting) and list.pop() is O(1) (no shifting required).
Q2:
This is a typical case where merging into a new dictionary is perferred over into the  existing one. In the code snippet inserts and update elements in dictionary a with dictionary b, which potentially makes later operations on the updated dictionary a in risk for its length and value might has changed. Unless changing the existing dictionary is the intended result, it is always safer to make a copy of dictionary a and then merging b into the new dictionary. 
Q3. 
This is a very typical mistake working with container classes such as list, array, etc. What the code sniplet does is to create a new list and then append 1 to it every time f() is called. Instead of returning [1], [1, 1, [1,1,1], it returns [1], [1], [1], because the function creates a new list everytime on invocation. To use the function to append to an existing list, we need to create a list and then pass the list to the function as a parameter to make sure each time the function appends value to the same list. 

Q1:
The second parametre of this function has a default value, which is a new list. During the execution of the 
definition of the function, the parametre "container" has been assigned to a new list and added to default
keyword aguments dictionary in the function object. When the function is called without the second parametre, 
the value is always appended to the same container. If this is the intended, it is very confusing and error 
prone. It is better implemented by decorator or closure. 

def container_by_list()
   container = []
   def add_item(value):
      container.append(value)
      return container
   return add_item

add_to_list = container_by_list()
add_to_list(2)
add_to_list(3)
add_to_list(4)

If the programmer intends to return a new list everytime the fundtion is called, it is better to avoid the
passing a list to it. Consider the following code.
def add_item(value):
   return [value]

Q2:
It function tries to iterate from both ends of the string and test if the string is symetrically identical. 
It has a bug that breaks the logic. The first char left to right in the string is s[0] and the iteration steps
are from 0 to len(s)//2 - 1, while the first one in reverse order is s[-1] and the iteration steps are from 
-1 to -len(s). Morevoer the function doesn't test the type of s, which may raise type error if s is not a 
string. Please find the corrections as follows. 

def is_palindrome(s):
   if not isinstance(s, str):
      raise TypeError
   for i in range(len(s)//2):
      if s[i] != s[-i-1]:
          return False
   return True

Q3:
The time complexity of this function is O(n to the power of 2) and the space complexity is o(1). Please note 
Big O notation concerns how computational complexity in terms of time and space changes as the data input 
scales, it doesn't necessarily requires mathematical correctness. In this case, the actual time complexity is
Sum(0<=k<n) n-k, n = len(s), however, for the sake of simplicity, Big O will still regards the time complexity
as O(n to the power of 2). The following functions improves the time complexity to O(n), however, as it uses a
dictionary to speed up the look up, reducing look up from O(n) by list to O(1) by dictionary, it adds extra 
space complexity of O(n).
def contains_pair_with_sum(lst, target):
   d = dict()
   for i in range(len(lst)):
      if lst[i] in d:
         return True
      d[target-lst[i]] = i
   return False

Q4:
Both responses remove duplicates from the list. A is faster taking time complexity of O(n), but it can't retain
the original order of the list. A better solution is to use dictionary's fromkeys() in later version of Python
as follows:
def remove_duplicates(lst):
   return list(dict.fromkeys(lst, 0))
Response B removes duplicates and retains thr original order, but it is significantly slower as it has time 
complexity of O(n to the power of 2)

Q5:
Both obj["age"] and obj["active"] are of type str. json.loads parses the object in single quoation and check
types of each value in the same way as they are defined in the python code. Any value put in quotations are
treated as string literals. Here is the correct:
data = '{"name": "Alice", "age": 30, "active": true}'
obj = json.loads(data)

Q6:
records = [
    {"id": 1, "score": "85"},
    {"id": 2, "score": None},
    {"id": 3, "score": "invalid"},
    {"id": 4, "score": "92"}
]
records = [
    {"id": 1, "score": "85"},
    {"id": 2, "score": None},
    {"id": 3, "score": "invalid"},
    {"id": 4, "score": "92"}
]
def cleanse_data(rs):
   s = n = 0
   clean = list()
   for r in rs:
      try:
         r["score"] = int(r["score"])
         clean.append(r)
         s += r["score"]
         n += 1
      except TypeError, ValueError, KeyError:
         continue
   return clean, round(s/n, 2) if n > 0 else None

ls, s = cleanse_data(records)
This function removes entries with invalid or missing score, return a new list containing only valid entry and
the average score.

Q7:
I would rephrase it to "because the code snippet has two nested loops, and for each iteration of the outer
loop, the statements inside in the inner loop are executed n timers in worst case."

Q8:
This function supplements and updates dict a with dict b, which may not be easily understood by its name 
"merge". It not only inserts all elements from b into a, it also overwrites elements in a that have the same
key with elements in b. This may lead to a surprising side effect. A safer way is to make a clone of a and then
to return the clone after being supplemented and updated by b. The following function implements the safer 
merge aforementioned. However, it is worth note that the builtin copy of dict is a shallow one, meaning that if
the elements in a and b reference to mutable objects, those elements in the clone reference to exact the same
objects. So the dict the function returns only read-safe. If we need it to be write-safe, we need to use 
copy.deepcopy, which is much costy. 

def merge(a, b):
   c = a.copy()
   for i in b:
      c[i] = b[i]
   return c # {**a, **b}

Q9:
This function doesn't code correct solutions for all possible exceptions. The common two exceptions for
division is type error and dividing by zero. The functions doesn't handle dividing by zero correctly. Please
find correction as follows. This function handles common exceptions returns acceptable result. For uncaught
exceptions, it let them bubble up. 

def divide(a,b):
   try:
      return a/b
   except TypeError:
      return 0
   except ZeroDivisionError:
      return float('inf')
      
Q10:
This function fails if lst contains negative numbers only. To find a value in a group, it is always safer to
start searching with one in the group. Please find the correction as follows. 

def max_number(lst):
   if not lst:
      raise ValueError("lst must be non-empty")
   largest = lst[0]
   for n in lst:
      if n > largest:
         largest = n
   return largest
   

Level 2

Q1:
A.f(1, 2) >> returns 1, 2
a.f(1, 2) >> too many parameters, 3 parameters are passed while expecting 2
A.f(a, 2) >> returns a, 2
a.f(2).   >> returns a, 2

q2:

"""