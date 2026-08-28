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
    delegated_identity: false
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
  score: 10.8
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Better's OpenID Connect / OAuth 2.0 identity provider for partner single sign-on, backed by AWS Cognito. Endpoints and metadata are published via the standard OIDC and OAuth authorization-server disco
  name: Better Identity Provider
  slug: better-identity-provider
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.better.com
- group: company
  title: ''
  type: Blog
  url: https://www.better.com/content
- group: operate
  title: ''
  type: Support
  url: https://www.better.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.better.com/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://www.better.com/rates
- group: agent
  title: ''
  type: WellKnown
  url: well-known/better-mortgage-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/better-mortgage-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/better-mortgage-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/better-mortgage-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/better-mortgage-domain-security.yml
created: '2026-07-17'
description: Better (Better Home & Finance Company, operating as Better Mortgage) is a New York-based fintech founded in 2014 by Vishal Garg that digitizes home finance end to end. Its online platform originates purchase mortgages, refinances, home equity lines of credit (HELOC), and VA loans, and connects borrowers with title, closing, homeowners insurance (via Better Cover), and real-estate agent matching. Better was the first fintech to fund over $100 billion in home loans entirely online and markets an "AI-powered" One Day Mortgage experience. Better does not publish a general-purpose public developer API, but it operates a live OpenID Connect / OAuth 2.0 identity provider (backed by AWS Cognito) for partner single sign-on, discoverable at its /.well-known endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/better-mortgage.png
layout: provider
modified: '2026-07-18'
name: Better Mortgage
nav: Providers
network: true
overview: 'Better Mortgage publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Mortgage, Lending, and Real-Estate.


  Better Mortgage''s developer surface includes engineering blog, support, pricing, authentication, and 6 more developer resources.'
random_paper: 12
scopes:
- name: Better Mortgage Scopes
  scope_count: 4
  slug: better-mortgage-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.2
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 79.6
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 18.2
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/better-mortgage/refs/heads/main/screenshots/better-mortgage-2026-07-25T202809.png
security:
- kind: authentication
  name: Better Mortgage Authentication
  slug: better-mortgage-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Better Mortgage Domain Security
  slug: better-mortgage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: better-mortgage
tags:
- Company
- Fintech
- Mortgage
- Lending
- Real-Estate
- Home Finance
- HELOC
- OpenID Connect
website: https://www.better.com
---
