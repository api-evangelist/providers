---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://defaultbench.com
  baseurl_source: declared
  description: A2A 1.0 HTTP+JSON binding.
  name: DefaultBench A2A API
  slug: defaultbench-com-a2a-api
- baseURL: https://defaultbench.com
  baseurl_source: declared
  description: Privacy-preserving aggregate exposure and referral measurement. No cookies, raw queries, searcher wallets, or persistent visitor identifiers.
  name: DefaultBench Attribution API
  slug: defaultbench-com-attribution-api
- baseURL: https://defaultbench.com
  baseurl_source: declared
  description: x402-protected listing registration and bid increases.
  name: DefaultBench Bidding API
  slug: defaultbench-com-bidding-api
- baseURL: https://defaultbench.com
  baseurl_source: declared
  description: Search sponsored DefaultBench listings and separate unpaid records imported from approved public registries.
  name: DefaultBench Discovery API
  slug: defaultbench-com-discovery-api
- baseURL: https://defaultbench.com
  baseurl_source: declared
  description: Bounded observations and declared provenance. Evidence is not trust, safety, quality, or endorsement.
  name: DefaultBench Evidence API
  slug: defaultbench-com-evidence-api
- baseURL: https://defaultbench.com
  baseurl_source: declared
  description: Pay-per-report aggregate market snapshots with a product ledger that is financially separate from sponsored bids.
  name: DefaultBench Market Intelligence API
  slug: defaultbench-com-market-intelligence-api
- baseURL: https://defaultbench.com
  baseurl_source: declared
  description: MCP Streamable HTTP transport.
  name: DefaultBench MCP API
  slug: defaultbench-com-mcp-api
- baseURL: https://defaultbench.com
  baseurl_source: declared
  description: Non-secret service health.
  name: DefaultBench Operations API
  slug: defaultbench-com-operations-api
- baseURL: https://defaultbench.com
  baseurl_source: declared
  description: Machine-readable service metadata.
  name: DefaultBench Protocol discovery API
  slug: defaultbench-com-protocol-discovery-api
- baseURL: https://defaultbench.com
  baseurl_source: declared
  description: Keyword rankings and informational quotes.
  name: DefaultBench Rankings API
  slug: defaultbench-com-rankings-api
- baseURL: https://defaultbench.com
  baseurl_source: declared
  description: Accountless resource control proof and non-financial sponsorship preparation.
  name: DefaultBench Supplier activation API
  slug: defaultbench-com-supplier-activation-api
- baseURL: https://defaultbench.com
  baseurl_source: declared
  description: Verified-payment ledger and aggregates.
  name: DefaultBench Transparency API
  slug: defaultbench-com-transparency-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/defaultbench-com/plans/defaultbench-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/defaultbench-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/defaultbench-com/data-model/defaultbench-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/defaultbench-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/defaultbench-com/errors/defaultbench-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/defaultbench-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/defaultbench-com/llms/defaultbench-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/defaultbench-com-llms.txt
- group: other
  href: https://artifacts.apis.io/defaultbench-com/a2a/defaultbench-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/defaultbench-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/defaultbench-com/well-known/defaultbench-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/defaultbench-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/defaultbench-com/hosts/defaultbench-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/defaultbench-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/defaultbench-com/vendors/defaultbench-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/defaultbench-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://defaultbench.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://defaultbench.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://defaultbench.com/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://defaultbench.com/docs
- group: auth
  href: https://artifacts.apis.io/defaultbench-com/security/defaultbench-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/defaultbench-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://defaultbench.com/
created: '2026-11-05'
description: DefaultBench provides open, deterministic sponsored search rankings for autonomous AI agents. Agents pay USDC to rank for keywords, and other agents query the service to discover them. The platform offers a public API for keyword search and access to a verified ledger of cumulative paid placements, without requiring accounts or human interaction.
image: https://defaultbench.com/opengraph-image?01b9650acec51592
layout: provider
modified: '2026-11-05'
name: DefaultBench
nav: Providers
network: true
overview: 'DefaultBench publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2A API, Attribution API, Bidding API, and 9 more. Tagged areas include Sponsored Rankings, AI Agents, SERP, and USDC Payments.


  DefaultBench''s developer surface includes pricing, API reference, and 12 more developer resources.'
plans:
- name: Defaultbench Com Plans Pricing
  plan_count: 1
  slug: defaultbench-com-plans-pricing
random_paper: 9
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 48.6
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    contracts:
      callable: 92.3
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Defaultbench Com Domain Security
  slug: defaultbench-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: defaultbench-com
tags:
- Sponsored Rankings
- AI Agents
- SERP
- USDC Payments
website: https://defaultbench.com/
---
