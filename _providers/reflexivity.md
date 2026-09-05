---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Reflexivity's institutional REST API. Documented by the company as "JSON REST based services" whose requests are authenticated with an OAuth 2.0 Bearer token obtained from the Reflexivity OAuth servic
  name: Reflexivity API
  slug: reflexivity-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://reflexivity.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.tgl.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.tgl.ai/
- group: company
  title: ''
  type: Blog
  url: https://reflexivity.com/en/blog
- group: operate
  title: ''
  type: Support
  url: https://support.reflexivity.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://reflexivity.com/app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reflexivity.com/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reflexivity.com/en/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reflexivity.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://reflexivity.com/en#solutions
- group: agent
  title: ''
  type: WellKnown
  url: well-known/reflexivity-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reflexivity-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reflexivity-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/reflexivity-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reflexivity-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reflexivity-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/reflexivity-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/reflexivity-packages.yml
coverage:
  checked: '2026-08-26'
  detail: Reflexivity markets a RESTful API and its own docs say the endpoints are "detailed in the OpenAPI specifications within the service documentation", but that documentation host (api-docs.tgl.ai) 301s to docs.reflexivity.com and returns a Theneo "no-project-found?reason=PASSWORD_PROTECTED" interstitial, while the spec paths under the live API host answer 401 rather than 404 — the contract exists and is served, only never anonymously.
  evidence:
  - status: 301
    url: https://api-docs.tgl.ai/
  - status: 200
    url: https://docs.reflexivity.com/no-project-found?reason=PASSWORD_PROTECTED
  - status: 401
    url: https://api.reflexivity.com/alfred/v1/openapi.json
  - status: 404
    url: https://api.reflexivity.com/openapi.json
  - status: 200
    url: https://identity.reflexivity.com/.well-known/oauth-authorization-server
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: Reflexivity (founded 2019 in New York as Toggle AI) is an institutional investment analysis platform that pairs licensed market data from S&P Global, LSEG Datastream, Cboe and Nasdaq with explainable AI agents that write and execute code to answer research questions across more than 40,000 stocks, bonds and commodities. Its published capabilities are Deep Research, Knowledge Graph, Portfolio Insights, Scenario Analysis, Document Intelligence and Smart Screening, delivered through a browser terminal and through a RESTful API sold to technology teams for custom model deployment, white-label distribution and real-time data feeds. The company raised a $30M Series B in October 2024 led by Greycroft with Interactive Brokers participating, is SOC 2 Type 2 audited annually, and gates both API credentials and its API reference behind a sales relationship.
image: https://reflexivity.com/favicon.ico
layout: provider
modified: '2026-08-26'
name: Reflexivity
nav: Providers
network: true
overview: 'Reflexivity publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Investment Analysis, Market Data, and Artificial Intelligence.


  Reflexivity''s developer surface includes documentation, API reference, engineering blog, support, signup flow, pricing, and 12 more developer resources.'
plans:
- name: Reflexivity Plans Pricing
  plan_count: 0
  slug: reflexivity-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Reflexivity Rate Limits
  slug: reflexivity-rate-limits
scopes:
- name: Reflexivity Scopes
  scope_count: 0
  slug: reflexivity-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 32.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reflexivity/refs/heads/main/screenshots/reflexivity-2026-09-02T153231.png
security:
- kind: authentication
  name: Reflexivity Authentication
  slug: reflexivity-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Reflexivity Domain Security
  slug: reflexivity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reflexivity
tags:
- Company
- Financial-Services
- Investment Analysis
- Market Data
- Artificial Intelligence
- Machine-Learning
- Fintech
- Research
- Knowledge Graph
- Agents
website: https://reflexivity.com/en
---
