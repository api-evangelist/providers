---
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Human Review & Approval REST API as documented
  name: AgentFabric REST API
  slug: agentfabric-rest-api
- baseURL: https://rest.agentfabric.dev
  baseurl_source: declared
  description: 'agentfabric-dev API as documented publicly: 31 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: agentfabric-dev API
  slug: agentfabric-dev-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/agentfabric-dev/rules/agentfabric-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/agentfabric-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/agentfabric-dev/json-ld/agentfabric-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentfabric-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentfabric-dev/vocabulary/agentfabric-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentfabric-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentfabric-dev/data-model/agentfabric-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentfabric-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/agentfabric-dev/authentication/agentfabric-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentfabric-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentfabric-dev/conformance/agentfabric-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentfabric-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentfabric-dev/llms/agentfabric-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentfabric-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/agentfabric-dev/hosts/agentfabric-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentfabric-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentfabric-dev/vendors/agentfabric-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentfabric-dev-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.agentfabric.dev/
- group: auth
  href: https://artifacts.apis.io/agentfabric-dev/security/agentfabric-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentfabric-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentfabric.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://agentfabric.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://agentfabric.dev/signup/
- group: start
  title: ''
  type: SignUp
  url: https://agentfabric.dev/signup/
created: '2026-10-30'
description: AgentFabric.dev provides a Human Review & Approval API for AI agents, enabling agents to send generated content such as URLs, images, and documents to human reviewers for approval, feedback, and audit trails. It supports both Model Context Protocol (MCP) and traditional REST interfaces, offering self‑sign‑up via create_tenant, no credit‑card required, and a dashboard for managing reviews. This service is designed to integrate seamlessly with AI workflows, ensuring compliance and oversight.
json_schemas:
- name: GetV1ReviewRequestidResponse
  property_count: 8
  slug: agentfabric-dev-get-v1-review-requestid-response
- name: PostV1ReviewRequestidDecisionRequest
  property_count: 3
  slug: agentfabric-dev-post-v1-review-requestid-decision-request
- name: PostV1ReviewRequestidDecisionResponse
  property_count: 3
  slug: agentfabric-dev-post-v1-review-requestid-decision-response
- name: PostV1ReviewRequestidNotifyResponse
  property_count: 2
  slug: agentfabric-dev-post-v1-review-requestid-notify-response
- name: PostV1ReviewRequestsRequest
  property_count: 5
  slug: agentfabric-dev-post-v1-review-requests-request
- name: PostYourEndpointRequest
  property_count: 4
  slug: agentfabric-dev-post-your-endpoint-request
jsonld:
- class_count: 41
  name: Agentfabric Dev Context
  property_count: 63
  slug: agentfabric-dev-context
layout: provider
modified: '2026-10-30'
name: agentfabric-dev
nav: Providers
network: true
overview: 'agentfabric-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, HumanReview, MCP, and REST.


  The agentfabric-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  agentfabric-dev''s developer surface includes authentication, documentation, getting-started guide, signup flow, and 11 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: agentfabric-dev API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: agentfabric-dev-rules
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 42.9
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentfabric Dev Authentication
  slug: agentfabric-dev-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Agentfabric Dev Domain Security
  slug: agentfabric-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agentfabric-dev
tags:
- Company
- AI
- HumanReview
- MCP
- REST
- Automation
website: https://agentfabric.dev/
---
