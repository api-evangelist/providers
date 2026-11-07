---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 96
  human_in_the_loop: 1
  name: Okareo Agentic Access
  operation_count: 157
  slug: okareo-agentic-access
  summary_line: 157 operations · 96 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Manage account, profile, and users.
  name: Okareo Admin API
  slug: okareo-admin-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Query analytics metadata and run analytics queries.
  name: Okareo Analytics API
  slug: okareo-analytics-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Authentication, token exchange, and API key management.
  name: Okareo Auth & API Keys API
  slug: okareo-auth-api-keys-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Chat sessions, messages, and tool registry.
  name: Okareo Chat API
  slug: okareo-chat-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Create, generate, validate, and manage Checks.
  name: Okareo Checks API
  slug: okareo-checks-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Create and manage dashboards and scenario-trend views.
  name: Okareo Dashboards API
  slug: okareo-dashboards-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Query datapoints and manage filters.
  name: Okareo Datapoints API
  slug: okareo-datapoints-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Register and manage Drivers (simulated callers/users).
  name: Okareo Drivers API
  slug: okareo-drivers-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: The Inbox API from Okareo — 1 operation(s) for inbox.
  name: Okareo Inbox API
  slug: okareo-inbox-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Register Targets/models under test and organize them into groups.
  name: Okareo Models API
  slug: okareo-models-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Ingest live conversations and receive provider monitoring webhooks.
  name: Okareo Monitoring API
  slug: okareo-monitoring-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: The Notes API from Okareo — 2 operation(s) for notes.
  name: Okareo Notes API
  slug: okareo-notes-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Configure notifications and view notification history.
  name: Okareo Notifications API
  slug: okareo-notifications-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: The Organization API from Okareo — 1 operation(s) for organization.
  name: Okareo Organization API
  slug: okareo-organization-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Create and manage Projects.
  name: Okareo Projects API
  slug: okareo-projects-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Create, upload, generate, and download Scenario sets.
  name: Okareo Scenarios & Datasets API
  slug: okareo-scenarios-datasets-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Retrieve reusable template variables.
  name: Okareo Templates API
  slug: okareo-templates-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Run, submit, compare, and inspect evaluation Runs.
  name: Okareo Test Runs & Evaluations API
  slug: okareo-test-runs-evaluations-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Ingest and query traces from live agent runs.
  name: Okareo Traces API
  slug: okareo-traces-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Retrieve account usage metrics.
  name: Okareo Usage API
  slug: okareo-usage-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Voice calls, streaming, and observers.
  name: Okareo Voice API
  slug: okareo-voice-api
- baseURL: https://api.okareo.com
  baseurl_source: declared
  description: Configure voice provider integrations.
  name: Okareo Voice Integrations API
  slug: okareo-voice-integrations-api
artifact_total: 35
common:
- group: agent
  href: https://artifacts.apis.io/okareo/agentic-access/okareo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/okareo-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/okareo/plans/okareo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/okareo-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/okareo/rules/okareo-rules.yml
  title: ''
  type: Spectral
  url: rules/okareo-rules.yml
- group: design
  href: https://artifacts.apis.io/okareo/json-ld/okareo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/okareo-context.jsonld
- group: design
  href: https://artifacts.apis.io/okareo/vocabulary/okareo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/okareo-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/okareo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/okareo/data-model/okareo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/okareo-data-model.yml
- group: design
  href: https://artifacts.apis.io/okareo/errors/okareo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/okareo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/okareo/conformance/okareo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/okareo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/okareo/llms/okareo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/okareo-llms.txt
- group: other
  href: https://artifacts.apis.io/okareo/hosts/okareo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/okareo-hosts.yml
- group: build
  href: https://artifacts.apis.io/okareo/packages/okareo-packages.yml
  title: ''
  type: SDKs
  url: packages/okareo-packages.yml
- group: build
  href: https://artifacts.apis.io/okareo/packages/okareo-packages.yml
  title: ''
  type: Packages
  url: packages/okareo-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://okareo.com/company/news/ai4-2026
- group: auth
  href: https://artifacts.apis.io/okareo/security/okareo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/okareo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://okareo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.okareo.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://okareo.com/docs/getting-started/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://okareo.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://okareo.com/blog/posts
- group: start
  title: ''
  type: SignUp
  url: https://app.okareo.com/account/sign-up
- group: other
  title: ''
  type: SignIn
  url: https://app.okareo.com/account/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://okareo.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://okareo.com/terms
created: '2026-10-18'
description: Okareo provides a platform to simulate real users for voice and text agents, enabling synthetic data generation, fine‑tuning, and comprehensive evaluation of conversational AI. Their service creates realistic driver simulations across multiple languages and dialects, helping teams detect edge cases, improve agent performance, and ensure compliance. Okareo’s tools support CI integration, RAG, and agent monitoring, delivering scalable, parallel synthetic interactions for robust testing and development.
image: https://framerusercontent.com/images/oCOATXPZSeGlROinQxI6daaezQ.png
json_schemas:
- name: DatapointFilterItem
  property_count: 19
  slug: okareo-datapoint-filter-item
- name: DatapointListItem
  property_count: 43
  slug: okareo-datapoint-list-item
- name: DriverModelSchema
  property_count: 13
  slug: okareo-driver-model-schema
- name: ScenarioSetGenerate
  property_count: 15
  slug: okareo-scenario-set-generate
- name: TestRunItem
  property_count: 23
  slug: okareo-test-run-item
- name: TestRunPayloadV2
  property_count: 13
  slug: okareo-test-run-payload-v2
jsonld:
- class_count: 120
  name: Okareo Context
  property_count: 299
  slug: okareo-context
layout: provider
modified: '2026-10-18'
name: Okareo
nav: Providers
network: true
overview: 'Okareo publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Analytics API, Auth & API Keys API, and 19 more. Tagged areas include Company, Artificial Intelligence, Synthetic Data, Voice Agents, and Testing.


  The Okareo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Okareo''s developer surface includes documentation, getting-started guide, pricing, engineering blog, signup flow, and 19 more developer resources.'
plans:
- name: Okareo Plans Pricing
  plan_count: 2
  slug: okareo-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Okareo API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: okareo-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 43.4
    contract_governance: 35.6
    contract_quality: 59.0
    developer_ergonomics: 20.8
    discoverability: 74.1
    operational_transparency: 0.0
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/okareo/okareo-2026-11-03T140534.png
security:
- kind: domain-security
  name: Okareo Domain Security
  slug: okareo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: okareo-add-and-retrieve-datapoints
  slug: okareo-add-and-retrieve-datapoints
- name: okareo-run-test-and-evaluate
  slug: okareo-run-test-and-evaluate
slug: okareo
tags:
- Company
- Artificial Intelligence
- Synthetic Data
- Voice Agents
- Testing
website: https://okareo.com/
---
