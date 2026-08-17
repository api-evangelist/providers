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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The Rallyware tenant API — identity, task programs, tasks and task units, unit results, badges and KPIs for a customer's field organization. A JSON-LD / Hydra REST API on API Platform (Symfony), secur
  name: Rallyware Platform API
  slug: rallyware-platform-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rallyware-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.rallyware.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rallyware.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.rallyware.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rallyware.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rallyware.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.rallyware.com/security-2
- group: auth
  title: ''
  type: Compliance
  url: https://www.rallyware.com/security-2
- group: auth
  title: ''
  type: TrustCenter
  url: security/rallyware-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rallyware-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rallyware-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rallyware
- group: build
  title: ''
  type: Packages
  url: packages/rallyware-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rallyware-packages.yml
- group: design
  title: ''
  type: Components
  url: components/rallyware-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rallyware-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rallyware-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rallyware-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rallyware-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rallyware-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rallyware-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rallyware-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rallyware-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Rallyware is an AI-powered sales performance and workforce enablement platform that guides distributed sellers, distributors, and field teams toward the next best action using real-time performance data, adaptive learning, gamification, and behavioral insights. It replaces fragmented enablement tools with a single orchestration system for large field and direct-selling organizations, and markets open APIs and pre-built connectors for CRM, POS, WFM, inventory, and HR systems. Rallyware runs a production REST API — JSON-LD/Hydra over API Platform, secured with OAuth2 — but does not publish it. There is no developer portal, no API reference and no OpenAPI, and the API is deployed one tenant per host and provisioned under an enterprise contract. The only public, machine-readable description of that API is Rallyware's own React Native SDK on npm, which ships the API client, its OAuth2 auth strategies, and an embeddable component library; the artifacts in this repository are derived
  from it.
image: https://www.rallyware.com/wp-content/uploads/2026/03/featured-image.png
layout: provider
modified: '2026-08-14'
name: Rallyware
nav: Providers
network: true
overview: 'Rallyware publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales Enablement, Workforce Enablement, Learning and Development, and Performance Management.


  Rallyware''s developer surface includes engineering blog, support, authentication, and 21 more developer resources.'
plans:
- name: Rallyware Plans Pricing
  plan_count: 0
  slug: rallyware-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 0
  name: Rallyware Rate Limits
  slug: rallyware-rate-limits
score:
  band: emerging
  composite: 24.6
  delta: 8.8
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 15.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
security:
- kind: authentication
  name: Rallyware Authentication
  slug: rallyware-authentication
  summary_line: oauth2/http · 4 schemes
- kind: domain-security
  name: Rallyware Domain Security
  slug: rallyware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rallyware Vulnerability Disclosure
  slug: rallyware-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Rallyware Trust Center
  slug: rallyware-trust-center
  summary_line: SOC 2, GDPR
slug: rallyware
tags:
- Company
- Sales Enablement
- Workforce Enablement
- Learning and Development
- Performance Management
- Gamification
- Direct Selling
- Enterprise Software
website: https://www.rallyware.com/
---
