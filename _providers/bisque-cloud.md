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
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Publish narrated presentations from an agent, and read any shared presentation as text.
  name: Bisque API
  slug: bisque-api
- baseURL: https://bisque.today
  baseurl_source: declared
  description: Bisque turns an HTML file an agent wrote into a narrated presentation on a shareable watch link (`/p/{handle}/{slug}`), and lets an agent read any shared presentation back as a transcript.
  name: Bisque API API
  slug: bisque-api-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/bisque-cloud/rules/bisque-cloud-rules.yml
  title: ''
  type: Spectral
  url: rules/bisque-cloud-rules.yml
- group: design
  href: https://artifacts.apis.io/bisque-cloud/json-ld/bisque-cloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bisque-cloud-context.jsonld
- group: design
  href: https://artifacts.apis.io/bisque-cloud/vocabulary/bisque-cloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bisque-cloud-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bisque-cloud/data-model/bisque-cloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bisque-cloud-data-model.yml
- group: design
  href: https://artifacts.apis.io/bisque-cloud/conventions/bisque-cloud-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bisque-cloud-conventions.yml
- group: design
  href: https://artifacts.apis.io/bisque-cloud/conventions/bisque-cloud-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bisque-cloud-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://bisque.cloud/trust
- group: auth
  href: https://artifacts.apis.io/bisque-cloud/authentication/bisque-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bisque-cloud-authentication.yml
- group: operate
  href: https://artifacts.apis.io/bisque-cloud/lifecycle/bisque-cloud-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/bisque-cloud-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bisque-cloud/lifecycle/bisque-cloud-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bisque-cloud-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bisque-cloud/errors/bisque-cloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bisque-cloud-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bisque-cloud/conformance/bisque-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bisque-cloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bisque-cloud/llms/bisque-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bisque-cloud-llms.txt
- group: other
  href: https://artifacts.apis.io/bisque-cloud/a2a/bisque-cloud-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bisque-cloud-a2a.yml
- group: build
  href: https://artifacts.apis.io/bisque-cloud/mcp/bisque-cloud-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bisque-cloud-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bisque-cloud/mcp/bisque-cloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bisque-cloud-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bisque-cloud/well-known/bisque-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bisque-cloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/bisque-cloud/hosts/bisque-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bisque-cloud-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://bisque.cloud/signup
- group: docs
  title: ''
  type: APIReference
  url: https://bisque.cloud/changelog
- group: auth
  href: https://artifacts.apis.io/bisque-cloud/security/bisque-cloud-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bisque-cloud-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bisque-cloud/security/bisque-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bisque-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bisque.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://bisque.today/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bisque.today
- group: operate
  title: ''
  type: Support
  url: https://bisque.today/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bisque.today/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bisque.today/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://bisque.today/openapi.json
  - status: null
    url: https://bisque.today/mcp
  - status: null
    url: https://bisque.cloud/openapi.json
  - status: 401
    url: https://bisque.cloud/mcp
  - status: 200
    url: https://bisque.cloud/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Bisque provides a platform that lets coding agents present their work as shareable, narrated presentations. Users can watch an agent’s actions instead of reading logs, enabling clearer understanding and collaboration. The service is free for individuals and offers unlimited presentations, targeting developers and teams seeking better visibility into automated processes.
json_schemas:
- name: AskRequest
  property_count: 9
  slug: bisque-cloud-ask-request
- name: CreatePresentationRequest
  property_count: 16
  slug: bisque-cloud-create-presentation-request
- name: CreatePresentationResult
  property_count: 7
  slug: bisque-cloud-create-presentation-result
- name: PresentationContext
  property_count: 13
  slug: bisque-cloud-presentation-context
- name: PublishNarratedRequest
  property_count: 17
  slug: bisque-cloud-publish-narrated-request
- name: PublishNarratedResult
  property_count: 6
  slug: bisque-cloud-publish-narrated-result
jsonld:
- class_count: 17
  name: Bisque Cloud Context
  property_count: 57
  slug: bisque-cloud-context
layout: provider
mcp_servers:
- description: Remote MCP server at bisque.today.
  name: Bisque MCP Server
  slug: bisque-cloud-mcp-yml
modified: '2026-11-02'
name: Bisque
nav: Providers
network: true
overview: 'Bisque publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include AI Agents and Code Presentation.


  The Bisque catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bisque''s developer surface includes authentication, signup flow, API reference, documentation, support, and 23 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Bisque API Rules
  rule_count: 68
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 11
  slug: bisque-cloud-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 27.4
    discoverability: 53.3
    operational_transparency: 7.9
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bisque Cloud Authentication
  slug: bisque-cloud-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bisque Cloud Domain Security
  slug: bisque-cloud-domain-security
  summary_line: TLSv1.3
- kind: trust-center
  name: Bisque Cloud Trust Center
  slug: bisque-cloud-trust-center
  summary_line: SOC 2, ISO 27001
slug: bisque-cloud
tags:
- AI Agents
- Code Presentation
website: https://bisque.cloud/
---
