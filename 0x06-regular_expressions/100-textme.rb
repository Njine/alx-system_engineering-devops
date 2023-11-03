#!/usr/bin/env ruby

if ARGV.length == 1
    match_data = ARGV[0].match(/^.*\[from:(.*?)\].*\[to:(.*?)\].*\[flags:(.*?)\].*$/i)
    if match_data
      sender, number, flags = match_data.captures
      puts "#{sender},#{number},#{flags}"
    end
end
  