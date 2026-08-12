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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: REST API for the SafetyCulture platform — inspections, templates, assets, actions, issues, users, groups, schedules, training, credentials, and webhooks. Bearer-token auth over HTTPS.
  name: SafetyCulture API
  slug: safetyculture-api
artifact_total: 8
asyncapis:
- description: ''
  name: Safetyculture Webhooks
  slug: safetyculture-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://safetyculture.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.safetyculture.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.safetyculture.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.safetyculture.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.safetyculture.com/reference/getting-started
- group: company
  title: ''
  type: Blog
  url: https://safetyculture.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://safetyculture.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.safetyculture.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://safetyculture.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://safetyculture.com/legal/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://safetyculture.com/partner-program/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SafetyCulture
- group: operate
  title: ''
  type: StatusPage
  url: https://status.safetyculture.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/safetyculture-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/safetyculture-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/safetyculture-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/safetyculture-security.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/safetyculture-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/safetyculture-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/safetyculture-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/safetyculture-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/safetyculture-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://safetyculture.com/security
- group: build
  title: ''
  type: Packages
  url: packages/safetyculture-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/safetyculture-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/safetyculture-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/safetyculture-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/safetyculture-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/safetyculture-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://safetyculture.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/safetyculture-trust-center.yml
created: '2026-07-17'
description: SafetyCulture (formerly iAuditor) is a workplace operations and safety platform used by frontline teams to run inspections, capture and track issues, assign corrective actions, manage assets and sites, deliver training, and provision users. Its public REST API at https://api.safetyculture.io exposes more than 380 documented operations across inspections, templates, assets, actions, issues, users, groups, schedules, training, credentials, and webhooks, secured with bearer API tokens (service-user and personal). Near real-time webhooks stream a rich catalog of inspection, action, incident, media, and training events, and SCIM 2.0 supports user provisioning via Microsoft Entra ID and Okta.
image: https://safetyculture.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: safetyculture-mcp.yml
  slug: safetyculture-mcpyml
modified: '2026-07-21'
name: SafetyCulture
nav: Providers
network: true
overview: 'SafetyCulture publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Applications, Safety, Inspections, and Workplace Operations.


  The SafetyCulture catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SafetyCulture''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 25 more developer resources.'
random_paper: 32
rate_limits:
- limit_count: 6
  name: Safetyculture Rate Limits
  slug: safetyculture-rate-limits
score:
  band: strong
  composite: 58.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 71.1
  previous_composite: 58.2
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Safetyculture Authentication
  slug: safetyculture-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Safetyculture Domain Security
  slug: safetyculture-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Safetyculture Vulnerability Disclosure
  slug: safetyculture-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Safetyculture Trust Center
  slug: safetyculture-trust-center
  summary_line: SOC 2, ISO 27001
slug: safetyculture
tags:
- Company
- Business Applications
- Safety
- Inspections
- Workplace Operations
- EHS
- Compliance
- Training
- Field Service
- Webhooks
website: https://safetyculture.com
---
