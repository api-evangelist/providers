---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 52
  human_in_the_loop: 3
  name: Evidinvest Com Agentic Access
  operation_count: 60
  slug: evidinvest-com-agentic-access
  summary_line: 60 operations · 52 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: REST API exposing 54 financial data, valuation, SEC filing, and portfolio tools, every figure traceable to an SEC filing.
  name: EvidInvest Financial Data API
  slug: evidinvest-financial-data-api
- baseURL: https://mcp.evidinvest.com
  baseurl_source: declared
  description: The Calculations API from evidinvest-com — 5 operation(s) for calculations.
  name: evidinvest-com Calculations API
  slug: evidinvest-com-calculations-api
- baseURL: https://mcp.evidinvest.com
  baseurl_source: declared
  description: The Financial Data API from evidinvest-com — 13 operation(s) for financial data.
  name: evidinvest-com Financial Data API
  slug: evidinvest-com-financial-data-api
- baseURL: https://mcp.evidinvest.com
  baseurl_source: declared
  description: The Machine Payments API from evidinvest-com — 6 operation(s) for machine payments.
  name: evidinvest-com Machine Payments API
  slug: evidinvest-com-machine-payments-api
- baseURL: https://mcp.evidinvest.com
  baseurl_source: declared
  description: The Market Data API from evidinvest-com — 5 operation(s) for market data.
  name: evidinvest-com Market Data API
  slug: evidinvest-com-market-data-api
- baseURL: https://mcp.evidinvest.com
  baseurl_source: declared
  description: The Portfolio API from evidinvest-com — 2 operation(s) for portfolio.
  name: evidinvest-com Portfolio API
  slug: evidinvest-com-portfolio-api
- baseURL: https://mcp.evidinvest.com
  baseurl_source: declared
  description: The SEC Filings API from evidinvest-com — 6 operation(s) for sec filings.
  name: evidinvest-com SEC Filings API
  slug: evidinvest-com-sec-filings-api
- baseURL: https://mcp.evidinvest.com
  baseurl_source: declared
  description: The User Lists API from evidinvest-com — 6 operation(s) for user lists.
  name: evidinvest-com User Lists API
  slug: evidinvest-com-user-lists-api
- baseURL: https://mcp.evidinvest.com
  baseurl_source: declared
  description: The Valuation API from evidinvest-com — 17 operation(s) for valuation.
  name: evidinvest-com Valuation API
  slug: evidinvest-com-valuation-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/evidinvest-com/agentic-access/evidinvest-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/evidinvest-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/evidinvest-com/rules/evidinvest-com-rules.yml
  title: ''
  type: Spectral
  url: rules/evidinvest-com-rules.yml
- group: design
  href: https://artifacts.apis.io/evidinvest-com/vocabulary/evidinvest-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/evidinvest-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/evidinvest-com/errors/evidinvest-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/evidinvest-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/evidinvest-com/conformance/evidinvest-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/evidinvest-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/evidinvest-com/llms/evidinvest-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/evidinvest-com-llms.txt
- group: other
  href: https://artifacts.apis.io/evidinvest-com/a2a/evidinvest-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/evidinvest-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/evidinvest-com/well-known/evidinvest-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/evidinvest-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/evidinvest-com/hosts/evidinvest-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/evidinvest-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/evidinvest-com/vendors/evidinvest-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/evidinvest-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://evidinvest.com/sign-up?redirect_url=%2Fsettings%2Fapi-keys
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evidinvest
- group: auth
  href: https://artifacts.apis.io/evidinvest-com/authentication/evidinvest-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/evidinvest-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/evidinvest-com/security/evidinvest-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evidinvest-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://evidinvest.com/
- group: docs
  title: ''
  type: Documentation
  url: https://evidinvest.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://evidinvest.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://evidinvest.com/blog
- group: operate
  title: ''
  type: Support
  url: https://evidinvest.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evidinvest.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://evidinvest.com/terms-of-service
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://aether.evidinvest.com/mcp
  - status: null
    url: https://mcp.evidinvest.com/v1/openapi.json
  - status: null
    url: https://api.aether.evidinvest.com/mcp
  - status: 401
    url: https://mcp.evidinvest.com/mcp
  - status: 401
    url: https://evidinvest.com/api/graphql
  - status: 200
    url: https://evidinvest.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: EvidInvest provides a valuation platform that delivers fair value estimates for over 500 US public companies, derived from SEC filings using seven independent methods. The service offers a web interface and a free REST API for developers to retrieve valuation data, sector information, and financial metrics without requiring an account. EvidInvest aims to democratize financial analysis by making rigorous valuation models accessible via both UI and programmatic access.
image: https://evidinvest.com/logo-1800x500.png
layout: provider
modified: '2026-10-30'
name: evidinvest-com
nav: Providers
network: true
overview: 'evidinvest-com publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Calculations API, Financial Data API, Machine Payments API, and 6 more. Tagged areas include Company, Finance, Valuation, API, and Data.


  The evidinvest-com catalog on APIs.io includes 1 Spectral governance ruleset.


  evidinvest-com''s developer surface includes signup flow, authentication, documentation, pricing, engineering blog, support, and 15 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: evidinvest-com API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 3
  slug: evidinvest-com-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 49.1
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Evidinvest Com Authentication
  slug: evidinvest-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Evidinvest Com Domain Security
  slug: evidinvest-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: evidinvest-com
tags:
- Company
- Finance
- Valuation
- API
- Data
website: https://evidinvest.com/
---
