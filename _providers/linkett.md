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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linkett-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linkett-llms.txt
- group: company
  title: ''
  type: Website
  url: https://linkett.com
- group: company
  title: ''
  type: About
  url: https://linkett.com/about/
- group: commercial
  title: ''
  type: Plans
  url: plans/linkett-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://linkett.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://linkett.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://linkett.com/contact/
- group: start
  title: ''
  type: Login
  url: https://portal3.linkett.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://linkett.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://linkett.com/privacy-policy/
coverage:
  checked: '2026-08-12'
  detail: Linkett sells a WiFi sensor and a hosted reporting dashboard as an end-user product only — its real application host portal3.linkett.com is a Rails customer login that returns 404 for /openapi.json, /api, /graphql and every /.well-known path, and the marketing site's full 300-URL archive history contains no developer, docs or API page at all.
  evidence:
  - status: 200
    url: https://portal3.linkett.com/login
  - status: 404
    url: https://portal3.linkett.com/openapi.json
  - status: 404
    url: https://portal3.linkett.com/graphql
  - status: 404
    url: https://sync3-1.linkett.com/.well-known/agent-card.json
  - status: 202
    url: https://linkett.com/robots.txt
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Linkett is a digital out-of-home (DOOH) analytics platform for digital signage and retail displays. A proprietary WiFi sensor mounted at the screen passively gathers audience data from nearby smartphones with no app required, and a hosted dashboard reports real-time campaign performance metrics such as impressions, dwell time, frequency and conversion rate, alongside demographic and behavioural insight, giving advertising agencies detailed client reporting and giving advertisers measurement they can tie back to return on ad spend. Linkett is a WestonExpressions Inc. company with offices in Toronto, Ontario and Mountain View, California, says it is used by 100+ digital out-of-home networks, and was surfaced through the 500 Global portfolio. It sells self-serve at $25 and $50 per month plus a one-time $130 hardware fee, with custom integrations offered only on a contact-sales enterprise tier. As of this enrichment pass Linkett publishes no public developer portal, API reference,
  SDK, or machine-readable API specification on any host it controls, and its marketing site is served behind a bot/CAPTCHA challenge that blocks automated retrieval of every path.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linkett.png
layout: provider
modified: '2026-08-12'
name: Linkett
nav: Providers
network: true
overview: 'Linkett is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Digital Signage, Digital Out Of Home, and DOOH.


  Linkett''s developer surface includes pricing, engineering blog, support, and 8 more developer resources.'
plans:
- name: Linkett Plans Pricing
  plan_count: 3
  slug: linkett-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Linkett Domain Security
  slug: linkett-domain-security
  summary_line: TLSv1.3 · DMARC
slug: linkett
tags:
- Company
- Advertising
- Digital Signage
- Digital Out Of Home
- DOOH
- Analytics
- Audience Measurement
- Retail Media
website: https://linkett.com
---
