#!/usr/bin/env ruby
# The regex /hb?tn/ matches:
#'h' : the Literal character 'h'
# b? : the character'b' zero or one time (optional) 
# tn : the literal characters 'tn'
puts ARGV[0].scan(/hbt?n/).join  