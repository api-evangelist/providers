---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 71.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 28
  human_in_the_loop: 1
  name: Airtm Agentic Access
  operation_count: 69
  slug: airtm-agentic-access
  summary_line: 69 operations · 28 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: The current generation of the Airtm Enterprise Payments API. REST over HTTPS with HTTP Basic authentication (API key + secret), covering payouts (two-step create/commit), bulk payouts, payins with hos
  name: Airtm Enterprise API V2
  slug: airtm-enterprise-api-v2
- description: The legacy first-generation Airtm payments API, still published as OpenAPI 3.1.0 and served from the payments.air-pay.io host. Covers purchases/payins, payouts (including a one-step payout), operation
  name: Airtm Enterprise API V1
  slug: airtm-enterprise-api-v1
- description: The OAuth 2.0 resource server that lets a partner application move USDC in and out of an individual Airtm user's wallet on that user's behalf, read the wallet balance, and check KYC status. Authorized
  name: Airtm Wallet Resource (Connect) API
  slug: airtm-wallet-resource-connect-api
artifact_total: 11
asyncapis:
- description: ''
  name: Airtm Webhooks
  slug: airtm-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.airtm.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.airtm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.airtm.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.airtm.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.airtm.com/en/support/solutions/folders/47000770266
- group: operate
  title: ''
  type: Support
  url: https://help.airtm.com/en/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.airtm.com/en/blog/
- group: start
  title: ''
  type: SignUp
  url: https://www.airtm.com/en/select-account/
- group: start
  title: ''
  type: Login
  url: https://app.airtm.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airtm.com/en/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airtm.com/en/terms-and-conditions/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.airtm.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/airtm-trust-center.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/airtm-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/airtm-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airtm-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/airtm-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/airtm-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/airtm-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/airtm-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/airtm-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/airtm-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/airtm-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/airtm-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/airtm-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/airtm-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/airtm-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/airtm-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/airtm-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/airtm-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/airtm-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/airtm-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/airtm-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airtm-agentic-access.yml
- group: auth
  title: ''
  type: Security
  url: https://www.airtm.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/airtm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airtm-domain-security.yml
created: '2026-08-06'
description: 'Airtm is a US-registered (Airtm Inc., Delaware; FinCEN MSB #31000329787639) digital dollar wallet and cross-border payments network operating since 2015, built for freelancers, remote workers, contractors and businesses in emerging markets. Balances are held as USDC on Stellar and can be moved in and out through 500+ local payment methods, a US virtual account with ACH details, a USD virtual card, and peer-to-peer transfer. For businesses, Airtm publishes the Enterprise Payments API — a REST API for programmatic payouts to recipients in 190+ countries, hosted-checkout payins, bulk payouts, external bank and crypto accounts, withdrawals and reporting — plus an OAuth 2.0 / OIDC authorization server and a Wallet Resource (Connect) API that lets a partner application move value in and out of an individual user''s Airtm wallet on that user''s behalf.'
image: https://app.airtm.com/favicon.ico
layout: provider
modified: '2026-08-06'
name: Airtm
nav: Providers
network: true
overview: 'Airtm publishes 2 APIs on the [APIs.io](https://apis.io/) network: Enterprise API V2 and Enterprise API V1. Tagged areas include payments, payouts, cross-border-payments, fintech, and digital-wallet.


  The Airtm catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Airtm''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 31 more developer resources.'
random_paper: 89
rate_limits:
- limit_count: 1
  name: Airtm Rate Limits
  slug: airtm-rate-limits
scopes:
- name: Airtm Scopes
  scope_count: 8
  slug: airtm-scopes
  summary_line: 8 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: strong
  composite: 63.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 70.5
    developer_ergonomics: 71.7
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 71.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Airtm Authentication
  slug: airtm-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Airtm Domain Security
  slug: airtm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Airtm Vulnerability Disclosure
  slug: airtm-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Airtm Trust Center
  slug: airtm-trust-center
  summary_line: trust center published
slug: airtm
tags:
- payments
- payouts
- cross-border-payments
- fintech
- digital-wallet
- stablecoin
- usdc
- stellar
- mass-payouts
- remittances
- latin-america
- emerging-markets
- money-services-business
- oauth2
- openid-connect
website: https://www.airtm.com/
---
