---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.everstring.com/'', ''status'': 302, ''note'': ''declared website redirects to https://www.zoominfo.com/products/operations — a different registrable domain (everstring.com -> zoominfo.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The EverString Enrichment API exposed EverString's data cloud, AI, and machine-learning components as a micro-service - similar-company discovery, ML-generated keywords, industry classification, and f
  name: EverString Enrichment API
  slug: everstring-enrichment-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everstring-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.everstring.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.everstring.com/
- group: build
  title: ''
  type: Packages
  url: packages/everstring-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/everstring-llms.txt
created: '2026-07-17'
description: EverString was a B2B predictive marketing and sales intelligence platform that used data science, machine learning, and a proprietary business data cloud to help go-to-market teams identify their best-fit accounts. Its capabilities included predictive lead and account scoring, account-based marketing segmentation, firmographic enrichment, similar-company discovery, ML-generated keywords, and industry classification, exposed to developers through an Enrichment API on developer.everstring.com secured with access-token authentication. Founded in 2012 and backed by investors including Lightspeed Venture Partners, EverString was acquired by ZoomInfo in November 2019 and its data and predictive capabilities were folded into the ZoomInfo platform; the everstring.com website now redirects to ZoomInfo Operations and the standalone developer portal has been largely decommissioned. This profile documents the historical API surface and current public footprint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/everstring.png
layout: provider
modified: '2026-07-19'
name: Everstring
nav: Providers
network: true
overview: Everstring publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Predictive Marketing, Sales Intelligence, Data Enrichment, and Firmographics.
random_paper: 5
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/everstring/refs/heads/main/screenshots/everstring-2026-07-25T213759.png
security:
- kind: domain-security
  name: Everstring Domain Security
  slug: everstring-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: everstring
tags:
- Company
- Predictive Marketing
- Sales Intelligence
- Data Enrichment
- Firmographics
- Account Based Marketing
- Lead Scoring
- Machine-Learning
- Acquired
website: https://www.everstring.com/
---
