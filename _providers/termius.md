---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: Create a new Group
  name: Termius group API
  slug: termius-group-api
- description: Create or Delete a host inside the vault or the group
  name: Termius host API
  slug: termius-host-api
artifact_total: 7
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/termius-api-bridge-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://termius.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.termius.com
- group: docs
  title: ''
  type: APIReference
  url: https://termius.com/api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://termius.com/documentation/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.termius.com/hc/en-us/
- group: company
  title: ''
  type: Blog
  url: https://termius.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/termius
- group: commercial
  title: ''
  type: Pricing
  url: https://termius.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://account.termius.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://termius.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://termius.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.termius.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/termius-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://termius.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.termius.com
- group: auth
  title: ''
  type: Compliance
  url: https://security.termius.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/termius-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/termius-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/termius-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/termius-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/termius-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/termius-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/termius-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/termius-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/termius-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/termius-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/termius-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/termius-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/termius-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/termius-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/termius-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Termius is a modern, cross-platform SSH client for DevOps professionals, network engineers, and infrastructure teams, available on Windows, macOS, Linux, iOS, iPadOS, and Android. It provides secure remote access with encrypted team vaults, shared and synced credentials, SSH keys, snippets, SFTP, port forwarding, jump hosts, and session organization. For programmatic use Termius ships the API Bridge — a self-hosted REST API (OpenAPI 3.0) that encrypts infrastructure data locally and pushes hosts and groups into a Termius Team vault — plus an official command-line client. The company also runs a Security Center with a SOC 2 report.
image: https://framerusercontent.com/images/JcjJ8OLLESSIHYJ4Rdi4fZmDkQw.png
layout: provider
mcp_servers:
- description: ''
  name: termius-mcp.yml
  slug: termius-mcpyml
modified: '2026-07-21'
name: Termius
nav: Providers
network: true
overview: 'Termius publishes 2 APIs on the [APIs.io](https://apis.io/) network: group API and host API. Tagged areas include Company, Enterprise Saas, SSH, SSH Client, and Terminal.


  Termius'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 57
score:
  band: developing
  composite: 49.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 50.0
    developer_ergonomics: 53.8
    discoverability: 66.7
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 49.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Termius Authentication
  slug: termius-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Termius Domain Security
  slug: termius-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Termius Vulnerability Disclosure
  slug: termius-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Termius Trust Center
  slug: termius-trust-center
  summary_line: SOC 2
slug: termius
tags:
- Company
- Enterprise Saas
- SSH
- SSH Client
- Terminal
- Developer Tools
- DevOps
- Infrastructure
- Security
- Remote Access
website: https://termius.com/
---
