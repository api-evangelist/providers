---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The OAuth 2.0 authorization server that fronts the SiFive Cloud Services (SCS) portal at scs.sifive.com, where SiFive Core Designer and the rest of the SiFive development tooling are delivered. It pub
  name: SiFive Cloud Services OAuth 2.0
  slug: sifive-cloud-services-oauth
artifact_total: 7
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sifive-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.sifive.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sifive.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.sifive.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sifive.com/software
- group: operate
  title: ''
  type: Support
  url: https://support.sifive.com/
- group: operate
  title: ''
  type: Community
  url: https://forums.sifive.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sifive.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.sifive.com/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sifive
- group: start
  title: ''
  type: SignUp
  url: https://scs.sifive.com/accounts/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sifive.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sifive.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.sifive.com/psirt-report-vulnerability
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sifive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sifive-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sifive-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sifive-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sifive-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/sifive-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sifive-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sifive-cli.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sifive-duh-schema.json
- group: design
  title: ''
  type: DataModel
  url: data-model/sifive-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sifive-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sifive-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sifive-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sifive-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sifive-llms.txt
created: '2026-08-05'
description: 'SiFive is a semiconductor intellectual-property company founded by the creators of the RISC-V instruction set architecture at UC Berkeley — Krste Asanovic, Yunsup Lee and Andrew Waterman — and licenses configurable RISC-V processor core IP rather than manufacturing chips. Its catalog spans the Essential (E/S/U), Performance (P500/P600/P800), Intelligence (X100/X200/X300/XM) and Automotive (E6-A/E7-A/S7-A) core families plus system IP including SiFive Insight trace and debug, IOMMU Gen 2, Shield and WorldGuard. Customers configure a Core Design and generate a downloadable Dev Kit of RTL, testbench, software and documentation through SiFive Core Designer, delivered from the SiFive Cloud Services (SCS) portal at scs.sifive.com. The public developer surface is software tooling rather than a hosted REST API: the Freedom SDK for Metal and for Linux, Freedom Studio, Freedom Tools, the SiFive Kernel Library and the open-source DUH hardware-IP description toolchain and JSON Schema published
  on npm and GitHub.'
image: https://www.sifive.com/assets/sifive-ogp.jpeg
json_schemas:
- name: Sifive Duh
  property_count: 0
  slug: sifive-duh
layout: provider
mcp_servers:
- description: ''
  name: sifive-mcp.yml
  slug: sifive-mcpyml
modified: '2026-08-05'
name: SiFive
nav: Providers
network: true
overview: 'SiFive publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, RISC-V, Processor IP, and Chip Design.


  SiFive''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, authentication, CLI, and 22 more developer resources.'
random_paper: 50
scopes:
- name: Sifive Scopes
  scope_count: 3
  slug: sifive-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 32.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 32.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Sifive Authentication
  slug: sifive-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Sifive Domain Security
  slug: sifive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sifive Vulnerability Disclosure
  slug: sifive-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sifive
tags:
- Company
- Semiconductors
- RISC-V
- Processor IP
- Chip Design
- Embedded
- Hardware
- Developer Tools
- Electronic Design Automation
- OAuth
website: https://www.sifive.com/
---
