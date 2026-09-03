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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 43
  human_in_the_loop: 5
  name: Statsig Agentic Access
  operation_count: 66
  slug: statsig-agentic-access
  summary_line: 66 operations · 43 acting · 5 human-in-the-loop
api_count: 4
apis:
- baseURL: https://events.statsigapi.net
  baseurl_source: declared
  description: The Statsig Events API handles the ingestion of event data from both client and server SDKs. It receives exposure events, custom events, and diagnostic data at the events.statsigapi.net endpoint. This
  name: Statsig Events API
  slug: events-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Access audit log entries tracking changes made to project configuration through the console or API.
  name: statsig Audit Logs API
  slug: statsig-audit-logs-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Manage autotune configurations that automatically optimize parameter values based on a target metric.
  name: statsig Autotunes API
  slug: statsig-autotunes-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Endpoints for downloading full project configuration specs for server-side local evaluation.
  name: statsig Configuration API
  slug: statsig-configuration-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Manage dynamic configurations with full CRUD operations for server-driven configuration values.
  name: statsig Dynamic Configs API
  slug: statsig-dynamic-configs-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Manage A/B test experiments including creation, configuration, starting, resetting, and analysis.
  name: statsig Experiments API
  slug: statsig-experiments-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Endpoints for evaluating feature gates for users, returning boolean pass/fail values along with rule identification.
  name: statsig Feature Gates API
  slug: statsig-feature-gates-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Manage feature gates including creation, updates, rules, overrides, enabling, disabling, launching, and archiving.
  name: statsig Gates API
  slug: statsig-gates-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Manage holdout groups that exclude users from receiving specific features for measuring long-term impact.
  name: statsig Holdouts API
  slug: statsig-holdouts-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Endpoints for initializing client SDKs with all evaluated feature gates, configs, experiments, and layers for a given user.
  name: statsig Initialization API
  slug: statsig-initialization-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Manage API keys for the project including server secret keys, client SDK keys, and console API keys.
  name: statsig Keys API
  slug: statsig-keys-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Manage layers that enable sharing parameters across multiple experiments while maintaining mutual exclusivity.
  name: statsig Layers API
  slug: statsig-layers-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Access and manage metric definitions and metric sources used in experiment analysis.
  name: statsig Metrics API
  slug: statsig-metrics-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Manage user segments for targeting rules across gates, configs, and experiments.
  name: statsig Segments API
  slug: statsig-segments-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: The Tags API from statsig — 1 operation(s) for tags.
  name: statsig Tags API
  slug: statsig-tags-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Manage target application definitions that scope feature configurations to specific applications.
  name: statsig Target Apps API
  slug: statsig-target-apps-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Manage user data and lookup user properties within the Statsig project.
  name: statsig Users API
  slug: statsig-users-api
artifact_total: 63
asyncapis:
- description: 'Statsig''s webhook system provides real-time event-driven notifications for exposure events and configuration changes. Webhooks are triggered at runtime as users are assigned to gates and experiments, '
  name: Statsig Webhook Events
  slug: statsig-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Statsig Client SDK Audit Logs API
  slug: open-statsig-audit-logs-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Autotunes API
  slug: open-statsig-autotunes-api
- collection_type: open
  name: Statsig Client SDK API
  slug: open-statsig-client-sdk-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Configuration API
  slug: open-statsig-configuration-api
- collection_type: open
  name: Statsig Console API
  slug: open-statsig-console-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Dynamic Configs API
  slug: open-statsig-dynamic-configs-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Events API
  slug: open-statsig-events-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Experiments API
  slug: open-statsig-experiments-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Feature Gates API
  slug: open-statsig-feature-gates-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Gates API
  slug: open-statsig-gates-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Holdouts API
  slug: open-statsig-holdouts-api
- collection_type: open
  name: Statsig HTTP API
  slug: open-statsig-http-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Initialization API
  slug: open-statsig-initialization-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Keys API
  slug: open-statsig-keys-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Layers API
  slug: open-statsig-layers-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Metrics API
  slug: open-statsig-metrics-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Segments API
  slug: open-statsig-segments-api
- collection_type: open
  name: Statsig Server SDK API
  slug: open-statsig-server-sdk-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Tags API
  slug: open-statsig-tags-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Target Apps API
  slug: open-statsig-target-apps-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Users API
  slug: open-statsig-users-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Webhooks API
  slug: open-statsig-webhooks-api
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
name: Statsig
nav: Providers
network: true
overview: 'Statsig publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Events API, Audit Logs API, Autotunes API, and 14 more.


  The Statsig catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Statsig''s developer surface includes authentication and 15 more developer resources.'
plans:
- name: Statsig Plans Pricing
  plan_count: 3
  slug: statsig-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Statsig Rate Limits
  slug: statsig-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Statsig API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: statsig-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Statsig API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: statsig-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Statsig API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 3
    info: 0
    warn: 5
  slug: statsig-rules
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 61.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 28.8
    contract_quality: 72.6
    developer_ergonomics: 21.4
    discoverability: 57.4
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  regulatory:
    applies: false
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
