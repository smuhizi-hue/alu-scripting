#!/usr/bin/env ruby
# This regex matches 'hb' followed by 't' repeating 2 to 5 times, then 'n'
puts ARGV[0].scan(/hbt{2,5}n/).join