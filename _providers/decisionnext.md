---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/decisionnext-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decisionnext.com/
- group: company
  title: ''
  type: Blog
  url: https://decisionnext.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://decisionnext.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://decisionnext.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://decisionnext.com/terms-conditions/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/decisionnext/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/marketplace/pp/prodview-b2s6cxniqaysm
- group: auth
  title: ''
  type: Compliance
  url: https://decisionnext.com/company/
- group: commercial
  title: ''
  type: Plans
  url: plans/decisionnext-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/decisionnext-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/decisionnext-llms.txt
coverage:
  checked: '2026-08-12'
  detail: DecisionNext ships an enterprise SaaS analytics product only — api., docs. and developer.decisionnext.com do not resolve in DNS, the 294-URL sitemap contains no developer, API or documentation page, and every /.well-known/, /openapi.json, /swagger.json and /api-docs probe on decisionnext.com returned 404; its GitHub org exists but has zero public repositories.
  evidence:
  - status: 404
    url: https://decisionnext.com/openapi.json
  - status: 404
    url: https://decisionnext.com/.well-known/api-catalog
  - status: 404
    url: https://decisionnext.com/developers
  - status: 200
    url: https://decisionnext.com/sitemap.xml
  - status: 200
    url: https://api.github.com/orgs/DecisionNext/repos
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: DecisionNext is a San Francisco-founded (2015) AI and machine-learning software company whose prescriptive analytics platform helps commodity-driven businesses decide what to buy and sell, when, at what price, and on what formula. The platform is organised in three layers — MarketView (transparent, commodity-specific price and supply forecasts built on USDA, CME and 100+ other market sources), Enterprise (scenario, formula, mix and timing optimisation through applications such as ScenarioLab, DecisionBuilder, MarketSim, DataMiner, YieldMax and MarketPosition) and Governance (executive accountability and market benchmarking). It serves food and agriculture (beef, pork, poultry, dairy, grains, edible oils) and natural resources (iron ore, thermal coal, LNG, copper, nickel, zinc, shipping). DecisionNext is delivered as a SaaS product — sold direct and through AWS Marketplace — and, as of this profiling pass, publishes no public API, SDK, developer portal or machine-readable specification.
image: https://decisionnext.com/images/dn-logo-color.svg
layout: provider
modified: '2026-08-12'
name: DecisionNext
nav: Providers
network: true
overview: 'DecisionNext is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Artificial Intelligence, Machine-Learning, and Forecasting.


  DecisionNext''s developer surface includes engineering blog, support, pricing, and 9 more developer resources.'
plans:
- name: Decisionnext Plans Pricing
  plan_count: 1
  slug: decisionnext-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Decisionnext Rate Limits
  slug: decisionnext-rate-limits
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/decisionnext/refs/heads/main/screenshots/decisionnext-2026-09-02T145238.png
security:
- kind: domain-security
  name: Decisionnext Domain Security
  slug: decisionnext-domain-security
  summary_line: TLSv1.3 · DMARC
slug: decisionnext
tags:
- Company
- Analytics
- Artificial Intelligence
- Machine-Learning
- Forecasting
- Commodities
- Agriculture
- Food and Beverage
- Mining and Natural Resources
- Supply Chain
- Procurement
- Pricing
- Risk Management
- Decision Support
- Software-as-a-Service
website: https://decisionnext.com/
---
