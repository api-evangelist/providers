---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 105
  human_in_the_loop: 2
  name: Roark Agentic Access
  operation_count: 191
  slug: roark-agentic-access
  summary_line: 191 operations · 105 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Agent API from Roark — 10 operation(s) for agent.
  name: Roark Agent API
  slug: roark-agent-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Agent Config API from Roark — 5 operation(s) for agent config.
  name: Roark Agent Config API
  slug: roark-agent-config-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Agent Endpoint API from Roark — 2 operation(s) for agent endpoint.
  name: Roark Agent Endpoint API
  slug: roark-agent-endpoint-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Analytics API from Roark — 2 operation(s) for analytics.
  name: Roark Analytics API
  slug: roark-analytics-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Autoimprove API from Roark — 7 operation(s) for autoimprove.
  name: Roark Autoimprove API
  slug: roark-autoimprove-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Benchmark API from Roark — 6 operation(s) for benchmark.
  name: Roark Benchmark API
  slug: roark-benchmark-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Call API from Roark — 9 operation(s) for call.
  name: Roark Call API
  slug: roark-call-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Chat API from Roark — 4 operation(s) for chat.
  name: Roark Chat API
  slug: roark-chat-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The CLI Auth API from Roark — 1 operation(s) for cli auth.
  name: Roark CLI Auth API
  slug: roark-cli-auth-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Config API from Roark — 2 operation(s) for config.
  name: Roark Config API
  slug: roark-config-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Customer Flow API from Roark — 5 operation(s) for customer flow.
  name: Roark Customer Flow API
  slug: roark-customer-flow-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Customer Flow Edge Case API from Roark — 3 operation(s) for customer flow edge case.
  name: Roark Customer Flow Edge Case API
  slug: roark-customer-flow-edge-case-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Dashboard API from Roark — 6 operation(s) for dashboard.
  name: Roark Dashboard API
  slug: roark-dashboard-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Health API from Roark — 1 operation(s) for health.
  name: Roark Health API
  slug: roark-health-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The HTTP Request Definition API from Roark — 2 operation(s) for http request definition.
  name: Roark HTTP Request Definition API
  slug: roark-http-request-definition-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Issue API from Roark — 2 operation(s) for issue.
  name: Roark Issue API
  slug: roark-issue-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Knowledge Base API from Roark — 2 operation(s) for knowledge base.
  name: Roark Knowledge Base API
  slug: roark-knowledge-base-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Me API from Roark — 3 operation(s) for me.
  name: Roark Me API
  slug: roark-me-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Metric API from Roark — 5 operation(s) for metric.
  name: Roark Metric API
  slug: roark-metric-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Metric Collection Job API from Roark — 5 operation(s) for metric collection job.
  name: Roark Metric Collection Job API
  slug: roark-metric-collection-job-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Metric Policy API from Roark — 2 operation(s) for metric policy.
  name: Roark Metric Policy API
  slug: roark-metric-policy-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Organization Project API Key API from Roark — 2 operation(s) for organization project api key.
  name: Roark Organization Project API Key API
  slug: roark-organization-project-api-key-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Organization Project API from Roark — 2 operation(s) for organization project.
  name: Roark Organization Project API
  slug: roark-organization-project-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Organization Project Member API from Roark — 2 operation(s) for organization project member.
  name: Roark Organization Project Member API
  slug: roark-organization-project-member-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Phone Number API from Roark — 4 operation(s) for phone number.
  name: Roark Phone Number API
  slug: roark-phone-number-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Project API from Roark — 1 operation(s) for project.
  name: Roark Project API
  slug: roark-project-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Prospect Simulation API from Roark — 3 operation(s) for prospect simulation.
  name: Roark Prospect Simulation API
  slug: roark-prospect-simulation-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Simulation API from Roark — 10 operation(s) for simulation.
  name: Roark Simulation API
  slug: roark-simulation-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Simulation Environment API from Roark — 2 operation(s) for simulation environment.
  name: Roark Simulation Environment API
  slug: roark-simulation-environment-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Simulation Job API from Roark — 3 operation(s) for simulation job.
  name: Roark Simulation Job API
  slug: roark-simulation-job-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Simulation Persona API from Roark — 2 operation(s) for simulation persona.
  name: Roark Simulation Persona API
  slug: roark-simulation-persona-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Simulation Run Plan API from Roark — 2 operation(s) for simulation run plan.
  name: Roark Simulation Run Plan API
  slug: roark-simulation-run-plan-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Simulation Run Plan Job API from Roark — 7 operation(s) for simulation run plan job.
  name: Roark Simulation Run Plan Job API
  slug: roark-simulation-run-plan-job-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Simulation Template API from Roark — 1 operation(s) for simulation template.
  name: Roark Simulation Template API
  slug: roark-simulation-template-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Usage API from Roark — 1 operation(s) for usage.
  name: Roark Usage API
  slug: roark-usage-api
