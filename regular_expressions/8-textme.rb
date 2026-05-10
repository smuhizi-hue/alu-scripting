#!/usr/bin/env ruby
# This regex uses capturing groups () to grab specific parts of the string
# \[from:(.*?)\] matches '[from:' followed by any characters until the first ']'
# \[to:(.*?)\] matches '[to:' followed by any characters until the first ']'
# \[flags:(.*?)\] matches '[flags:' followed by any characters until the first ']'

match = ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

# scan returns an array of arrays. If a match is found, we join the first sub-array with commas.
puts match.join(',') if match.any?