#!/usr/bin/env ruby
# The regex /[A-Z]/ matches:
# [A-Z] : any single capital letter from A to Z
puts ARGV[0].scan(/[A-Z]/).join