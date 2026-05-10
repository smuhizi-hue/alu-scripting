#!/usr/bin/env ruby
# The regex /^\d{10}$/ matches:
# ^     : Start of the string
# \d{10}: Exactly 10 digits (0-9)
# $     : End of the string
puts ARGV[0].scan(/^\d{10}$/).join