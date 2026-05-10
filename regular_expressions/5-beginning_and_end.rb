#!/usr/bin/env ruby
# The regex /^h.+?n$/ matches:
# ^ : beginning of the string
# h : the literal character 'h'
# .+? : one or more of any character (non-greedy)
# n : the literal character 'n'
# $ : end of the string
puts ARGV[0].scan(/^h.+?n$/).join