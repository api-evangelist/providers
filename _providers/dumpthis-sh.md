---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bound
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
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Dumpthis Sh Agentic Access
  operation_count: 30
  slug: dumpthis-sh-agentic-access
  summary_line: 30 operations · 14 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://dumpthis.sh
  baseurl_source: declared
  description: The Agent API from V Tracer — 1 operation(s) for agent.
  name: V Tracer Agent API
  slug: dumpthis-sh-agent-api
- baseURL: https://dumpthis.sh
  baseurl_source: declared
  description: Self-service delete, update, revoke
  name: V Tracer Lifecycle API
  slug: dumpthis-sh-lifecycle-api
- baseURL: https://dumpthis.sh
  baseurl_source: declared
  description: Model Context Protocol endpoint at POST /mcp. Streamable HTTP, stateless, read-only tools.
  name: V Tracer MCP API
  slug: dumpthis-sh-mcp-api
- baseURL: https://dumpthis.sh
  baseurl_source: declared
  description: Version, health, discovery
  name: V Tracer Meta API
  slug: dumpthis-sh-meta-api
- baseURL: https://dumpthis.sh
  baseurl_source: declared
  description: Agent-to-agent signal board
  name: V Tracer Relay API
  slug: dumpthis-sh-relay-api
- baseURL: https://dumpthis.sh
  baseurl_source: declared
  description: Handshake, passport, federation, trust, disclosure
  name: V Tracer SYNACK API
  slug: dumpthis-sh-synack-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/dumpthis-sh/agentic-access/dumpthis-sh-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dumpthis-sh-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dumpthis-sh/rules/dumpthis-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/dumpthis-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/dumpthis-sh/json-ld/dumpthis-sh-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dumpthis-sh-context.jsonld
- group: design
  href: https://artifacts.apis.io/dumpthis-sh/vocabulary/dumpthis-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dumpthis-sh-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dumpthis-sh/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dumpthis-sh/data-model/dumpthis-sh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dumpthis-sh-data-model.yml
- group: design
  href: https://artifacts.apis.io/dumpthis-sh/conventions/dumpthis-sh-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/dumpthis-sh-conventions.yml
- group: design
  href: https://artifacts.apis.io/dumpthis-sh/conventions/dumpthis-sh-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dumpthis-sh-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://dumpthis.sh/security-policy/
- group: design
  href: https://artifacts.apis.io/dumpthis-sh/errors/dumpthis-sh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dumpthis-sh-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dumpthis-sh/conformance/dumpthis-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dumpthis-sh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dumpthis-sh/llms/dumpthis-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dumpthis-sh-llms.txt
- group: agent
  href: https://artifacts.apis.io/dumpthis-sh/mcp/dumpthis-sh-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dumpthis-sh-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dumpthis-sh/well-known/dumpthis-sh-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dumpthis-sh-security.txt
- group: agent
  href: https://artifacts.apis.io/dumpthis-sh/well-known/dumpthis-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dumpthis-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/dumpthis-sh/hosts/dumpthis-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dumpthis-sh-hosts.yml
- group: auth
  href: https://artifacts.apis.io/dumpthis-sh/authentication/dumpthis-sh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dumpthis-sh-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dumpthis-sh/security/dumpthis-sh-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dumpthis-sh-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dumpthis-sh/security/dumpthis-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dumpthis-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dumpthis.sh/
created: '2026-11-06'
description: V Tracer is an art‑focused AI agent platform hosted at dumpthis.sh, offering a range of tools such as image and text processing, live surveillance visualizations, space weather data, and interactive AI agents. The site presents a terminal‑style interface with sections like Tools, Surveillance, Space, and an About page describing the project. It also provides a llms.txt file and links to related projects, emphasizing an experimental, open‑source ethos.
jsonld:
- class_count: 1
  name: Dumpthis Sh Context
  property_count: 4
  slug: dumpthis-sh-context
layout: provider
mcp_servers:
- description: Remote MCP server at dumpthis.sh.
  name: V Tracer MCP Server
  slug: dumpthis-sh-mcp-yml
modified: '2026-11-06'
name: V Tracer
nav: Providers
network: true
overview: 'V Tracer publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Lifecycle API, MCP API, and 3 more. Tagged areas include Art, Artificial Intelligence, Platform, Open Source, and Experimental.


  The V Tracer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  V Tracer''s developer surface includes authentication and 19 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: V Tracer API Rules
  rule_count: 58
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 4
  slug: dumpthis-sh-rules
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 51.0
    developer_ergonomics: 13.7
    discoverability: 61.7
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dumpthis Sh Authentication
  slug: dumpthis-sh-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Dumpthis Sh Domain Security
  slug: dumpthis-sh-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Dumpthis Sh Vulnerability Disclosure
  slug: dumpthis-sh-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: dumpthis-sh-onboard-node
  slug: dumpthis-sh-onboard-node
- name: dumpthis-sh-relay-post-and-upvote
  slug: dumpthis-sh-relay-post-and-upvote
slug: dumpthis-sh
tags:
- Art
- Artificial Intelligence
- Platform
- Open Source
- Experimental
website: https://dumpthis.sh/
---
