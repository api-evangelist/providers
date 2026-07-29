---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Relay App Agentic Access
  operation_count: 8
  slug: relay-app-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 3
apis:
- description: Operations for managing and inspecting workflow run instances
  name: Relay App Runs API
  slug: relay-app-runs-api
- description: Webhook trigger endpoints for initiating workflow runs
  name: Relay App Webhooks API
  slug: relay-app-webhooks-api
- description: Operations for managing and triggering workflow runs
  name: Relay App Workflows API
  slug: relay-app-workflows-api
artifact_total: 18
collections:
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
overview: 'Relay App publishes 3 APIs on the [APIs.io](https://apis.io/) network: Runs API, Webhooks API, and Workflows API. Tagged areas include Automation, Workflow, Integration, No-Code, and AI.


  The Relay App catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Relay App''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Relay App Plans Pricing
  plan_count: 3
  slug: relay-app-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Relay App Rate Limits
  slug: relay-app-rate-limits
rules:
- name: Relay App API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: relay-app-jsonschema-spectral-rules
- name: Relay App API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 7
  slug: relay-app-rules
score:
  band: developing
  composite: 51.3
  delta: -4.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 77.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- Workflow
- Integration
- No-Code
- AI
- Webhooks
website: https://www.relay.app
---
