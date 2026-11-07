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
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API for Brain Memory platform as documented
  name: Brain Memory API
  slug: brain-memory-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/brainmemory-ai/conformance/brainmemory-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brainmemory-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brainmemory-ai/llms/brainmemory-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brainmemory-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/brainmemory-ai/well-known/brainmemory-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brainmemory-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/brainmemory-ai/well-known/brainmemory-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brainmemory-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/brainmemory-ai/hosts/brainmemory-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainmemory-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/brainmemory-ai/vendors/brainmemory-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brainmemory-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brainmemory.ai/terms/
- group: auth
  title: ''
  type: Security
  url: https://brainmemory.ai/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brainmemory.ai/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://brainmemory.ai/docs/
- group: company
  title: ''
  type: Blog
  url: https://brainmemory.ai/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://brainmemory.ai/docs/reference/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://brainmemory.ai/docs/getting-started/installation
- group: auth
  href: https://artifacts.apis.io/brainmemory-ai/security/brainmemory-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brainmemory-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/brainmemory-ai/security/brainmemory-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainmemory-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brainmemory.ai/
coverage:
  checked: '2026-11-03'
  detail: Documentation is public but provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://brainmemory.ai/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Brain Memory provides a hierarchical, file-system‑based memory system for AI coding agents. Inspired by human neuroscience, it offers deterministic recall, decay, and consolidation across many models and tools, with open‑source npm packages and a hosted MCP connector. The platform stores memories as readable Markdown files, enabling easy versioning, portability, and integration with Claude Code, OpenAI Codex, GitHub Copilot, Kilo, and more.
image: https://brainmemory.ai/opengraph-image?b26d321acc0f44ef
layout: provider
modified: '2026-11-02'
name: Brain Memory
nav: Providers
network: true
overview: 'Brain Memory is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Memory, Agents, Open Source, and Neuroscience.


  Brain Memory''s developer surface includes documentation, engineering blog, API reference, getting-started guide, and 12 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 30.5
    developer_ergonomics: 15.5
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainmemory Ai Domain Security
  slug: brainmemory-ai-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Brainmemory Ai Vulnerability Disclosure
  slug: brainmemory-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: brainmemory-ai
tags:
- Artificial Intelligence
- Memory
- Agents
- Open Source
- Neuroscience
website: https://brainmemory.ai/
---
