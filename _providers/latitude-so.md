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
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 58
  human_in_the_loop: 2
  name: Latitude So Agentic Access
  operation_count: 139
  slug: latitude-so-agentic-access
  summary_line: 139 operations · 58 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Account API from Latitude — 2 operation(s) for account.
  name: Latitude Account API
  slug: latitude-so-account-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Agent Score API from Latitude — 3 operation(s) for agent score.
  name: Latitude Agent Score API
  slug: latitude-so-agent-score-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Analytics API from Latitude — 1 operation(s) for analytics.
  name: Latitude Analytics API
  slug: latitude-so-analytics-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Annotations API from Latitude — 2 operation(s) for annotations.
  name: Latitude Annotations API
  slug: latitude-so-annotations-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The API Keys API from Latitude — 2 operation(s) for api keys.
  name: Latitude API Keys API
  slug: latitude-so-api-keys-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Datasets API from Latitude — 10 operation(s) for datasets.
  name: Latitude Datasets API
  slug: latitude-so-datasets-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Experiments API from Latitude — 2 operation(s) for experiments.
  name: Latitude Experiments API
  slug: latitude-so-experiments-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Health API from Latitude — 1 operation(s) for health.
  name: Latitude Health API
  slug: latitude-so-health-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Imports API from Latitude — 4 operation(s) for imports.
  name: Latitude Imports API
  slug: latitude-so-imports-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Incidents API from Latitude — 2 operation(s) for incidents.
  name: Latitude Incidents API
  slug: latitude-so-incidents-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Members API from Latitude — 2 operation(s) for members.
  name: Latitude Members API
  slug: latitude-so-members-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Memory API from Latitude — 8 operation(s) for memory.
  name: Latitude Memory API
  slug: latitude-so-memory-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Monitors API from Latitude — 6 operation(s) for monitors.
  name: Latitude Monitors API
  slug: latitude-so-monitors-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The OAuth Keys API from Latitude — 2 operation(s) for oauth keys.
  name: Latitude OAuth Keys API
  slug: latitude-so-oauth-keys-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Projects API from Latitude — 3 operation(s) for projects.
  name: Latitude Projects API
  slug: latitude-so-projects-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Saved Searches API from Latitude — 3 operation(s) for saved searches.
  name: Latitude Saved Searches API
  slug: latitude-so-saved-searches-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Scores API from Latitude — 1 operation(s) for scores.
  name: Latitude Scores API
  slug: latitude-so-scores-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Sessions API from Latitude — 9 operation(s) for sessions.
  name: Latitude Sessions API
  slug: latitude-so-sessions-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Signals API from Latitude — 15 operation(s) for signals.
  name: Latitude Signals API
  slug: latitude-so-signals-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Spans API from Latitude — 1 operation(s) for spans.
  name: Latitude Spans API
  slug: latitude-so-spans-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Tools API from Latitude — 8 operation(s) for tools.
  name: Latitude Tools API
  slug: latitude-so-tools-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Traces API from Latitude — 10 operation(s) for traces.
  name: Latitude Traces API
  slug: latitude-so-traces-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Usage API from Latitude — 1 operation(s) for usage.
  name: Latitude Usage API
  slug: latitude-so-usage-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Users API from Latitude — 8 operation(s) for users.
  name: Latitude Users API
  slug: latitude-so-users-api
- baseURL: https://api.latitude.so
  baseurl_source: declared
  description: The Well-known API from Latitude — 1 operation(s) for well-known.
  name: Latitude Well Known API
  slug: latitude-so-well-known-api
artifact_total: 42
asyncapis:
- description: ''
  name: Latitude So Webhooks
  slug: latitude-so-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/latitude-so/agentic-access/latitude-so-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/latitude-so-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/latitude-so/plans/latitude-so-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/latitude-so-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/latitude-so/rules/latitude-so-rules.yml
  title: ''
  type: Spectral
  url: rules/latitude-so-rules.yml
- group: design
  href: https://artifacts.apis.io/latitude-so/json-ld/latitude-so-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/latitude-so-context.jsonld
- group: design
  href: https://artifacts.apis.io/latitude-so/vocabulary/latitude-so-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/latitude-so-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/latitude-so/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/latitude-so/asyncapi/latitude-so-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/latitude-so-webhooks.yml
- group: design
  href: https://artifacts.apis.io/latitude-so/data-model/latitude-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/latitude-so-data-model.yml
- group: start
  href: https://artifacts.apis.io/latitude-so/sandbox/latitude-so-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/latitude-so-sandbox.yml
