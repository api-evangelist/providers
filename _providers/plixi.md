---
access_model:
  confidence: medium
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://plixi.com
- group: commercial
  title: ''
  type: Pricing
  url: https://plixi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://plixi.com/pricing
- group: start
  title: ''
  type: Login
  url: https://plixi.com/login
- group: company
  title: ''
  type: Blog
  url: https://plixi.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://plixi.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plixi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plixi.com/privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plixi-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/plixi-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plixi-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Plixi is a consumer Instagram-growth subscription with no developer surface at all — /api, /developers, /docs and /openapi.json return 404, no api./docs./developer. subdomain resolves, and the only /.well-known/ 200s are the marketing site's HTML single-page-app shell rather than documents.
  evidence:
  - status: 404
    url: https://plixi.com/developers
  - status: 404
    url: https://plixi.com/openapi.json
  - status: 404
    url: https://plixi.com/graphql
  - status: 200
    url: https://plixi.com/.well-known/agent-card.json
  - status: 530
    url: https://help.plixi.com/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Plixi is an AI-powered Instagram growth platform that helps influencers, businesses, e-commerce brands, and content creators gain authentic followers through organic automation rather than bots or fake accounts. The service combines paid advertising, micro-interactions, and niche audience-data clustering with a machine-learning targeting feature (AI-Match) that lets users train the algorithm by rating accounts. It provides a real-time analytics dashboard, optional expert account management (Plixi Experts), and a subscription model across Basic, Pro, and Experts tiers. Plixi is a consumer SaaS product and does not publish a public developer API; it was surfaced as a portfolio company of Canaan Partners and added to the API Evangelist network.
image: https://cdn.plixi.com/images/plixi-logo-new.png
layout: provider
modified: '2026-08-13'
name: Plixi
nav: Providers
network: true
overview: 'Plixi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social-Media, Instagram, Marketing, and Growth.


  Plixi''s developer surface includes pricing, signup flow, engineering blog, support, and 7 more developer resources.'
plans:
- name: Plixi Plans Pricing
  plan_count: 3
  slug: plixi-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Plixi Rate Limits
  slug: plixi-rate-limits
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Plixi Domain Security
  slug: plixi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: plixi
tags:
- Company
- Social-Media
- Instagram
- Marketing
- Growth
- Analytics
- Software-as-a-Service
- Influencer
website: https://plixi.com
---
