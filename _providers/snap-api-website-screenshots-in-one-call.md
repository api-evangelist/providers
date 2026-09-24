---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: REST/HTTP screenshot and rendering API. GET /v1/take (alias /v1/render) captures screenshots and PDFs; /v1/record for scroll/video recording; /v1/usage for plan and credit metering. API-key authentica
  name: Snap API
  slug: snap-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://snap.flyhold.in/
- group: docs
  title: ''
  type: Documentation
  url: https://snap.flyhold.in/docs.html
- group: docs
  title: ''
  type: APIReference
  url: https://snap.flyhold.in/docs.html
- group: start
  title: ''
  type: GettingStarted
  url: https://snap.flyhold.in/guides-n8n.html
- group: commercial
  title: ''
  type: Pricing
  url: https://snap.flyhold.in/pricing.md
- group: start
  title: ''
  type: SignUp
  url: https://snap.flyhold.in/register.html
- group: start
  title: ''
  type: Login
  url: https://snap.flyhold.in/login.html
- group: operate
  title: ''
  type: Support
  url: https://snap.flyhold.in/support.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snap.flyhold.in/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snap.flyhold.in/privacy.html
- group: agent
  title: ''
  type: LLMsTxt
  url: https://snap.flyhold.in/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/snap-api-website-screenshots-in-one-call/refs/heads/main/security/snap-api-website-screenshots-in-one-call-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snap-api-website-screenshots-in-one-call-domain-security.yml
created: '2026-09-17'
description: Single-endpoint website-screenshot and rendering service that captures any public URL with a Chromium engine, returning PNG/JPEG/WebP images, PDFs, or scroll/video recordings via one GET request. Designed for developers, n8n workflows, and automated pipelines. API-key authenticated (query param, X-API-Key header, or Authorization Bearer) with a perpetual free tier of 200 screenshots/month and paid Starter/Growth plans, a <=1h render cache, and credit metering exposed at /v1/usage.
image: https://snap.flyhold.in/brand/logo-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Snap API MCP Server
  slug: snap-api-mcp-server
modified: '2026-09-17'
name: Snap API
nav: Providers
network: true
overview: 'Snap API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include screenshot-api, Developer Tools, Web Capture, n8n, and Web Scraping.


  Snap API''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, and 6 more developer resources.'
plans:
- name: Snap Api Website Screenshots In One Call Plans Pricing
  plan_count: 3
  slug: snap-api-website-screenshots-in-one-call-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Snap Api Website Screenshots In One Call Rate Limits
  slug: snap-api-website-screenshots-in-one-call-rate-limits
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 46.0
    catalog_earned_first_party: 12.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 70.4
    operational_transparency: 0.0
  previous_composite: 31.3
  provenance:
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Snap Api Website Screenshots In One Call Authentication
  slug: snap-api-website-screenshots-in-one-call-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Snap Api Website Screenshots In One Call Domain Security
  slug: snap-api-website-screenshots-in-one-call-domain-security
  summary_line: TLSv1.3
slug: snap-api-website-screenshots-in-one-call
tags:
- screenshot-api
- Developer Tools
- Web Capture
- n8n
- Web Scraping
- PDF Generation
- Automation
- Rendering
website: https://snap.flyhold.in/
---
