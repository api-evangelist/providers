---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: ThetaRay publishes an API developer portal at api.thetaray.com, hosted on Redocly Cloud. The portal root redirects to /openapi and then to an OIDC login at auth.cloud.redocly.com, so the API reference
  name: ThetaRay Developer Portal API Surface
  slug: thetaray-developer-portal-api-surface
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thetaray-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thetaray.com/
- group: company
  title: ''
  type: Blog
  url: https://thetaray.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://thetaray.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://thetaray.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thetaray.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thetaray.com/privacy-policy/
- group: company
  title: ''
  type: Partners
  url: https://thetaray.com/partners/
- group: design
  title: ''
  type: Vocabulary
  url: https://thetaray.com/glossary-of-terms/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/thetaray-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thetaray-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/thetaray-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thetaray-well-known.yml
coverage:
  checked: '2026-08-05'
  detail: ThetaRay's API developer portal at api.thetaray.com is a Redocly Cloud site whose every route — including /openapi and /_spec/* — 302s to an OIDC login at auth.cloud.redocly.com, and the separate docs.thetaray.com host 302s to a Microsoft Entra SAML sign-in, so the OpenAPI that portal exists to serve is readable only by existing ThetaRay customers.
  evidence:
  - status: 302
    url: https://api.thetaray.com/openapi
  - status: 401
    url: https://api.thetaray.com/_spec/openapi.yaml
  - status: 302
    url: http://docs.thetaray.com/
  - status: 401
    url: https://api.thetaray.com/mcp
  - status: 404
    url: https://api.thetaray.com/openapi.json
  - status: 200
    url: https://api.thetaray.com/.well-known/oauth-authorization-server
  reason: customer-only-docs
  state: gated
created: '2026-08-05'
description: ThetaRay is an Israeli/US financial-crime-compliance software company that applies its patented "Cognitive AI" anomaly-detection technology to anti-money-laundering (AML) transaction monitoring, sanctions and customer screening, PEP screening, and customer risk assessment for banks, fintechs and payment service providers. Its cloud-native SaaS platform ingests SWIFT and domestic payment traffic, KYC/customer data and risk indicators to surface suspected money laundering, terrorist financing and sanctions-evasion typologies in cross-border and domestic payments, with an agentic AI investigation product ("RAY") that automates and explains alert triage inside a single case manager. ThetaRay markets an API-based architecture for integrating monitoring and screening into existing workflows, and publishes a developer portal at api.thetaray.com — but that portal, the documentation host docs.thetaray.com, and every specification behind them sit behind customer SSO, so no machine-readable
  contract is publicly retrievable. Offices in New York, London, Madrid, Tel Aviv and Dubai; also distributed through the Microsoft commercial marketplace.
image: https://thetaray.com/wp-content/themes/thetaray/images/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: thetaray-mcp.yml
  slug: thetaray-mcpyml
modified: '2026-08-05'
name: ThetaRay
nav: Providers
network: true
overview: 'ThetaRay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include anti-money-laundering, financial-crime, transaction-monitoring, sanctions-screening, and kyc.


  ThetaRay''s developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 54
scopes:
- name: Thetaray Scopes
  scope_count: 4
  slug: thetaray-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 21.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 87.0
    governance: 22.9
    operational_transparency: 0.0
  previous_composite: 21.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Thetaray Authentication
  slug: thetaray-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Thetaray Domain Security
  slug: thetaray-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thetaray
tags:
- anti-money-laundering
- financial-crime
- transaction-monitoring
- sanctions-screening
- kyc
- regtech
- risk-assessment
- artificial-intelligence
- banking
- fintech
- payments
- compliance
- mcp
website: https://thetaray.com/
---
