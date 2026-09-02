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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Pixie Agentic Access
  operation_count: 4
  slug: pixie-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: Python-dialect domain-specific language and API for querying and analyzing telemetry data collected by Pixie within a Kubernetes cluster. PxL scripts allow developers to filter, aggregate, and visuali
  name: Pixie PxL Script API
  slug: pixie-pxl-api
- description: Plugin API that allows configuring PxL scripts to export observability data from Pixie at regularly scheduled intervals to external systems. Supports integrations including a Grafana datasource plugin
  name: Pixie Plugin System API
  slug: pixie-plugin-api
- description: Operations for listing and inspecting Pixie-instrumented Kubernetes clusters connected to the Pixie Cloud.
  name: Pixie Clusters API
  slug: pixie-clusters-api
- description: Health and status endpoints for the Pixie service.
  name: Pixie Health API
  slug: pixie-health-api
- description: Operations for executing PxL scripts against a cluster and retrieving telemetry query results.
  name: Pixie Scripts API
  slug: pixie-scripts-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pixie Clusters API
  slug: open-pixie-clusters-api
- collection_type: open
  name: Pixie Clusters Health API
  slug: open-pixie-health-api
- collection_type: open
  name: Pixie Clusters Scripts API
  slug: open-pixie-scripts-api
- collection_type: open
  name: Pixie API
  slug: open-pixie
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/pixie-io/pixie/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/pixie-io/pixie/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/pixie-io/pixie/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/pixie-io/pixie/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/pixie-io/pixie/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/pixie-io/pixie/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pixie-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pixie-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pixie-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pixieai
- group: company
  title: ''
  type: Website
  url: https://px.dev/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/pixie-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/pixie-pxl-script-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/pixie-plugin-schema.json
- group: docs
  title: ''
  type: Documentation
  url: https://docs.px.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.px.dev/installing-pixie/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pixie-io
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/pixie-io/pixie
- group: company
  title: ''
  type: Blog
  url: https://blog.px.dev/
- group: operate
  title: ''
  type: Community
  url: https://px.dev/community/
- group: operate
  title: ''
  type: Slack
  url: https://slackin.px.dev/
created: '2026-03-16'
description: Pixie is a Kubernetes observability platform that uses eBPF to automatically collect telemetry data including full-body application requests, resource and network metrics, and application profiles without manual instrumentation.
finops:
- name: Pixie Finops
  service_category: Observability
  slug: pixie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pixie.png
json_schemas:
- name: Pixie Plugin Configuration
  property_count: 7
  slug: pixie-plugin
- name: Pixie PxL Script
  property_count: 10
  slug: pixie-pxl-script
jsonld:
- class_count: 0
  name: Pixie Context
  property_count: 7
  slug: pixie-context
layout: provider
modified: '2026-05-19'
name: Pixie
nav: Providers
network: true
overview: 'Pixie publishes 3 APIs on the [APIs.io](https://apis.io/) network: Clusters API, Health API, and Scripts API. Tagged areas include eBPF, Kubernetes, Monitoring, and Observability.


  The Pixie catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pixie''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 17 more developer resources.'
plans:
- name: Pixie Plans Pricing
  plan_count: 1
  slug: pixie-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Pixie Rate Limits
  slug: pixie-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Pixie API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: pixie-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 13
    catalog_gap: 66.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 64.4
    developer_ergonomics: 47.6
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 100.0
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pixie/refs/heads/main/screenshots/pixie-2026-06-20T191740.png
security:
- kind: authentication
  name: Pixie Authentication
  slug: pixie-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pixie Domain Security
  slug: pixie-domain-security
  summary_line: TLSv1.3 · HSTS
slug: pixie
tags:
- eBPF
- Kubernetes
- Monitoring
- Observability
website: https://px.dev/
---
