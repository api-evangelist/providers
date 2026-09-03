---
access_model:
  confidence: high
  label: No public API · Aggregator-based data access (partner-gated)
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - research
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
  url: security/td-bank-group-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/td-bank-group-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.td.com/ca/en
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/td
- group: company
  title: ''
  type: Blog
  url: https://stories.td.com/ca/en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.td.com/ca/en/privacy
- group: company
  title: ''
  type: News
  url: https://stories.td.com/ca/en/news/2023-12-14-td-bank-group-and-plaid-enter-into-north-american-data-acces
created: '2026-07-23'
description: 'TD Bank Group (The Toronto-Dominion Bank) is one of Canada''s Big Six chartered banks — a federally regulated Schedule I bank headquartered in Toronto and listed on the TSX and NYSE under the ticker TD. It is among North America''s largest banks by assets, serving roughly 27 million customers worldwide across Canadian Personal & Commercial Banking (TD Canada Trust), U.S. Retail (TD Bank, N.A. — America''s Most Convenient Bank, a separately profiled entity), and Wholesale Banking (TD Securities). Like the rest of Canada''s banking sector, TD''s open-finance posture is voluntary: Canada''s Consumer-Driven Banking framework was legislated in 2024 (Consumer-Driven Banking Act) but is not yet operational, so the Canadian parent exposes no first-party public developer API. Consumer financial-data access today is aggregator-based — TD signed a North American data-access agreement with Plaid in December 2023 — while payments run over the shared Canadian rails (Interac e-Transfer and
  Payments Canada''s Real-Time Rail, with Interac as the RTR exchange solution provider). The FDX-aligned, Akoya-based open-banking API suite published at developer.td.com belongs to the U.S. subsidiary TD Bank, N.A., not this Canadian entity.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: TD Bank Group
nav: Providers
network: true
overview: 'TD Bank Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Canada, Big Six, and Schedule I Bank.


  TD Bank Group''s developer surface includes engineering blog, product news, and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/td-bank-group/refs/heads/main/screenshots/td-bank-group-2026-09-02T162634.png
security:
- kind: domain-security
  name: Td Bank Group Domain Security
  slug: td-bank-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: td-bank-group
tags:
- Financial-Services
- Banking
- Canada
- Big Six
- Schedule I Bank
- Open Banking
- Consumer-Driven Banking
- Interac
- Payments
- Data Aggregation
website: https://www.td.com/ca/en
---
