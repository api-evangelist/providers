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
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The PACER Case Locator (PCL) API allows users to programmatically search the nationwide index of federal court cases for U.S. district, bankruptcy, and appellate courts.
  name: PACER Case Locator (PCL) API
  slug: pacer-case-locator-pcl-
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pacer-case-locator-pcl--domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pacer.uscourts.gov
- group: docs
  title: ''
  type: Documentation
  url: https://pacer.uscourts.gov/file-case/developer-resources
- group: operate
  title: ''
  type: Contact
  url: mailto:developers@psc.uscourts.gov
- group: company
  title: ''
  type: Blog
  url: https://pacer.uscourts.gov/rss.xml
created: '2024-11-20'
description: The PACER Case Locator (PCL) is a nationwide index of federal court cases. The public PCL API allows users to programmatically search the PCL for federal cases across U.S. district, bankruptcy, and appellate courts using the same search functionality and dataset as the PCL web application.
finops:
- name: Pacer Case Locator Pcl  Finops
  service_category: API
  slug: pacer-case-locator-pcl--finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pacer-case-locator-pcl-.png
layout: provider
modified: '2026-04-28'
name: PACER Case Locator (PCL)
nav: Providers
network: true
overview: 'PACER Case Locator (PCL) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Courts, Federal Cases, Government, and Legal.


  PACER Case Locator (PCL)''s developer surface includes documentation, engineering blog, and 3 more developer resources.'
plans:
- name: Pacer Case Locator Pcl  Plans Pricing
  plan_count: 3
  slug: pacer-case-locator-pcl--plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Pacer Case Locator Pcl  Rate Limits
  slug: pacer-case-locator-pcl--rate-limits
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pacer-case-locator-pcl-/refs/heads/main/screenshots/pacer-case-locator-pcl--2026-06-20T191307.png
security:
- kind: domain-security
  name: Pacer Case Locator Pcl  Domain Security
  slug: pacer-case-locator-pcl--domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pacer-case-locator-pcl-
tags:
- Courts
- Federal Cases
- Government
- Legal
website: https://pacer.uscourts.gov
---
