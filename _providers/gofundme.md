---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.5
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: REST API (v2.0) for the GoFundMe Pro (formerly Classy) fundraising platform. 290 operations across 70 resource families — organizations, campaigns, campaign series and Studio campaigns, fundraising pa
  name: GoFundMe Pro API
  slug: gofundme-pro-api
- description: GoFundMe Pro's single sign-on service, implemented against OpenID Connect, letting third-party apps register and log people in with their Classy/GoFundMe Pro account. Authorization endpoint at login.c
  name: Classy Login (OpenID Connect SSO)
  slug: classy-login-openid-connect-sso
- description: Payment and embedded-checkout service behind GoFundMe Pro donation and registration flows. Ships a JavaScript embedded-checkout library (classypay.js) that renders a hosted checkout form into a host p
  name: Classy Pay
  slug: classy-pay
artifact_total: 11
asyncapis:
- description: ''
  name: Gofundme Webhooks
  slug: gofundme-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gofundme-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gofundme.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.gofundme.com/pro/overview/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gofundme.com/pro/overview/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.gofundme.com/pro/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.gofundme.com/pro/overview/get-started
- group: operate
  title: ''
  type: Support
  url: https://prosupport.gofundme.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://prosupport.gofundme.com/hc/en-us/sections/35654895701787-API-and-partner-apps
- group: company
  title: ''
  type: Blog
  url: https://pro.gofundme.com/c/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/classy-org
- group: commercial
  title: ''
  type: Pricing
  url: https://pro.gofundme.com/c/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://developers.gofundme.com/pro/overview/request-access
- group: start
  title: ''
  type: Login
  url: https://www.classy.org/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pro.gofundme.com/c/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pro.gofundme.com/c/legal/privacy-notice/
- group: build
  title: ''
  type: Postman
  url: https://github.com/classy-org/postman-collections
- group: operate
  title: ''
  type: StatusPage
  url: https://status.classy.org
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.gofundme.com/pro/reference/deprecation
- group: auth
  title: ''
  type: Security
  url: https://www.gofundme.com/c/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.gofundme.com/c/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/gofundme-trust-center.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://prosupport.gofundme.com/hc/en-us/articles/37726683210267-Release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gofundme-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/gofundme-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gofundme-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gofundme-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gofundme-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gofundme-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gofundme-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gofundme-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gofundme-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gofundme-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gofundme-llms.txt
created: '2026-08-04'
description: 'GoFundMe is the world''s largest social fundraising platform, operating both the consumer crowdfunding site at gofundme.com and GoFundMe Pro (formerly Classy, acquired in 2022) — the enterprise fundraising suite nonprofits use for donation pages, peer-to-peer campaigns, recurring giving, ticketed events and Giving Cart checkout. The developer surface is GoFundMe Pro: a REST API (v2.0) documented with a public OpenAPI 3.0 definition covering campaigns, transactions, supporters, fundraising pages and teams, recurring donation plans, designations, promo codes, payouts and reporting; OAuth2 client-credentials and member tokens; Svix-powered webhooks for supporter, transaction and recurring-plan events; a Classy Login OpenID Connect single-sign-on service; and Classy Pay embedded checkout. The consumer gofundme.com product publishes no public API.'
image: https://pro.gofundme.com/wp-content/uploads/2025/04/social-share-gfm-pro.png
layout: provider
mcp_servers:
- description: ''
  name: gofundme-mcp.yml
  slug: gofundme-mcpyml
modified: '2026-08-04'
name: GoFundMe
nav: Providers
network: true
overview: 'GoFundMe publishes 1 API on the [APIs.io](https://apis.io/) network: Pro API. Tagged areas include Fundraising, Nonprofit, Crowdfunding, Donations, and Payments.


  The GoFundMe catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GoFundMe''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 62
rate_limits:
- limit_count: 1
  name: Gofundme Rate Limits
  slug: gofundme-rate-limits
scopes:
- name: Gofundme Scopes
  scope_count: 2
  slug: gofundme-scopes
  summary_line: 2 scopes · clientCredentials/password
score:
  band: strong
  composite: 64.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 68.5
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 84.2
  previous_composite: 64.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 75.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Gofundme Authentication
  slug: gofundme-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Gofundme Domain Security
  slug: gofundme-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gofundme Vulnerability Disclosure
  slug: gofundme-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gofundme Trust Center
  slug: gofundme-trust-center
  summary_line: PCI DSS, NIST Cybersecurity Framework, ISO 27001
slug: gofundme
tags:
- Fundraising
- Nonprofit
- Crowdfunding
- Donations
- Payments
- Peer-to-Peer Fundraising
- Recurring Giving
- Events
- Philanthropy
- Social Impact
- CRM
- Webhooks
website: https://www.gofundme.com
---
