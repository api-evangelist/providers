---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Arcjet Agentic Access
  operation_count: 2
  slug: arcjet-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: The primary, supported interface to Arcjet. SDKs ship for Node.js, Next.js, Bun, Deno, SvelteKit, NestJS, Remix, Astro, React Router, Fastify, and Python, each wrapping the Connect/gRPC Decide protoco
  name: Arcjet SDKs
  slug: arcjet-sdks
- baseURL: https://decide.arcjet.com
  baseurl_source: declared
  description: The Decide API from Arcjet — 1 operation(s) for decide.
  name: Arcjet Decide API
  slug: arcjet-decide-api
- baseURL: https://decide.arcjet.com
  baseurl_source: declared
  description: The Report API from Arcjet — 1 operation(s) for report.
  name: Arcjet Report API
  slug: arcjet-report-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Arcjet Decide API
  slug: open-arcjet-decide-api
- collection_type: open
  name: Arcjet Decide Report API
  slug: open-arcjet-report-api
- collection_type: open
  name: Arcjet Decide API
  slug: open-arcjet
common:
- group: company
  title: ''
  type: Blog
  url: https://arcjet.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://arcjet.com/blog/atom
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arcjet/refs/heads/main/capabilities/arcjet-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/arcjet-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arcjet/refs/heads/main/agentic-access/arcjet-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/arcjet-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arcjet/refs/heads/main/security/arcjet-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arcjet-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arcjet/refs/heads/main/security/arcjet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcjet-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arcjet/refs/heads/main/authentication/arcjet-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/arcjet/refs/heads/main/plans/arcjet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arcjet-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/arcjet/refs/heads/main/rate-limits/arcjet-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/arcjet-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/arcjet/refs/heads/main/finops/arcjet-finops.yml
  title: ''
  type: FinOps
  url: finops/arcjet-finops.yml
created: '2026-06-20'
description: Arcjet is a security-as-code platform for developers, delivering rate limiting, bot detection, email validation, sensitive-information detection, and a Shield WAF as building blocks embedded directly in application code via SDKs. The SDK is the primary interface; it runs a local WebAssembly analysis module and calls Arcjet's Decide service - a Connect/gRPC (protobuf) decision API at decide.arcjet.com - for stateful decisions like rate limiting and advanced bot detection.
finops:
- has_sources: true
  method: generated
  name: Arcjet Finops
  primary_unit: ''
  service_category: Security
  slug: arcjet-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arcjet.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.arcjet.com over HTTP.
  name: Arcjet MCP Server
  slug: arcjet
modified: '2026-10-06'
name: Arcjet
nav: Providers
network: true
overview: 'Arcjet publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Decide API, Report API, and 1 more. Tagged areas include Security, Rate Limiting, Bot Detection, WAF, and Developer Security.


  Arcjet''s developer surface includes engineering blog, authentication, documentation, and 11 more developer resources.'
plans:
- name: Arcjet Plans Pricing
  plan_count: 5
  slug: arcjet-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Arcjet Rate Limits
  slug: arcjet-rate-limits
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 47.8
    developer_ergonomics: 39.3
    discoverability: 68.3
    operational_transparency: 10.5
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: true
    score: 0.0
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
