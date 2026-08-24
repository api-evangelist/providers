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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: A data-feed API that returns every field in the FEVO Sales Report — orders and order adjustments — so a customer can pull FEVO transaction data directly into their own data warehouse. Queries run by O
  name: FEVO Order API
  slug: order-api
- description: The client-side embed surface. A single script tag loads GMWidget from gofevo.com (or gofevo.uk for the UK), and GMWidget.open('offerSlug') opens the FEVO Social Checkout drawer over the partner's own
  name: FEVO Embedded Checkout (Distributed Commerce Button)
  slug: embedded-checkout
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fevo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fevo.com
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/fevo_stock/
- group: docs
  title: ''
  type: Documentation
  url: https://intercom.help/fevoenterprise/en/
- group: operate
  title: ''
  type: Support
  url: https://www.fevo.com/ticket-help
- group: company
  title: ''
  type: Blog
  url: https://www.fevo.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.fevo.com/demo-request
- group: start
  title: ''
  type: Login
  url: https://www.gofevo.com/manage/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wf.fevo.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wf.fevo.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fevo-tech
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fevo-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/fevo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fevo-packages.yml
- group: design
  title: ''
  type: Components
  url: components/fevo-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fevo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fevo-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fevo-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fevo-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fevo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/fevo-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fevo-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/fevo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fevo-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fevo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fevo-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fevo-llms.txt
created: '2026-08-12'
description: 'FEVO is a New York social-commerce and group-ticketing platform, launched in 2016, that lets fans buy, split and share orders for live events together. Its Social Checkout drawer and Distributed Commerce Button embed into a client''s own site, sitting in front of existing ticketing and inventory systems, while the FEVO Enterprise console at gofevo.com handles offer creation, gating, discounting, payouts and reporting. The developer surface is deliberately narrow: a client-side JavaScript widget (GMWidget) any partner can embed, and an Order API data feed that pushes FEVO Sales Report fields into a customer data warehouse using a User ID and Access Key issued by a FEVO representative. FEVO reports 800+ brands in sports, music and entertainment and more than 24 million tickets sold.'
image: https://cdn.prod.website-files.com/63c2beaea55341844ce65d4e/682d14798ca7154c6364947c_FEVO%20Logomark.png
layout: provider
modified: '2026-08-12'
name: Fevo
nav: Providers
network: true
overview: 'Fevo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ticketing, Event, Group Sales, and Social Commerce.


  Fevo''s developer surface includes documentation, support, engineering blog, signup flow, changelog, authentication, and 21 more developer resources.'
plans:
- name: Fevo Plans Pricing
  plan_count: 0
  slug: fevo-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Fevo Rate Limits
  slug: fevo-rate-limits
score:
  band: thin
  composite: 34.7
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 34.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 65.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Fevo Authentication
  slug: fevo-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Fevo Domain Security
  slug: fevo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fevo Vulnerability Disclosure
  slug: fevo-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Fevo Trust Center
  slug: fevo-trust-center
  summary_line: SOC 2
slug: fevo
tags:
- Company
- Ticketing
- Event
- Group Sales
- Social Commerce
- E-Commerce
- Checkout
- Sports
- Live Entertainment
- Embedded Commerce
website: https://www.fevo.com
---
