---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 26
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bash-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gnu.org/software/bash/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gnu.org/software/bash/manual/bash.html
- group: company
  title: ''
  type: Website
  url: https://git.savannah.gnu.org/cgit/bash.git
- group: company
  title: ''
  type: Website
  url: https://ftp.gnu.org/gnu/bash/
- group: commercial
  title: ''
  type: License
  url: https://www.gnu.org/licenses/gpl-3.0.html
- group: company
  title: ''
  type: Website
  url: https://google.github.io/styleguide/shellguide.html
- group: company
  title: ''
  type: Website
  url: https://github.com/awesome-lists/awesome-bash
- group: company
  title: ''
  type: Website
  url: https://savannah.gnu.org/bugs/?group=bash
- group: company
  title: ''
  type: Website
  url: https://tiswww.case.edu/php/chet/bash/bashtop.html
- group: other
  title: ''
  type: ProjectInfo
  url: ''
created: '2024-01-01'
description: GNU Bash (Bourne Again SHell) is the default Unix shell and command-line interpreter on most Linux distributions and macOS. Developed by Brian Fox for the GNU Project as a free replacement for the Bourne shell, Bash provides a rich scripting language with variables, control structures, functions, I/O redirection, job control, and process management. Bash scripts are the foundational automation tool for system administration, CI/CD pipelines, DevOps tooling, and software build systems.
features:
- description: Core built-in commands (cd, echo, read, test, export, alias) executed without forking.
  name: Built-in Commands
- description: Full scripting language with variables, arrays, conditionals, loops, and functions.
  name: Shell Scripting
- description: String manipulation, pattern matching, and variable substitution via parameter expansion.
  name: Parameter Expansion
- description: Redirect stdin, stdout, stderr to files, devices, and between processes with pipes.
  name: I/O Redirection
- description: Background and foreground process management with fg, bg, jobs, and signals.
  name: Job Control
- description: Integer arithmetic via $(()) and let built-in for numeric computation in scripts.
  name: Arithmetic Expansion
- description: Treat command output as a file using process substitution for pipeline flexibility.
  name: Process Substitution
- description: Command-line editing with history, completion, and key bindings via GNU Readline.
  name: Readline Integration
- description: Indexed and associative arrays for complex data structures in shell scripts.
  name: Array Support
- description: Generate arbitrary strings and file lists via brace expansion patterns.
  name: Brace Expansion
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bash.png
integrations:
- name: curl
- name: grep
- name: awk
- name: sed
- name: jq
- name: make
- name: ssh
- name: rsync
layout: provider
modified: '2026-04-21'
name: Bash Shell
nav: Providers
network: true
overview: 'Bash Shell is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Bash, Command-Line, DevOps, and Linux.


  Bash Shell''s developer surface includes documentation and 9 more developer resources.'
random_paper: 34
score:
  band: minimal
  composite: 6.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bash/refs/heads/main/screenshots/bash-2026-06-20T173028.png
security:
- kind: domain-security
  name: Bash Domain Security
  slug: bash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bash
tags:
- Automation
- Bash
- Command-Line
- DevOps
- Linux
- Scripting
- Shell
- Unix
use_cases:
- description: Automate system tasks, user management, log rotation, and maintenance scripts.
  name: System Administration
- description: Build, test, and deploy scripts in GitHub Actions, GitLab CI, Jenkins, and CircleCI.
  name: CI/CD Pipelines
- description: Infrastructure provisioning, configuration management, and deployment orchestration.
  name: DevOps Automation
- description: Text processing pipelines using grep, awk, sed, and shell pipelines.
  name: Data Processing
- description: HTTP API calls with curl and response parsing for automation and testing.
  name: API Scripting
- description: Bulk file operations, directory traversal, and file transformation scripts.
  name: File Management
- description: Manage environment variables, PATH, and shell configuration via .bashrc and .profile.
  name: Environment Management
website: https://www.gnu.org/software/bash/
---
