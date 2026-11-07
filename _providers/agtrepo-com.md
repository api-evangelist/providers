---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Agtrepo Com Agentic Access
  operation_count: 28
  slug: agtrepo-com-agentic-access
  summary_line: 28 operations · 16 acting
api_count: 1
apis:
- description: Encrypted, pay-per-use persistent memory storage for AI agents and humans.
  name: A2A Persistent Memory API
  slug: a2a-persistent-memory-api
- baseURL: https://agtrepo.com
  baseurl_source: declared
  description: Profile, credit balance, and key-request inbox (session-gated)
  name: A2A Account API
  slug: agtrepo-com-account-api
- baseURL: https://agtrepo.com
  baseurl_source: declared
  description: Wallet-connect login (challenge/response), for the human-facing site
  name: A2A Auth API
  slug: agtrepo-com-auth-api
- baseURL: https://agtrepo.com
  baseurl_source: declared
  description: Stripe credit purchase for humans without crypto
  name: A2A Billing API
  slug: agtrepo-com-billing-api
- baseURL: https://agtrepo.com
  baseurl_source: declared
  description: Machine-readable service metadata
  name: A2A Discovery API
  slug: agtrepo-com-discovery-api
- baseURL: https://agtrepo.com
  baseurl_source: declared
  description: Named or anonymous feedback, delivered by email
  name: A2A Feedback API
  slug: agtrepo-com-feedback-api
- baseURL: https://agtrepo.com
  baseurl_source: declared
  description: Request/approve/deny access to a private memory's content key
  name: A2A Key Requests API
  slug: agtrepo-com-key-requests-api
- baseURL: https://agtrepo.com
  baseurl_source: declared
  description: Store, read, extend, and share encrypted memories
  name: A2A Memory API
  slug: agtrepo-com-memory-api
- baseURL: https://agtrepo.com
  baseurl_source: declared
  description: Tag-based document search, creator search, and the top-creators leaderboard
  name: A2A Search API
  slug: agtrepo-com-search-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/agtrepo-com/agentic-access/agtrepo-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agtrepo-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agtrepo-com/rules/agtrepo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agtrepo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agtrepo-com/json-ld/agtrepo-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agtrepo-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agtrepo-com/vocabulary/agtrepo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agtrepo-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agtrepo-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agtrepo-com/data-model/agtrepo-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agtrepo-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/agtrepo-com/errors/agtrepo-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agtrepo-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agtrepo-com/conformance/agtrepo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agtrepo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agtrepo-com/llms/agtrepo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agtrepo-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/agtrepo-com/well-known/agtrepo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agtrepo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agtrepo-com/hosts/agtrepo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agtrepo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agtrepo-com/vendors/agtrepo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agtrepo-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agtrepo-com/security/agtrepo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agtrepo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agtrepo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://agtrepo.com/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agtrepo.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agtrepo.com/privacy
created: '2026-11-01'
description: A2A Persistent Memory Protocol provides a self‑hosted, client‑encrypted storage service where every operation is metered and paid per request via x402 payments on Base. No accounts or API keys are required; users encrypt data locally and the server stores only ciphertext. The platform offers storage, retrieval, TTL extension, and key sharing, with revenue split between creators and the protocol. Detailed pricing, legal terms, and status are publicly available.
jsonld:
- class_count: 1
  name: Agtrepo Com Context
  property_count: 1
  slug: agtrepo-com-context
layout: provider
modified: '2026-11-01'
name: A2A
nav: Providers
network: true
overview: 'A2A publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Auth API, Billing API, and 6 more. Tagged areas include Company, Persistent-Memory, MCP, Payments, and Encryption.


  The A2A catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  A2A''s developer surface includes API reference and 16 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: A2A API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: agtrepo-com-rules
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 47.5
    developer_ergonomics: 10.0
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 27.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 13.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agtrepo Com Domain Security
  slug: agtrepo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agtrepo-com
tags:
- Company
- Persistent-Memory
- MCP
- Payments
- Encryption
- Storage
website: https://agtrepo.com/
---
