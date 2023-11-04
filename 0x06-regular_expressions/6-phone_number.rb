#!/usr/bin/env ruby

if ARGV[0]
    match = ARGV[0][/^\d{10}$/]
    puts match ? match : ""
end 
