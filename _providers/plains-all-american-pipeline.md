---
access_model:
  confidence: high
  label: No public API access — shipper tooling is customer-only behind portal logins
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.paalp.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.plains.com/ — the company moved its corporate domain from paalp.com to plains.com (probed 2026-09-03, re-confirmed 2026-09-17)''}'
  - '{''url'': ''https://www.paa-enom.com/s/'', ''status'': 302, ''note'': ''Electronic Nominations (Enom) portal JS-redirects to /s/login — Salesforce Experience Cloud, credentials required (probed 2026-09-17)''}'
  - '{''url'': ''https://shipperappl.plainsallamerican.com/s/'', ''status'': 200, ''note'': ''Shipper Application Portal — Salesforce Experience Cloud login shell, no public reference (probed 2026-09-17)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
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
  score: 17.6
  scored_at: '2026-09-17'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Investor Relations
  url: https://ir.plains.com/
- group: company
  title: ''
  type: Careers
  url: https://www.plains.com/careers/
- group: other
  title: ''
  type: Tariffs
  url: https://www.plains.com/customer-services/tariffs/
- group: company
  title: ''
  type: Website
  url: https://www.plains.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/plains-all-american
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.plains.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.plains.com/legal-notices
- group: operate
  title: ''
  type: Contact
  url: https://www.plains.com/contact-us
- group: company
  title: ''
  type: Newsroom
  url: https://www.plains.com/newsroom/news
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.plains.com/investor-relations
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plains-all-american-pipeline/refs/heads/main/security/plains-all-american-pipeline-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plains-all-american-pipeline-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plains-all-american-pipeline/refs/heads/main/well-known/plains-all-american-pipeline-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/plains-all-american-pipeline-well-known.yml
coverage:
  checked: '2026-09-17'
  detail: 'Plains is a crude-oil and NGL pipeline operator: plains.com carries tariffs, price bulletins and two login-gated Salesforce shipper portals, api.plains.com answers an empty 404 on every path, and the stub record''s developer.paalp.com / api.paalp.com hosts do not exist in DNS.'
  evidence:
  - status: 200
    url: https://www.plains.com/customers
  - status: 404
    url: https://api.plains.com/openapi.json
  - status: 302
    url: https://www.paa-enom.com/s/
  - status: 404
    url: https://www.plains.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'Plains All American Pipeline, L.P. (NASDAQ: PAA) is a Houston-based, Fortune 500 midstream energy company that owns and operates pipeline transportation, terminalling, storage and gathering assets for crude oil and natural gas liquids across the United States and Canada. Plains publishes no public API, developer portal, SDK or machine-readable contract: its only online customer surfaces are the Electronic Nominations (Enom) portal and the Shipper Application Portal, both login-gated Salesforce Experience Cloud sites, alongside public tariff and crude-oil price-bulletin pages on plains.com. This profile records that absence honestly rather than describing an API that does not exist.'
finops:
- name: Plains All American Pipeline Finops
  service_category: Midstream Energy
  slug: plains-all-american-pipeline-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plains-all-american-pipeline.png
layout: provider
modified: '2026-09-17'
name: Plains All American Pipeline
nav: Providers
network: true
overview: Plains All American Pipeline is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Pipelines, Midstream, Crude Oil, and NGL.
plans:
- name: Plains All American Pipeline Plans Pricing
  plan_count: 0
  slug: plains-all-american-pipeline-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Plains All American Pipeline Rate Limits
  slug: plains-all-american-pipeline-rate-limits
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.4
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.0
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/plains-all-american-pipeline/refs/heads/main/screenshots/plains-all-american-pipeline-2026-06-20T191746.png
security:
- kind: domain-security
  name: Plains All American Pipeline Domain Security
  slug: plains-all-american-pipeline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: plains-all-american-pipeline
tags:
- Energy
- Pipelines
- Midstream
- Crude Oil
- NGL
- Oil and Gas
- Logistics
website: https://www.plains.com
---
