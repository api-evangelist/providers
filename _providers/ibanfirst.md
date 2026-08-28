---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.2
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: 'REST API for automated cross-border payments and currency exchange: manage multi-currency accounts (wallets) and their IBANs, read balances and financial movements, create and delete beneficiaries wit'
  name: iBanFirst API
  slug: ibanfirst-api
- description: First-party hosted remote MCP server, launched with API 1.7.0 on 2026-06-05, exposing 16 read tools over wallets, balances, financial movements, payments, live FX rates, spot trades, fixed forwards an
  name: iBanFirst MCP Connector
  slug: ibanfirst-mcp-connector
- description: PSD2 access-to-account API for registered third-party providers, covering account information services (AIS), payment initiation services (PIS) and strong customer authentication. A sandbox is publish
  name: iBanFirst PSD2 XS2A API
  slug: ibanfirst-psd2-xs2a-api
artifact_total: 11
asyncapis:
- description: ''
  name: Ibanfirst Webhooks
  slug: ibanfirst-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.ibanfirst.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ibanfirst.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ibanfirst.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ibanfirst.com/api/clientapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ibanfirst.com/guides/quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.ibanfirst.com/en/
- group: company
  title: ''
  type: Blog
  url: https://blog.ibanfirst.com/en
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iBanFirst
- group: commercial
  title: ''
  type: Pricing
  url: https://ibanfirst.com/fees
- group: start
  title: ''
  type: SignUp
  url: https://info.ibanfirst.com/en/request-an-account
- group: start
  title: ''
  type: Login
  url: https://platform.ibanfirst.com/login?lang=en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ibanfirst.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ibanfirst.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/productibf/ibanfirst-rest-api-workspace/collection/d24hl8d/ibanfirst-rest-api
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ibanfirst.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ibanfirst-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ibanfirst-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.ibanfirst.com/llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ibanfirst-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ibanfirst-security.txt
- group: auth
  title: ''
  type: Security
  url: https://ibanfirst.com/security-policy.html
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibanfirst-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibanfirst-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ibanfirst-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ibanfirst-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ibanfirst-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://ibanfirst.com/psd2-api
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ibanfirst-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ibanfirst-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ibanfirst-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ibanfirst-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ibanfirst-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/ibanfirst-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ibanfirst-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ibanfirst-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ibanfirst-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ibanfirst-clientapi-overlay.yaml
created: '2026-08-17'
description: iBanFirst is a Brussels-headquartered cross-border payment and foreign-exchange platform for businesses, licensed as a payment institution by the National Bank of Belgium (company number 0849.872.824) and operating across Belgium, France, the Netherlands, Germany, Spain, Romania, Bulgaria, Italy, Hungary and the United Kingdom. It provides multi-currency "augmented currency accounts" with dedicated IBANs, SWIFT and SEPA payments with payment tracking, spot FX in 30+ currencies, and fixed forward payment contracts for currency-risk hedging. Its developer surface is a public REST API (iBanFirst API 1.6.0, 38 operations over accounts, financial movements, beneficiaries, payments, spot trades, fixed forwards, documents and webhook subscriptions), X-WSSE token authentication, HMAC-SHA256-signed webhooks for payment and trade events, a separate eIDAS/QWAC-gated PSD2 XS2A API for AIS and PIS third-party providers, and a hosted first-party remote MCP server that gives agents read access
  to treasury data.
image: https://ibanfirst.com/_next/static/media/iban-og-image.1rlnmbejef6_m.jpg
layout: provider
mcp_servers:
- description: ''
  name: iBanFirst MCP
  slug: ibanfirst-mcp
- description: ''
  name: iBanFirst MCP Server
  slug: ibanfirst-mcp-server
modified: '2026-08-17'
name: iBanFirst
nav: Providers
network: true
overview: 'iBanFirst publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech Insurtech, Cross-Border Payments, Foreign Exchange, and B2B Payments.


  The iBanFirst catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  iBanFirst''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Ibanfirst Plans Pricing
  plan_count: 1
  slug: ibanfirst-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Ibanfirst Rate Limits
  slug: ibanfirst-rate-limits
score:
  band: strong
  composite: 62.6
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 30.3
    contract_quality: 59.2
    developer_ergonomics: 66.1
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 36.8
  previous_composite: 62.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Ibanfirst Authentication
  slug: ibanfirst-authentication
  summary_line: apiKey/oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Ibanfirst Domain Security
  slug: ibanfirst-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ibanfirst Vulnerability Disclosure
  slug: ibanfirst-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ibanfirst
tags:
- Company
- Fintech Insurtech
- Cross-Border Payments
- Foreign Exchange
- B2B Payments
- Treasury
- multi-currency-accounts
- Swift
- SEPA
- PSD2
- Open Banking
- currency-risk-management
- Webhook
- MCP
- Belgium
- Europe
website: https://www.ibanfirst.com/
---
