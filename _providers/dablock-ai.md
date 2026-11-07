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
    agent_card: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dablock Ai Agentic Access
  operation_count: 8
  slug: dablock-ai-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://dablock.ai
  baseurl_source: declared
  description: The Aiv.csv API from DABLOCK — 1 operation(s) for aiv.csv.
  name: DABLOCK Aiv.csv API
  slug: dablock-ai-aiv-csv-api
- baseURL: https://dablock.ai
  baseurl_source: declared
  description: The Aiv.json API from DABLOCK — 1 operation(s) for aiv.json.
  name: DABLOCK Aiv.json API
  slug: dablock-ai-aiv-json-api
- baseURL: https://dablock.ai
  baseurl_source: declared
  description: The Brands API from DABLOCK — 1 operation(s) for brands.
  name: DABLOCK Brands API
  slug: dablock-ai-brands-api
- baseURL: https://dablock.ai
  baseurl_source: declared
  description: The Brands.json API from DABLOCK — 1 operation(s) for brands.json.
  name: DABLOCK Brands.json API
  slug: dablock-ai-brands-json-api
- baseURL: https://dablock.ai
  baseurl_source: declared
  description: The History.json API from DABLOCK — 1 operation(s) for history.json.
  name: DABLOCK History.json API
  slug: dablock-ai-history-json-api
- baseURL: https://dablock.ai
  baseurl_source: declared
  description: The Index.md API from DABLOCK — 1 operation(s) for index.md.
  name: DABLOCK Index.md API
  slug: dablock-ai-index-md-api
- baseURL: https://dablock.ai
  baseurl_source: declared
  description: The Measurement Status.json API from DABLOCK — 1 operation(s) for measurement status.json.
  name: DABLOCK Measurement Status.json API
  slug: dablock-ai-measurement-status-json-api
- baseURL: https://dablock.ai
  baseurl_source: declared
  description: The Methodology.json API from DABLOCK — 1 operation(s) for methodology.json.
  name: DABLOCK Methodology.json API
  slug: dablock-ai-methodology-json-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/dablock-ai/agentic-access/dablock-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dablock-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dablock-ai/rules/dablock-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/dablock-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/dablock-ai/errors/dablock-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dablock-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dablock-ai/conformance/dablock-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dablock-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dablock-ai/llms/dablock-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dablock-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/dablock-ai/well-known/dablock-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dablock-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/dablock-ai/well-known/dablock-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dablock-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/dablock-ai/hosts/dablock-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dablock-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/dablock-ai/vendors/dablock-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dablock-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://dablock.ai/security/
- group: auth
  href: https://artifacts.apis.io/dablock-ai/security/dablock-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dablock-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dablock-ai/security/dablock-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dablock-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dablock.ai/
created: '2026-11-04'
description: DABLOCK provides an AI-powered visibility index for Crypto and Web3 projects, offering free, machine‑readable data desks with JSON, CSV, markdown, and MCP formats. Published by VECTORY, the service is open, no‑key, and licensed under CC BY 4.0, aiming to increase transparency and accessibility of blockchain analytics.
image: https://dablock.ai/favicon.svg
layout: provider
modified: '2026-11-04'
name: DABLOCK
nav: Providers
network: true
overview: 'DABLOCK publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aiv.csv API, Aiv.json API, Brands API, and 5 more. Tagged areas include Company, Cryptocurrency, Web3, Data, and Artificial Intelligence.


  The DABLOCK catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: DABLOCK API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: dablock-ai-rules
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 41.3
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dablock Ai Domain Security
  slug: dablock-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Dablock Ai Vulnerability Disclosure
  slug: dablock-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dablock-ai
tags:
- Company
- Cryptocurrency
- Web3
- Data
- Artificial Intelligence
- Analytics
website: https://dablock.ai/
---
