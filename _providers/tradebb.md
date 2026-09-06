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
api_count: 1
apis:
- description: 'TradeBB exposes a single publicly consumable machine-readable interface: an llms.txt file designed for LLM consumption. There is no public REST/GraphQL API, MCP server, or agent skills.'
  name: TradeBB
  slug: tradebb
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tradebb-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tradebb-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/tradebb-conformance.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.tradebb.ai/help-center
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tradebb.ai/help-center/getting-started/how-to-import-your-first-trades
- group: operate
  title: ''
  type: Support
  url: https://www.tradebb.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://www.tradebb.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tradebb.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.tradebb.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.tradebb.ai/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tradebb.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tradebb.ai/privacy-policy
coverage:
  checked: '2026-08-09'
  detail: TradeBB is an end-user trading-journal SaaS with no developer program at all — the only machine-readable document it serves is /llms.txt, its api.tradebb.ai backend answers every probed path with a 404 problem+json, and the apis.json the submitter cited does not exist.
  evidence:
  - status: 200
    url: https://www.tradebb.ai/llms.txt
  - status: 404
    url: https://www.tradebb.ai/apis.json
  - status: 404
    url: https://api.tradebb.ai/openapi.json
  - status: 404
    url: https://www.tradebb.ai/developers
  - status: 404
    url: https://www.tradebb.ai/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-03'
description: An automated, AI-assisted trading journal and trade-analysis tool that imports, syncs, reviews, and analyzes trades across stocks, options, futures, forex, crypto, CFD, and multi-asset markets. Offers broker-file import, read-only broker sync, performance dashboards, and a Mentor Mode for coaches and educators.
image: https://static.tradebb.ai/20251121/home.webp
layout: provider
modified: '2026-08-09'
name: TradeBB
nav: Providers
network: true
overview: 'TradeBB publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include trading-journal, Trade Analytics, Fintech, trading-tools, and Stocks.


  TradeBB''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 6 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.4
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tradebb/refs/heads/main/screenshots/tradebb-2026-09-02T164042.png
security:
- kind: domain-security
  name: Tradebb Domain Security
  slug: tradebb-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tradebb
tags:
- trading-journal
- Trade Analytics
- Fintech
- trading-tools
- Stocks
- Options
- Futures
- Forex
- Crypto
- CFD
- AI Assistant
- llms-txt
---
