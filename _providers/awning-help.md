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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'How to work with Awning: tools, workflows, and MCP endpoint for AI assistants.'
  name: Awning Agent API
  slug: awning-agent-api
- description: 'Awning API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Awning API
  slug: awning-help-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/awning-help/rules/awning-help-rules.yml
  title: ''
  type: Spectral
  url: rules/awning-help-rules.yml
- group: design
  href: https://artifacts.apis.io/awning-help/json-ld/awning-help-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/awning-help-context.jsonld
- group: design
  href: https://artifacts.apis.io/awning-help/vocabulary/awning-help-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/awning-help-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/awning-help/data-model/awning-help-data-model.yml
  title: ''
  type: DataModel
  url: data-model/awning-help-data-model.yml
- group: auth
  href: https://artifacts.apis.io/awning-help/authentication/awning-help-authentication.yml
  title: ''
  type: Authentication
  url: authentication/awning-help-authentication.yml
- group: design
  href: https://artifacts.apis.io/awning-help/conformance/awning-help-conformance.yml
  title: ''
  type: Conformance
  url: conformance/awning-help-conformance.yml
- group: agent
  href: https://artifacts.apis.io/awning-help/llms/awning-help-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/awning-help-llms.txt
- group: agent
  href: https://artifacts.apis.io/awning-help/mcp/awning-help-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/awning-help-mcp.yml
- group: agent
  href: https://artifacts.apis.io/awning-help/well-known/awning-help-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/awning-help-well-known.yml
- group: other
  href: https://artifacts.apis.io/awning-help/hosts/awning-help-hosts.yml
  title: ''
  type: Hosts
  url: hosts/awning-help-hosts.yml
- group: docs
  title: ''
  type: APIReference
  url: https://awning.help/agents/reference
- group: auth
  href: https://artifacts.apis.io/awning-help/security/awning-help-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/awning-help-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://awning.help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://awning.help/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://awning.help/terms
coverage:
  checked: '2026-11-02'
  detail: Public documentation exists but no machine-readable OpenAPI, AsyncAPI, GraphQL, or other spec is published.
  evidence:
  - status: 200
    url: https://awning.help/agents/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Awning is a platform that lets users find and book local services, classes, and rentals. Users can choose a time and book directly on Awning, or let AI assistants such as ChatGPT and Claude handle the booking. Businesses list themselves through their own assistant, enabling seamless scheduling.
image: https://awning.help/favicon.ico
json_schemas:
- name: PostSiteToolsCallRequest
  property_count: 2
  slug: awning-help-post-site-tools-call-request
jsonld:
- class_count: 1
  name: Awning Help Context
  property_count: 2
  slug: awning-help-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.awning.help requiring OAuth.
  name: Awning MCP Server
  slug: awning-help-mcp-yml
modified: '2026-11-02'
name: Awning
nav: Providers
network: true
overview: 'Awning is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Booking, Local Services, AI Assistant, Marketplace, and Scheduling.


  The Awning catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Awning''s developer surface includes authentication, API reference, and 13 more developer resources.'
plans:
- name: Awning Help Plans Pricing
  plan_count: 0
  slug: awning-help-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Awning Help Rate Limits
  slug: awning-help-rate-limits
rules:
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: Awning API Rules
  rule_count: 28
  severity_counts:
    error: 26
    hint: 0
    info: 1
    warn: 1
  slug: awning-help-rules
scopes:
- name: Awning Help Scopes
  scope_count: 0
  slug: awning-help-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 16.4
    developer_ergonomics: 15.5
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 22.9
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
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Awning Help Authentication
  slug: awning-help-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Awning Help Domain Security
  slug: awning-help-domain-security
  summary_line: TLSv1.3 · HSTS
slug: awning-help
tags:
- Booking
- Local Services
- AI Assistant
- Marketplace
- Scheduling
website: https://awning.help/
---
