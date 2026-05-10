#!/usr/bin/env ruby
# The regex /[A-Z]+/ matches:
# [A-Z]+ : one or more consecutive capital letters from A to Z
puts ARGV[0].scan(/[A-Z]+/).join