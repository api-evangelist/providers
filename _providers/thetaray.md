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
  - security
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-02'
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
  name: ThetaRay MCP Server
  slug: thetaray-mcp-server
modified: '2026-08-05'
name: ThetaRay
nav: Providers
network: true
overview: 'ThetaRay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Anti-Money Laundering, Financial Crime, Transaction Monitoring, Sanctions Screening, and KYC.


  ThetaRay''s developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 5
scopes:
- name: Thetaray Scopes
  scope_count: 4
  slug: thetaray-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 73.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 33.3
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 33.3
    operational_transparency: 0.0
  previous_composite: 24.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 53.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thetaray/refs/heads/main/screenshots/thetaray-2026-09-02T163525.png
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
- Anti-Money Laundering
- Financial Crime
- Transaction Monitoring
- Sanctions Screening
- KYC
- RegTech
- Risk Assessment
- Artificial Intelligence
- Banking
- Fintech
- Payments
- Compliance
- MCP
website: https://thetaray.com/
---
