---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The Hidden Road prime brokerage and clearing API suite, announced generally available on 2023-05-04. Four service surfaces are confirmed live under https://api.hiddenroad.com/v0/ — accountactivity, me
  name: Hidden Road API (v0)
  slug: hidden-road-api-v0
- description: A daily CSV feed of OTC spot crypto-asset transactions executed by Hidden Road Partners CIV NL B.V., published under the EU Markets in Crypto-Assets Regulation post-trade transparency obligation. File
  name: Hidden Road MiCA Post-Trade Transparency Feed
  slug: hidden-road-mica-post-trade-transparency-feed
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/hidden-road-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hidden-road-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ripple.com/products/prime-brokerage/
- group: start
  title: ''
  type: Login
  url: https://portal.ops.hiddenroad.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.hiddenroad.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://ripple.com/contact/sales/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ripple.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ripple.com/legal/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://ripple.com/legal/compliance/
- group: design
  title: ''
  type: Conformance
  url: conformance/hidden-road-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hidden-road-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hidden-road-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hidden-road-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hidden-road-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hidden-road-well-known.yml
created: '2026-08-22'
description: Hidden Road is a global, multi-asset non-bank prime broker and clearing firm serving institutional counterparties across digital assets, foreign exchange, precious metals, exchange-traded derivatives, OTC swaps and fixed-income repo. Ripple acquired Hidden Road for $1.25B in 2025 and now operates it as Ripple Prime; hiddenroad.com redirects to ripple.com/products/prime-brokerage/. Hidden Road ships a real, customer-only API suite — the Account Activity API (streamed balances, trades, positions and fees over a bitemporal store), the Risk API (real-time margin utilisation and tail-risk metrics), the Automated Treasury Management API (programmatic collateral and credit-limit distribution) and an OTC surface — served from https://api.hiddenroad.com/v0/ behind an Auth0 OAuth 2.0 / OIDC authorization server at auth.hiddenroad.com. No public reference, OpenAPI, SDK or sandbox documentation is published; the only machine-readable artifact a member of the public can read is the daily
  MiCA post-trade transparency CSV feed the firm's Netherlands entity publishes under its EU regulatory obligation.
image: https://static.hiddenroad.com/images/logo.png
layout: provider
modified: '2026-08-22'
name: Hidden Road
nav: Providers
network: true
overview: 'Hidden Road publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Prime Brokerage, Clearing, and Digital Assets.


  Hidden Road''s developer surface includes support and 14 more developer resources.'
plans:
- name: Hidden Road Plans Pricing
  plan_count: 0
  slug: hidden-road-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Hidden Road Rate Limits
  slug: hidden-road-rate-limits
scopes:
- name: Hidden Road Scopes
  scope_count: 0
  slug: hidden-road-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 27.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Hidden Road Authentication
  slug: hidden-road-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Hidden Road Domain Security
  slug: hidden-road-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hidden Road Vulnerability Disclosure
  slug: hidden-road-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Hidden Road Trust Center
  slug: hidden-road-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: hidden-road
tags:
- Company
- Financial-Services
- Prime Brokerage
- Clearing
- Digital Assets
- Foreign Exchange
- Capital Markets
- Trading
- Institutional Finance
- Collateral Management
- Risk Management
- Regulated
website: https://ripple.com/products/prime-brokerage/
---
