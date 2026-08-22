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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.9
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://clarisights.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clarisights-mcp.yml
- group: company
  title: ''
  type: Blog
  url: https://clarisights.com/Blog/Collection
- group: start
  title: ''
  type: Login
  url: https://app.clarisights.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clarisights.com/legal/privacy
- group: auth
  title: ''
  type: Security
  url: https://clarisights.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://clarisights.com/legal/certifications
- group: auth
  title: ''
  type: TrustCenter
  url: security/clarisights-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clarisights-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clarisights-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clarisights-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clarisights-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clarisights-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clarisights-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/clarisights-packages.yml
- group: design
  title: ''
  type: Components
  url: components/clarisights-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clarisights-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/clarisights-plans-pricing.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clarisights
- group: docs
  title: ''
  type: Documentation
  url: https://help.clarisights.com/en/
- group: operate
  title: ''
  type: Support
  url: https://help.clarisights.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.clarisights.com/en/collections/3767521-using-clarisights-101
created: '2026-07-17'
description: Clarisights is an enterprise marketing analytics platform that unifies marketing data from channels, web analytics, attribution platforms, and the data warehouse into a single self-service system. Marketing teams explore data, build custom dashboards, and generate trustworthy insights without SQL or data-engineering support, accelerating reporting cycles and reducing manual spreadsheet work. Clarisights also ships a Marketing Data MCP server that connects governed marketing data to AI tools such as Claude, ChatGPT, Cursor, and Gemini, exposing discovery, query, and report-navigation tools scoped by the same workspace access controls as the UI. The platform advertises 50+ connectors, ISO 27001 certification, and SOC 2 Type 2 attestation.
image: https://clarisights.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Clarisights Marketing Data MCP
  slug: clarisights-marketing-data-mcp
modified: '2026-08-13'
name: Clarisights
nav: Providers
network: true
overview: 'Clarisights is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing Analytics, Marketing Intelligence, Business Intelligence, and Data Integration.


  Clarisights'' developer surface includes engineering blog, authentication, documentation, support, getting-started guide, and 18 more developer resources.'
plans:
- name: Clarisights Plans Pricing
  plan_count: 0
  slug: clarisights-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Clarisights Rate Limits
  slug: clarisights-rate-limits
score:
  band: emerging
  composite: 25.7
  delta: -1.9
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 27.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clarisights/refs/heads/main/screenshots/clarisights-2026-07-25T205504.png
security:
- kind: authentication
  name: Clarisights Authentication
  slug: clarisights-authentication
  summary_line: delegated-user-login · 1 scheme
- kind: domain-security
  name: Clarisights Domain Security
  slug: clarisights-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Clarisights Vulnerability Disclosure
  slug: clarisights-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Clarisights Trust Center
  slug: clarisights-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, GDPR
slug: clarisights
tags:
- Company
- Marketing Analytics
- Marketing Intelligence
- Business Intelligence
- Data Integration
- Reporting
- Dashboards
- MCP
- AI
website: https://clarisights.com/
---
