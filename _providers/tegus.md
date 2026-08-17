---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The OpenID Connect / OAuth 2.0 authorization server that fronts sign-in for the Tegus platform. It is an Auth0 tenant operated by AlphaSense (DNS CNAMEs to tegus.alphasense.auth0app.com) and it publis
  name: Tegus Identity (OpenID Connect)
  slug: identity
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.tegus.com/
- group: start
  title: ''
  type: Login
  url: https://app.tegus.co/users/sign_in
- group: start
  title: ''
  type: SignUp
  url: https://www.alpha-sense.com/trial-request-tegus-ref/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tegus.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alpha-sense.com/privacy-notice/
- group: operate
  title: ''
  type: Support
  url: https://help.alpha-sense.com/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCsGxYKyEAcper1LW5vlDdJw
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/tegus_stock/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tegus-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tegus-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tegus-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tegus-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tegus-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tegus-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tegus-llms.txt
coverage:
  checked: '2026-08-05'
  detail: 'AlphaSense absorbed Tegus in July 2024: the ReadMe-hosted Tegus developer hub now 302s to /inactive, status.tegus.com (which carried an "Our Public API" component) and api/docs/developer.tegus.com|.co all return NXDOMAIN, and tegus.com is a ten-page marketing site whose only live machine-readable documents are the Auth0 OIDC discovery, RFC 8414 metadata and JWKS on auth.tegus.com.'
  evidence:
  - status: 302
    url: https://tegus.readme.io/
  - status: 404
    url: https://www.tegus.com/.well-known/security.txt
  - status: 404
    url: https://www.tegus.com/openapi.json
  - status: 403
    url: https://app.tegus.co/openapi.json
  - status: 200
    url: https://auth.tegus.com/.well-known/openid-configuration
  reason: defunct
  state: none
created: '2026-08-05'
description: 'Tegus is an investment-research platform for institutional investors, built around an expert-call transcript library of more than 260,000 compliance-reviewed 1:1 transcripts covering 27,000+ public and private companies, alongside company financial models and KPIs, SEC filings, earnings-call transcripts and a Tegus Formulas Excel add-in that streams those datapoints into analyst workbooks. AlphaSense completed its acquisition of Tegus on 8 July 2024 for approximately $930M, and Tegus now operates as a brand inside AlphaSense. The standalone Tegus developer surface has been retired with it: the ReadMe-hosted developer hub at tegus.readme.io returns 302 to /inactive, the status page that formerly carried an "Our Public API" component no longer resolves, and no OpenAPI, GraphQL SDL, MCP server or agent card is published at any tegus.com or tegus.co host. The only live machine-readable documents in the namespace are the OpenID Connect discovery, RFC 8414 authorization-server metadata
  and JWKS served by auth.tegus.com. Programmatic access to the Tegus corpus is now delivered through the AlphaSense developer platform, profiled separately in this network.'
image: https://tegus.com/images/tegus-seo-img.png
layout: provider
modified: '2026-08-05'
name: Tegus
nav: Providers
network: true
overview: 'Tegus publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Investment Research, Expert Networks, Market Intelligence, Financial Data, and Transcripts.


  Tegus'' developer surface includes signup flow, support, YouTube channel, authentication, and 11 more developer resources.'
random_paper: 105
scopes:
- name: Tegus Scopes
  scope_count: 14
  slug: tegus-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: emerging
  composite: 19.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 19.0
  provenance:
    conformance: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Tegus Authentication
  slug: tegus-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Tegus Domain Security
  slug: tegus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tegus
tags:
- Investment Research
- Expert Networks
- Market Intelligence
- Financial Data
- Transcripts
- Private Markets
- Equity Research
- OpenID Connect
- Acquired
website: https://www.tegus.com/
---
