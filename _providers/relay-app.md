---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Relay App Agentic Access
  operation_count: 8
  slug: relay-app-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.relay.app
  baseurl_source: declared
  description: Operations for managing and inspecting workflow run instances
  name: Relay App Runs API
  slug: relay-app-runs-api
- baseURL: https://api.relay.app
  baseurl_source: declared
  description: Webhook trigger endpoints for initiating workflow runs
  name: Relay App Webhooks API
  slug: relay-app-webhooks-api
- baseURL: https://api.relay.app
  baseurl_source: declared
  description: Operations for managing and triggering workflow runs
  name: Relay App Workflows API
  slug: relay-app-workflows-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Relay App Automation Runs API
  slug: open-relay-app-runs-api
- collection_type: open
  name: Relay App Automation Runs Webhooks API
  slug: open-relay-app-webhooks-api
- collection_type: open
  name: Relay App Automation Runs Workflows API
  slug: open-relay-app-workflows-api
- collection_type: open
  name: Relay App Automation API
  slug: open-relay-app
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/relay-app-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/relay-app-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/relay-app-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tryrelayapp
- group: company
  title: ''
  type: Website
  url: https://www.relay.app
- group: docs
  title: ''
  type: Documentation
  url: https://docs.relay.app/
- group: company
  title: ''
  type: Blog
  url: https://www.relay.app/blog
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/relay-app/refs/heads/main/json-ld/relay-app-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/relay-app/refs/heads/main/vocabulary/relay-app-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/relay-app/refs/heads/main/rules/relay-app-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.relay.app/llms.txt
created: '2026-03-16'
description: Relay.app is an AI-powered workflow automation platform that converts plain language into reliable visual workflows across 200+ app integrations. It supports webhook triggers, custom HTTP requests, scheduled automation, human-in-the-loop approval workflows, and MCP server tooling for AI agent integration. Developer features include API-triggered workflows, custom JavaScript execution, and integration with OpenAI, Anthropic, and other AI providers.
examples:
- key_count: 4
  name: Relay App Approve Workflow Step Example
  slug: relay-app-approve-workflow-step-example
- key_count: 4
  name: Relay App Trigger Webhook Example
  slug: relay-app-trigger-webhook-example
finops:
- name: Relay App Finops
  service_category: API
  slug: relay-app-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/relay-app.png
json_schemas:
- name: Relay App Workflow Run
  property_count: 7
  slug: relay-app-workflow-run
- name: Relay App Workflow
  property_count: 7
  slug: relay-app-workflow
json_structures:
- name: Relay App Workflow Structure
  property_count: 0
  slug: relay-app-workflow-structure
jsonld:
- class_count: 0
  name: Relay App Context
  property_count: 22
  slug: relay-app-context
layout: provider
modified: '2026-05-19'
name: Relay App
nav: Providers
network: true
overview: 'Relay App publishes 3 APIs on the [APIs.io](https://apis.io/) network: Runs API, Webhooks API, and Workflows API. Tagged areas include Automation, Workflows, Integration, No-Code, and Artificial Intelligence.


  The Relay App catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Relay App''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Relay App Plans Pricing
  plan_count: 3
  slug: relay-app-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Relay App Rate Limits
  slug: relay-app-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Relay App API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: relay-app-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Relay App API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 7
  slug: relay-app-rules
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 73.5
    catalog_earned_first_party: 0.0
    catalog_gap: 41.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 66.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/relay-app/refs/heads/main/screenshots/relay-app-2026-06-20T192825.png
security:
- kind: authentication
  name: Relay App Authentication
  slug: relay-app-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Relay App Domain Security
  slug: relay-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: relay-app
tags:
- Automation
- Workflows
- Integration
- No-Code
- Artificial Intelligence
- Webhook
website: https://www.relay.app
---
