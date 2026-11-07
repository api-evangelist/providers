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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Abmeter Ai Agentic Access
  operation_count: 53
  slug: abmeter-ai-agentic-access
  summary_line: 53 operations · 29 acting
api_count: 1
apis:
- baseURL: https://abmeter.ai/api/v1
  baseurl_source: declared
  description: The Agent Feedback API from ABMeter — 1 operation(s) for agent feedback.
  name: ABMeter Agent Feedback API
  slug: abmeter-ai-agent-feedback-api
- baseURL: https://abmeter.ai/api/v1
  baseurl_source: declared
  description: The Assignment Config API from ABMeter — 1 operation(s) for assignment config.
  name: ABMeter Assignment Config API
  slug: abmeter-ai-assignment-config-api
- baseURL: https://abmeter.ai/api/v1
  baseurl_source: declared
  description: The Audiences API from ABMeter — 2 operation(s) for audiences.
  name: ABMeter Audiences API
  slug: abmeter-ai-audiences-api
- baseURL: https://abmeter.ai/api/v1
  baseurl_source: declared
  description: The Event Types API from ABMeter — 2 operation(s) for event types.
  name: ABMeter Event Types API
  slug: abmeter-ai-event-types-api
- baseURL: https://abmeter.ai/api/v1
  baseurl_source: declared
  description: The Events API from ABMeter — 1 operation(s) for events.
  name: ABMeter Events API
  slug: abmeter-ai-events-api
- baseURL: https://abmeter.ai/api/v1
  baseurl_source: declared
  description: The Experiments API from ABMeter — 5 operation(s) for experiments.
  name: ABMeter Experiments API
  slug: abmeter-ai-experiments-api
- baseURL: https://abmeter.ai/api/v1
  baseurl_source: declared
  description: The Exposures API from ABMeter — 1 operation(s) for exposures.
  name: ABMeter Exposures API
  slug: abmeter-ai-exposures-api
- baseURL: https://abmeter.ai/api/v1
  baseurl_source: declared
  description: The Feature Flags API from ABMeter — 4 operation(s) for feature flags.
  name: ABMeter Feature Flags API
  slug: abmeter-ai-feature-flags-api
- baseURL: https://abmeter.ai/api/v1
  baseurl_source: declared
  description: The Metrics API from ABMeter — 2 operation(s) for metrics.
  name: ABMeter Metrics API
  slug: abmeter-ai-metrics-api
- baseURL: https://abmeter.ai/api/v1
  baseurl_source: declared
  description: The Parameters API from ABMeter — 2 operation(s) for parameters.
  name: ABMeter Parameters API
  slug: abmeter-ai-parameters-api
- baseURL: https://abmeter.ai/api/v1
  baseurl_source: declared
  description: The Spaces API from ABMeter — 2 operation(s) for spaces.
  name: ABMeter Spaces API
  slug: abmeter-ai-spaces-api
- baseURL: https://abmeter.ai/api/v1
  baseurl_source: declared
  description: The Up API from ABMeter — 1 operation(s) for up.
  name: ABMeter Up API
  slug: abmeter-ai-up-api
- baseURL: https://abmeter.ai/api/v1
  baseurl_source: declared
  description: The User Assignments API from ABMeter — 1 operation(s) for user assignments.
  name: ABMeter User Assignments API
  slug: abmeter-ai-user-assignments-api
- baseURL: https://abmeter.ai/api/v1
  baseurl_source: declared
  description: The Variants API from ABMeter — 2 operation(s) for variants.
  name: ABMeter Variants API
  slug: abmeter-ai-variants-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/abmeter-ai/agentic-access/abmeter-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/abmeter-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/abmeter-ai/rules/abmeter-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/abmeter-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/abmeter-ai/json-ld/abmeter-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/abmeter-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/abmeter-ai/vocabulary/abmeter-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/abmeter-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/abmeter-ai/data-model/abmeter-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/abmeter-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/abmeter-ai/authentication/abmeter-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/abmeter-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/abmeter-ai/errors/abmeter-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/abmeter-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/abmeter-ai/conformance/abmeter-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/abmeter-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/abmeter-ai/llms/abmeter-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/abmeter-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/abmeter-ai/mcp/abmeter-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/abmeter-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/abmeter-ai/mcp/abmeter-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/abmeter-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/abmeter-ai/well-known/abmeter-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/abmeter-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/abmeter-ai/hosts/abmeter-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/abmeter-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/abmeter-ai/vendors/abmeter-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/abmeter-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/abmeter-ai/packages/abmeter-ai-packages.yml
  title: ''
  type: Packages
  url: packages/abmeter-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://abmeter.ai/lab/sdks/js
- group: start
  title: ''
  type: Login
  url: https://abmeter.ai/login
- group: auth
  href: https://artifacts.apis.io/abmeter-ai/security/abmeter-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abmeter-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abmeter.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://abmeter.ai/lab
- group: docs
  title: ''
  type: Documentation
  url: https://abmeter.ai/lab/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://abmeter.ai/lab/quick-start
- group: operate
  title: ''
  type: Support
  url: https://abmeter.ai/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abmeter.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abmeter.ai/privacy
created: '2026-10-31'
description: ABMeter is a tool designed to make A/B testing a standard development practice for individuals and small teams, similar to unit tests. It was built because at the founder's previous job each squad used its own A/B testing tool, preventing comparison of results and confidence in statistical conclusions. ABMeter provides a shared platform for running experiments, offering quick start guides, API documentation, and support for integrating AI-generated code. For questions or consulting, contact the team via the provided email.
image: https://abmeter.ai/assets/abmeter-logo-be011116.svg
json_schemas:
- name: AudiencesInput
  property_count: 0
  slug: abmeter-ai-audiences-input
- name: EventType
  property_count: 6
  slug: abmeter-ai-event-type
- name: Experiment
  property_count: 13
  slug: abmeter-ai-experiment
- name: ExposureSubmission
  property_count: 8
  slug: abmeter-ai-exposure-submission
- name: GlobalAudience
  property_count: 4
  slug: abmeter-ai-global-audience
- name: ParameterExposure
  property_count: 8
  slug: abmeter-ai-parameter-exposure
jsonld:
- class_count: 16
  name: Abmeter Ai Context
  property_count: 44
  slug: abmeter-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.abmeter.ai.
  name: ABMeter MCP Server
  slug: abmeter-ai-mcp-yml
modified: '2026-10-31'
name: ABMeter
nav: Providers
network: true
overview: 'ABMeter publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Feedback API, Assignment Config API, Audiences API, and 11 more. Tagged areas include A/B Testing, Analytics, Experimentation, Software-as-a-Service, and Developer Tools.


  The ABMeter catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ABMeter''s developer surface includes authentication, documentation, getting-started guide, support, and 21 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: ABMeter API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: abmeter-ai-rules
scopes:
- name: Abmeter Ai Scopes
  scope_count: 0
  slug: abmeter-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 17.1
    contract_governance: 19.7
    contract_quality: 65.8
    developer_ergonomics: 36.9
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Abmeter Ai Authentication
  slug: abmeter-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Abmeter Ai Domain Security
  slug: abmeter-ai-domain-security
  summary_line: TLSv1.3
slug: abmeter-ai
tags:
- A/B Testing
- Analytics
- Experimentation
- Software-as-a-Service
- Developer Tools
website: https://abmeter.ai/
---
