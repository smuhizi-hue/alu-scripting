#!/usr/bin/env ruby
#This regex matches 'h', followed by 'b', followed by two to five 't's, and finally 'n'.
puts ARGV[0].scan(/hbt{2,5}n/).join