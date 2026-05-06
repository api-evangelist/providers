---
aid: bash
name: Bash Shell
description: GNU Bash (Bourne Again SHell) is the default Unix shell and command-line interpreter on most Linux distributions and macOS. Developed by Brian Fox for the GNU Project as a free replacement for the Bourne shell, Bash provides a rich scripting language with variables, control structures, functions, I/O redirection, job control, and process management. Bash scripts are the foundational automation tool for system administration, CI/CD pipelines, DevOps tooling, and software build systems.
type: Index
x-type: opensource
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Bash
  - Command-Line
  - DevOps
  - Linux
  - Scripting
  - Shell
  - Unix
url: https://raw.githubusercontent.com/api-evangelist/bash/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
apis: []
common:
  - type: Website
    url: https://www.gnu.org/software/bash/
    name: GNU Bash
  - type: Documentation
    url: https://www.gnu.org/software/bash/manual/bash.html
    name: Bash Reference Manual
  - type: Website
    url: https://git.savannah.gnu.org/cgit/bash.git
    name: Source Code Repository
  - type: Website
    url: https://ftp.gnu.org/gnu/bash/
    name: Download
  - type: License
    url: https://www.gnu.org/licenses/gpl-3.0.html
    name: GPL v3 License
  - type: Website
    url: https://google.github.io/styleguide/shellguide.html
    name: Google Shell Style Guide
  - type: Website
    url: https://github.com/awesome-lists/awesome-bash
    name: Awesome Bash
  - type: Website
    url: https://savannah.gnu.org/bugs/?group=bash
    name: Bug Tracker
  - type: Website
    url: https://tiswww.case.edu/php/chet/bash/bashtop.html
    name: Chet Ramey - Bash Maintainer
  - name: Project Info
    type: ProjectInfo
    data:
      - name: Current Version
        description: Bash 5.2 (released October 2022), with patch releases ongoing.
      - name: Original Author
        description: Brian Fox, written in 1988 for the GNU Project as a free replacement for the Bourne shell.
      - name: Current Maintainer
        description: Chet Ramey (Case Western Reserve University) has maintained Bash since 1990.
      - name: License
        description: GNU General Public License version 3 (GPL-3.0).
      - name: Language
        description: Written in C; available on all Unix-like systems and via WSL on Windows.
      - name: Package Registry
        description: Distributed as source tarball from ftp.gnu.org/gnu/bash/ and via OS package managers (apt, yum, brew).
  - name: Key Features
    type: Features
    data:
      - name: Built-in Commands
        description: Core built-in commands (cd, echo, read, test, export, alias) executed without forking.
      - name: Shell Scripting
        description: Full scripting language with variables, arrays, conditionals, loops, and functions.
      - name: Parameter Expansion
        description: String manipulation, pattern matching, and variable substitution via parameter expansion.
      - name: I/O Redirection
        description: Redirect stdin, stdout, stderr to files, devices, and between processes with pipes.
      - name: Job Control
        description: Background and foreground process management with fg, bg, jobs, and signals.
      - name: Arithmetic Expansion
        description: Integer arithmetic via $(()) and let built-in for numeric computation in scripts.
      - name: Process Substitution
        description: Treat command output as a file using process substitution for pipeline flexibility.
      - name: Readline Integration
        description: Command-line editing with history, completion, and key bindings via GNU Readline.
      - name: Array Support
        description: Indexed and associative arrays for complex data structures in shell scripts.
      - name: Brace Expansion
        description: Generate arbitrary strings and file lists via brace expansion patterns.
  - name: Use Cases
    type: UseCases
    data:
      - name: System Administration
        description: Automate system tasks, user management, log rotation, and maintenance scripts.
      - name: CI/CD Pipelines
        description: Build, test, and deploy scripts in GitHub Actions, GitLab CI, Jenkins, and CircleCI.
      - name: DevOps Automation
        description: Infrastructure provisioning, configuration management, and deployment orchestration.
      - name: Data Processing
        description: Text processing pipelines using grep, awk, sed, and shell pipelines.
      - name: API Scripting
        description: HTTP API calls with curl and response parsing for automation and testing.
      - name: File Management
        description: Bulk file operations, directory traversal, and file transformation scripts.
      - name: Environment Management
        description: Manage environment variables, PATH, and shell configuration via .bashrc and .profile.
  - name: Key Tools
    type: Integrations
    data:
      - name: curl
      - name: grep
      - name: awk
      - name: sed
      - name: jq
      - name: make
      - name: ssh
      - name: rsync
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
