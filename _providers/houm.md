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
  band: human-only
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
  score: 5.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/houm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://houm.com
- group: company
  title: ''
  type: Blog
  url: https://blog.houm.com
- group: operate
  title: ''
  type: Support
  url: https://help.houm.com/cl
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.houm.com/cl
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.houm.com/cl/articles/104/politic-1
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.houm.com/cl/articles/397/t-1
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/houm-com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/houm-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/houm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/houm-rate-limits.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/houm-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/houm-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/houm-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/houm-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/houm-packages.yml
coverage:
  checked: '2026-08-22'
  detail: 'Houm ships software only as an end-user product — no developer portal, no API reference and no machine-readable contract exists anywhere in its estate: developers.houm.com does not resolve, docs.houm.com is an AWS API Gateway custom domain with no route mapped (403 Missing Authentication Token), api.houm.com refuses every anonymous path with 403 Forbidden, the github.com/houm-com organization has 0 public repositories, and help.houm.com is an end-user help centre with no developer section. The only anonymously readable machine-readable surfaces are Houm''s own Auth0 OIDC discovery documents at auth.houm.com and the stock WordPress REST API on its blog host, neither of which is a Houm product API.'
  evidence:
  - status: 0
    url: https://developers.houm.com/
  - status: 403
    url: https://docs.houm.com/
  - status: 403
    url: https://api.houm.com/
  - status: 404
    url: https://houm.com/openapi.json
  - status: 200
    url: https://api.github.com/orgs/houm-com/repos
  - status: 200
    url: https://auth.houm.com/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Houm (Houm Technologies SpA) is a Chilean proptech operating a digital real-estate brokerage and rental-management marketplace across Chile, Mexico and Colombia, with operations in Santiago, Viña del Mar, Concepcion, Bogota and Ciudad de Mexico. Founded in 2018 by Benjamin Labra and Nicolas Knockaert, the company lets owners list, rent and sell apartments and houses without a guarantor (sin aval), guarantees on-time rent payment to the owner even when the tenant does not pay, and runs a network of freelance field agents ("Houmers") who photograph, show and manage properties. Its ReV pricing algorithm (houm.com/cl/algoritmo-precio) values a property online, and it also runs an investor product and a broker exchange (Houm Aliados / Canje Corredores). Houm raised a $35M Series A in 2021 led by Goodwater Capital. As of this profile Houm publishes no public developer program, API reference or machine-readable contract; its production backend at api.houm.com answers 403 to every anonymous
  request and carries no published documentation.
image: https://houm.com/static/images/seo/preview-cl.jpg
layout: provider
modified: '2026-08-22'
name: Houm
nav: Providers
network: true
overview: 'Houm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, PropTech, Property Management, and Rentals.


  Houm''s developer surface includes engineering blog, support, authentication, and 13 more developer resources.'
plans:
- name: Houm Plans Pricing
  plan_count: 0
  slug: houm-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Houm Rate Limits
  slug: houm-rate-limits
scopes:
- name: Houm Scopes
  scope_count: 0
  slug: houm-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.6
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/houm/refs/heads/main/screenshots/houm-2026-09-02T145752.png
security:
- kind: authentication
  name: Houm Authentication
  slug: houm-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Houm Domain Security
  slug: houm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: houm
tags:
- Company
- Real-Estate
- PropTech
- Property Management
- Rentals
- Marketplace
- Latin America
- Chile
- Mexico
- Colombia
website: https://houm.com
---
