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
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.lendinvest.com
- group: company
  title: ''
  type: Blog
  url: https://www.lendinvest.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.lendinvest.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://customerportal.lendinvest.com/s/brokerregistrationform
- group: start
  title: ''
  type: Login
  url: https://customerportal.lendinvest.com/s/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lendinvest.com/terms-and-conditions/user-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lendinvest.com/terms-and-conditions/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lend-invest
- group: build
  title: ''
  type: Packages
  url: packages/lendinvest-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lendinvest-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lendinvest-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/lendinvest-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lendinvest-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lendinvest-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lendinvest-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lendinvest-llms.txt
created: '2026-07-17'
description: LendInvest is a London-based fintech property finance platform and mortgage lender, founded in 2013 after spinning out of Montello Bridging Finance, and listed on the London Stock Exchange AIM market under the ticker LINV since July 2021. It originates and services short-term bridging finance, property development finance, buy-to-let and residential mortgages for UK intermediaries, brokers, property developers, landlords and investors, and runs a parallel capital business that lets individual, corporate and institutional investors put money into secured UK property loans. The company distributes almost entirely through mortgage intermediaries via its Mortgages Portal, and was the first UK fintech to securitise its own buy-to-let loan book. LendInvest publishes no public developer API, developer portal or SDKs; its broker and borrower integrations run through hosted portals rather than a documented public API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lendinvest.png
layout: provider
modified: '2026-07-19'
name: LendInvest
nav: Providers
network: true
overview: 'LendInvest is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Lending, Mortgages, and Property Finance.


  LendInvest''s developer surface includes engineering blog, support, signup flow, authentication, and 12 more developer resources.'
random_paper: 13
scopes:
- name: Lendinvest Scopes
  scope_count: 0
  slug: lendinvest-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.0
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 20.0
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lendinvest/refs/heads/main/screenshots/lendinvest-2026-07-25T224903.png
security:
- kind: authentication
  name: Lendinvest Authentication
  slug: lendinvest-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Lendinvest Domain Security
  slug: lendinvest-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lendinvest
tags:
- Company
- Fintech
- Lending
- Mortgages
- Property Finance
- Real-Estate
- Financial-Services
- United Kingdom
website: https://www.lendinvest.com
---
