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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://nazar.ai
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/nazar/refs/heads/main/plans/nazar-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nazar-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nazar/refs/heads/main/security/nazar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nazar-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nazar/refs/heads/main/llms/nazar-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nazar-llms.txt
- group: company
  title: ''
  type: Website
  url: https://nazar.ai
- group: start
  title: ''
  type: Login
  url: https://nazar.ai/login.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nazar
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/nazar_io
created: '2026-07-17'
description: Nazar (nazar.ai) is an AI-powered database performance and cost optimization platform that helps engineering and DBA teams monitor, analyze, and tune their databases. It supports Postgres, MySQL, SQL Server, MariaDB, Amazon Aurora, Oracle, and SAP HANA across cloud, on-premises, and hybrid environments. Capabilities include SQL.AI, an LLM-based tuning assistant, offensive SQL monitoring for slow-query detection, real-time lock visibility, and anomaly detection. Founded in Recife, Brazil and backed by 500 Global, Nazar counts financial-services and travel companies among its customers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nazar.png
layout: provider
modified: '2026-07-20'
name: Nazar
nav: Providers
network: true
overview: 'Nazar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Database, Database Monitoring, Performance, and Observability.


  Nazar''s developer surface includes pricing and 7 more developer resources.'
plans:
- name: Nazar Plans Pricing
  plan_count: 2
  slug: nazar-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.4
  facets:
    access_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/nazar/refs/heads/main/screenshots/nazar-2026-08-07T184744.png
security:
- kind: domain-security
  name: Nazar Domain Security
  slug: nazar-domain-security
  summary_line: TLSv1.3
slug: nazar
tags:
- Company
- Database
- Database Monitoring
- Performance
- Observability
- Cost Optimization
- SQL
- Artificial Intelligence
- DevOps
website: https://nazar.ai
---
