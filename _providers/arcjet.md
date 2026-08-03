---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Arcjet Agentic Access
  operation_count: 2
  slug: arcjet-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 3
apis:
- description: The primary, supported interface to Arcjet. SDKs ship for Node.js, Next.js, Bun, Deno, SvelteKit, NestJS, Remix, Astro, React Router, Fastify, and Python, each wrapping the Connect/gRPC Decide protoco
  name: Arcjet SDKs
  slug: arcjet-sdks
- description: The Decide API from Arcjet — 1 operation(s) for decide.
  name: Arcjet Decide API
  slug: arcjet-decide-api
- description: The Report API from Arcjet — 1 operation(s) for report.
  name: Arcjet Report API
  slug: arcjet-report-api
artifact_total: 11
collections:
- collection_type: open
  name: Arcjet Decide API
  slug: open-arcjet
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arcjet-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arcjet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arcjet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arcjet-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arcjet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arcjet
- group: company
  title: ''
  type: Website
  url: https://arcjet.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcjet.com
- group: commercial
  title: ''
  type: Plans
  url: plans/arcjet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/arcjet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/arcjet-finops.yml
created: '2026-06-20'
description: Arcjet is a security-as-code platform for developers, delivering rate limiting, bot detection, email validation, sensitive-information detection, and a Shield WAF as building blocks embedded directly in application code via SDKs. The SDK is the primary interface; it runs a local WebAssembly analysis module and calls Arcjet's Decide service - a Connect/gRPC (protobuf) decision API at decide.arcjet.com - for stateful decisions like rate limiting and advanced bot detection.
finops:
- name: Arcjet Finops
  service_category: Security
  slug: arcjet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arcjet.png
layout: provider
modified: '2026-06-20'
name: Arcjet
nav: Providers
network: true
overview: 'Arcjet publishes 2 APIs on the [APIs.io](https://apis.io/) network: Decide API and Report API. Tagged areas include Security, Rate Limiting, Bot Detection, WAF, and Developer Security.


  Arcjet''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Arcjet Plans Pricing
  plan_count: 5
  slug: arcjet-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 4
  name: Arcjet Rate Limits
  slug: arcjet-rate-limits
score:
  band: thin
  composite: 39.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arcjet/refs/heads/main/screenshots/arcjet-2026-06-20T172415.png
security:
- kind: authentication
  name: Arcjet Authentication
  slug: arcjet-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Arcjet Domain Security
  slug: arcjet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arcjet Vulnerability Disclosure
  slug: arcjet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: arcjet
tags:
- Security
- Rate Limiting
- Bot Detection
- WAF
- Developer Security
website: https://arcjet.com
---
