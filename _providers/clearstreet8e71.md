---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Clearstreet8E71 Agentic Access
  operation_count: 72
  slug: clearstreet8e71-agentic-access
  summary_line: 72 operations · 26 acting
api_count: 1
apis:
- baseURL: https://api.clearstreet.com
  baseurl_source: declared
  description: Manage trading accounts, balances, and portfolio history.
  name: Clearstreet8e71 Accounts API
  slug: clearstreet8e71-accounts-api
- baseURL: https://api.clearstreet.com
  baseurl_source: declared
  description: Endpoints for API service metadata.
  name: Clearstreet8e71 API version API
  slug: clearstreet8e71-api-version-api
- baseURL: https://api.clearstreet.com
  baseurl_source: declared
  description: Access clocks and financial calendars for market sessions and events.
  name: Clearstreet8e71 Calendar API
  slug: clearstreet8e71-calendar-api
- baseURL: https://api.clearstreet.com
  baseurl_source: declared
  description: Retrieve instrument analytics, market data, news, and related reference data.
  name: Clearstreet8e71 Instrument Data API
  slug: clearstreet8e71-instrument-data-api
- baseURL: https://api.clearstreet.com
  baseurl_source: declared
  description: Retrieve core details and discovery endpoints for tradable instruments.
  name: Clearstreet8e71 Instruments API
  slug: clearstreet8e71-instruments-api
- baseURL: https://api.clearstreet.com
  baseurl_source: declared
  description: Thread-centric AI assistant for conversational trading. Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/mes
  name: Clearstreet8e71 Omni AI API
  slug: clearstreet8e71-omni-ai-api
- baseURL: https://api.clearstreet.com
  baseurl_source: declared
  description: Place, monitor, and manage trading orders.
  name: Clearstreet8e71 Orders API
  slug: clearstreet8e71-orders-api
- baseURL: https://api.clearstreet.com
  baseurl_source: declared
  description: View positions and manage position instructions.
  name: Clearstreet8e71 Positions API
  slug: clearstreet8e71-positions-api
- baseURL: https://api.clearstreet.com
  baseurl_source: declared
  description: Browse private-market offerings and their indicative terms. Access requires the account holder to hold an accreditation attestation.
  name: Clearstreet8e71 Private Markets API
  slug: clearstreet8e71-private-markets-api
- baseURL: https://api.clearstreet.com
  baseurl_source: declared
  description: Search instruments and manage saved screeners.
  name: Clearstreet8e71 Screener API
  slug: clearstreet8e71-screener-api
- baseURL: https://api.clearstreet.com
  baseurl_source: declared
  description: Create and manage watchlists.
  name: Clearstreet8e71 Watchlist API
  slug: clearstreet8e71-watchlist-api
artifact_total: 22
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearstreet8e71/refs/heads/main/agentic-access/clearstreet8e71-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clearstreet8e71-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearstreet8e71/refs/heads/main/rules/clearstreet8e71-rules.yml
  title: ''
  type: Spectral
  url: rules/clearstreet8e71-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearstreet8e71/refs/heads/main/json-ld/clearstreet8e71-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clearstreet8e71-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearstreet8e71/refs/heads/main/vocabulary/clearstreet8e71-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clearstreet8e71-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearstreet8e71/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearstreet8e71/refs/heads/main/data-model/clearstreet8e71-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clearstreet8e71-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/clearstreet8e71/refs/heads/main/cli/clearstreet8e71-cli.yml
  title: ''
  type: CLI
  url: cli/clearstreet8e71-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearstreet8e71/refs/heads/main/errors/clearstreet8e71-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clearstreet8e71-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearstreet8e71/refs/heads/main/conformance/clearstreet8e71-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clearstreet8e71-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearstreet8e71/refs/heads/main/well-known/clearstreet8e71-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clearstreet8e71-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearstreet8e71/refs/heads/main/hosts/clearstreet8e71-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearstreet8e71-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearstreet8e71/refs/heads/main/vendors/clearstreet8e71-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clearstreet8e71-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.clearstreet.io/legal/security
- group: other
  title: ''
  type: Leadership
  url: https://www.clearstreet.io/about/team/andy-volz
- group: operate
  title: ''
  type: ChangeLog
  url: https://clearstreet.io/studio/releases
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearstreet8e71/refs/heads/main/authentication/clearstreet8e71-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clearstreet8e71-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearstreet8e71/refs/heads/main/security/clearstreet8e71-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearstreet8e71-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clearstreet.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clearstreet.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clearstreet.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clearstreet.com/guides/api-fundamentals/
- group: operate
  title: ''
  type: Support
  url: https://www.clearstreet.io/contact
- group: company
  title: ''
  type: Blog
  url: https://www.clearstreet.io/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clear-street
- group: start
  title: ''
  type: SignUp
  url: https://app.clearstreet.com/public/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clearstreet.io/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearstreet.io/legal/privacy-notice
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/clear-street/workspace/clear-street-api
created: '2026-10-08'
description: Clearstreet8e71 is a financial technology company offering a modern, cloud‑native brokerage platform for institutional investors and family offices. It provides real‑time trading APIs, market data, clearing, financing, and AI‑driven execution tools. The platform serves over 700 institutional clients, handling billions in assets, and emphasizes speed, transparency, and scalability for sophisticated traders.
image: https://cdn.sanity.io/images/40fnhjbe/production/c122608e711a69935fc1bbbbcc672f01e673e6dc-1200x630.jpg
json_schemas:
- name: AccountBalances
  property_count: 21
  slug: clearstreet8e71-account-balances
- name: AccountWithPersonalDetails
  property_count: 0
  slug: clearstreet8e71-account-with-personal-details
- name: InstrumentFundamentals
  property_count: 15
  slug: clearstreet8e71-instrument-fundamentals
- name: Instrument
  property_count: 0
  slug: clearstreet8e71-instrument
- name: Order
  property_count: 34
  slug: clearstreet8e71-order
- name: PositionInstruction
  property_count: 14
  slug: clearstreet8e71-position-instruction
jsonld:
- class_count: 120
  name: Clearstreet8E71 Context
  property_count: 396
  slug: clearstreet8e71-context
layout: provider
modified: '2026-10-08'
name: Clearstreet8e71
nav: Providers
network: true
overview: 'Clearstreet8e71 publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, API version API, Calendar API, and 8 more. Tagged areas include Company, Fintech, Brokerage, and Institutional.


  The Clearstreet8e71 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clearstreet8e71''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, support, and 21 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Clearstreet8e71 API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 2
  slug: clearstreet8e71-rules
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 70.1
    developer_ergonomics: 61.3
    discoverability: 58.9
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 11.1
security:
- kind: authentication
  name: Clearstreet8E71 Authentication
  slug: clearstreet8e71-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Clearstreet8E71 Domain Security
  slug: clearstreet8e71-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clearstreet8e71
tags:
- Company
- Fintech
- Brokerage
- Institutional
website: https://www.clearstreet.io
---
