---
access_model:
  confidence: high
  label: Partner-gated · Embedded banking / BaaS (no public developer portal)
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - website
  - api-gateway-probe
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/live-oak-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.liveoak.bank/
- group: company
  title: ''
  type: Blog
  url: https://resources.liveoak.bank/blog
- group: operate
  title: ''
  type: Support
  url: https://support.liveoak.bank/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.liveoak.bank/online-privacy-notice/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/live-oak-bank
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/liveoakbank
- group: start
  title: ''
  type: SignUp
  url: https://www.liveoak.bank/get-started/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/live-oak-bank-llms.txt
created: '2026-07-23'
description: 'Live Oak Bank (Live Oak Banking Company) is a digital, branchless, North Carolina state-chartered commercial bank founded in 2008 and headquartered in Wilmington, NC, operating as the primary subsidiary of Live Oak Bancshares, Inc. (NYSE: LOB). It is the largest originator of U.S. Small Business Administration (SBA) 7(a) loans in the country and serves small businesses in all 50 states with SBA and commercial lending, high-yield business and personal savings, CDs, and business checking with treasury services. Technology-forward for a bank of its size, Live Oak runs a cloud-native Finxact core (now Fiserv) with an Apiture-based digital banking platform, and in 2024 launched an in-house embedded-banking / Banking-as-a-Service (BaaS) program that lets software companies deliver Live Oak deposit and payment products to their own customers. Its API surface is real but partner-gated: a production AWS API gateway operates at api.liveoak.bank (returning MissingAuthenticationToken to
  unauthenticated callers, with Live-Oak-specific lob-identity-id / lob-foreign-entity-id headers), but Live Oak publishes no public self-serve developer portal, no downloadable OpenAPI/Swagger, and no public API reference. Consumer-permissioned data access is available through account aggregators rather than a first-party public API, and no FDX participation or CFPB Section 1033 data-access posture is publicly documented.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Live Oak Bank
nav: Providers
network: true
overview: 'Live Oak Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Small Business Lending, and SBA.


  Live Oak Bank''s developer surface includes engineering blog, support, signup flow, and 6 more developer resources.'
random_paper: 34
score:
  band: emerging
  composite: 13.4
  delta: -1.3
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/live-oak-bank/refs/heads/main/screenshots/live-oak-bank-2026-07-25T225349.png
security:
- kind: domain-security
  name: Live Oak Bank Domain Security
  slug: live-oak-bank-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: live-oak-bank
tags:
- Financial Services
- Banking
- United States
- Small Business Lending
- SBA
- Embedded Banking
- Banking-as-a-Service
- Digital Bank
- Open Finance
website: https://www.liveoak.bank/
---
