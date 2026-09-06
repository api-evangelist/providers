---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: A powerful web service enabling software applications to retrieve consumer credit data in XML format, supporting lending and financial institution workflows.
  name: MeridianLink Credit API
  slug: meridianlink-credit-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meridianlink-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meridianlink
- group: company
  title: ''
  type: Website
  url: https://www.meridianlink.com/
- group: company
  title: ''
  type: Blog
  url: https://www.meridianlink.com/feed/
created: '2025-02-24'
description: MeridianLink provides a powerful web service enabling software applications to retrieve consumer credit data in XML format. It offers lending and credit platform solutions for financial institutions.
finops:
- name: Meridianlink Finops
  service_category: API
  slug: meridianlink-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meridianlink.png
layout: provider
modified: '2026-04-28'
name: MeridianLink
nav: Providers
network: true
overview: 'MeridianLink publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Credit Data, Financial-Services, and Lending.


  MeridianLink''s developer surface includes engineering blog and 3 more developer resources.'
plans:
- name: Meridianlink Plans Pricing
  plan_count: 3
  slug: meridianlink-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Meridianlink Rate Limits
  slug: meridianlink-rate-limits
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 7.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meridianlink/refs/heads/main/screenshots/meridianlink-2026-06-20T185220.png
security:
- kind: domain-security
  name: Meridianlink Domain Security
  slug: meridianlink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meridianlink
tags:
- Banking
- Credit Data
- Financial-Services
- Lending
website: https://www.meridianlink.com/
---
