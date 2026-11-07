---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Perch provides a digital brochure platform; no public developer documentation or API contract is published.
  name: Perch API
  slug: perch-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/perchhq-com/hosts/perchhq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/perchhq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/perchhq-com/vendors/perchhq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/perchhq-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/perchhq-com/security/perchhq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/perchhq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://perchhq.io/
coverage:
  checked: '2026-10-29'
  detail: Perch's website provides only marketing information and does not publish any developer documentation or API specifications.
  evidence:
  - status: 200
    url: https://perchhq.io/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Perch provides a SaaS platform that enables real estate agents to create digital, share‑ready brochures for property listings. By integrating with MLS data, the service lets users host listing information, photo galleries, virtual tours, videos, and supporting documents such as floor plans and title documents. The brochures are lightweight, visually appealing, and designed to be easily shared with prospective buyers.
image: https://home-display.lovable.app/__l5e/assets-v1/d8e83294-02ad-4648-8391-86955603bb38/perch-og.jpg
layout: provider
modified: '2026-10-29'
name: Perch
nav: Providers
network: true
overview: Perch is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Software-as-a-Service, Digital Brochures, and Marketing.
random_paper: 7
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 4.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/perchhq-com/perchhq-com-2026-11-03T141128.png
security:
- kind: domain-security
  name: Perchhq Com Domain Security
  slug: perchhq-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: perchhq-com
tags:
- Company
- Real Estate
- Software-as-a-Service
- Digital Brochures
- Marketing
- Realtors
website: https://perchhq.io/
---
