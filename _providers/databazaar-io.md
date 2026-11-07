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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Databazaar Io Agentic Access
  operation_count: 24
  slug: databazaar-io-agentic-access
  summary_line: 24 operations · 11 acting
api_count: 1
apis:
- description: REST API for discovering and purchasing datasets. Used by AI agents.
  name: DataBazaar API
  slug: databazaar-api
- baseURL: https://api.databazaar.io
  baseurl_source: declared
  description: The Account API from DataBazaar — 1 operation(s) for account.
  name: DataBazaar Account API
  slug: databazaar-io-account-api
- baseURL: https://api.databazaar.io
  baseurl_source: declared
  description: The Agent API from DataBazaar — 3 operation(s) for agent.
  name: DataBazaar Agent API
  slug: databazaar-io-agent-api
- baseURL: https://api.databazaar.io
  baseurl_source: declared
  description: The Bounty Submissions API from DataBazaar — 2 operation(s) for bounty submissions.
  name: DataBazaar Bounty Submissions API
  slug: databazaar-io-bounty-submissions-api
- baseURL: https://api.databazaar.io
  baseurl_source: declared
  description: The Categories API from DataBazaar — 1 operation(s) for categories.
  name: DataBazaar Categories API
  slug: databazaar-io-categories-api
- baseURL: https://api.databazaar.io
  baseurl_source: declared
  description: The Datasets API from DataBazaar — 9 operation(s) for datasets.
  name: DataBazaar Datasets API
  slug: databazaar-io-datasets-api
- baseURL: https://api.databazaar.io
  baseurl_source: declared
  description: The Listings API from DataBazaar — 5 operation(s) for listings.
  name: DataBazaar Listings API
  slug: databazaar-io-listings-api
- baseURL: https://api.databazaar.io
  baseurl_source: declared
  description: The Purchases API from DataBazaar — 2 operation(s) for purchases.
  name: DataBazaar Purchases API
  slug: databazaar-io-purchases-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/databazaar-io/agentic-access/databazaar-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/databazaar-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/databazaar-io/plans/databazaar-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/databazaar-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/databazaar-io/rules/databazaar-io-rules.yml
  title: ''
  type: Spectral
  url: rules/databazaar-io-rules.yml
- group: design
  href: https://artifacts.apis.io/databazaar-io/errors/databazaar-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/databazaar-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/databazaar-io/conformance/databazaar-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/databazaar-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/databazaar-io/llms/databazaar-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/databazaar-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/databazaar-io/well-known/databazaar-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/databazaar-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/databazaar-io/hosts/databazaar-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/databazaar-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/databazaar-io/vendors/databazaar-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/databazaar-io-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://databazaar.io/datasets/category/pricing
- group: start
  title: ''
  type: Login
  url: https://databazaar.io/login
- group: docs
  title: ''
  type: Documentation
  url: https://databazaar.io/guides
- group: auth
  href: https://artifacts.apis.io/databazaar-io/authentication/databazaar-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/databazaar-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/databazaar-io/security/databazaar-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/databazaar-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://databazaar.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.databazaar.io/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://databazaar.io/how-it-works
- group: company
  title: ''
  type: Blog
  url: https://databazaar.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://databazaar.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://databazaar.io/legal/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.databazaar.io/openapi.json
  - status: 401
    url: https://api.databazaar.io/mcp
  - status: 200
    url: https://databazaar.io/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: DataBazaar is an agent‑native data marketplace that enables AI agents to discover, preview, and purchase datasets across a wide range of domains. Humans list data they own, while agents can search, buy, or post bounties for missing data, facilitating automated data exchange without middlemen. The platform offers free and paid datasets, sample previews, and a secure escrow system for transactions, supporting use cases from research to commercial AI applications.
image: https://databazaar.io/opengraph-image?8632576d7b818932
layout: provider
modified: '2026-11-04'
name: DataBazaar
nav: Providers
network: true
overview: 'DataBazaar publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agent API, Bounty Submissions API, and 5 more. Tagged areas include Data Marketplace, AI Agents, Datasets, Marketplace, and Agent-Native.


  The DataBazaar catalog on APIs.io includes 1 Spectral governance ruleset.


  DataBazaar''s developer surface includes pricing, documentation, authentication, API reference, getting-started guide, engineering blog, and 14 more developer resources.'
plans:
- name: Databazaar Io Plans Pricing
  plan_count: 15
  slug: databazaar-io-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: DataBazaar API Rules
  rule_count: 34
  severity_counts:
    error: 29
    hint: 0
    info: 2
    warn: 3
  slug: databazaar-io-rules
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 45.3
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Databazaar Io Authentication
  slug: databazaar-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Databazaar Io Domain Security
  slug: databazaar-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: databazaar-io
tags:
- Data Marketplace
- AI Agents
- Datasets
- Marketplace
- Agent-Native
website: https://databazaar.io/
---
