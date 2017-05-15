# Example 1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

# Example 2 # uncomment this to test with different input
#marker = "EY"
#replacement = "Eyjafjallajokull"
#line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

###
# YOUR CODE BELOW. DO NOT DELETE THIS LINE
###
mark_start = line.find(marker)
mark_end = line.find(' ',mark_start)
mark = line[mark_start:mark_end]
mark = replacement

before_mark = line[:mark_start]
after_mark = line[mark_end:]

replaced = before_mark + mark + after_mark

print (replaced)
