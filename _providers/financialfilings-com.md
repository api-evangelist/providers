---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: Your own API usage and spend. Free, never billed.
  name: financialfilings-com Account API
  slug: financialfilings-com-account-api
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: 'Lets an AI agent get its own API key: sign up, check status, ask the owner to confirm, add a card.'
  name: financialfilings-com Agent Account API
  slug: financialfilings-com-agent-account-api
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: Company profiles, identifiers and financials.
  name: financialfilings-com Companies API
  slug: financialfilings-com-companies-api
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: Supported countries.
  name: financialfilings-com Countries API
  slug: financialfilings-com-countries-api
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: The 11 filing categories (FRCF). Every filing type belongs to one.
  name: financialfilings-com Filing Categories API
  slug: financialfilings-com-filing-categories-api
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: Every filing type we classify filings into.
  name: financialfilings-com Filing Types API
  slug: financialfilings-com-filing-types-api
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: Find filings and read their documents and content.
  name: financialfilings-com Filings API
  slug: financialfilings-com-filings-api
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: Standardized income statement, balance sheet and cash flow data, and the dictionary of line items.
  name: financialfilings-com Financial Data API
  slug: financialfilings-com-financial-data-api
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: Browse the ISIC industry classification.
  name: financialfilings-com ISIC Classifications API
  slug: financialfilings-com-isic-classifications-api
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: Look up the company behind an ISIN.
  name: financialfilings-com ISINs API
  slug: financialfilings-com-isins-api
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: Supported filing languages.
  name: financialfilings-com Languages API
  slug: financialfilings-com-languages-api
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: 'Exchange listings per company: venue, ticker and FIGI.'
  name: financialfilings-com Security Listings API
  slug: financialfilings-com-security-listings-api
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: The original sources of filings.
  name: financialfilings-com Sources API
  slug: financialfilings-com-sources-api
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: The companies you follow. Filters and webhooks can use it.
  name: financialfilings-com Watchlist API
  slug: financialfilings-com-watchlist-api
- baseURL: https://api.financialreports.eu
  baseurl_source: declared
  description: Create and manage webhook subscriptions, and inspect their deliveries.
  name: financialfilings-com Webhooks (Management) API
  slug: financialfilings-com-webhooks-management-api
artifact_total: 23
asyncapis:
- description: ''
  name: Financialfilings Com Webhooks
  slug: financialfilings-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/financialfilings-com/plans/financialfilings-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/financialfilings-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/financialfilings-com/asyncapi/financialfilings-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/financialfilings-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/financialfilings-com/data-model/financialfilings-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/financialfilings-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/financialfilings-com/security/financialfilings-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/financialfilings-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/financialfilings-com/authentication/financialfilings-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/financialfilings-com-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://financialfilings.com/developers/deprecation-policy/
- group: design
  href: https://artifacts.apis.io/financialfilings-com/lifecycle/financialfilings-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/financialfilings-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/financialfilings-com/errors/financialfilings-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/financialfilings-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/financialfilings-com/llms/financialfilings-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/financialfilings-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/financialfilings-com/well-known/financialfilings-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/financialfilings-com-security.txt
- group: auth
  href: https://artifacts.apis.io/financialfilings-com/well-known/financialfilings-com-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/financialfilings-com-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/financialfilings-com/well-known/financialfilings-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/financialfilings-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/financialfilings-com/hosts/financialfilings-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/financialfilings-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/financialfilings-com/vendors/financialfilings-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/financialfilings-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://financialfilings.com/terms/
- group: commercial
  title: ''
  type: Pricing
  url: https://financialfilings.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://financialfilings.com/accounts/login/?next=%2Faccounts%2Fapi-dashboard%2F%3Fsource%3Dnavbar&source=navbar
- group: start
  title: ''
  type: DeveloperPortal
  url: https://financialfilings.com/developers/
- group: operate
  title: ''
  type: ChangeLog
  url: https://financialfilings.com/developers/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://financialfilings.com/mcp/
- group: docs
  title: ''
  type: APIReference
  url: https://api.financialreports.eu/redoc/
- group: auth
  href: https://artifacts.apis.io/financialfilings-com/security/financialfilings-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/financialfilings-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/financialfilings-com/security/financialfilings-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/financialfilings-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://financialfilings.com/
created: '2026-10-30'
description: FinancialFilings provides a searchable index of public company filings across 60 markets, covering over 54 million filings from more than 93,000 companies. Users can access data via a Markdown‑first REST API, download datasets, and integrate with cloud platforms. The service offers free web search, paid enterprise plans, and supports developers with comprehensive documentation, SDKs, and MCP compliance.
image: https://financialfilings.com/og/general.png?title=Everything+public+companies+file%2C&subtitle=in+one+place.&v=2
layout: provider
modified: '2026-10-30'
name: financialfilings-com
nav: Providers
network: true
overview: 'financialfilings-com publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agent Account API, Companies API, and 12 more. Tagged areas include API, Financial Data, Public Company Filings, Analytics, and Research.


  The financialfilings-com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  financialfilings-com''s developer surface includes authentication, pricing, changelog, getting-started guide, API reference, and 19 more developer resources.'
plans:
- name: Financialfilings Com Plans Pricing
  plan_count: 1
  slug: financialfilings-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Financialfilings Com Rate Limits
  slug: financialfilings-com-rate-limits
scopes:
- name: Financialfilings Com Scopes
  scope_count: 0
  slug: financialfilings-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.2
    catalog_earned_first_party: 8.0
    catalog_gap: 62.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 62.1
    developer_ergonomics: 40.5
    discoverability: 66.1
    operational_transparency: 61.1
  provenance:
    contracts:
      callable: 93.8
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Financialfilings Com Authentication
  slug: financialfilings-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Financialfilings Com Domain Security
  slug: financialfilings-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Financialfilings Com Vulnerability Disclosure
  slug: financialfilings-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: companies-list
  slug: financialfilings-com-companies-list
slug: financialfilings-com
tags:
- API
- Financial Data
- Public Company Filings
- Analytics
- Research
website: https://financialfilings.com/
---
