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
  href: https://artifacts.apis.io/daymark-health/hosts/daymark-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/daymark-health-hosts.yml
- group: other
  href: https://artifacts.apis.io/daymark-health/vendors/daymark-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/daymark-health-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.daymarkhealth.com/terms-of-use
- group: auth
  href: https://artifacts.apis.io/daymark-health/security/daymark-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daymark-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.daymarkhealth.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.daymarkhealth.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Daymark Health provides 24/7 in‑home and virtual cancer care, offering a specialized team that supports patients between appointments through phone, text, video, and home visits. Their platform coordinates testing, symptom management, care navigation, and communication, aiming to keep cancer care continuous and personalized.
image: https://sbaen2mzddkfje4u.public.blob.vercel-storage.com/Daymark_Portrait_Photography_2026-03-01_22-37%204.jpg?v=1779995687866
layout: provider
modified: '2026-10-22'
name: Daymark Health
nav: Providers
network: true
overview: Daymark Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Oncology, Telehealth, and Home Care.
random_paper: 4
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 6.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 6.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/daymark-health/daymark-health-2026-11-03T130333.png
security:
- kind: domain-security
  name: Daymark Health Domain Security
  slug: daymark-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: daymark-health
tags:
- Company
- Healthcare
- Oncology
- Telehealth
- Home Care
website: https://www.daymarkhealth.com/
---
