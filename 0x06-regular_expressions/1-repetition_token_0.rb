#!/usr/bin/env ruby

if ARGV[0]
    result = ARGV[0].scan(/hbt{2,5}n/)
    puts result ? result.join("") : ""
end
  