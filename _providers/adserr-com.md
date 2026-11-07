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
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/adserr-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/adserr-com/llms/adserr-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adserr-com-llms.txt
- group: other
  href: https://artifacts.apis.io/adserr-com/hosts/adserr-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adserr-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adserr-com/vendors/adserr-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adserr-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/adserr-com/security/adserr-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adserr-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adserr.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://adserr.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://adserr.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adserr.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://adserr.com/blog/
coverage:
  checked: '2026-11-01'
  detail: Adserr provides healthcare marketing services and does not offer a software API.
  evidence:
  - status: 404
    url: https://adserr.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-10-31'
description: Adserr is a healthcare‑only marketing and PR agency for hospitals, clinics and diagnostic centres in Kochi and Kerala, located opposite Aster Medcity. Doctor profiles and patient education are usually planned through the hospital or clinic, around the NMC’s October 2026 guidelines.
image: https://adserr.com/favicon.svg
layout: provider
modified: '2026-10-31'
name: Adserr
nav: Providers
network: true
overview: 'Adserr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Marketing, PR, Agency, and India.


  Adserr''s developer surface includes pricing, support, engineering blog, and 7 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 11.1
  provenance:
    mcp: derived
    skills: unknown
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
security:
- kind: domain-security
  name: Adserr Com Domain Security
  slug: adserr-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: adserr-com
tags:
- Healthcare
- Marketing
- PR
- Agency
- India
website: https://adserr.com/
---
