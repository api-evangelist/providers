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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 9.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/globacap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://globacap.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.apexgroup.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://globacap.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://globacap.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Globacap
- group: operate
  title: ''
  type: Support
  url: https://knowledge.globacap.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.globacap.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/globacap-trust-center.yml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/globacap-stock
- group: agent
  title: ''
  type: WellKnown
  url: well-known/globacap-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/globacap-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/globacap-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/globacap-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/globacap-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/globacap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/globacap-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/globacap-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Globacap sells private-markets workflow SaaS to institutions and has never run a developer program — api./developer./docs.globacap.com are all NXDOMAIN and absent from the Wayback index — and since the Apex Group acquisition globacap.com has collapsed to a single acquisition-announcement page that returns an S3 AccessDenied on every product, news and /llms.txt path.
  evidence:
  - status: 403
    url: https://globacap.com/products/register/
  - status: 403
    url: https://globacap.com/llms.txt
  - status: 401
    url: https://investor.globacap.com/api/graphql
  - status: 302
    url: https://globacap.zendesk.com/api/v2/help_center/en-gb/categories.json
  - status: 200
    url: https://login.globacap.com/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Globacap is a London-based private capital markets technology company, founded in 2017, that builds workflow-automation software-as-a-service for issuance, share register management, ongoing administration, transferability and settlement of private securities. Its platform is used by securities exchanges, securities firms, private banks and asset managers to run primary placements and secondary liquidity events, and the company states its technology has supported 200+ primary placements, matched and settled $800m+ of secondaries and administered $30bn+ in private markets assets. Globacap operates an FCA-regulated UK entity and a US-registered broker-dealer and alternative trading system. In November 2025 Apex Group agreed to acquire the company; the change of control completed in early 2026 and Globacap technology now sits inside Apex Group's digital/tokenisation initiative alongside Tokeny. As of this profile the public globacap.com site has been reduced to a single acquisition
  announcement page and Globacap publishes no public developer program, API reference or machine-readable API contract.
image: https://globacap.com/globacap-logo.svg
layout: provider
modified: '2026-08-22'
name: Globacap
nav: Providers
network: true
overview: 'Globacap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Private Capital Markets, Capital Markets, Securities, and Financial-Services.


  Globacap''s developer surface includes support, authentication, and 16 more developer resources.'
plans:
- name: Globacap Plans Pricing
  plan_count: 0
  slug: globacap-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Globacap Rate Limits
  slug: globacap-rate-limits
scopes:
- name: Globacap Scopes
  scope_count: 0
  slug: globacap-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 20.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 68.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Globacap Authentication
  slug: globacap-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Globacap Domain Security
  slug: globacap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Globacap Trust Center
  slug: globacap-trust-center
  summary_line: trust center published
slug: globacap
tags:
- Company
- Private Capital Markets
- Capital Markets
- Securities
- Financial-Services
- Fintech
- Tokenization
- Share Register
- Secondary Markets
- United Kingdom
website: https://globacap.com/
---
