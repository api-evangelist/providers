---
aid: command-line-interface
url: https://raw.githubusercontent.com/api-evangelist/command-line-interface/refs/heads/main/apis.yml
name: Command Line Interface
x-type: topic
description: Command Line Interface (CLI) is a text-based way of interacting with software by typing commands at a prompt. Modern CLI design draws on decades of UNIX conventions while incorporating contemporary practices around discoverability, human-friendly output, machine-readable formats, configuration, subcommands, and progressive disclosure of complexity. CLIs remain a central surface for developer tools, infrastructure automation, package managers, build systems, and anything that benefits from scripting and composition.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - CLI
  - Command Line
  - Developer Experience
  - Developer Tools
  - Scripting
  - Shell
  - Terminal
  - Tooling
  - UNIX
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: command-line-interface:design-guidelines
    name: Command Line Interface Guidelines
    description: An open source guide that distills decades of CLI design wisdom into concrete, actionable guidelines. Authored by engineers from Docker, Squarespace, and others, it covers philosophy, arguments and flags, output, errors, help, configuration, subcommands, and interactivity. A practical reference for designing modern command line tools.
    humanURL: https://clig.dev/
    baseURL: https://clig.dev
    tags:
      - Best Practices
      - CLI Design
      - Developer Experience
      - Guidelines
      - Open Source
    properties:
      - type: Documentation
        url: https://clig.dev/
      - type: GitHubRepository
        url: https://github.com/cli-guidelines/cli-guidelines
      - type: License
        url: https://creativecommons.org/licenses/by-sa/4.0/
    x-features:
      - Codifies nine high-level design principles for human-first CLIs
      - Covers arguments, flags, subcommands, help, configuration, output, and errors
      - Provides language-agnostic guidance applicable across ecosystems
      - Open source under Creative Commons license, accepting community contributions
      - Distinguishes human-readable from machine-readable output modes
    x-useCases:
      - Reviewing existing CLI tools against an industry-recognized rubric
      - Bootstrapping a CLI design style guide for a new product or platform
      - Educating teams on CLI conventions like POSIX flags and subcommands
      - Justifying UX decisions in code reviews of CLI changes
  - aid: command-line-interface:posix-utility-conventions
    name: POSIX Utility Conventions
    description: The POSIX Utility Conventions specify the expected behavior of command line utilities including argument parsing, flag styles, end-of-options separators, and exit status. Following POSIX makes a tool feel native to UNIX-like environments and predictable when composed in pipelines and shell scripts.
    humanURL: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html
    baseURL: https://pubs.opengroup.org
    tags:
      - Conventions
      - POSIX
      - Standards
      - UNIX
    properties:
      - type: Specification
        url: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html
      - type: Reference
        url: https://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html
    x-features:
      - Defines short flags, long flags, and option arguments
      - Specifies the `--` end-of-options sentinel
      - Standardizes exit status conventions
      - Foundation for getopt and getopts utilities
    x-useCases:
      - Writing portable CLI utilities for UNIX-like systems
      - Implementing argument parsers that match user expectations
      - Documenting tool behavior in man pages
  - aid: command-line-interface:cli-frameworks
    name: CLI Frameworks Landscape
    description: A survey of widely adopted CLI frameworks across programming language ecosystems. These libraries handle argument parsing, subcommand routing, flag validation, help text generation, shell completion, and other cross-cutting concerns so developers can focus on the actual command logic.
    humanURL: https://github.com/agarrharr/awesome-cli-apps
    baseURL: https://github.com
    tags:
      - Frameworks
      - Libraries
      - Open Source
      - Tooling
    properties:
      - type: Reference
        url: https://github.com/spf13/cobra
      - type: Reference
        url: https://github.com/click-contrib
      - type: Reference
        url: https://oclif.io/
      - type: Reference
        url: https://github.com/tj/commander.js
      - type: Reference
        url: https://github.com/yargs/yargs
      - type: Reference
        url: https://docs.python.org/3/library/argparse.html
      - type: Reference
        url: https://github.com/clap-rs/clap
    x-features:
      - Cobra (Go) used by kubectl, hugo, gh, and many CNCF projects
      - Click (Python) provides decorator-based command definition
      - oclif (Node.js) used by Heroku, Salesforce, and Adobe CLIs
      - Commander.js and yargs are popular in the Node.js ecosystem
      - clap (Rust) provides derive macros for ergonomic argument parsing
      - argparse ships in the Python standard library
    x-useCases:
      - Selecting an argument parsing library for a new CLI project
      - Generating shell completion scripts for bash, zsh, and fish
      - Standardizing CLI structure across a portfolio of internal tools
      - Adding subcommands and nested command trees to an existing CLI
  - aid: command-line-interface:heroku-cli-style-guide
    name: Heroku CLI Style Guide
    description: Heroku's internal style guide for CLI design, made public to share their lessons in building a polished developer experience. Covers naming, output, error handling, JSON output, and progressive disclosure of power-user features.
    humanURL: https://devcenter.heroku.com/articles/cli-style-guide
    baseURL: https://devcenter.heroku.com
    tags:
      - Best Practices
      - Developer Experience
      - Heroku
      - Style Guide
    properties:
      - type: Documentation
        url: https://devcenter.heroku.com/articles/cli-style-guide
    x-features:
      - Real-world style guide from a CLI-first developer platform
      - Covers naming, output, errors, and machine-readable formats
      - Aligns with broader CLI Guidelines philosophy
    x-useCases:
      - Establishing tone and output conventions for a new CLI
      - Comparing alternative approaches to error reporting and progress
common:
  - type: Website
    url: https://clig.dev/
  - type: Documentation
    url: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html
  - type: Reference
    url: https://en.wikipedia.org/wiki/Command-line_interface
  - type: Guide
    url: https://devcenter.heroku.com/articles/cli-style-guide
  - type: Resources
    url: https://github.com/agarrharr/awesome-cli-apps
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
