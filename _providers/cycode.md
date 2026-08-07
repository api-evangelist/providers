---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Cycode's REST API and webhooks for the ASPM / software supply chain security platform, including the Risk Intelligence Graph (RIG) reporting API. JWT bearer authentication obtained by exchanging a Cli
  name: Cycode API
  slug: cycode-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://cycode.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cycode.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cycode.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cycode.com/
- group: company
  title: ''
  type: Blog
  url: https://cycode.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cycodehq
- group: commercial
  title: ''
  type: Pricing
  url: https://cycode.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://cycode.com/free-trial/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cycode.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cycode.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cycode.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://cycode.com/trust/
- group: auth
  title: ''
  type: Compliance
  url: https://cycode.com/trust/
- group: auth
  title: ''
  type: Security
  url: https://cycode.com/bug-bounty/
- group: build
  title: ''
  type: CLI
  url: cli/cycode-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/cycode-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cycode-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cycode-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cycode-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cycode-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cycode-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cycode-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cycode-llms.txt
created: '2026-07-17'
description: Cycode is a complete Application Security Posture Management (ASPM) and software supply chain security platform that delivers visibility, security, and integrity across the entire software development lifecycle. Its Risk Intelligence Graph (RIG) correlates findings from SAST, SCA, secrets, IaC, and container scanning into a single risk model. Cycode exposes a REST API and webhooks, an official command-line interface (the `cycode` CLI for pip/Homebrew), and an official Model Context Protocol (MCP) server for AI-assisted scanning. Founded in 2019 and backed by Insight Partners, Cycode is certified SOC 2 Type II, ISO 27001, and CSA STAR Level 1. This profile was enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cycode.png
layout: provider
mcp_servers:
- description: ''
  name: cycode-mcp.yml
  slug: cycode-mcpyml
modified: '2026-07-18'
name: Cycode
nav: Providers
network: true
overview: 'Cycode publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Application Security, Software Supply Chain Security, and ASPM.


  Cycode''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, CLI, authentication, and 16 more developer resources.'
random_paper: 66
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 36.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cycode/refs/heads/main/screenshots/cycode-2026-07-25T211037.png
security:
- kind: authentication
  name: Cycode Authentication
  slug: cycode-authentication
  summary_line: apiToken/oauth2 · 2 schemes
- kind: domain-security
  name: Cycode Domain Security
  slug: cycode-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cycode Vulnerability Disclosure
  slug: cycode-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Cycode Trust Center
  slug: cycode-trust-center
  summary_line: SOC 2 Type II, ISO 27001, CSA STAR Level 1
slug: cycode
tags:
- Company
- Cybersecurity
- Application Security
- Software Supply Chain Security
- ASPM
- DevSecOps
- Secrets Scanning
- SAST
- SCA
- Developer Tools
- MCP
- CLI
website: https://cycode.com/
---
