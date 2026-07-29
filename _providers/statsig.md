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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
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
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 43
  human_in_the_loop: 5
  name: Statsig Agentic Access
  operation_count: 66
  slug: statsig-agentic-access
  summary_line: 66 operations · 43 acting · 5 human-in-the-loop
api_count: 18
apis:
- description: The Statsig Events API handles the ingestion of event data from both client and server SDKs. It receives exposure events, custom events, and diagnostic data at the events.statsigapi.net endpoint. This
  name: Statsig Events API
  slug: events-api
- description: Access audit log entries tracking changes made to project configuration through the console or API.
  name: statsig Audit Logs API
  slug: statsig-audit-logs-api
- description: Manage autotune configurations that automatically optimize parameter values based on a target metric.
  name: statsig Autotunes API
  slug: statsig-autotunes-api
- description: Endpoints for downloading full project configuration specs for server-side local evaluation.
  name: statsig Configuration API
  slug: statsig-configuration-api
- description: Manage dynamic configurations with full CRUD operations for server-driven configuration values.
  name: statsig Dynamic Configs API
  slug: statsig-dynamic-configs-api
- description: Manage A/B test experiments including creation, configuration, starting, resetting, and analysis.
  name: statsig Experiments API
  slug: statsig-experiments-api
- description: Endpoints for evaluating feature gates for users, returning boolean pass/fail values along with rule identification.
  name: statsig Feature Gates API
  slug: statsig-feature-gates-api
- description: Manage feature gates including creation, updates, rules, overrides, enabling, disabling, launching, and archiving.
  name: statsig Gates API
  slug: statsig-gates-api
- description: Manage holdout groups that exclude users from receiving specific features for measuring long-term impact.
  name: statsig Holdouts API
  slug: statsig-holdouts-api
- description: Endpoints for initializing client SDKs with all evaluated feature gates, configs, experiments, and layers for a given user.
  name: statsig Initialization API
  slug: statsig-initialization-api
- description: Manage API keys for the project including server secret keys, client SDK keys, and console API keys.
  name: statsig Keys API
  slug: statsig-keys-api
- description: Manage layers that enable sharing parameters across multiple experiments while maintaining mutual exclusivity.
  name: statsig Layers API
  slug: statsig-layers-api
- description: Access and manage metric definitions and metric sources used in experiment analysis.
  name: statsig Metrics API
  slug: statsig-metrics-api
- description: Manage user segments for targeting rules across gates, configs, and experiments.
  name: statsig Segments API
  slug: statsig-segments-api
- description: The Tags API from statsig — 1 operation(s) for tags.
  name: statsig Tags API
  slug: statsig-tags-api
- description: Manage target application definitions that scope feature configurations to specific applications.
  name: statsig Target Apps API
  slug: statsig-target-apps-api
- description: Manage user data and lookup user properties within the Statsig project.
  name: statsig Users API
  slug: statsig-users-api
- description: Endpoint for receiving event data from third-party applications via webhook integration.
  name: statsig Webhooks API
  slug: statsig-webhooks-api
artifact_total: 46
asyncapis:
- description: 'Statsig''s webhook system provides real-time event-driven notifications for exposure events and configuration changes. Webhooks are triggered at runtime as users are assigned to gates and experiments, '
  name: Statsig Webhook Events
  slug: statsig-webhooks-asyncapi
collections:
- collection_type: open
  name: Statsig Client SDK API
  slug: open-statsig-client-sdk-api
- collection_type: open
  name: Statsig Console API
  slug: open-statsig-console-api
- collection_type: open
  name: Statsig Events API
  slug: open-statsig-events-api
- collection_type: open
  name: Statsig HTTP API
  slug: open-statsig-http-api
- collection_type: open
  name: Statsig Server SDK API
  slug: open-statsig-server-sdk-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/statsig-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/statsig-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/statsig-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/statsig-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/statsig-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/statsig
- group: design
  title: ''
  type: JSONLD
  url: json-ld/statsig-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/statsig-feature-gate-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/statsig-experiment-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/statsig-event-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/statsig-feature-gate-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/statsig-experiment-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/statsig-event-structure.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/statsig-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/statsig-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.statsig.com/llms.txt
description: Statsig is a feature management and experimentation platform that helps product teams ship features safely with feature flags, run A/B tests, and measure the impact of every feature on key metrics.
examples:
- key_count: 2
  name: Statsig Check Gate Example
  slug: statsig-check-gate-example
- key_count: 2
  name: Statsig Create Experiment Example
  slug: statsig-create-experiment-example
- key_count: 2
  name: Statsig Create Gate Example
  slug: statsig-create-gate-example
- key_count: 2
  name: Statsig List Gates Example
  slug: statsig-list-gates-example
- key_count: 2
  name: Statsig Log Events Example
  slug: statsig-log-events-example
finops:
- name: Statsig Finops
  service_category: Feature Flags & Experimentation
  slug: statsig-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/statsig.png
json_schemas:
- name: Statsig Event
  property_count: 7
  slug: statsig-event
- name: Statsig Experiment
  property_count: 17
  slug: statsig-experiment
- name: Statsig Feature Gate
  property_count: 12
  slug: statsig-feature-gate
json_structures:
- name: Statsig Event Structure
  property_count: 0
  slug: statsig-event-structure
- name: Statsig Experiment Structure
  property_count: 0
  slug: statsig-experiment-structure
- name: Statsig Feature Gate Structure
  property_count: 0
  slug: statsig-feature-gate-structure
jsonld:
- class_count: 0
  name: Statsig Context
  property_count: 13
  slug: statsig-context
layout: provider
modified: '2026-05-19'
name: statsig
nav: Providers
network: true
overview: 'statsig publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Events API, Audit Logs API, Autotunes API, and 15 more.


  The statsig catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  statsig''s developer surface includes authentication and 15 more developer resources.'
plans:
- name: Statsig Plans Pricing
  plan_count: 3
  slug: statsig-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 3
  name: Statsig Rate Limits
  slug: statsig-rate-limits
rules:
- name: statsig API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: statsig-asyncapi-spectral-rules
- name: statsig API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: statsig-jsonschema-spectral-rules
- name: statsig API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 3
    info: 0
    warn: 5
  slug: statsig-rules
score:
  band: developing
  composite: 48.0
  delta: -3.4
  facets:
    commercial_clarity: 47.4
    contract_quality: 78.4
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/screenshots/statsig-2026-06-20T194528.png
security:
- kind: authentication
  name: Statsig Authentication
  slug: statsig-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Statsig Domain Security
  slug: statsig-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Statsig Trust Center
  slug: statsig-trust-center
  summary_line: trust center published
slug: statsig
---
