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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/chemours/hosts/chemours-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chemours-hosts.yml
- group: other
  href: https://artifacts.apis.io/chemours/vendors/chemours-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chemours-vendors.yml
- group: auth
  href: https://artifacts.apis.io/chemours/security/chemours-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chemours-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chemours.com/en/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.chemours.com/investors-home/default.aspx
- group: company
  title: ''
  type: Careers
  url: https://www.chemours.com/en/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chemours
coverage:
  checked: '2026-10-19'
  detail: Chemours is a chemicals manufacturer whose chemours.com site (Cloudflare-challenged to plain GETs, readable when rendered) offers brands, SDS lookup, sustainability and investor pages but no developer program, API docs, llms.txt or developer/api subdomain.
  evidence:
  - status: 200
    url: https://www.chemours.com/en/
  - status: 404
    url: https://www.chemours.com/llms.txt
  - status: 404
    url: https://www.chemours.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-05-05'
description: 'The Chemours Company is a global chemistry company (NYSE: CC) that manufactures titanium dioxide (Ti-Pure), refrigerants and thermal management fluids (Opteon, Freon), fluoropolymers (Teflon, Nafion) and performance chemicals for industries including semiconductors, energy transition, automotive and construction. Its public website chemours.com covers brands, products, safety data sheet lookup, sustainability reporting and investor relations; no public developer program or API documentation was found.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chemours.png
layout: provider
modified: '2026-10-19'
name: Chemours
nav: Providers
network: true
overview: Chemours is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Chemicals, Manufacturing, Fluoropolymers, Refrigerants, and Titanium Dioxide.
random_paper: 6
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 24.0
    catalog_earned_first_party: 0.0
    catalog_gap: 91.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 42.9
    operational_transparency: 0.0
  previous_composite: 2.9
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
screenshot: https://apis.io/screenshots/chemours/chemours-2026-06-20T174257.png
security:
- kind: domain-security
  name: Chemours Domain Security
  slug: chemours-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chemours
tags:
- Chemicals
- Manufacturing
- Fluoropolymers
- Refrigerants
- Titanium Dioxide
- Fortune 1000
website: https://www.chemours.com/en/
---
