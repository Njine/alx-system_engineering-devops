#!/usr/bin/env ruby

if ARGV[0]
    result = ARGV[0].scan(/[[:upper:]]/)
    puts result ? result.join("") : ""
end
  
