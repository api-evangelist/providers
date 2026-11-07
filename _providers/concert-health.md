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
- description: Concert Health provides a collaborative care platform; API details are not publicly documented.
  name: Concert Health API
  slug: concert-health-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/concert-health/hosts/concert-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/concert-health-hosts.yml
- group: other
  href: https://artifacts.apis.io/concert-health/vendors/concert-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/concert-health-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://concerthealth.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://concerthealth.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://concerthealth.com/blog
- group: auth
  href: https://artifacts.apis.io/concert-health/security/concert-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/concert-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://concerthealth.com/
coverage:
  checked: '2026-10-10'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on concerthealth.com or api.concerthealth.com.
  evidence:
  - status: 0
    url: https://api.concerthealth.com/openapi.json
  - status: 404
    url: https://concerthealth.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Concert Health is a behavioral health medical group that partners with medical groups, health systems, and health plans to integrate collaborative care into primary care. They provide a turnkey solution that improves patient outcomes, with over 70,000 lives cared for nationwide. The company offers resources, research, pathways, and a blog to support partners and patients.
image: https://concerthealth.com/hubfs/2023_Website/Images/webp/img-1270x1258_FatherDaughter2a.webp
layout: provider
modified: '2026-10-10'
name: Concert Health
nav: Providers
network: true
overview: 'Concert Health is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Behavioral Health, Collaborative Care, Medical Groups, Health Systems, and Health Plans.


  Concert Health''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 7.8
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
screenshot: https://apis.io/screenshots/concert-health/concert-health-2026-11-03T125038.png
security:
- kind: domain-security
  name: Concert Health Domain Security
  slug: concert-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: concert-health
tags:
- Behavioral Health
- Collaborative Care
- Medical Groups
- Health Systems
- Health Plans
- Primary Care
website: https://concerthealth.com/
---
