---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Prepare UK CT600 corporation tax returns and FRS 105 micro-entity accounts: company lookup, eligibility, live tax computation, draft filings and document generation. Money in POUNDS throughout. Submis'
  name: CT600 API
  slug: ct600-api
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/axel-trade/well-known/axel-trade-axeltrade-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/axel-trade-axeltrade-security.txt
- group: commercial
  href: https://artifacts.apis.io/axel-trade/plans/axel-trade-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/axel-trade-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://axel.trade/security
- group: agent
  href: https://artifacts.apis.io/axel-trade/llms/axel-trade-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/axel-trade-llms.txt
- group: auth
  href: https://artifacts.apis.io/axel-trade/well-known/axel-trade-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/axel-trade-security.txt
- group: auth
  href: https://artifacts.apis.io/axel-trade/well-known/axel-trade-portal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/axel-trade-portal-security.txt
- group: auth
  href: https://artifacts.apis.io/axel-trade/well-known/axel-trade-file-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/axel-trade-file-security.txt
- group: auth
  href: https://artifacts.apis.io/axel-trade/well-known/axel-trade-ct600-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/axel-trade-ct600-security.txt
- group: agent
  href: https://artifacts.apis.io/axel-trade/well-known/axel-trade-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/axel-trade-well-known.yml
- group: other
  href: https://artifacts.apis.io/axel-trade/hosts/axel-trade-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axel-trade-hosts.yml
- group: other
  href: https://artifacts.apis.io/axel-trade/vendors/axel-trade-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axel-trade-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://axeltrade.statuspage.io
- group: auth
  title: ''
  type: Security
  url: https://axel.trade/security
- group: auth
  href: https://artifacts.apis.io/axel-trade/security/axel-trade-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/axel-trade-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/axel-trade/security/axel-trade-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/axel-trade-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/axel-trade/security/axel-trade-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axel-trade-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axel.trade/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.axel.trade
- group: docs
  title: ''
  type: Documentation
  url: https://ct600.axel.trade/api
- group: docs
  title: ''
  type: APIReference
  url: https://ct600.axel.trade/api
- group: start
  title: ''
  type: GettingStarted
  url: https://axel.trade/about
- group: operate
  title: ''
  type: Support
  url: https://axel.trade/support
- group: company
  title: ''
  type: Blog
  url: https://axel.trade/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://axel.trade/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://axel.trade/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axel.trade/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://ct600.axel.trade/api/mcp
  - status: 401
    url: https://file.axel.trade/api/mcp
  - status: 401
    url: https://intel.axel.trade/mcp
  - status: 200
    url: https://axel.trade/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: A.X.E.L (axel.trade) provides an online filing service for UK limited companies to submit their annual accounts and CT600 corporation tax returns, as well as a job management platform for tradespeople. The service offers a one‑off £49 filing fee, optional self‑assessment returns, and a free tier for basic lead management, aiming to simplify compliance and business operations for small enterprises.
image: https://axel.trade/opengraph-image.png?opengraph-image.871a0f6c.png
layout: provider
modified: '2026-10-29'
name: axel-trade
nav: Providers
network: true
overview: 'axel-trade is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Tax, Accounting, and Software.


  axel-trade''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Axel Trade Plans Pricing
  plan_count: 5
  slug: axel-trade-plans-pricing
random_paper: 15
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Axel Trade Domain Security
  slug: axel-trade-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Axel Trade Vulnerability Disclosure
  slug: axel-trade-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Axel Trade Trust Center
  slug: axel-trade-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: axel-trade
tags:
- Company
- Finance
- Tax
- Accounting
- Software
- UK
website: https://axel.trade/
---
