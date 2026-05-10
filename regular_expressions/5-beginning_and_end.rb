#!/usr/bin/env ruby
# The regex /h.n/ matches:
# h : the literal character 'h'
# . : any single character (except a newline)
# n : the literal character 'n'
puts ARGV[0].scan(/h.n/).join