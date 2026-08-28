---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Prizeout partner integration surface. A partner loads the first-party JavaScript publisher SDK (prizeout-publisher-sdk.js), or the native iOS/Android SDK, and passes partner credentials plus a use
  name: Prizeout Publisher Widget and SDKs
  slug: prizeout-publisher-widget
artifact_total: 8
asyncapis:
- description: ''
  name: Prizeout Partner Callbacks
  slug: prizeout-partner-callbacks
common:
- group: company
  title: ''
  type: Website
  url: https://www.prizeout.com/
- group: company
  title: ''
  type: About
  url: https://www.prizeout.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.prizeout.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.prizeout.com/hc/en-us
- group: operate
  title: ''
  type: Contact
  url: https://www.prizeout.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prizeout.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prizeout.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prizeout
- group: start
  title: ''
  type: SignUp
  url: https://partners.prizeout.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/prizeout-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prizeout-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/prizeout-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/prizeout-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/prizeout-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/prizeout-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prizeout-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prizeout-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prizeout-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/prizeout-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/prizeout-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/prizeout-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/prizeout-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/prizeout-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prizeout-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/prizeout-partner-callbacks.yml
created: '2026-08-26'
description: Prizeout is a New York City based advertising-technology and fintech company that turns a cash-out, payout or rewards balance into a bonused digital gift card. Its button sits on partner platforms wherever a withdrawal happens - online gaming and lottery apps, sportsbooks, earned-wage-access and payroll providers, insurance and marketplace platforms, and banks and credit unions - and runs a real-time auction in which participating brands bid to place a gift-card offer in front of the user, typically returning more value than the cash amount. Prizeout distributes the platform through an embeddable browser widget loaded by a first-party JavaScript publisher SDK, plus native iOS (Swift) and Android SDKs, and a set of partner-implemented HTTP callbacks for balance check, session validation and cash-out success/failure. Its CashBack+ product line (Offers, Actions, Pay and Credit Card Rewards) is delivered to credit unions through the Prizeout Partners CUSO.
image: https://assets.prizeout.com/widget/cobranded-logos/PrizeoutLogoCircle.svg
layout: provider
modified: '2026-08-26'
name: Prizeout
nav: Providers
network: true
overview: 'Prizeout publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Rewards, Gift Cards, and Payouts.


  The Prizeout catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Prizeout''s developer surface includes engineering blog, support, signup flow, authentication, sandbox, changelog, and 19 more developer resources.'
plans:
- name: Prizeout Plans Pricing
  plan_count: 0
  slug: prizeout-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Prizeout Rate Limits
  slug: prizeout-rate-limits
score:
  band: developing
  composite: 41.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 42.7
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 46.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Prizeout Authentication
  slug: prizeout-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Prizeout Domain Security
  slug: prizeout-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Prizeout Vulnerability Disclosure
  slug: prizeout-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Prizeout Trust Center
  slug: prizeout-trust-center
  summary_line: trust center published
slug: prizeout
tags:
- Company
- Advertising
- Rewards
- Gift Cards
- Payouts
- Financial Services
- Credit Unions
- Banking
- Loyalty
- Embedded Finance
- AdTech
- FinTech
website: https://www.prizeout.com/
---
