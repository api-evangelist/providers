---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/black-ore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blackore.ai
- group: start
  title: ''
  type: Login
  url: https://auth.blackore.ai/u/login/identifier
- group: commercial
  title: ''
  type: Pricing
  url: https://blackore.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://blackore.ai/news
- group: operate
  title: ''
  type: Support
  url: https://blackore.ai/schedule-a-call
- group: auth
  title: ''
  type: Compliance
  url: https://blackore.ai/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blackore.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blackore.ai/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/black-ore-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/black-ore-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/black-ore-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/black-ore-trust-center.yml
created: '2026-07-17'
description: Black Ore is an enterprise AI company building Tax Autopilot, an AI-native platform that automates tax preparation and review for accounting firms and financial-services professionals. Its models ingest source documents, then classify and extract data using machine learning and computer vision, compute individual (1040) and pass-through (1041/1065, K-1/K-3) returns, generate workpapers, and route results through CPA-supervised quality review, pushing prepared data into existing tax software such as CCH Axcess, Drake, Lacerte, ProSystem fx, and UltraTax. Founded in 2022 and backed by Andreessen Horowitz, Oak HC/FT, Founders Fund, General Catalyst, and Khosla Ventures.
image: https://cdn.prod.website-files.com/68ecfebb353873d3847e78ca/69e8b6da93005a6e8ddf6ac0_open-graph-black-ore.jpg
layout: provider
modified: '2026-07-18'
name: Black Ore
nav: Providers
network: true
overview: 'Black Ore is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Tax, Accounting, and Artificial Intelligence.


  Black Ore''s developer surface includes pricing, engineering blog, support, authentication, and 9 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.8
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/black-ore/refs/heads/main/screenshots/black-ore-2026-07-25T203234.png
security:
- kind: authentication
  name: Black Ore Authentication
  slug: black-ore-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Black Ore Domain Security
  slug: black-ore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Black Ore Trust Center
  slug: black-ore-trust-center
  summary_line: SOC 2 Type II
slug: black-ore
tags:
- Company
- Fintech
- Tax
- Accounting
- Artificial Intelligence
- Financial-Services
- Automation
- Machine-Learning
website: https://blackore.ai
---
