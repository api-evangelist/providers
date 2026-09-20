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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.4
  scored_at: '2026-09-19'
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
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Access audit log entries tracking changes made to project configuration through the console or API.
  name: statsig Audit Logs API
  slug: statsig-audit-logs-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage autotune configurations that automatically optimize parameter values based on a target metric.
  name: statsig Autotunes API
  slug: statsig-autotunes-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Endpoints for downloading full project configuration specs for server-side local evaluation.
  name: statsig Configuration API
  slug: statsig-configuration-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage dynamic configurations with full CRUD operations for server-driven configuration values.
  name: statsig Dynamic Configs API
  slug: statsig-dynamic-configs-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage A/B test experiments including creation, configuration, starting, resetting, and analysis.
  name: statsig Experiments API
  slug: statsig-experiments-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Endpoints for evaluating feature gates for users, returning boolean pass/fail values along with rule identification.
  name: statsig Feature Gates API
  slug: statsig-feature-gates-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage feature gates including creation, updates, rules, overrides, enabling, disabling, launching, and archiving.
  name: statsig Gates API
  slug: statsig-gates-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage holdout groups that exclude users from receiving specific features for measuring long-term impact.
  name: statsig Holdouts API
  slug: statsig-holdouts-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Endpoints for initializing client SDKs with all evaluated feature gates, configs, experiments, and layers for a given user.
  name: statsig Initialization API
  slug: statsig-initialization-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage API keys for the project including server secret keys, client SDK keys, and console API keys.
  name: statsig Keys API
  slug: statsig-keys-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage layers that enable sharing parameters across multiple experiments while maintaining mutual exclusivity.
  name: statsig Layers API
  slug: statsig-layers-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Access and manage metric definitions and metric sources used in experiment analysis.
  name: statsig Metrics API
  slug: statsig-metrics-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage user segments for targeting rules across gates, configs, and experiments.
  name: statsig Segments API
  slug: statsig-segments-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Tags API from statsig — 1 operation(s) for tags.
  name: statsig Tags API
  slug: statsig-tags-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage target application definitions that scope feature configurations to specific applications.
  name: statsig Target Apps API
  slug: statsig-target-apps-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage user data and lookup user properties within the Statsig project.
  name: statsig Users API
  slug: statsig-users-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: 'The Statsig Console API is the provider''s own published contract — the CRUD API for everything available in console.statsig.com without the web UI. Statsig maintains an OpenAPI 3.0 document for it at '
  name: statsig Console API
  slug: statsig-console-api
artifact_total: 69
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
- group: company
  title: ''
  type: Website
  url: https://www.statsig.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/agentic-access/statsig-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/statsig-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/security/statsig-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/statsig-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/security/statsig-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/statsig-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/authentication/statsig-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/json-ld/statsig-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/statsig-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/json-schema/statsig-feature-gate-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/statsig-feature-gate-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/json-schema/statsig-experiment-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/statsig-experiment-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/json-schema/statsig-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/statsig-event-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/json-structure/statsig-feature-gate-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/statsig-feature-gate-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/json-structure/statsig-experiment-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/statsig-experiment-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/json-structure/statsig-event-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/statsig-event-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/rules/statsig-rules.yml
  title: ''
  type: SpectralRules
  url: rules/statsig-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/vocabulary/statsig-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/statsig-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.statsig.com/llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/packages/statsig-packages.yml
  title: ''
  type: Packages
  url: packages/statsig-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/packages/statsig-packages.yml
  title: ''
  type: SDKs
  url: packages/statsig-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/mcp/statsig-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/statsig-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/mcp/statsig-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/statsig-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/grpc/statsig-forward-proxy.proto
  title: ''
  type: Protobuf
  url: grpc/statsig-forward-proxy.proto
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/well-known/statsig-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/statsig-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/conformance/statsig-conformance.yml
  title: ''
  type: Conformance
  url: conformance/statsig-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/security/statsig-trust-center.yml
  title: ''
  type: Compliance
  url: security/statsig-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/security/statsig-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/statsig-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.statsig.com/legal/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/conventions/statsig-conventions.yml
  title: ''
  type: Conventions
  url: conventions/statsig-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/errors/statsig-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/statsig-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/data-model/statsig-data-model.yml
  title: ''
  type: DataModel
  url: data-model/statsig-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/lifecycle/statsig-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/statsig-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.statsig.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/changelog/statsig-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/statsig-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/cli/statsig-cli.yml
  title: ''
  type: CLI
  url: cli/statsig-cli.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/plans/statsig-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/statsig-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/rate-limits/statsig-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/statsig-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/finops/statsig-finops.yml
  title: ''
  type: FinOps
  url: finops/statsig-finops.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/examples/statsig-check-gate-example.json
  title: ''
  type: Examples
  url: examples/statsig-check-gate-example.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/asyncapi/statsig-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/statsig-webhooks-asyncapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/asyncapi/statsig-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/statsig-webhooks-asyncapi.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/llms/statsig-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/statsig-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.statsig.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.statsig.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.statsig.com/console-api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.statsig.com/sdks/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.statsig.com/contact
