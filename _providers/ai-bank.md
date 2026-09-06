---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  url: https://www.aibank.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ai-bank-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ai-bank-llms.txt
coverage:
  checked: '2026-08-06'
  detail: AI Bank's open-banking host open.aibank.com resolves in DNS (119.253.84.40) but never completes a TCP connection from the public internet, and the corporate site at www.aibank.com carries no developer, 开放平台 or API section anywhere in its navigation — the bank's embedded-finance integrations are reached through partner business agreements, so no contract or reference is publicly readable.
  evidence:
  - status: 200
    url: https://www.aibank.com/
  - status: 0
    url: https://open.aibank.com/
  - status: 200
    url: https://www.aibank.com/.well-known/agent-card.json
  reason: partner-login
  state: gated
created: '2026-08-06'
description: AI Bank (aiBank, 百信银行 / 中信百信银行股份有限公司 — CITIC aiBank Co., Ltd.) is a Beijing-based digital direct bank, launched in November 2017 as China's first independent legal-person direct bank, a joint venture founded by China CITIC Bank and Baidu. It operates with no physical branches, serving retail customers — particularly younger consumers — and small and micro enterprises entirely through digital channels. Its own site describes the business lines as wealth management (财富管理), consumer finance (消费金融), industrial digital finance (产业数字金融), bills and notes (票据业务) and ecosystem finance (生态金融). The bank is positioned as an open-banking operator that embeds banking capability into partner platforms, but it publishes no public developer portal, API reference or machine-readable specification; its integration surface is reached through partner business agreements rather than public self-service onboarding.
layout: provider
modified: '2026-08-06'
name: AI Bank
nav: Providers
network: true
overview: AI Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Digital Banking, Financial-Services, and Consumer Finance.
random_paper: 8
score:
  band: minimal
  composite: 1.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 1.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ai-bank/refs/heads/main/screenshots/ai-bank-2026-08-07T161057.png
security:
- kind: domain-security
  name: Ai Bank Domain Security
  slug: ai-bank-domain-security
  summary_line: no transport/DNS hardening detected
slug: ai-bank
tags:
- Company
- Banking
- Digital Banking
- Financial-Services
- Consumer Finance
- SME Lending
- Wealth Management
- Fintech
- China
website: https://www.aibank.com/
---
