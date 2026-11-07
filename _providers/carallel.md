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
- description: Carallel platform API (no public documentation discovered)
  name: Carallel API
  slug: carallel-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/carallel/hosts/carallel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carallel-hosts.yml
- group: other
  href: https://artifacts.apis.io/carallel/vendors/carallel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carallel-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carallel.com/terms-of-use-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carallel.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://carallel.com/news
- group: company
  title: ''
  type: Blog
  url: https://carallel.com/category/article/blog/
- group: auth
  href: https://artifacts.apis.io/carallel/security/carallel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carallel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carallel.com
coverage:
  checked: '2026-10-07'
  detail: Attempted to fetch OpenAPI spec at known endpoints on api.carallel.com but received 404 responses, and no documentation host is listed.
  evidence:
  - status: 404
    url: https://api.carallel.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Carallel provides personalized guidance and digital health tools to identify and support caregivers, helping health plans, providers, and employers improve outcomes and reduce costs. Founded in 2017, the Lake Forest‑based company offers a platform that connects caregivers with resources, advocacy, and on‑demand assistance, aiming to alleviate caregiver burden and enhance patient care quality.
image: https://carallel.com/wp-content/uploads/2021/08/identify-icon.svg
layout: provider
modified: '2026-10-06'
name: Carallel
nav: Providers
network: true
overview: 'Carallel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Caregiving, Digital Health, and Platform.


  Carallel''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 10.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/carallel/carallel-2026-11-03T123235.png
security:
- kind: domain-security
  name: Carallel Domain Security
  slug: carallel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carallel
tags:
- Company
- Healthcare
- Caregiving
- Digital Health
- Platform
- B2B
website: https://carallel.com
---
