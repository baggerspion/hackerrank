h = int(raw_input().strip())
m = int(raw_input().strip())

nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
       "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
       "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]

if m == 0: print "%s o' clock" % nums[h]
elif m == 1: print "one minute past %s" % nums[h]
elif m ==15: print "quarter past %s" % nums[h]
elif m == 30: print "half past %s" % nums[h]
elif m == 45: print "quarter to %s" % nums[h + 1]
elif m == 59: print "one minute to %s" % nums[h + 1]
elif m < 30: print "%s minutes past %s" % (nums[m], nums[h])
else: print "%s minutes to %s" % (nums[60 - m], nums[h + 1]) 
