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
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://blueleaf.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.blueleaf.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://www.blueleaf.com/developer/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blueleaf.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://secure.blueleaf.com/sign_in
- group: operate
  title: ''
  type: Support
  url: https://support.blueleaf.com/
- group: company
  title: ''
  type: Blog
  url: https://www.blueleaf.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blueleaf.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blueleaf.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/blueleaf-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/blueleaf-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blueleaf-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blueleaf-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/blueleaf-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.blueleaf.com/security/
- group: auth
  title: ''
  type: Security
  url: https://www.blueleaf.com/security/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blueleaf-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/blueleaf-trust-center.yml
created: '2026-07-17'
description: Blueleaf is a wealth management software platform for financial advisors and enterprise RIAs that combines a branded client portal, automated investment performance reporting, account aggregation across custodians and institutions, automated billing, and portfolio rebalancing into one system. Its data-access API lets partners pull householded account balances, holdings, and transactions without handling end-user banking credentials, and it operates an OAuth 2.0 / OpenID Connect identity provider at secure.blueleaf.com. Blueleaf is backed by 500 Global and Anthemis and was added to the API Evangelist network and enriched from its public developer, security, and OIDC discovery surfaces.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blueleaf.png
layout: provider
modified: '2026-07-18'
name: BlueLeaf
nav: Providers
network: true
overview: 'BlueLeaf is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wealth Management, Fintech, Financial Advisors, and Investment Reporting.


  BlueLeaf''s developer surface includes documentation, pricing, support, engineering blog, authentication, and 13 more developer resources.'
random_paper: 41
scopes:
- name: Blueleaf Scopes
  scope_count: 3
  slug: blueleaf-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 28.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 28.8
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blueleaf/refs/heads/main/screenshots/blueleaf-2026-07-25T203457.png
security:
- kind: authentication
  name: Blueleaf Authentication
  slug: blueleaf-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Blueleaf Domain Security
  slug: blueleaf-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Blueleaf Trust Center
  slug: blueleaf-trust-center
  summary_line: SOC 2, ISO 27001
slug: blueleaf
tags:
- Company
- Wealth Management
- Fintech
- Financial Advisors
- Investment Reporting
- Account Aggregation
- Client Portal
- OAuth
- OpenID Connect
website: https://blueleaf.com
---
