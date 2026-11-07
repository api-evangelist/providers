---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Earningsfeed Com Agentic Access
  operation_count: 11
  slug: earningsfeed-com-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 1
apis:
- baseURL: https://earningsfeed.com
  baseurl_source: declared
  description: Retrieve information about the authenticated user's account.
  name: Earnings Feed Account API
  slug: earningsfeed-com-account-api
- baseURL: https://earningsfeed.com
  baseurl_source: declared
  description: Look up company profiles by CIK or search by name/ticker. Includes SEC classification, industry codes, contact information, and filing activity flags.
  name: Earnings Feed Companies API
  slug: earningsfeed-com-companies-api
- baseURL: https://earningsfeed.com
  baseurl_source: declared
  description: Access SEC EDGAR filings including annual reports (10-K), quarterly reports (10-Q), current reports (8-K), ownership filings (Forms 3/4/5), and more. We check EDGAR every minute for new filings.
  name: Earnings Feed Filings API
  slug: earningsfeed-com-filings-api
- baseURL: https://earningsfeed.com
  baseurl_source: declared
  description: Track insider trading activity from SEC Forms 3, 4, and 5. Monitor purchases, sales, grants, and other transactions by corporate officers, directors, and 10% owners.
  name: Earnings Feed Insider API
  slug: earningsfeed-com-insider-api
- baseURL: https://earningsfeed.com
  baseurl_source: declared
  description: Access institutional investment holdings from SEC Form 13F filings. Track positions held by hedge funds, mutual funds, and other institutional managers with $100M+ in assets.
  name: Earnings Feed Institutional API
  slug: earningsfeed-com-institutional-api
- baseURL: https://earningsfeed.com
  baseurl_source: declared
  description: Manage webhook endpoints to receive notifications when new SEC filings match your alert preferences. Webhooks are signed with HMAC-SHA256 for verification.
  name: Earnings Feed Webhooks API
  slug: earningsfeed-com-webhooks-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/earningsfeed-com/agentic-access/earningsfeed-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/earningsfeed-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/earningsfeed-com/plans/earningsfeed-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/earningsfeed-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/earningsfeed-com/rules/earningsfeed-com-rules.yml
  title: ''
  type: Spectral
  url: rules/earningsfeed-com-rules.yml
- group: design
  href: https://artifacts.apis.io/earningsfeed-com/json-ld/earningsfeed-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/earningsfeed-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/earningsfeed-com/vocabulary/earningsfeed-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/earningsfeed-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/earningsfeed-com/data-model/earningsfeed-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/earningsfeed-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/earningsfeed-com/errors/earningsfeed-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/earningsfeed-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/earningsfeed-com/conformance/earningsfeed-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/earningsfeed-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/earningsfeed-com/llms/earningsfeed-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/earningsfeed-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/earningsfeed-com/well-known/earningsfeed-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/earningsfeed-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/earningsfeed-com/hosts/earningsfeed-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/earningsfeed-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/earningsfeed-com/vendors/earningsfeed-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/earningsfeed-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/earningsfeed-com/packages/earningsfeed-com-packages.yml
  title: ''
  type: SDKs
  url: packages/earningsfeed-com-packages.yml
- group: build
  href: https://artifacts.apis.io/earningsfeed-com/packages/earningsfeed-com-packages.yml
  title: ''
  type: Packages
  url: packages/earningsfeed-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://earningsfeed.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://earningsfeed.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://earningsfeed.com/pricing
- group: start
  title: ''
  type: Login
  url: https://earningsfeed.com/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/earningsfeed
- group: docs
  title: ''
  type: Documentation
  url: https://earningsfeed.com/api/docs
- group: company
  title: ''
  type: Blog
  url: https://earningsfeed.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://earningsfeed.com/api
- group: auth
  href: https://artifacts.apis.io/earningsfeed-com/authentication/earningsfeed-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/earningsfeed-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/earningsfeed-com/security/earningsfeed-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/earningsfeed-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://earningsfeed.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://earningsfeed.com/api/mcp
  - status: 200
    url: https://earningsfeed.com/
  reason: partner-login
  state: gated
created: '2026-11-06'
description: Earnings Feed provides free access to SEC filings as they are accepted by EDGAR, including 8‑K, 10‑K, 10‑Q, and Form 4 insider trades. Users can search by ticker, filter by form type, and build watchlists with digests. The service offers an API and MCP server for programmatic access to real‑time filing data, supporting financial research and monitoring.
image: https://earningsfeed.com/api/og/home
json_schemas:
- name: CompanyProfile
  property_count: 20
  slug: earningsfeed-com-company-profile
- name: CompanySearchResponse
  property_count: 3
  slug: earningsfeed-com-company-search-response
- name: FilingDetail
  property_count: 17
  slug: earningsfeed-com-filing-detail
- name: FilingsFeedResponse
  property_count: 4
  slug: earningsfeed-com-filings-feed-response
- name: InstitutionalHoldingsResponse
  property_count: 3
  slug: earningsfeed-com-institutional-holdings-response
- name: MeResponse
  property_count: 3
  slug: earningsfeed-com-me-response
jsonld:
- class_count: 24
  name: Earningsfeed Com Context
  property_count: 125
  slug: earningsfeed-com-context
layout: provider
modified: '2026-11-06'
name: Earnings Feed
nav: Providers
network: true
overview: 'Earnings Feed publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Companies API, Filings API, and 3 more. Tagged areas include Finance, SEC, Filings, and Data.


  The Earnings Feed catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Earnings Feed''s developer surface includes pricing, documentation, engineering blog, API reference, authentication, and 20 more developer resources.'
plans:
- name: Earningsfeed Com Plans Pricing
  plan_count: 3
  slug: earningsfeed-com-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 110
  extends:
  - spectral:oas
  name: Earnings Feed API Rules
  rule_count: 69
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 6
  slug: earningsfeed-com-rules
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 68.1
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Earningsfeed Com Authentication
  slug: earningsfeed-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Earningsfeed Com Domain Security
  slug: earningsfeed-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: earningsfeed-com
tags:
- Finance
- SEC
- Filings
- Data
website: https://earningsfeed.com/
---
