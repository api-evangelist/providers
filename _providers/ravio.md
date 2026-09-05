---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ravio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ravio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ravio.com
created: '2026-07-17'
description: Ravio is a real-time compensation benchmarking and total-rewards platform for people and reward teams. Companies connect their HRIS to contribute anonymized headcount and pay data and, in return, access live salary, equity and benefits benchmarks segmented by role, level, location and sector, replacing static annual salary surveys. Backed by Northzone. No public developer API, docs portal or SDK surface was discovered during enrichment; security posture (Vanta trust center, domain security) was probed.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ravio.png
layout: provider
modified: '2026-07-20'
name: Ravio
nav: Providers
network: true
overview: Ravio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Compensation, Benchmarking, and Total Rewards.
random_paper: 20
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 1
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Ravio Domain Security
  slug: ravio-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Ravio Trust Center
  slug: ravio-trust-center
  summary_line: trust center published
slug: ravio
tags:
- Company
- Enterprise
- Compensation
- Benchmarking
- Total Rewards
- Human Resources
- HR Tech
- Software-as-a-Service
website: https://ravio.com
---