- baseURL: https://api.roark.ai
  baseurl_source: declared
  description: The Webhook API from Roark — 2 operation(s) for webhook.
  name: Roark Webhook API
  slug: roark-webhook-api
artifact_total: 55
asyncapis:
- description: ''
  name: Roark Webhooks
  slug: roark-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/roark/agentic-access/roark-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/roark-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/roark/plans/roark-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/roark-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/roark/rules/roark-rules.yml
  title: ''
  type: Spectral
  url: rules/roark-rules.yml
- group: design
  href: https://artifacts.apis.io/roark/json-ld/roark-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/roark-context.jsonld
- group: design
  href: https://artifacts.apis.io/roark/vocabulary/roark-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/roark-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/roark/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/roark/asyncapi/roark-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/roark-webhooks.yml
- group: design
  href: https://artifacts.apis.io/roark/data-model/roark-data-model.yml
  title: ''
  type: DataModel
  url: data-model/roark-data-model.yml
- group: operate
  href: https://artifacts.apis.io/roark/changelog/roark-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/roark-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://roark.ai/security
- group: auth
  href: https://artifacts.apis.io/roark/authentication/roark-authentication.yml
  title: ''
  type: Authentication
  url: authentication/roark-authentication.yml
- group: design
  href: https://artifacts.apis.io/roark/errors/roark-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/roark-problem-types.yml
- group: design
  href: https://artifacts.apis.io/roark/conformance/roark-conformance.yml
  title: ''
  type: Conformance
  url: conformance/roark-conformance.yml
- group: agent
  href: https://artifacts.apis.io/roark/llms/roark-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/roark-llms.txt
- group: other
  href: https://artifacts.apis.io/roark/a2a/roark-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/roark-a2a.yml
- group: other
  href: https://artifacts.apis.io/roark/hosts/roark-hosts.yml
  title: ''
  type: Hosts
  url: hosts/roark-hosts.yml
- group: other
  href: https://artifacts.apis.io/roark/vendors/roark-vendors.yml
  title: ''
  type: Vendors
  url: vendors/roark-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://changelog.roark.ai/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.roark.ai
- group: auth
  title: ''
  type: Security
  url: https://roark.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://platform.roark.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/roarkhq
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.roark.ai/changelog
- group: auth
  href: https://artifacts.apis.io/roark/security/roark-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/roark-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/roark/security/roark-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/roark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://roark.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.roark.ai/login
- group: docs
  title: ''
  type: Documentation
  url: https://docs.roark.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.roark.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.roark.ai/documentation/getting-started/introduction
- group: company
  title: ''
  type: Blog
  url: https://roark.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://roark.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://roark.ai/signup
created: '2026-10-29'
description: Roark provides a platform for voice AI testing, evaluation, and continuous improvement. Their services include simulation testing, post‑call analysis, human review, and self‑improvement loops for voice agents across industries such as healthcare, finance, insurance, and retail. Roark helps organizations ensure production‑grade voice AI performance by offering load testing, health checks, benchmarking, and detailed analytics, enabling rapid iteration and reliable deployment of conversational agents.
image: https://roark.ai/og.png
json_schemas:
- name: DashboardInput
  property_count: 6
  slug: roark-dashboard-input
- name: Dashboard
  property_count: 10
  slug: roark-dashboard
- name: GetSimulationPlanJobResponse
  property_count: 11
  slug: roark-get-simulation-plan-job-response
- name: MetricCollectionJobMetricValuesResponse
  property_count: 0
  slug: roark-metric-collection-job-metric-values-response
- name: SimulationJobResponse
  property_count: 20
  slug: roark-simulation-job-response
- name: UpdateDashboardInput
  property_count: 6
  slug: roark-update-dashboard-input
jsonld:
- class_count: 120
  name: Roark Context
  property_count: 325
  slug: roark-context
layout: provider
modified: '2026-10-29'
name: Roark
nav: Providers
network: true
overview: 'Roark publishes 36 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Agent Config API, Agent Endpoint API, and 33 more. Tagged areas include Company, VoiceAI, Testing, Evaluation, and Benchmarking.


  The Roark catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Roark''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Roark Plans Pricing
  plan_count: 3
  slug: roark-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Roark API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 1
  slug: roark-rules
score:
  band: strong
  composite: 66.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 73.6
    developer_ergonomics: 54.2
    discoverability: 66.1
    operational_transparency: 55.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Roark Authentication
  slug: roark-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Roark Domain Security
  slug: roark-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Roark Trust Center
  slug: roark-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
skill_count: 5
skills:
- name: roark-analytics-query
  slug: roark-analytics-query
- name: roark-create-and-list-projects
  slug: roark-create-and-list-projects
- name: roark-create-and-retrieve-customer-flow
  slug: roark-create-and-retrieve-customer-flow
- name: health-check
  slug: roark-health-check
- name: roark-webhook-create-and-manage
  slug: roark-webhook-create-and-manage
slug: roark
tags:
- Company
- VoiceAI
- Testing
- Evaluation
- Benchmarking
website: https://roark.ai
---
