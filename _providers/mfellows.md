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
    dynamic_client_registration: false
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://moneyfellows.com
- group: company
  title: ''
  type: About
  url: https://moneyfellows.com/en-us/about-us-page/
- group: company
  title: ''
  type: Blog
  url: https://moneyfellows.com/en-us/3elmelgeib-home/
- group: operate
  title: ''
  type: Support
  url: https://moneyfellows.com/en-us/contact-us-page/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moneyfellows.com/en-us/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moneyfellows.com/en-us/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mfellows-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mfellows-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mfellows-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mfellows-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mfellows-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mfellows-llms.txt
created: '2026-07-17'
description: Money Fellows (moneyfellows.com) is an Egyptian fintech that digitizes the traditional rotating savings and credit association (ROSCA, or "gam'eya") into app-based "money circles." Over 8 million users save collectively and access payouts and credit through flexible 6, 10, or 12-month circles, with loan amounts up to 1,200,000 EGP, plus a cashback debit card and goal-based savings. The company is regulated by the Central Bank of Egypt and backed by 500 Global. Money Fellows is a consumer (B2C) mobile-first product and publishes no public developer API, SDKs, or developer portal; the only machine-discoverable surface on the domain is the Umbraco CMS OpenID Connect / OAuth 2.0 member-auth server that backs the marketing website. This profile was surfaced as a 500 Global portfolio lead and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mfellows.png
layout: provider
modified: '2026-07-20'
name: MFellows
nav: Providers
network: true
overview: 'MFellows is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Financial-Services, Savings, and Lending.


  MFellows'' developer surface includes engineering blog, support, authentication, and 9 more developer resources.'
random_paper: 12
scopes:
- name: Mfellows Scopes
  scope_count: 2
  slug: mfellows-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 17.6
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mfellows/refs/heads/main/screenshots/mfellows-2026-08-07T172807.png
security:
- kind: authentication
  name: Mfellows Authentication
  slug: mfellows-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Mfellows Domain Security
  slug: mfellows-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mfellows
tags:
- Company
- Fintech
- Financial-Services
- Savings
- Lending
- ROSCA
- Payments
- Egypt
- Mobile
- Consumer Finance
website: https://moneyfellows.com
---
