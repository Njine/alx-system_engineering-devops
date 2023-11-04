#!/usr/bin/env ruby

if ARGV[0]
    result = ARGV[0].scan(/h\wn/)
    puts result ? result.join("") : ""
end
  