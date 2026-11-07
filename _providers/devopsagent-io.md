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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for DevOps Agent platform providing automation and AI assistance.
  name: DevOps Agent API
  slug: devops-agent-api
- description: 'DevOps Agent API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DevOps Agent API
  slug: devopsagent-io-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/devopsagent-io/rules/devopsagent-io-rules.yml
  title: ''
  type: Spectral
  url: rules/devopsagent-io-rules.yml
- group: design
  href: https://artifacts.apis.io/devopsagent-io/json-ld/devopsagent-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/devopsagent-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/devopsagent-io/vocabulary/devopsagent-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/devopsagent-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/devopsagent-io/data-model/devopsagent-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/devopsagent-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/devopsagent-io/conformance/devopsagent-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/devopsagent-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/devopsagent-io/well-known/devopsagent-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/devopsagent-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/devopsagent-io/hosts/devopsagent-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/devopsagent-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/devopsagent-io/vendors/devopsagent-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/devopsagent-io-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.devopsagent.io
- group: auth
  title: ''
  type: Security
  url: https://devopsagent.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://devopsagent.io/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://devopsagent.io/login
- group: docs
  title: ''
  type: Documentation
  url: https://devopsagent.io/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devopsagent.io/developers
- group: auth
  href: https://artifacts.apis.io/devopsagent-io/security/devopsagent-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/devopsagent-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://devopsagent.io/
coverage:
  checked: '2026-11-05'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://devopsagent.io/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DevOps Agent provides an AI‑powered command center that lets users manage AWS, Azure, GCP and Kubernetes resources through natural language. It offers a conversational interface for 749 tools covering compute, storage, networking, CI/CD, IaC, monitoring and security, with sandbox mode, credential isolation and safety guardrails. The service targets developers, solo operators and teams that need to automate multi‑cloud infrastructure without using dashboards.
json_schemas:
- name: GetApiGatewayV1ResourcesIdResponse
  property_count: 7
  slug: devopsagent-io-get-api-gateway-v1-resources-id-response
- name: GetResourcesIdResponse
  property_count: 6
  slug: devopsagent-io-get-resources-id-response
- name: PostMcpMessagesRequest
  property_count: 4
  slug: devopsagent-io-post-mcp-messages-request
- name: PostMcpMessagesResponse
  property_count: 4
  slug: devopsagent-io-post-mcp-messages-response
- name: PostMcpRequest
  property_count: 4
  slug: devopsagent-io-post-mcp-request
- name: PostMcpResponse
  property_count: 4
  slug: devopsagent-io-post-mcp-response
jsonld:
- class_count: 14
  name: Devopsagent Io Context
  property_count: 26
  slug: devopsagent-io-context
layout: provider
modified: '2026-11-05'
name: DevOps Agent
nav: Providers
network: true
overview: 'DevOps Agent is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DevOps, Cloud Automation, Artificial Intelligence, and Multi-Cloud.


  The DevOps Agent catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DevOps Agent''s developer surface includes documentation and 15 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: DevOps Agent API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: devopsagent-io-rules
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 19.0
    discoverability: 53.6
    operational_transparency: 26.3
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Devopsagent Io Domain Security
  slug: devopsagent-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: devopsagent-io
tags:
- Company
- DevOps
- Cloud Automation
- Artificial Intelligence
- Multi-Cloud
website: https://devopsagent.io/
---
