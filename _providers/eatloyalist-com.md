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
    mcp_server: documented
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
  score: 18.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Loyalist hospitality platform providing loyalty and guest engagement features.
  name: Loyalist API
  slug: loyalist-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/eatloyalist-com/llms/eatloyalist-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eatloyalist-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/eatloyalist-com/well-known/eatloyalist-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/eatloyalist-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/eatloyalist-com/hosts/eatloyalist-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eatloyalist-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/eatloyalist-com/vendors/eatloyalist-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eatloyalist-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eatloyalist.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eatloyalist.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://eatloyalist.com/blog/
- group: auth
  href: https://artifacts.apis.io/eatloyalist-com/security/eatloyalist-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eatloyalist-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eatloyalist.com/
coverage:
  checked: '2026-11-06'
  detail: Documentation is hosted on Notion with no public OpenAPI or other machine‑readable contract.
  evidence:
  - status: 404
    url: https://api.eatloyalist.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: Loyalist is an AI‑powered hospitality platform that helps restaurants, hotels, and hospitality groups act on guest data. It provides tools for loyalty programs, guest engagement, and data‑driven insights to improve customer experiences and operational efficiency across the hospitality industry.
image: https://www.loyalist.com/images/og-home.jpg
layout: provider
modified: '2026-11-06'
name: Loyalist
nav: Providers
network: true
overview: 'Loyalist is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, Artificial Intelligence, Loyalty, and Data.


  Loyalist''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eatloyalist Com Domain Security
  slug: eatloyalist-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eatloyalist-com
tags:
- Company
- Hospitality
- Artificial Intelligence
- Loyalty
- Data
website: https://eatloyalist.com/
---
