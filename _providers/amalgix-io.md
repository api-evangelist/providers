---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Amalgix Io Agentic Access
  operation_count: 8
  slug: amalgix-io-agentic-access
  summary_line: 8 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.amalgix.io
  baseurl_source: declared
  description: Artificial Intelligence tools
  name: Amalgix AI API
  slug: amalgix-io-ai-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/amalgix-io/agentic-access/amalgix-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amalgix-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/amalgix-io/rules/amalgix-io-rules.yml
  title: ''
  type: Spectral
  url: rules/amalgix-io-rules.yml
- group: design
  href: https://artifacts.apis.io/amalgix-io/vocabulary/amalgix-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amalgix-io-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://amalgix.io/#terms
- group: design
  href: https://artifacts.apis.io/amalgix-io/errors/amalgix-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amalgix-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/amalgix-io/conformance/amalgix-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amalgix-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/amalgix-io/llms/amalgix-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amalgix-io-llms.txt
- group: other
  href: https://artifacts.apis.io/amalgix-io/a2a/amalgix-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/amalgix-io-a2a.yml
- group: auth
  href: https://artifacts.apis.io/amalgix-io/well-known/amalgix-io-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amalgix-io-status-security.txt
- group: auth
  href: https://artifacts.apis.io/amalgix-io/well-known/amalgix-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amalgix-io-security.txt
- group: agent
  href: https://artifacts.apis.io/amalgix-io/well-known/amalgix-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amalgix-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/amalgix-io/hosts/amalgix-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amalgix-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/amalgix-io/vendors/amalgix-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amalgix-io-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.amalgix.io/
- group: auth
  href: https://artifacts.apis.io/amalgix-io/security/amalgix-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amalgix-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amalgix-io/security/amalgix-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amalgix-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amalgix.io/
- group: docs
  title: ''
  type: Documentation
  url: https://amalgix.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://amalgix.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://amalgix.io/docs#getting-started
created: '2026-11-01'
description: Amalgix provides AI agents with financial filing and contract intelligence, offering paid per‑use analysis of SEC filings, contracts, spreadsheets, and multilingual documents. The platform returns structured, evidence‑backed JSON with confidence scores, risk flags, and citations, supporting MCP and REST APIs. It emphasizes data privacy, encrypted transit, and optional wallet/API‑key attribution for usage billing via the x402 protocol.
image: https://amalgix.io/assets/og-image.png
layout: provider
modified: '2026-11-01'
name: Amalgix
nav: Providers
network: true
overview: 'Amalgix publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: AI API. Tagged areas include Artificial Intelligence, Finance, Document Intelligence, and MCP.


  The Amalgix catalog on APIs.io includes 1 Spectral governance ruleset.


  Amalgix''s developer surface includes documentation, API reference, getting-started guide, and 17 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Amalgix API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: amalgix-io-rules
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 41.6
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 13.2
  previous_composite: 28.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amalgix Io Domain Security
  slug: amalgix-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amalgix Io Vulnerability Disclosure
  slug: amalgix-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amalgix-io
tags:
- Artificial Intelligence
- Finance
- Document Intelligence
- MCP
website: https://amalgix.io/
---
