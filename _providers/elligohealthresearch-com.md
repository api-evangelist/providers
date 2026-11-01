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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/elligohealthresearch-com/hosts/elligohealthresearch-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/elligohealthresearch-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elligo.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.elligo.com/about-us/leadership
- group: auth
  href: https://artifacts.apis.io/elligohealthresearch-com/security/elligohealthresearch-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elligohealthresearch-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://elligohealthresearch.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://elligohealthresearch.com
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Elligohealthresearch is a health research company focused on accelerating clinical trial recruitment and patient engagement through technology platforms. It provides services that connect trial sponsors with participants, offering tools for data collection, monitoring, and analytics to improve trial efficiency and outcomes. Backed by Norwest Venture Partners, the company aims to streamline the clinical research process and enhance patient experiences across studies.
image: https://cdn.prod.website-files.com/68aed38c4938325f2149c859/69650cdd601c307b7b476ac4_OpenGraph.png
layout: provider
modified: '2026-10-26'
name: Elligohealthresearch
nav: Providers
network: true
overview: Elligohealthresearch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, ClinicalTrials, Research, and Technology.
random_paper: 3
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Elligohealthresearch Com Domain Security
  slug: elligohealthresearch-com-domain-security
  summary_line: TLSv1.3
slug: elligohealthresearch-com
tags:
- Company
- Health
- ClinicalTrials
- Research
- Technology
website: https://elligohealthresearch.com
---
