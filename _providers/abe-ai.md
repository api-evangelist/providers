---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://abe.ai/'', ''status'': 301, ''note'': ''declared website redirects to https://www.yodlee.com/technology — a different registrable domain (abe.ai -> yodlee.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abe-ai-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/abe-ai-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://abe.ai/
created: '2026-07-17'
description: Abe AI was a conversational-AI platform for banks and credit unions, delivering a financial virtual assistant (chatbot and voice) across web, mobile, SMS, and smart-speaker channels so consumers could check balances, track spending, and bank by natural language. Founded in Orlando, Florida and backed by Techstars, Abe AI was acquired by Envestnet | Yodlee in 2019; its conversational-banking technology was folded into Yodlee's fintech data platform. The abe.ai domain now 301-redirects to yodlee.com/fintech/conversational-ai and no longer operates an independent developer or API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/abe-ai.png
layout: provider
modified: '2026-07-17'
name: Abe AI
nav: Providers
network: true
overview: Abe AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Conversational AI, Financial-Services, Banking, and Chatbots.
random_paper: 18
score:
  band: minimal
  composite: 1.5
  coverage:
    artifact_dirs: 3
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
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abe-ai/refs/heads/main/screenshots/abe-ai-2026-07-25T181342.png
security:
- kind: domain-security
  name: Abe Ai Domain Security
  slug: abe-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: abe-ai
tags:
- Company
- Conversational AI
- Financial-Services
- Banking
- Chatbots
- Virtual Assistant
- Fintech
- Acquired
website: https://abe.ai/
---
