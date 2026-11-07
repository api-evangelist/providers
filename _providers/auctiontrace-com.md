---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Auctiontrace Com Agentic Access
  operation_count: 23
  slug: auctiontrace-com-agentic-access
  summary_line: 23 operations · 7 acting
api_count: 2
apis:
- baseURL: https://auctiontrace.com
  baseurl_source: declared
  description: The Buyer Client API from AuctionTrace — 1 operation(s) for buyer client.
  name: AuctionTrace Buyer Client API
  slug: auctiontrace-com-buyer-client-api
- baseURL: https://auctiontrace.com
  baseurl_source: declared
  description: The Buyer Kit API from AuctionTrace — 1 operation(s) for buyer kit.
  name: AuctionTrace Buyer Kit API
  slug: auctiontrace-com-buyer-kit-api
- baseURL: https://auctiontrace.com
  baseurl_source: declared
  description: The Catalog API from AuctionTrace — 1 operation(s) for catalog.
  name: AuctionTrace Catalog API
  slug: auctiontrace-com-catalog-api
- baseURL: https://auctiontrace.com
  baseurl_source: declared
  description: The Datasets API from AuctionTrace — 3 operation(s) for datasets.
  name: AuctionTrace Datasets API
  slug: auctiontrace-com-datasets-api
- baseURL: https://auctiontrace.com
  baseurl_source: declared
  description: The Healthz API from AuctionTrace — 1 operation(s) for healthz.
  name: AuctionTrace Healthz API
  slug: auctiontrace-com-healthz-api
- baseURL: https://auctiontrace.com
  baseurl_source: declared
  description: The Human Checkout API from AuctionTrace — 2 operation(s) for human checkout.
  name: AuctionTrace Human Checkout API
  slug: auctiontrace-com-human-checkout-api
- baseURL: https://auctiontrace.com
  baseurl_source: declared
  description: The Human Interest API from AuctionTrace — 1 operation(s) for human interest.
  name: AuctionTrace Human Interest API
  slug: auctiontrace-com-human-interest-api
- baseURL: https://auctiontrace.com
  baseurl_source: declared
  description: The Human Offers API from AuctionTrace — 1 operation(s) for human offers.
  name: AuctionTrace Human Offers API
  slug: auctiontrace-com-human-offers-api
- baseURL: https://auctiontrace.com
  baseurl_source: declared
  description: The Human Orders API from AuctionTrace — 5 operation(s) for human orders.
  name: AuctionTrace Human Orders API
  slug: auctiontrace-com-human-orders-api
- baseURL: https://auctiontrace.com
  baseurl_source: declared
  description: The Offer Feedback API from AuctionTrace — 2 operation(s) for offer feedback.
  name: AuctionTrace Offer Feedback API
  slug: auctiontrace-com-offer-feedback-api
- baseURL: https://auctiontrace.com
  baseurl_source: declared
  description: The Outcome Assessment API from AuctionTrace — 3 operation(s) for outcome assessment.
  name: AuctionTrace Outcome Assessment API
  slug: auctiontrace-com-outcome-assessment-api
- baseURL: https://auctiontrace.com
  baseurl_source: declared
  description: The Trade List API from AuctionTrace — 1 operation(s) for trade list.
  name: AuctionTrace Trade List API
  slug: auctiontrace-com-trade-list-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/auctiontrace-com/agentic-access/auctiontrace-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/auctiontrace-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/auctiontrace-com/rules/auctiontrace-com-rules.yml
  title: ''
  type: Spectral
  url: rules/auctiontrace-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/auctiontrace-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/auctiontrace-com/conventions/auctiontrace-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/auctiontrace-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/auctiontrace-com/conventions/auctiontrace-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/auctiontrace-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/auctiontrace-com/errors/auctiontrace-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/auctiontrace-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/auctiontrace-com/conformance/auctiontrace-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/auctiontrace-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/auctiontrace-com/mcp/auctiontrace-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/auctiontrace-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/auctiontrace-com/hosts/auctiontrace-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auctiontrace-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/auctiontrace-com/vendors/auctiontrace-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auctiontrace-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/auctiontrace-com/authentication/auctiontrace-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/auctiontrace-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/auctiontrace-com/security/auctiontrace-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auctiontrace-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auctiontrace.com/
created: '2026-11-02'
description: AuctionTrace provides tools to evaluate the performance of entry‑side (ES) trading strategies. Their platform lets users replay historical entries, add buying and selling pressure, and measure the impact on outcomes. It offers research kits and human‑reviewed comparisons to help traders understand edge after entry, with a focus on transparent, data‑driven analysis.
layout: provider
mcp_servers:
- description: Remote MCP server at auctiontrace.com.
  name: AuctionTrace MCP Server
  slug: auctiontrace-com-mcp-yml
modified: '2026-11-02'
name: AuctionTrace
nav: Providers
network: true
overview: 'AuctionTrace publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Buyer Client API, Buyer Kit API, Catalog API, and 9 more. Tagged areas include Company, Trading, Analytics, Finance, and ES-Strategy.


  The AuctionTrace catalog on APIs.io includes 1 Spectral governance ruleset.


  AuctionTrace''s developer surface includes authentication and 12 more developer resources.'
plans:
- name: Auctiontrace Com Plans Pricing
  plan_count: 2
  slug: auctiontrace-com-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: AuctionTrace API Rules
  rule_count: 37
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 4
  slug: auctiontrace-com-rules
scopes:
- name: Auctiontrace Com Scopes
  scope_count: 0
  slug: auctiontrace-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 47.5
    catalog_earned_first_party: 8.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 46.3
    developer_ergonomics: 18.3
    discoverability: 61.7
    operational_transparency: 0.0
  previous_composite: 30.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Auctiontrace Com Authentication
  slug: auctiontrace-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Auctiontrace Com Domain Security
  slug: auctiontrace-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: auctiontrace-com
tags:
- Company
- Trading
- Analytics
- Finance
- ES-Strategy
website: https://auctiontrace.com/
---
