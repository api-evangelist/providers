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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aa-audience-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aa-audience-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aa-audience-llms.txt
- group: company
  title: ''
  type: Website
  url: https://aaaudi.com
coverage:
  checked: '2026-08-12'
  detail: AA Audience ships no software to integrate with - the whole product is delivered through third-party DSPs and DMPs, and its five-page S3-hosted marketing site (homepage unchanged since March 2018) has no developer page, no docs, no spec at any path, and a Login link that is a dead href="#" button on a page with no form.
  evidence:
  - status: 200
    url: https://aaaudi.com/
  - status: 403
    url: https://aaaudi.com/openapi.json
  - status: 403
    url: https://aaaudi.com/.well-known/agent-card.json
  - status: 403
    url: https://aaaudi.com/llms.txt
  - status: 0
    url: https://docs.aaaudi.com
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: AA Audience is an adtech and data company that estimates a mobile user's credit score from their online activity using proprietary machine learning models. It collects data from partner mobile apps and ad networks, analyzes it, and connects with popular DSPs and DMPs so its clients - banks, credit card companies, and financial services firms - can target audiences interested in credit cards, loans, and financial services with guaranteed ROI. Publishers integrate a JavaScript header-bidding tag to enrich their bid stream; advertisers buy segments into their own DMP or as a DealID for their DSP, from a stated floor of $1 CPM. Surfaced as a portfolio company of 500 Global and added to the API Evangelist network. No public API, developer portal, documentation, specification, SDK, or public repository was found during enrichment - the site is five static HTML pages served from an S3 bucket whose homepage has not changed since March 2018, and the Login link in the navigation is a
  dead button on a page with no form.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aa-audience.png
layout: provider
modified: '2026-08-12'
name: AA Audience
nav: Providers
network: true
overview: AA Audience is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Data, Machine-Learning, and Credit Scoring.
plans:
- name: Aa Audience Plans Pricing
  plan_count: 0
  slug: aa-audience-plans-pricing
random_paper: 19
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 5
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aa-audience/refs/heads/main/screenshots/aa-audience-2026-07-25T181314.png
security:
- kind: domain-security
  name: Aa Audience Domain Security
  slug: aa-audience-domain-security
  summary_line: TLSv1.3
slug: aa-audience
tags:
- Company
- Advertising
- Data
- Machine-Learning
- Credit Scoring
- Financial-Services
- Audience Targeting
- Adtech
website: https://aaaudi.com
---
