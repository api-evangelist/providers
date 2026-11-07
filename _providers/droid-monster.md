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
- description: API reference page listed at https://droid.monster/api, but no machine‑readable specification was found.
  name: Droid API
  slug: droid-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/droid-monster/llms/droid-monster-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/droid-monster-llms.txt
- group: other
  href: https://artifacts.apis.io/droid-monster/hosts/droid-monster-hosts.yml
  title: ''
  type: Hosts
  url: hosts/droid-monster-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://droid.monster/terms
- group: start
  title: ''
  type: SignUp
  url: https://droid.monster/jobs/register-for-future-internship-opportunities-at-mujin-040c5442
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://droid.monster/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://droid.monster/news
- group: auth
  href: https://artifacts.apis.io/droid-monster/security/droid-monster-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/droid-monster-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://droid.monster/
coverage:
  checked: '2026-11-06'
  detail: Documentation page https://droid.monster/api returns HTML with no OpenAPI or other spec.
  evidence:
  - status: 404
    url: https://droid.monster/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Droid provides a structured reference platform for commercially available robots. It aggregates specifications, source documents, and manufacturer data, offering searchable, comparable units for each robot model. The site presents detailed provenance for every figure, enabling engineers, researchers, and hobbyists to verify and explore robot specifications across the industry.
image: https://droid.monster/opengraph-image
layout: provider
modified: '2026-11-05'
name: Droid
nav: Providers
network: true
overview: 'Droid is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Data, Reference, and Open Data.


  Droid''s developer surface includes signup flow and 7 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Droid Monster Domain Security
  slug: droid-monster-domain-security
  summary_line: TLSv1.3
slug: droid-monster
tags:
- Company
- Robotics
- Data
- Reference
- Open Data
website: https://droid.monster/
---
