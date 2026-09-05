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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mirado-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mirado.ai
- group: company
  title: ''
  type: Blog
  url: https://mirado.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://mirado.ai/get-started
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mirado.ai/privacy
- group: company
  title: ''
  type: About
  url: https://www.mirado.ai/about
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/miradoai
- group: company
  title: ''
  type: Twitter
  url: https://x.com/MiradoAI
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mirado-llms.txt
coverage:
  checked: '2026-08-12'
  detail: 'Mirado sells an integration — publishers embed its card-linked offers in their own banking apps — but publishes nothing about it: there is no developer subdomain in DNS, the only non-marketing host is app.mirado.ai which serves a /login route to anonymous callers, and the sole onboarding path is the /get-started lead form ("submit your information and our team will get back to you") routed to partnerships@mirado.ai.'
  evidence:
  - status: 200
    url: https://www.mirado.ai/get-started
  - status: 200
    url: https://app.mirado.ai/
  - status: 404
    url: https://mirado.ai/openapi.json
  - status: 404
    url: https://mirado.ai/llms.txt
  - status: 404
    url: https://mirado.ai/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: Mirado is a B2B card-linked-offer and rewards infrastructure company that sits between marketers and publishers. Marketers — from Fortune 500 retailers to local businesses — fund cash-back offers that Mirado delivers into the apps of publishers such as banks and fintech apps, and Mirado attributes the resulting sales with first-party card and bank transaction data so marketers can measure incremental lift rather than impressions. The company states a reach of more than 100 million cardholders across 15+ financial partners, and describes itself as having evolved from its origins in consumer rewards into B2B advertising infrastructure. Mirado is an early-stage company backed by Version One Ventures. As of this enrichment pass (2026-08-12) it publishes a marketing site at mirado.ai (marketers, publishers, about, blog, get-started, privacy) and a login-gated customer console at app.mirado.ai, but no developer portal, no API documentation, and no machine-readable API surface of any
  kind. Full contract discovery across all three hosts returned 404 on every OpenAPI, GraphQL, MCP, llms.txt and /.well-known/ path. Onboarding for both sides of the marketplace is a lead-capture form handled by partnerships@mirado.ai.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mirado.png
layout: provider
modified: '2026-08-12'
name: Mirado
nav: Providers
network: true
overview: 'Mirado is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Rewards, Loyalty, Card-Linked Offers, and Advertising.


  Mirado''s developer surface includes engineering blog, signup flow, and 7 more developer resources.'
plans:
- name: Mirado Plans Pricing
  plan_count: 0
  slug: mirado-plans-pricing
random_paper: 6
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mirado/refs/heads/main/screenshots/mirado-2026-08-07T183707.png
security:
- kind: domain-security
  name: Mirado Domain Security
  slug: mirado-domain-security
  summary_line: TLSv1.3 · HSTS
slug: mirado
tags:
- Company
- Rewards
- Loyalty
- Card-Linked Offers
- Advertising
- MarTech
- Publishers
- Fintech
website: https://mirado.ai
---
