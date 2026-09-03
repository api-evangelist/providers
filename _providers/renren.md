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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/renren-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.renren.com/
created: '2026-07-17'
description: Renren (人人网), originally launched as Xiaonei in 2005 and renamed in 2009, was one of China's largest social networking platforms and was widely described as the "Facebook of China," especially popular among university students. Renren Inc. listed on the NYSE in 2011; the social-networking business later declined and the assets were sold in 2018. The site is now operated by Chengdu Renren Interactive Entertainment Technology Co., Ltd. and is undergoing a service upgrade. Historically Renren ran an Open Platform with an OAuth2 REST API (wiki.dev.renren.com) for third-party login and social integration; that developer surface is now defunct and no live API endpoints respond.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/renren.png
layout: provider
modified: '2026-07-20'
name: Renren
nav: Providers
network: true
overview: Renren is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Social Networking, Social-Media, and Web.
random_paper: 20
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/renren/refs/heads/main/screenshots/renren-2026-09-02T153527.png
security:
- kind: domain-security
  name: Renren Domain Security
  slug: renren-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: renren
tags:
- Company
- Consumer
- Social Networking
- Social-Media
- Web
- China
website: http://www.renren.com/
---
