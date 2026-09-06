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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Azure CLI is the official cross-platform command-line tool for managing Microsoft Azure resources and services from the terminal.
  name: Azure CLI
  slug: azure-cli
artifact_total: 24
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Azure/azure-cli/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Azure/azure-cli/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Azure/azure-cli/blob/dev/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Azure/azure-cli/blob/dev/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Azure/azure-cli/blob/dev/CONTRIBUTING.rst
- group: commercial
  title: ''
  type: License
  url: https://github.com/Azure/azure-cli/blob/dev/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-cli-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-cli-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://learn.microsoft.com/en-us/cli/azure/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-cli
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/cli/azure/release-notes-azure-cli
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/atom/
created: '2026-03-25'
description: Azure CLI is the official cross-platform command-line tool for managing Microsoft Azure resources and services from the terminal.
features:
- description: Runs on Windows, macOS, and Linux with identical command syntax.
  name: Cross-Platform Support
- description: Interactive shell with auto-complete and inline help for command discovery.
  name: Interactive Mode
- description: Output as JSON, YAML, table, or TSV for pipeline integration.
  name: Multiple Output Formats
- description: Filter and transform output with JMESPath query language using --query.
  name: JMESPath Querying
- description: Run Azure CLI in the browser via Azure Cloud Shell without local installation.
  name: Azure Cloud Shell
- description: Embed Azure CLI commands in Bash and PowerShell automation scripts.
  name: Bash Scripting Integration
- description: Extend CLI functionality with official and community extensions.
  name: Extension Support
- description: Authenticate with service principals for automated/non-interactive scenarios.
  name: Service Principal Auth
finops:
- name: Azure Cli Finops
  service_category: API
  slug: azure-cli-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-cli.png
integrations:
- description: Use Azure CLI in Azure DevOps pipelines with the AzureCLI task.
  name: Azure DevOps
- description: Authenticate and run Azure CLI commands in GitHub Actions workflows.
  name: GitHub Actions
- description: Complement Terraform with Azure CLI for tasks outside the Terraform provider.
  name: Terraform
- description: Access a pre-configured Azure CLI environment via browser.
  name: Azure Cloud Shell
- description: Integrated terminal support and Azure CLI extension for Visual Studio Code.
  name: VS Code
layout: provider
modified: '2026-04-19'
name: Azure CLI
nav: Providers
network: true
overview: 'Azure CLI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Provider CLI and Command Line Interface.


  Azure CLI''s developer surface includes documentation, getting-started guide, changelog, engineering blog, and 10 more developer resources.'
plans:
- name: Azure Cli Plans Pricing
  plan_count: 3
  slug: azure-cli-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Azure Cli Rate Limits
  slug: azure-cli-rate-limits
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 25.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-cli/refs/heads/main/screenshots/azure-cli-2026-06-20T172838.png
security:
- kind: domain-security
  name: Azure Cli Domain Security
  slug: azure-cli-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Azure Cli Vulnerability Disclosure
  slug: azure-cli-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: azure-cli
tags:
- Cloud Provider CLI
- Command Line Interface
use_cases:
- description: Provision Azure resources like VMs, storage accounts, and databases from the command line.
  name: Resource Provisioning
- description: Automate Azure infrastructure tasks in CI/CD pipelines and deployment scripts.
  name: DevOps Automation
- description: Query resource metrics, logs, and health status from the terminal.
  name: Monitoring and Diagnostics
- description: Perform bulk operations across multiple Azure resources in a single script.
  name: Batch Operations
- description: Complement Terraform and Bicep with scripted Azure CLI commands.
  name: Infrastructure as Code
website: https://learn.microsoft.com/en-us/cli/azure/
---
