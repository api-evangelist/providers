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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
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
random_paper: 5
rate_limits:
- limit_count: 5
  name: Pacer Case Locator Pcl  Rate Limits
  slug: pacer-case-locator-pcl--rate-limits
score:
  band: emerging
  composite: 18.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 18.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.9
  scored_at: '2026-08-03'
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
