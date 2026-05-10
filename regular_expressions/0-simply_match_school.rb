#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regex matching method
# The regex /School/ matches the literal word "School"
puts ARGV[0].scan(/School/).join