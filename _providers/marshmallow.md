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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marshmallow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.marshmallow.com/
- group: company
  title: ''
  type: About
  url: https://www.marshmallow.com/our-story
- group: company
  title: ''
  type: Blog
  url: https://www.marshmallow.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/marshmallow-insurance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/marshmallowltd
- group: other
  title: ''
  type: OpenIDConfiguration
  url: well-known/marshmallow-openid-configuration.json
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.marshmallow.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: Authentication
  url: authentication/marshmallow-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/marshmallow-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/marshmallow-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/marshmallow-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/marshmallow-packages.yml
- group: design
  title: ''
  type: Components
  url: components/marshmallow-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/marshmallow-llms.txt
- group: start
  title: ''
  type: CustomerPortal
  url: https://account.marshmallow.com/
- group: other
  title: ''
  type: Claims
  url: https://www.marshmallow.com/claims
- group: operate
  title: ''
  type: Support
  url: https://www.marshmallow.com/help
- group: auth
  title: ''
  type: Compliance
  url: https://www.marshmallow.com/solvency-and-financial-condition-report
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.marshmallow.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.marshmallow.com/terms-and-conditions
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-25'
description: 'Marshmallow is a London-headquartered UK insurtech founded in 2017 by twins Alexander and Oliver Kent-Braham with engineer David Goate, built around a single underserved segment: people who have recently moved to the United Kingdom. Traditional UK motor underwriters ignore overseas driving history and price newcomers punitively, so Marshmallow built its own pricing, fraud and underwriting models that consume global rather than only national driving data. It is one of the small number of UK insurtechs that owns the whole value chain rather than renting a carrier''s paper: Marshmallow Financial Services Limited distributes and is authorised and regulated by the Financial Conduct Authority (FRN 797672), Marshmallow Credit Services Limited holds a separate FCA authorisation (FRN 1024606) for its car-finance product, and Marshmallow Insurance Limited is an authorised insurance undertaking regulated by the Gibraltar Financial Services Commission that underwrites motor risk and files
  an annual Solvency and Financial Condition Report. Lines of business are private motor and telematics motor, van, home (buildings, contents and personal possessions) and car finance, sold direct-to-consumer through an app and web quote flow with offices in London and Budapest. The company reached unicorn valuation in 2021 and was ranked Europe''s second fastest-growing company by the Financial Times in 2023. Its API posture is honest and narrow: Marshmallow publishes NO public, self-serve developer portal and NO downloadable OpenAPI. There is no developer., developers. or api-docs surface; api.marshmallow.com and docs.marshmallow.com exist but return 403 to anonymous callers, and account.marshmallow.com / app.marshmallow.com are consumer login walls. The only anonymously reachable machine-readable artifact is an OpenID Connect discovery document at auth.marshmallow.com, which advertises authorization-code with PKCE, client-credentials, refresh-token and token-exchange grants, mTLS client
  authentication and certificate-bound tokens, and publishes only the openid scope — real OAuth infrastructure serving Marshmallow''s own apps and partners, with no public client registration. Marshmallow is therefore a technology-first insurer whose APIs are entirely internal and partner-gated, and no ACORD, AL3, ACORD XML or NGDS reference appears anywhere on its public properties.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Marshmallow
nav: Providers
network: true
overview: 'Marshmallow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Insurtech, Property and Casualty, and Motor Insurance.


  Marshmallow''s developer surface includes engineering blog, authentication, support, and 19 more developer resources.'
random_paper: 15
scopes:
- name: Marshmallow Scopes
  scope_count: 1
  slug: marshmallow-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials/refreshToken/tokenExchange
score:
  band: emerging
  composite: 23.9
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 23.9
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marshmallow/refs/heads/main/screenshots/marshmallow-2026-07-25T230257.png
security:
- kind: authentication
  name: Marshmallow Authentication
  slug: marshmallow-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Marshmallow Domain Security
  slug: marshmallow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: marshmallow
tags:
- Insurance
- United Kingdom
- Insurtech
- Property and Casualty
- Motor Insurance
- Home Insurance
- Telematics
- Underwriting
- Claims
- Direct to Consumer
- Partner Gated
- No Public API
website: https://www.marshmallow.com/
---