- group: operate
  title: ''
  type: Community
  url: https://www.statsig.com/slack
- group: company
  title: ''
  type: Blog
  url: https://www.statsig.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.statsig.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.statsig.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.statsig.com/terms
- group: operate
  title: ''
  type: FAQ
  url: https://docs.statsig.com/faq
created: '2026-05-04'
description: 'Statsig is a product development platform that combines feature management, experimentation and analytics in one system. Teams gate releases behind feature flags, run A/B, A/B/n, switchback, holdout and multi-armed-bandit experiments, and read the impact of every change against their own metrics — in Statsig Cloud, which ingests and stores the event data, or Warehouse Native, which runs the same analysis directly against the customer''s Snowflake, BigQuery, Databricks or Athena warehouse without moving user-level data out of it. Around that core it ships product analytics, web analytics, session replay, infra analytics, dynamic configs, parameter stores and 30+ SDKs. Its programmable surface is unusually complete: a first-party OpenAPI covering 324 Console API operations, a low-latency HTTP evaluation API, gRPC protobufs for the self-hosted Forward Proxy, an authenticated remote MCP server with OAuth, a public documentation MCP server, published Agent Skills, a Terraform provider
  and a CLI. Statsig is based in Bellevue, Washington.'
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
mcp_servers:
- description: Statsig ships TWO distinct remote MCP servers. The authenticated Statsig MCP server at https://api.statsig.com/v1/mcp exposes the Console API surface — gates, experiments, dynamic configs, segments, l
  name: Statsig MCP
  slug: statsig-mcp
modified: '2026-09-17'
name: Statsig
nav: Providers
network: true
overview: 'Statsig publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Events API, Audit Logs API, Autotunes API, and 15 more. Tagged areas include Feature Flags, Experimentation, A/B Testing, Product Analytics, and Session Replay.


  The Statsig catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Statsig''s developer surface includes authentication, changelog, CLI, code examples, documentation, API reference, getting-started guide, and 46 more developer resources.'
plans:
- name: Statsig Plans Pricing
  plan_count: 3
  slug: statsig-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
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
  band: exemplar
  composite: 76.9
  coverage:
    artifact_dirs: 33
    catalog_earned: 84.5
    catalog_earned_first_party: 24.0
    catalog_gap: 30.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 76.3
    contract_governance: 47.0
    contract_quality: 76.4
    developer_ergonomics: 78.6
    discoverability: 81.5
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 79.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: true
    score: 27.8
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
- kind: vulnerability-disclosure
  name: Statsig Vulnerability Disclosure
  slug: statsig-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Statsig Trust Center
  slug: statsig-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR, HIPAA
skill_count: 3
skills:
- name: statsig-create-cloud-metric
  slug: statsig-create-cloud-metric
- name: statsig-dashboard
  slug: statsig-dashboard
- name: statsig
  slug: statsig
slug: statsig
tags:
- Feature Flags
- Experimentation
- A/B Testing
- Product Analytics
- Session Replay
- Developer Tools
- Data Warehouse
- Configuration Management
website: https://www.statsig.com/
---
