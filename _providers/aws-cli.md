---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The AWS CLI v2 is the official command-line interface for Amazon Web Services, providing unified access to all AWS services from the terminal with auto-completion, AWS SSO support, and improved perfor
  name: AWS CLI
  slug: aws-cli
artifact_total: 22
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-cli-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-cli-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-cli-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/cli/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cli/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/aws/aws-cli
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/aws/aws-cli/blob/v2/CHANGELOG.rst
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://github.com/aws/aws-cli/issues
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/awscli
created: '2026-03-25'
description: The AWS Command Line Interface (AWS CLI) is a unified tool to manage AWS services from the command line. With just one tool to download and configure, you can control multiple AWS services and automate them through scripts. AWS CLI v2 supports all AWS services with auto-completion, AWS SSO, and improved performance. It is open-source, available on Linux, macOS, and Windows, and is the official CLI for Amazon Web Services.
features:
- description: Control all AWS services from a single command-line tool with consistent syntax and output formatting.
  name: Unified AWS Service Access
- description: Shell auto-completion for commands, subcommands, options, and resource names in bash, zsh, and fish.
  name: Auto-Completion
- description: Native AWS IAM Identity Center (SSO) integration for credential management and multi-account access.
  name: AWS SSO Support
- description: Multiple output formats including JSON, YAML, text, and table, with JMESPath query filtering.
  name: Output Formatting
- description: Supports named profiles, environment variables, instance metadata, and credential process plugins.
  name: Credential Management
- description: Interactive step-by-step wizards for complex workflows like IAM role creation and DynamoDB table setup.
  name: Wizard Commands
- description: Built-in wait commands to poll until AWS resources reach desired states like running or available.
  name: Waiters
- description: Automatic pagination with configurable page size and support for --no-paginate and --page-size flags.
  name: Pagination Control
- description: Stream large binary outputs like EC2 console logs and Lambda function logs directly to stdout.
  name: Streaming Output
- description: Extensible plugin architecture for adding custom commands and credential providers.
  name: Plugin System
finops:
- name: Aws Cli Finops
  service_category: API
  slug: aws-cli-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-cli.png
layout: provider
modified: '2026-04-19'
name: AWS CLI
nav: Providers
network: true
overview: 'AWS CLI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CLI, Cloud Computing, Command Line Interface, DevOps, and Open Source.


  AWS CLI''s developer surface includes documentation, getting-started guide, release notes, support, Stack Overflow tag, and 8 more developer resources.'
plans:
- name: Aws Cli Plans Pricing
  plan_count: 3
  slug: aws-cli-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Aws Cli Rate Limits
  slug: aws-cli-rate-limits
score:
  band: thin
  composite: 31.2
  delta: -2.1
  facets:
    commercial_clarity: 68.4
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 33.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-cli/refs/heads/main/screenshots/aws-cli-2026-06-20T172742.png
security:
- kind: domain-security
  name: Aws Cli Domain Security
  slug: aws-cli-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws Cli Vulnerability Disclosure
  slug: aws-cli-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws Cli Trust Center
  slug: aws-cli-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-cli
tags:
- CLI
- Cloud Computing
- Command Line Interface
- DevOps
- Open Source
use_cases:
- description: Automate AWS infrastructure provisioning, configuration, and teardown in CI/CD pipelines and scripts.
  name: Infrastructure Automation
- description: Manage multiple AWS accounts and regions using named profiles and AWS Organizations.
  name: Multi-Account Management
- description: Query and filter AWS resource inventories with JMESPath expressions and output formatting.
  name: Resource Querying
- description: Process multiple AWS resources in bulk using shell scripting loops and CLI output piping.
  name: Batch Operations
- description: Speed up development workflows with quick access to S3, Lambda, DynamoDB, and other services.
  name: Developer Workflows
website: https://aws.amazon.com/cli/
---
