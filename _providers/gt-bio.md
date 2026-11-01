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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/gt-bio/hosts/gt-bio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gt-bio-hosts.yml
- group: other
  href: https://artifacts.apis.io/gt-bio/vendors/gt-bio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gt-bio-vendors.yml
- group: auth
  href: https://artifacts.apis.io/gt-bio/security/gt-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gt-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gt.bio
coverage:
  checked: '2026-10-29'
  detail: GT Bio's website does not mention any developer program, API documentation, or machine-readable contracts.
  evidence:
  - status: 200
    url: https://www.gt.bio
  reason: not-a-software-company
  state: none
created: '2026-10-29'
description: GT Bio is a biotechnology company focused on developing cell type‑specific delivery technologies for genetic medicines. Their platform, Deliveromics, uses AI‑powered in‑vivo ligand and delivery screening to discover scalable, ground‑truth‑oriented solutions that enable precise therapeutic targeting. By integrating advanced analytics and engineering, GT Bio aims to accelerate the creation of next‑generation drug delivery systems for a range of genetic therapies.
image: http://static1.squarespace.com/static/692f2929f78c400281c7bd96/t/694771fd172b3879699a5241/1766289917995/Company+Logo.png?format=1500w
layout: provider
modified: '2026-10-29'
name: GT Bio
nav: Providers
network: true
overview: GT Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Genetic Medicines, AI, Drug Delivery, and Startup.
plans:
- name: Gt Bio Plans Pricing
  plan_count: 0
  slug: gt-bio-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Gt Bio Rate Limits
  slug: gt-bio-rate-limits
scopes:
- name: Gt Bio Scopes
  scope_count: 0
  slug: gt-bio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gt Bio Authentication
  slug: gt-bio-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Gt Bio Domain Security
  slug: gt-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gt-bio
tags:
- Biotechnology
- Genetic Medicines
- AI
- Drug Delivery
- Startup
website: https://gt.bio
---
