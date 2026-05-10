#!/usr/bin/env ruby
# The regex /\d{10}/ matches:
# \d{10} : exactly 10 digits
puts ARGV[0].scan(/\d{10}/).join