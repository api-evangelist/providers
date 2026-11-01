---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/pilotoken/hosts/pilotoken-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pilotoken-hosts.yml
- group: other
  href: https://artifacts.apis.io/pilotoken/vendors/pilotoken-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pilotoken-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.pilotoken.com/login
- group: auth
  href: https://artifacts.apis.io/pilotoken/security/pilotoken-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pilotoken-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pilotoken.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pilotoken.com/
- group: company
  title: ''
  type: Blog
  url: https://www.pilotoken.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pilotoken.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pilotoken.com/cgu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pilotoken.com/confidentialite
coverage:
  checked: '2026-10-18'
  detail: No OpenAPI or other machine‑readable contract was found at common API endpoints.
  evidence:
  - status: 404
    url: https://api.pilotoken.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: PiloToken provides a local AI request proxy that compresses and caches calls to large language model APIs, reducing token usage and costs. It integrates with popular tools like VS Code, Python agents, and various LLM providers, offering a zero‑trust, offline‑first solution that keeps data on the user's machine while delivering significant savings.
image: https://www.pilotoken.com/og-image.png
layout: provider
modified: '2026-10-18'
name: PiloToken
nav: Providers
network: true
overview: 'PiloToken is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Proxy, Cost‑Saving, and Open Source.


  PiloToken''s developer surface includes documentation, engineering blog, pricing, and 7 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pilotoken Domain Security
  slug: pilotoken-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pilotoken
tags:
- Company
- Artificial Intelligence
- Proxy
- Cost‑Saving
- Open Source
website: https://pilotoken.com/
---
