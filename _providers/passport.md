---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: 'REST-like JSON API for international shipping and landed cost. Endpoints cover shipping rate requests including duties and taxes (/rate), shipping label generation (/ship) and voiding (/void/{code}), '
  name: Passport Global API
  slug: passport-global-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://passportglobal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.passportglobal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.passportglobal.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.passportglobal.com/
- group: operate
  title: ''
  type: Support
  url: https://passportglobal.com/contact-sales/
- group: company
  title: ''
  type: Blog
  url: https://passportglobal.com/news-and-articles/
- group: company
  title: ''
  type: BlogRSS
  url: https://passportglobal.com/feed/
- group: start
  title: ''
  type: Login
  url: https://portal.passportglobal.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://passportglobal.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://passportglobal.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://passportglobal.com/gdpr/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.passportglobal.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/passport-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/passport-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/passport-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/passport-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/passport-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/passport-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/passport-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/passport-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/passport-examples.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/passport-public-api-overlay.yaml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/passport-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/passport-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/passport-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/passport-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: Passport (Passport Global, Inc.) is a cross-border ecommerce logistics and compliance platform founded in 2017 that helps direct-to-consumer brands sell and ship internationally to 190+ markets. The company combines its own international parcel network (Passport Shipping) with in-country enablement, marketplace management, trade and fiscal compliance, seller/merchant-of-record services, duty drawback, and returns. Its public REST API — the Passport Global API, currently version 3.15 — exposes landed-cost rating, shipping label generation and voiding, order submission and management, cart-level duty and tax quoting, currency-converted product pricing, and a tax-and-duty calculator, authenticated with an X-Access-Token API key issued by the Passport onboarding team.
image: https://passportglobal.com/wp-content/uploads/2024/12/passport-international-shipping-compliance-localization.png
layout: provider
mcp_servers:
- description: ''
  name: passport-mcp.yml
  slug: passport-mcpyml
modified: '2026-08-04'
name: Passport
nav: Providers
network: true
overview: 'Passport publishes 1 API on the [APIs.io](https://apis.io/) network: Global API. Tagged areas include Company, shipping, logistics, cross-border-ecommerce, and international-shipping.


  Passport''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 20 more developer resources.'
random_paper: 101
score:
  band: developing
  composite: 46.9
  delta: -1.3
  facets:
    commercial_clarity: 42.1
    contract_quality: 49.5
    developer_ergonomics: 53.8
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 48.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Passport Authentication
  slug: passport-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Passport Domain Security
  slug: passport-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: passport
tags:
- Company
- shipping
- logistics
- cross-border-ecommerce
- international-shipping
- customs-compliance
- landed-cost
- duties-and-taxes
- parcel-delivery
- ecommerce
- merchant-of-record
- trade-compliance
website: https://passportglobal.com/
---
