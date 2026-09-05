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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.vystarcu.org/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vystar-credit-union
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vystar-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vystar-llms.txt
created: '2026-07-23'
description: 'VyStar Credit Union is a member-owned, not-for-profit financial cooperative headquartered in Jacksonville, Florida. Founded in 1952 as Jax Navy Federal Credit Union to serve military members at Naval Air Station Jacksonville and renamed VyStar in 2002, it is one of the largest credit unions in the United States, with roughly $14 billion in assets, more than 950,000 members, and approximately 80 branches across Florida and Georgia. It is state-chartered and federally insured by the NCUA. Like most US credit unions, VyStar publishes no public, first-party developer API program: there is no live developer portal, no downloadable OpenAPI or Swagger definition, and no documented first-party data-access API. Consumer-permissioned account data is shared with third parties through financial-data aggregators rather than a documented open API, and the United States has no single mandated open-banking contract. VyStar''s open-finance posture is therefore aggregator-mediated, with the
  emerging CFPB Section 1033 Personal Financial Data Rights rule as the relevant regulatory horizon.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23T15:30:00Z'
name: VyStar Credit Union
nav: Providers
network: true
overview: VyStar Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Credit Union, United States, and Open Finance.
random_paper: 9
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vystar/refs/heads/main/screenshots/vystar-2026-09-02T170345.png
security:
- kind: domain-security
  name: Vystar Domain Security
  slug: vystar-domain-security
  summary_line: TLSv1.2 · DMARC
slug: vystar
tags:
- Financial-Services
- Banking
- Credit Union
- United States
- Open Finance
- Consumer Finance
- Data Aggregation
website: https://www.vystarcu.org/
---
