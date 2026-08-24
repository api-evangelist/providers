---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Icontainers Agentic Access
  operation_count: 15
  slug: icontainers-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 1
apis:
- description: The Brutus API is iContainers' published REST contract for programmatic freight quoting and booking. It exposes quote creation for FCL, LCL, air and LTL shipments, quote retrieval by UUID, price calcu
  name: iContainers Brutus API
  slug: icontainers-brutus-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/icontainers-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/icontainers-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/icontainers-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.icontainers.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.icontainers.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.icontainers.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.icontainers.com/
- group: operate
  title: ''
  type: Support
  url: https://www.icontainers.com/help/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.icontainers.com/help/
- group: company
  title: ''
  type: Blog
  url: https://www.icontainers.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://www.icontainers.com/signup/
- group: start
  title: ''
  type: Login
  url: https://www.icontainers.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.icontainers.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.icontainers.com/us/privacy-policy/
- group: design
  title: ''
  type: Conventions
  url: conventions/icontainers-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/icontainers-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/icontainers-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/icontainers-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/icontainers-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/icontainers-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/icontainers-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/icontainers-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/icontainers-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/icontainers-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/icontainers-brutus-overlay.yaml
created: '2026-08-17'
description: iContainers is a digital freight forwarder founded in 2007 in Barcelona and now part of Agility Logistics, following its 2019/2022 merger with Shipa Freight. The platform lets SMEs, importers/exporters, moving companies, freight agents and individuals search, compare, book, insure, document and track international ocean freight (FCL and LCL), air freight, air express and customs clearance across 250,000+ trade routes to 300+ destinations. Developer access is published as the "Brutus API" — an OpenAPI 3.0.0 contract rendered on developer.icontainers.com covering FCL/LCL/air/LTL quoting, rate price calculation, place/port search, booking a rate, booking track-and-trace, and booking document upload/download — secured with JWT bearer tokens. iContainers also sells a white-label freight forwarding portal, and its operational layer is supplied by the third-party platform VelocityOS.ai.
image: https://icontainers-public.s3.us-east-1.amazonaws.com/images/iContainers+Logo.svg
layout: provider
modified: '2026-08-17'
name: iContainers
nav: Providers
network: true
overview: 'iContainers publishes 1 API on the [APIs.io](https://apis.io/) network: Brutus API. Tagged areas include Company, Marketplace, Logistics, Freight, and Shipping.


  iContainers'' developer surface includes authentication, documentation, API reference, support, engineering blog, signup flow, sandbox, and 19 more developer resources.'
plans:
- name: Icontainers Plans Pricing
  plan_count: 0
  slug: icontainers-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Icontainers Rate Limits
  slug: icontainers-rate-limits
score:
  band: developing
  composite: 43.6
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 54.5
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 21.1
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Icontainers Authentication
  slug: icontainers-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Icontainers Domain Security
  slug: icontainers-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: icontainers
tags:
- Company
- Marketplace
- Logistics
- Freight
- Shipping
- Ocean Freight
- Air Freight
- Supply Chain
- Customs
- Freight Quoting
- Container Shipping
- Track and Trace
website: https://www.icontainers.com/
---
