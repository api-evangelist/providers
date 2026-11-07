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
    mcp_server: false
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
  score: 18.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dabyte Ai Agentic Access
  operation_count: 8
  slug: dabyte-ai-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://dabyte.ai
  baseurl_source: declared
  description: The Aiv.csv API from DABYTE — 1 operation(s) for aiv.csv.
  name: DABYTE Aiv.csv API
  slug: dabyte-ai-aiv-csv-api
- baseURL: https://dabyte.ai
  baseurl_source: declared
  description: The Aiv.json API from DABYTE — 1 operation(s) for aiv.json.
  name: DABYTE Aiv.json API
  slug: dabyte-ai-aiv-json-api
- baseURL: https://dabyte.ai
  baseurl_source: declared
  description: The Brands API from DABYTE — 1 operation(s) for brands.
  name: DABYTE Brands API
  slug: dabyte-ai-brands-api
- baseURL: https://dabyte.ai
  baseurl_source: declared
  description: The Brands.json API from DABYTE — 1 operation(s) for brands.json.
  name: DABYTE Brands.json API
  slug: dabyte-ai-brands-json-api
- baseURL: https://dabyte.ai
  baseurl_source: declared
  description: The History.json API from DABYTE — 1 operation(s) for history.json.
  name: DABYTE History.json API
  slug: dabyte-ai-history-json-api
- baseURL: https://dabyte.ai
  baseurl_source: declared
  description: The Index.md API from DABYTE — 1 operation(s) for index.md.
  name: DABYTE Index.md API
  slug: dabyte-ai-index-md-api
- baseURL: https://dabyte.ai
  baseurl_source: declared
  description: The Measurement Status.json API from DABYTE — 1 operation(s) for measurement status.json.
  name: DABYTE Measurement Status.json API
  slug: dabyte-ai-measurement-status-json-api
- baseURL: https://dabyte.ai
  baseurl_source: declared
  description: The Methodology.json API from DABYTE — 1 operation(s) for methodology.json.
  name: DABYTE Methodology.json API
  slug: dabyte-ai-methodology-json-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/dabyte-ai/agentic-access/dabyte-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dabyte-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dabyte-ai/rules/dabyte-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/dabyte-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/dabyte-ai/errors/dabyte-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dabyte-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dabyte-ai/conformance/dabyte-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dabyte-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dabyte-ai/llms/dabyte-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dabyte-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/dabyte-ai/well-known/dabyte-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dabyte-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/dabyte-ai/well-known/dabyte-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dabyte-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/dabyte-ai/hosts/dabyte-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dabyte-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/dabyte-ai/vendors/dabyte-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dabyte-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://dabyte.ai/security/
- group: auth
  href: https://artifacts.apis.io/dabyte-ai/security/dabyte-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dabyte-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dabyte-ai/security/dabyte-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dabyte-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dabyte.ai/
created: '2026-11-04'
description: DABYTE is a data desk covering SaaS & AI Tools, published by VECTORY. It provides a free, machine‑readable visibility index for SaaS and AI applications, offering JSON, CSV, markdown, and MCP formats under a CC BY 4.0 license. The service is openly accessible without an API key, aiming to increase transparency and discoverability of AI‑enabled products across the web.
image: https://dabyte.ai/favicon.svg
layout: provider
modified: '2026-11-04'
name: DABYTE
nav: Providers
network: true
overview: 'DABYTE publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aiv.csv API, Aiv.json API, Brands API, and 5 more. Tagged areas include Software-as-a-Service, AI Tools, Visibility Index, Open Data, and CC-BY.


  The DABYTE catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: DABYTE API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: dabyte-ai-rules
score:
  band: emerging
  composite: 21.0
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
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dabyte Ai Domain Security
  slug: dabyte-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Dabyte Ai Vulnerability Disclosure
  slug: dabyte-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dabyte-ai
tags:
- Software-as-a-Service
- AI Tools
- Visibility Index
- Open Data
- CC-BY
website: https://dabyte.ai/
---
