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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Sempra Energy runs a Google Apigee API program. api.sempra.com is the Apigee runtime gateway — an unrouted request returns the genuine Apigee messaging.adaptors.http.flow.ApplicationNotFound JSON faul
  name: Sempra Developer Portal APIs
  slug: sempra-developer-portal-apis
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sempra-energy-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sempra-energy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sempra-energy-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sempra-energy-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/sempra-energy-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sempra-energy-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sempra-energy-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/sempra-energy-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sempra.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sempra
- group: company
  title: ''
  type: Website
  url: https://www.sempra-energy.com
coverage:
  checked: '2026-08-28'
  detail: 'Sempra Energy''s Google Apigee developer portal at developer.sempra.com is publicly reachable and invites developers to "sign up today and start using Sempra APIs", but its own anonymous catalog endpoint /portals/api/sites/sempra-prod/liveportal/apis answers HTTP 200 with "apiDocs": [] and "apiProducts": [] — not one API product is published to unauthenticated visitors, so the contract, reference and operation list exist only behind portal registration and login. A live proxy is routed at https://api.sempra.com/v1 and answers every anonymous request with an Apigee oauth.v2.InvalidAccessToken 401, so the API is real and callable — just not by anyone who has not been issued a token through that portal.'
  evidence:
  - status: 200
    url: https://developer.sempra.com/portals/api/sites/sempra-prod/liveportal/apis
  - status: 200
    url: https://developer.sempra.com/portals/api/sites/sempra-prod/liveportal/menus
  - status: 401
    url: https://api.sempra.com/v1/graphql
  - status: 404
    url: https://api.sempra.com/
  - status: 200
    url: https://www.sempra.com/robots.txt
  - status: 403
    url: https://www.sempra.com/.well-known/security.txt
  reason: partner-login
  state: gated
created: '2026-03-24'
description: Sempra Energy is a San Diego-headquartered North American energy infrastructure holding company and a Fortune 500 constituent, operating regulated utilities and energy infrastructure across California, Texas and Mexico. Its businesses include San Diego Gas & Electric and Southern California Gas Company in California, Oncor Electric Delivery in Texas, and Sempra Infrastructure, which develops LNG export terminals, natural gas pipelines and renewable generation in North America. Sempra operates a Google Apigee API program — an API gateway at api.sempra.com and a developer portal at developer.sempra.com inviting developers to "sign up today and start using Sempra APIs" — but publishes no API product, contract or reference to unauthenticated visitors, so the entire integration surface sits behind portal registration.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sempra-energy.png
layout: provider
modified: '2026-08-28'
name: Sempra Energy
nav: Providers
network: true
overview: 'Sempra Energy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Energy, Utilities, Natural Gas, and Electricity.


  Sempra Energy''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Sempra Energy Plans Pricing
  plan_count: 0
  slug: sempra-energy-plans-pricing
press:
- date: '2026-05-25'
  title: Sempra Provides Strategic Update And Financial Outlook ...
  url: https://www.prnewswire.com/news-releases/sempra-provides-strategic-update-and-financial-outlook-at-virtual-investor-day-301321509.html
- date: '2026-05-25'
  title: Sempra Energy and National Renewable ...
  url: https://www.sempra.com/sempra-energy-and-national-renewable-energy-laboratory-collaborate-advance-future-net-zero-energy
- date: '2026-05-25'
  title: February 27, 2020 Sempra Energy ...
  url: https://www.sec.gov/Archives/edgar/data/0000086521/000008652120000003/ex9912019123110-k.htm
- date: '2026-05-25'
  title: Sempra Energy Unit PXiSE, Mitsui Sign Equity Investment ...
  url: https://www.sempra.com/sempra-energy-unit-pxise-mitsui-sign-equity-investment-agreement-advanced-smart-grid-control
- date: '2026-05-25'
  title: Acquired 13% stake in Sempra Infrastructure Partners for ...
  url: https://www.linkedin.com/posts/cppinvestmentsinvestissementsrpc_we-have-entered-into-a-definitive-agreement-activity-7376233520333168640-6bQZ
- date: '2026-05-13'
  title: <a href="https://www.sempra.com/newsroom/press-releases/sempra-declares-common-dividend-4" hreflang="en">Sempra Declares Common Dividend</a>
  url: https://www.sempra.com/newsroom/press-releases/sempra-declares-common-dividend-4
- date: '2026-05-12'
  title: <a href="https://www.sempra.com/newsroom/press-releases/socalgas-urges-shareholders-vote-retirement-all-outstanding-shares" hreflang="en">SoCalGas Urges Shareholders to Vote FOR Retirement of All Outstanding Shares of Preferred Stock at a Premium</a>
  url: https://www.sempra.com/newsroom/press-releases/socalgas-urges-shareholders-vote-retirement-all-outstanding-shares
- date: '2026-05-08'
  title: '<a href="https://www.sempra.com/newsroom/spotlight-articles/energy-and-national-security-conversation-with-jeffrey-w-martin" hreflang="en">Energy and National Security: Conversation with Jeffrey W. Martin and LTG H.R. McMaster </a>'
  url: https://www.sempra.com/newsroom/spotlight-articles/energy-and-national-security-conversation-with-jeffrey-w-martin
random_paper: 20
rate_limits:
- limit_count: 0
  name: Sempra Energy Rate Limits
  slug: sempra-energy-rate-limits
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Sempra Energy Authentication
  slug: sempra-energy-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sempra Energy Domain Security
  slug: sempra-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sempra-energy
tags:
- Fortune 500
- Energy
- Utilities
- Natural Gas
- Electricity
- Energy Infrastructure
- LNG
- Apigee
website: https://www.sempra-energy.com
---
