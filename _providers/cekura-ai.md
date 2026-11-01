---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 200
  human_in_the_loop: 2
  name: Cekura Ai Agentic Access
  operation_count: 302
  slug: cekura-ai-agentic-access
  summary_line: 302 operations · 200 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.cekura.ai
  baseurl_source: declared
  description: The AI Agents API from Cekura — 1 operation(s) for ai agents.
  name: Cekura AI Agents API
  slug: cekura-ai-ai-agents-api
- baseURL: https://api.cekura.ai
  baseurl_source: declared
  description: The Call Logs API from Cekura — 2 operation(s) for call logs.
  name: Cekura Call Logs API
  slug: cekura-ai-call-logs-api
- baseURL: https://api.cekura.ai
  baseurl_source: declared
  description: The dashboards API from Cekura — 9 operation(s) for dashboards.
  name: Cekura Dashboards API
  slug: cekura-ai-dashboards-api
- baseURL: https://api.cekura.ai
  baseurl_source: declared
  description: The Evaluators API from Cekura — 34 operation(s) for evaluators.
  name: Cekura Evaluators API
  slug: cekura-ai-evaluators-api
- baseURL: https://api.cekura.ai
  baseurl_source: declared
  description: The Metrics API from Cekura — 2 operation(s) for metrics.
  name: Cekura Metrics API
  slug: cekura-ai-metrics-api
- baseURL: https://api.cekura.ai
  baseurl_source: declared
  description: The Observability API from Cekura — 47 operation(s) for observability.
  name: Cekura Observability API
  slug: cekura-ai-observability-api
- baseURL: https://api.cekura.ai
  baseurl_source: declared
  description: The Results API from Cekura — 17 operation(s) for results.
  name: Cekura Results API
  slug: cekura-ai-results-api
- baseURL: https://api.cekura.ai
  baseurl_source: declared
  description: The Runs API from Cekura — 7 operation(s) for runs.
  name: Cekura Runs API
  slug: cekura-ai-runs-api
- baseURL: https://api.cekura.ai
  baseurl_source: declared
  description: The Scenarios API from Cekura — 6 operation(s) for scenarios.
  name: Cekura Scenarios API
  slug: cekura-ai-scenarios-api
- baseURL: https://api.cekura.ai
  baseurl_source: declared
  description: The Schedules API from Cekura — 2 operation(s) for schedules.
  name: Cekura Schedules API
  slug: cekura-ai-schedules-api
- baseURL: https://api.cekura.ai
  baseurl_source: declared
  description: The slack API from Cekura — 1 operation(s) for slack.
  name: Cekura Slack API
  slug: cekura-ai-slack-api
- baseURL: https://api.cekura.ai
  baseurl_source: declared
  description: The test_framework API from Cekura — 128 operation(s) for test_framework.
  name: Cekura Test Framework API
  slug: cekura-ai-test-framework-api
- baseURL: https://api.cekura.ai
  baseurl_source: declared
  description: The user API from Cekura — 8 operation(s) for user.
  name: Cekura User API
  slug: cekura-ai-user-api
artifact_total: 32
asyncapis:
- description: ''
  name: Cekura Ai Webhooks
  slug: cekura-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/cekura-ai/agentic-access/cekura-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cekura-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cekura-ai/plans/cekura-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cekura-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cekura-ai/rules/cekura-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/cekura-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/cekura-ai/json-ld/cekura-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cekura-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/cekura-ai/vocabulary/cekura-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cekura-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cekura-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cekura-ai/asyncapi/cekura-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cekura-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/cekura-ai/data-model/cekura-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cekura-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/cekura-ai/changelog/cekura-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cekura-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/cekura-ai/authentication/cekura-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cekura-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/cekura-ai/errors/cekura-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cekura-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cekura-ai/conformance/cekura-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cekura-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cekura-ai/llms/cekura-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cekura-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/cekura-ai/a2a/cekura-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cekura-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cekura-ai/mcp/cekura-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cekura-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cekura-ai/well-known/cekura-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cekura-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/cekura-ai/hosts/cekura-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cekura-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/cekura-ai/vendors/cekura-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cekura-ai-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.cekura.ai/sign-up
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.cekura.ai/changelog
- group: auth
  href: https://artifacts.apis.io/cekura-ai/security/cekura-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cekura-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cekura.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.cekura.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cekura.ai/documentation/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cekura.ai/documentation/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cekura.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.cekura.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://www.cekura.ai/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cekura-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cekura.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cekura.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cekura.ai/privacy-policy
created: '2026-10-28'
description: Cekura provides automated quality assurance for voice AI and chat AI agents. Their platform lets developers test, monitor, and continuously improve voice agents by simulating real production calls, identifying issues, and suggesting fixes. Features include benchmark comparisons across leading platforms, detailed metric labs, observability tracing, and integrations with partners like LiveKit, Cisco, and ElevenLabs. Cekura aims to accelerate agent deployment, ensuring reliability and performance before going live.
image: https://www.cekura.ai/og_image.png
json_schemas:
- name: Organization
  property_count: 61
  slug: cekura-ai-organization
- name: PatchedProject
  property_count: 69
  slug: cekura-ai-patched-project
- name: Project
  property_count: 69
  slug: cekura-ai-project
- name: ResultDetailV2
  property_count: 41
  slug: cekura-ai-result-detail-v2
- name: SchemaCombinedResultsReport
  property_count: 16
  slug: cekura-ai-schema-combined-results-report
- name: SchemaScenario
  property_count: 33
  slug: cekura-ai-schema-scenario
jsonld:
- class_count: 120
  name: Cekura Ai Context
  property_count: 458
  slug: cekura-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.cekura.ai.
  name: Cekura MCP Server
  slug: cekura-ai-mcp-yml
modified: '2026-10-28'
name: Cekura
nav: Providers
network: true
overview: 'Cekura publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI Agents API, Call Logs API, Dashboards API, and 10 more. Tagged areas include Company, VoiceAI, QA, Testing, and Benchmarking.


  The Cekura catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Cekura''s developer surface includes changelog, authentication, signup flow, documentation, API reference, getting-started guide, support, and 25 more developer resources.'
plans:
- name: Cekura Ai Plans Pricing
  plan_count: 3
  slug: cekura-ai-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Cekura API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: cekura-ai-rules
score:
  band: strong
  composite: 58.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 69.4
    developer_ergonomics: 58.9
    discoverability: 65.0
    operational_transparency: 28.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cekura Ai Authentication
  slug: cekura-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cekura Ai Domain Security
  slug: cekura-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: cekura-ai-call-logs-mark-metric-vote
  slug: cekura-ai-call-logs-mark-metric-vote
- name: cekura-ai-create-and-update-scenario
  slug: cekura-ai-create-and-update-scenario
- name: cekura-ai-create-project-and-enable-personalities
  slug: cekura-ai-create-project-and-enable-personalities
- name: cekura-ai-queue-failure-analysis
  slug: cekura-ai-queue-failure-analysis
- name: cekura-ai-run-chat
  slug: cekura-ai-run-chat
slug: cekura-ai
tags:
- Company
- VoiceAI
- QA
- Testing
- Benchmarking
website: https://cekura.ai
---
