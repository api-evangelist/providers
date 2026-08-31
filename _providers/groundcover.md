---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The groundcover platform REST API. Data query endpoints run gcQL pipelines against logs (POST /api/logs/v2/search), trace spans (POST /api/traces/v2/search) and Kubernetes events (POST /api/k8s/v2/eve
  name: Groundcover
  slug: groundcover
artifact_total: 10
asyncapis:
- description: ''
  name: Groundcover Webhooks
  slug: groundcover-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/groundcover-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/groundcover-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/groundcover-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/groundcover-com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/groundcover-com
- group: company
  title: ''
  type: Website
  url: https://www.groundcover.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.groundcover.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.groundcover.com/use-groundcover/remote-access-and-apis/api-examples
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.groundcover.com/getting-started/5-quick-steps-to-get-you-started
- group: operate
  title: ''
  type: Support
  url: https://www.groundcover.com/support-plans
- group: commercial
  title: ''
  type: Pricing
  url: https://www.groundcover.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/groundcover-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.groundcover.com/start
- group: start
  title: ''
  type: Login
  url: https://app.groundcover.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.groundcover.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.groundcover.com/privacy-policy
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.groundcover.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/groundcover-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.groundcover.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/groundcover-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/groundcover-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/groundcover-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/groundcover-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/groundcover-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/groundcover-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/groundcover-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/groundcover-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/groundcover-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/groundcover-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/groundcover-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/groundcover-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/groundcover-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/groundcover-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/groundcover-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/groundcover-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/groundcover-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/groundcover-rate-limits.yml
created: '2026-03-27'
description: groundcover is a cloud-native observability platform that uses eBPF for zero-instrumentation monitoring of Kubernetes and Linux workloads, covering logs, metrics, traces, Kubernetes events, real user monitoring, synthetics and AI/LLM observability. Its BYOC (bring your own cloud) architecture keeps the data plane inside the customer's own VPC, which lets it price per monitored host rather than per ingested byte. Programmatic access is delivered through a REST API at api.groundcover.com (gcQL search endpoints for logs, traces and Kubernetes events, a Prometheus-compatible metrics API, and management endpoints for monitors, silences, ingestion keys and pipelines), a remote MCP server at mcp.groundcover.com for agents, official Go, Python and TypeScript SDKs, a CLI, and Terraform, Pulumi and Crossplane providers.
finops:
- name: Groundcover Finops
  service_category: API
  slug: groundcover-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groundcover.png
layout: provider
mcp_servers:
- description: groundcover publishes a first-party hosted (remote) MCP server that brings live observability data — logs, traces, Kubernetes events, live entity state, monitor issues, monitor definitions and metrics
  name: groundcover MCP Server
  slug: groundcover-mcp-server
modified: '2026-08-29'
name: Groundcover
nav: Providers
network: true
overview: 'Groundcover publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AIOps, Observability, Kubernetes, eBPF, and Monitoring.


  The Groundcover catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Groundcover''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, engineering blog, and 30 more developer resources.'
plans:
- name: Groundcover Plans Pricing
  plan_count: 4
  slug: groundcover-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Groundcover Rate Limits
  slug: groundcover-rate-limits
scopes:
- name: Groundcover Scopes
  scope_count: 0
  slug: groundcover-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 54.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/groundcover/refs/heads/main/screenshots/groundcover-2026-06-20T182415.png
security:
- kind: authentication
  name: Groundcover Authentication
  slug: groundcover-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Groundcover Domain Security
  slug: groundcover-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Groundcover Trust Center
  slug: groundcover-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: groundcover
tags:
- AIOps
- Observability
- Kubernetes
- eBPF
- Monitoring
- Logs
- Traces
- Metrics
- OpenTelemetry
- MCP
website: https://www.groundcover.com
---
