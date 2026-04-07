# Nested Loop, if, elif ladder
'''
Pattern-1:
* * * * *
*       *
*       *
*       *
*       *
*       *
* * * * *

Pattern-2:
    *
   * *
  * * *
 * * * *
* * * * *
'''

'''
Nested loop -> একটা লুপের ভিতরে আরেকটা লুপ
Outer loop -> বাইরের লুপ -> লাইন যতগুলো ততবার রান হবে -> 7
Inner loop -> ভিতরের লুপ -> স্টার প্রিন্ট করা
'''

i = 1
while i < 8:
    j = 1
    while j < 6:
        print("*", end="")
        j += 1
    print("")
    i += 1