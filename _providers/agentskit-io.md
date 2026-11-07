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
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
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
  score: 18.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Programmatic API reference for AgentsKit packages.
  name: AgentsKit API
  slug: agentskit-api
- description: 'AgentsKit API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AgentsKit API
  slug: agentskit-io-api
artifact_total: 4
common:
- group: build
  href: https://artifacts.apis.io/agentskit-io/packages/agentskit-io-packages.yml
  title: ''
  type: SDKs
  url: packages/agentskit-io-packages.yml
- group: build
  href: https://artifacts.apis.io/agentskit-io/packages/agentskit-io-packages.yml
  title: ''
  type: Packages
  url: packages/agentskit-io-packages.yml
- group: design
  href: https://artifacts.apis.io/agentskit-io/rules/agentskit-io-rules.yml
  title: ''
  type: Spectral
  url: rules/agentskit-io-rules.yml
- group: design
  href: https://artifacts.apis.io/agentskit-io/vocabulary/agentskit-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentskit-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentskit-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentskit-io/conformance/agentskit-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentskit-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentskit-io/llms/agentskit-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentskit-io-llms.txt
- group: other
  href: https://artifacts.apis.io/agentskit-io/hosts/agentskit-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentskit-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentskit-io/vendors/agentskit-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentskit-io-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.agentskit.io/showcase/sandbox
- group: auth
  href: https://artifacts.apis.io/agentskit-io/security/agentskit-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentskit-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agentskit.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.agentskit.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.agentskit.io/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.agentskit.io/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.agentskit.io/community
- group: company
  title: ''
  type: Blog
  url: https://www.agentskit.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EmersonBraun
- group: operate
  title: ''
  type: Roadmap
  url: https://www.agentskit.io/docs/reference/contribute/roadmap
coverage:
  checked: '2026-11-01'
  detail: Documentation is public but no OpenAPI/GraphQL/AsyncAPI/Proto/WSDL contract is provided.
  evidence:
  - status: 200
    url: https://www.agentskit.io/docs/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Build agents without gluing many libraries together. AgentsKit offers a composable TypeScript foundation for runtime, tools, memory, RAG, and chat interfaces. It supports OpenAI, Anthropic, Gemini, Kimi, local models, and custom adapters, providing six interchangeable contracts that let developers swap layers without touching the rest of the stack. Users can install ready-made agents, scaffold new ones from descriptions, run them on any provider, and diagnose setups directly from the terminal. The platform presents a connected toolkit ranging from source code to production-ready delivery, emphasizing flexibility, low overhead, and a tiny core under 10KB.
image: https://www.agentskit.io/favicon.ico
layout: provider
modified: '2026-11-01'
name: AgentsKit
nav: Providers
network: true
overview: 'AgentsKit is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Agents, TypeScript, Platform, and LLM.


  The AgentsKit catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentsKit''s developer surface includes sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 13 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: AgentsKit API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: agentskit-io-rules
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 35.0
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 22.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentskit Io Domain Security
  slug: agentskit-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentskit-io
tags:
- Artificial Intelligence
- Agents
- TypeScript
- Platform
- LLM
website: https://www.agentskit.io/
---
