---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Client-facing REST API for PremiaLab's portfolio analytics, quantitative strategy database, and risk reporting platform. Protected by OAuth2/OpenID Connect; access is provisioned for institutional cli
  name: PremiaLab Client API
  slug: premialab-client-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/premialab-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/premialab-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/premialab-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/premialab-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://premialab.com/
- group: company
  title: ''
  type: Blog
  url: https://premialab.com/news
- group: operate
  title: ''
  type: Support
  url: https://premialab.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://premialab.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://premialab.com/privacy
created: '2026-07-17'
description: PremiaLab is a portfolio performance and risk analytics platform for institutional investors — asset owners, asset managers, and consultants who collectively manage roughly $20 trillion in assets. Its platform provides a quantitative strategy database of more than 7,000 single- and multi-asset systematic (QIS) strategies from 18 leading investment banks, position-based risk analytics (stress tests, sensitivities and VaR across asset classes), the proprietary Premialab Pure Factors model for decomposing market risk premia, independent price verification with daily index-level reconciliation, and standardized QIS Index futures offered in partnership with Eurex. PremiaLab exposes a client-facing REST API at api.premialab.com that is protected by an OAuth2 / OpenID Connect authorization server; API access is provisioned for institutional clients rather than through self-service developer signup. This profile was surfaced as a Balderton Capital portfolio company and enriched from
  PremiaLab's public web and authentication surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/premialab.png
layout: provider
modified: '2026-07-20'
name: PremiaLab
nav: Providers
network: true
overview: 'PremiaLab publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Investment Management, and Risk Analytics.


  PremiaLab''s developer surface includes authentication, engineering blog, support, and 6 more developer resources.'
random_paper: 17
scopes:
- name: Premialab Scopes
  scope_count: 7
  slug: premialab-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Premialab Authentication
  slug: premialab-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Premialab Domain Security
  slug: premialab-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: premialab
tags:
- Company
- Financial-Services
- Fintech
- Investment Management
- Risk Analytics
- Portfolio Analytics
- Quantitative Investment Strategies
- Factor Investing
website: https://premialab.com/
---
