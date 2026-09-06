---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.mint.com'', ''status'': 301, ''note'': ''declared website redirects to https://mint.intuit.com/ — a different registrable domain (mint.com -> intuit.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.mint.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mint-domain-security.yml
created: '2026-07-17'
description: 'Mint was a personal finance, budgeting, and money-management product originally built by Aaron Patzer and backed by First Round Capital and Uncork Capital (then SoftTech VC) before its 2009 acquisition by Intuit. Intuit shut the standalone Mint service down and reimagined its features (transaction review, spending tracking, net-worth monitoring, account linking across 17,000+ financial institutions) inside Credit Karma. Mint exposes no public developer API, developer portal, or API reference; this profile is retained as a network company record. Sector: fintech.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mint.png
layout: provider
modified: '2026-07-20'
name: Mint
nav: Providers
network: true
overview: Mint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Personal Finance, Budgeting, and Money Management.
random_paper: 20
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mint/refs/heads/main/screenshots/mint-2026-08-07T172956.png
security:
- kind: domain-security
  name: Mint Domain Security
  slug: mint-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mint
tags:
- Company
- Fintech
- Personal Finance
- Budgeting
- Money Management
- Consumer
- Intuit
website: https://www.mint.com
---
