#!/usr/bin/env ruby
# The regex /hbt+n/ matches:
# hb : the literal characters 'hb'
# t+ : the character 't' one or more times
# n  : the literal character 'n'
puts ARGV[0].scan(/hbt+n/).join