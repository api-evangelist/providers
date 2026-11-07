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
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: MCP endpoint for integrating AI agents with capital.new
  name: capital.new MCP
  slug: capital-new-mcp
- description: 'capital.new API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: capital.new API
  slug: capital-new-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/capital-new/rules/capital-new-rules.yml
  title: ''
  type: Spectral
  url: rules/capital-new-rules.yml
- group: design
  href: https://artifacts.apis.io/capital-new/json-ld/capital-new-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/capital-new-context.jsonld
- group: design
  href: https://artifacts.apis.io/capital-new/vocabulary/capital-new-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/capital-new-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/capital-new/data-model/capital-new-data-model.yml
  title: ''
  type: DataModel
  url: data-model/capital-new-data-model.yml
- group: design
  href: https://artifacts.apis.io/capital-new/conformance/capital-new-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capital-new-conformance.yml
- group: other
  href: https://artifacts.apis.io/capital-new/hosts/capital-new-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capital-new-hosts.yml
- group: other
  href: https://artifacts.apis.io/capital-new/vendors/capital-new-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capital-new-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capital.new/privacy
- group: auth
  href: https://artifacts.apis.io/capital-new/security/capital-new-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capital-new-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capital.new/
- group: docs
  title: ''
  type: Documentation
  url: https://capital.new/docs
coverage:
  checked: '2026-11-04'
  detail: Provider only offers an MCP endpoint and documentation without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://capital.new/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: capital.new is building the funding layer for AI agents. It enables agents to request capital and operate under a mandate. The platform is pre‑seed, not a lender, and aims to provide a seamless funding interface for AI applications. It offers an MCP endpoint for integration with AI agents and provides documentation for developers.
image: https://capital.new/og.png
json_schemas:
- name: PostMcpRequest
  property_count: 3
  slug: capital-new-post-mcp-request
jsonld:
- class_count: 1
  name: Capital New Context
  property_count: 3
  slug: capital-new-context
layout: provider
modified: '2026-11-04'
name: capital.new
nav: Providers
network: true
overview: 'capital.new is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Funding, Artificial Intelligence, Agents, Pre-Seed, and MCP.


  The capital.new catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  capital.new''s developer surface includes documentation and 10 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: capital.new API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: capital-new-rules
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 17.4
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Capital New Domain Security
  slug: capital-new-domain-security
  summary_line: TLSv1.3
slug: capital-new
tags:
- Funding
- Artificial Intelligence
- Agents
- Pre-Seed
- MCP
website: https://capital.new/
---
