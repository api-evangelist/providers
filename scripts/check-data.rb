#!/usr/bin/env ruby
# frozen_string_literal: true
#
# Parse every data file the way GitHub Pages will, and fail loudly if one of
# them will not load.
#
# Jekyll does NOT read _data/*.json with a JSON parser. It hands them to
# SafeYAML -> Psych, and YAML is stricter than JSON about escapes: it accepts
# \uXXXX only for the Basic Multilingual Plane and rejects the surrogate pairs
# JSON uses for anything above U+FFFF. A single emoji in a provider description,
# written by a plain json.dump (ensure_ascii=True by default), is therefore
# enough to kill the entire site build before one page renders. That is exactly
# what took providers.apievangelist.com down on 2026-08-11.
#
# Anything that rewrites a file under _data/ must go through dump_json() in
# scripts/build-listing.py, which desurrogates and writes ensure_ascii=False.
# This script is the backstop for when something forgets.
#
# Usage:
#   ruby scripts/check-data.rb           # every data file
#   ruby scripts/check-data.rb a.json b  # only these paths

require "psych"

ROOT = File.expand_path("..", __dir__)

# A JSON surrogate-pair escape: \ud83e, \udd16 and friends (U+D800-U+DFFF).
SURROGATE_ESCAPE = /\\u[dD][89a-fA-F][0-9a-fA-F]{2}/

def data_files
  Dir.glob(File.join(ROOT, "_data", "**", "*.{json,yml,yaml}")).sort +
    Dir.glob(File.join(ROOT, "_config.yml"))
end

def diagnose(path)
  # Read as binary and force UTF-8 so an encoding problem in the file cannot
  # blow up the diagnosis itself.
  body = File.binread(path).force_encoding("UTF-8")
  hits = body.scan(SURROGATE_ESCAPE).uniq
  return nil if hits.empty?

  "contains #{hits.size} JSON surrogate escape(s) (#{hits.first(4).join(', ')}) — " \
    "YAML cannot represent these. Rewrite the file through dump_json() in " \
    "scripts/build-listing.py (desurrogate + ensure_ascii=False) rather than a bare json.dump."
rescue StandardError
  nil
end

targets = ARGV.empty? ? data_files : ARGV.map { |a| File.expand_path(a) }
targets = targets.select { |p| File.file?(p) }

failed = []
targets.each do |path|
  Psych.parse_file(path)
rescue StandardError => e
  failed << [path, e.message, diagnose(path)]
end

rel = ->(p) { p.sub(%r{\A#{Regexp.escape(ROOT)}/}, "") }

if failed.empty?
  puts "check-data: #{targets.size} file(s) parse under Psych — the Pages build will read them."
  exit 0
end

warn "check-data: #{failed.size} of #{targets.size} file(s) will BREAK the GitHub Pages build.\n\n"
failed.each do |path, message, hint|
  warn "  #{rel.call(path)}"
  warn "    #{message.lines.first.to_s.strip}"
  warn "    -> #{hint}" if hint
  warn ""
end
warn "Jekyll parses _data/*.json as YAML (SafeYAML -> Psych), not as JSON."
exit 1
