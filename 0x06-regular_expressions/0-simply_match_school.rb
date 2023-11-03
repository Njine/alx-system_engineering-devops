#!/usr/bin/env ruby

input_string = ARGV[0]

# Use the Oniguruma regular expression to match "School"
regex = /School/

# Check if the input string matches the regular expression
if input_string.match(regex)
  puts "School"
else
  puts ""
end