- group: design
  href: https://artifacts.apis.io/latitude-so/errors/latitude-so-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/latitude-so-problem-types.yml
- group: design
  href: https://artifacts.apis.io/latitude-so/conformance/latitude-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/latitude-so-conformance.yml
- group: agent
  href: https://artifacts.apis.io/latitude-so/llms/latitude-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/latitude-so-llms.txt
- group: other
  href: https://artifacts.apis.io/latitude-so/a2a/latitude-so-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/latitude-so-a2a.yml
- group: agent
  href: https://artifacts.apis.io/latitude-so/well-known/latitude-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/latitude-so-well-known.yml
- group: other
  href: https://artifacts.apis.io/latitude-so/hosts/latitude-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/latitude-so-hosts.yml
- group: other
  href: https://artifacts.apis.io/latitude-so/vendors/latitude-so-vendors.yml
  title: ''
  type: Vendors
  url: vendors/latitude-so-vendors.yml
- group: build
  href: https://artifacts.apis.io/latitude-so/packages/latitude-so-packages.yml
  title: ''
  type: SDKs
  url: packages/latitude-so-packages.yml
- group: build
  href: https://artifacts.apis.io/latitude-so/packages/latitude-so-packages.yml
  title: ''
  type: Packages
  url: packages/latitude-so-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://latitude.so/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://latitude.so/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://latitude.so/pricing
- group: start
  title: ''
  type: Login
  url: https://console.latitude.so/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://latitude.so/changelog
- group: company
  title: ''
  type: Blog
  url: https://latitude.so/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.latitude.so/getting-started/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.latitude.so/
- group: docs
  title: ''
  type: APIReference
  url: https://api.latitude.so/docs
- group: auth
  href: https://artifacts.apis.io/latitude-so/authentication/latitude-so-authentication.yml
  title: ''
  type: Authentication
  url: authentication/latitude-so-authentication.yml
- group: auth
  href: https://artifacts.apis.io/latitude-so/security/latitude-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/latitude-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://latitude.so/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://docs.latitude.so/mcp
  - status: 200
    url: https://latitude.so/
  reason: no-developer-program
  state: none
created: '2026-10-18'
description: Latitude provides an AI agent observability and monitoring platform that helps developers track, debug, and improve the performance of AI-powered agents. The service offers real‑time telemetry, tracing, cost analysis, and tool‑call insights across multiple environments. It includes a developer portal, comprehensive documentation, pricing plans, and community resources such as Slack and GitHub integrations, enabling teams to build self‑healing, observable AI agents.
image: https://latitude.so/images/og-image.png
json_schemas:
- name: AnalyticsQuery
  property_count: 0
  slug: latitude-so-analytics-query
- name: CreateSignalBody
  property_count: 5
  slug: latitude-so-create-signal-body
- name: SessionDetail
  property_count: 35
  slug: latitude-so-session-detail
- name: SignalDetail
  property_count: 24
  slug: latitude-so-signal-detail
- name: SpanDetail
  property_count: 58
  slug: latitude-so-span-detail
- name: TraceDetail
  property_count: 31
  slug: latitude-so-trace-detail
jsonld:
- class_count: 120
  name: Latitude So Context
  property_count: 266
  slug: latitude-so-context
layout: provider
modified: '2026-10-18'
name: Latitude
nav: Providers
network: true
overview: 'Latitude publishes 25 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agent Score API, Analytics API, and 22 more. Tagged areas include Company, Artificial Intelligence, Observability, Monitoring, and Platform.


  The Latitude catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Latitude''s developer surface includes sandbox, pricing, changelog, engineering blog, getting-started guide, documentation, API reference, and 23 more developer resources.'
plans:
- name: Latitude So Plans Pricing
  plan_count: 2
  slug: latitude-so-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Latitude API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 8
  slug: latitude-so-rules
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 70.8
    developer_ergonomics: 58.9
    discoverability: 66.1
    operational_transparency: 23.7
  previous_composite: 57.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Latitude So Authentication
  slug: latitude-so-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Latitude So Domain Security
  slug: latitude-so-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: latitude-so-account-setup
  slug: latitude-so-account-setup
- name: latitude-so-create-monitor
  slug: latitude-so-create-monitor
- name: latitude-so-import-workflow
  slug: latitude-so-import-workflow
- name: latitude-so-retrieve-session-details
  slug: latitude-so-retrieve-session-details
slug: latitude-so
tags:
- Company
- Artificial Intelligence
- Observability
- Monitoring
- Platform
- Agents
website: https://latitude.so/
---
