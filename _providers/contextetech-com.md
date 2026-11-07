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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 20.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Contexte Tech API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Contexte Tech API
  slug: contextetech-com-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/contextetech-com/rules/contextetech-com-rules.yml
  title: ''
  type: Spectral
  url: rules/contextetech-com-rules.yml
- group: design
  href: https://artifacts.apis.io/contextetech-com/vocabulary/contextetech-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/contextetech-com-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://contextetech.com/securite
- group: design
  href: https://artifacts.apis.io/contextetech-com/conformance/contextetech-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contextetech-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/contextetech-com/llms/contextetech-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contextetech-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/contextetech-com/mcp/contextetech-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/contextetech-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/contextetech-com/well-known/contextetech-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/contextetech-com-security.txt
- group: agent
  href: https://artifacts.apis.io/contextetech-com/well-known/contextetech-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contextetech-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/contextetech-com/hosts/contextetech-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contextetech-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/contextetech-com/security/contextetech-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/contextetech-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/contextetech-com/security/contextetech-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextetech-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contextetech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://contextetech.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://contextetech.com/docs/mcp
- group: agent
  title: ''
  type: llms.txt
  url: https://contextetech.com/llms.txt
coverage:
  checked: '2026-11-04'
  detail: The provider's documentation pages are human‑readable HTML but publish no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://contextetech.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Contexte Tech is a French platform offering a library of AI resources, including prompts, datasets, MCP models, and tools. It provides open‑source resources, pricing information, and guidance for selecting appropriate AI models, hardware, and costs. The site emphasizes data privacy, decentralized research, and transparent licensing, aiming to help users make informed AI decisions.
image: https://contextetech.com/og/contexte-tech.webp
layout: provider
mcp_servers:
- description: Remote MCP server at contextetech.com.
  name: Contexte Tech MCP Server
  slug: contextetech-com-mcp-yml
modified: '2026-11-04'
name: Contexte Tech
nav: Providers
network: true
overview: 'Contexte Tech is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Library, Open Source, and French.


  The Contexte Tech catalog on APIs.io includes 1 Spectral governance ruleset.


  Contexte Tech''s developer surface includes documentation, API reference, and 13 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: Contexte Tech API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: contextetech-com-rules
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 16.7
    discoverability: 56.7
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contextetech Com Domain Security
  slug: contextetech-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Contextetech Com Vulnerability Disclosure
  slug: contextetech-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: contextetech-com
tags:
- Company
- Artificial Intelligence
- Library
- Open Source
- French
website: https://contextetech.com/
---
