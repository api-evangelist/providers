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
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API for querying capabilities, discovering agents and managing governance.
  name: Capability Host Protocol API
  slug: capability-host-protocol-api
- baseURL: https://capabilityhostprotocol.com
  baseurl_source: declared
  description: CHP is the governed execution layer of the agentic web. This API exposes a natural-language query endpoint (/ask), the well-known discovery manifests, and the MCP server endpoint. For full tool invoca
  name: Capability Host Protocol — Public API API
  slug: capability-host-protocol-public-api-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/capabilityhostprotocol-com/rules/capabilityhostprotocol-com-rules.yml
  title: ''
  type: Spectral
  url: rules/capabilityhostprotocol-com-rules.yml
- group: design
  href: https://artifacts.apis.io/capabilityhostprotocol-com/json-ld/capabilityhostprotocol-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/capabilityhostprotocol-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/capabilityhostprotocol-com/vocabulary/capabilityhostprotocol-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/capabilityhostprotocol-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/capabilityhostprotocol-com/conformance/capabilityhostprotocol-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capabilityhostprotocol-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/capabilityhostprotocol-com/data-model/capabilityhostprotocol-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/capabilityhostprotocol-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/capabilityhostprotocol-com/cli/capabilityhostprotocol-com-cli.yml
  title: ''
  type: CLI
  url: cli/capabilityhostprotocol-com-cli.yml
- group: design
  href: https://artifacts.apis.io/capabilityhostprotocol-com/errors/capabilityhostprotocol-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/capabilityhostprotocol-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/capabilityhostprotocol-com/llms/capabilityhostprotocol-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capabilityhostprotocol-com-llms.txt
- group: other
  href: https://artifacts.apis.io/capabilityhostprotocol-com/a2a/capabilityhostprotocol-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/capabilityhostprotocol-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/capabilityhostprotocol-com/well-known/capabilityhostprotocol-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capabilityhostprotocol-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/capabilityhostprotocol-com/hosts/capabilityhostprotocol-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capabilityhostprotocol-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/capabilityhostprotocol-com/vendors/capabilityhostprotocol-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capabilityhostprotocol-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/capabilityhostprotocol-com/packages/capabilityhostprotocol-com-packages.yml
  title: ''
  type: SDKs
  url: packages/capabilityhostprotocol-com-packages.yml
- group: build
  href: https://artifacts.apis.io/capabilityhostprotocol-com/packages/capabilityhostprotocol-com-packages.yml
  title: ''
  type: Packages
  url: packages/capabilityhostprotocol-com-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://capabilityhostprotocol.com/adapters/webhook
- group: start
  title: ''
  type: Sandbox
  url: https://capabilityhostprotocol.com/adapters/sandbox
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.capabilityhostprotocol.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.capabilityhostprotocol.com/docs/quickstart-agents
- group: auth
  href: https://artifacts.apis.io/capabilityhostprotocol-com/security/capabilityhostprotocol-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capabilityhostprotocol-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capabilityhostprotocol.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.capabilityhostprotocol.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.capabilityhostprotocol.com/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://www.capabilityhostprotocol.com/blog
- group: other
  title: ''
  type: Image
  url: https://capabilityhostprotocol.com/opengraph-image?fbbeb843739d50f9
created: '2026-11-04'
description: Govern what your AI agents can actually do — every capability declared, every invocation allowed or denied, every result captured as replayable, tamper-evident evidence in one command. CHP is the open protocol for declaring, discovering, invoking, governing, and proving what agents, products, and organizations can do.
image: https://capabilityhostprotocol.com/opengraph-image?fbbeb843739d50f9
json_schemas:
- name: AskResponse
  property_count: 4
  slug: capabilityhostprotocol-com-ask-response
jsonld:
- class_count: 2
  name: Capabilityhostprotocol Com Context
  property_count: 5
  slug: capabilityhostprotocol-com-context
layout: provider
modified: '2026-11-04'
name: Capability Host Protocol
nav: Providers
network: true
overview: 'Capability Host Protocol publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including — Public API API, and 1 more. Tagged areas include Artificial Intelligence, Governance, Protocol, Capabilities, and Agents.


  The Capability Host Protocol catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Capability Host Protocol''s developer surface includes CLI, sandbox, getting-started guide, documentation, API reference, engineering blog, and 18 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Capability Host Protocol API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: capabilityhostprotocol-com-rules
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 42.0
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 3.9
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Capabilityhostprotocol Com Domain Security
  slug: capabilityhostprotocol-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: capabilityhostprotocol-com
tags:
- Artificial Intelligence
- Governance
- Protocol
- Capabilities
- Agents
website: https://capabilityhostprotocol.com/
---
