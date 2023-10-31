#!/usr/bin/env ruby
puts (match = ARGV[0][/^\d{10}$/]) ? match : ""
