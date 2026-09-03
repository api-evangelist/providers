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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Elastic Observability Agentic Access
  operation_count: 14
  slug: elastic-observability-agentic-access
  summary_line: 14 operations · 11 acting
api_count: 1
apis:
- description: 'The Elastic Observability product surface: logs, metrics, APM traces, synthetics, RUM, universal profiling and SLOs on the Elastic Stack. The callable contracts are the four APM Server intake APIs lis'
  name: Elastic Observability
  slug: elastic-observability
- baseURL: https://{deployment}.apm.{region}.cloud.es.io:443
  baseurl_source: declared
  description: The Server Info API from Elastic Observability — 1 operation(s) for server info.
  name: Elastic Observability Server Info API
  slug: elastic-observability-server-info-api
- baseURL: https://{deployment}.apm.{region}.cloud.es.io:443
  baseurl_source: declared
  description: APIs that query the APM Server for configuration changes.
  name: Elastic Observability agent config API
  slug: elastic-observability-agent-config-api
- baseURL: https://{deployment}.apm.{region}.cloud.es.io:443
  baseurl_source: declared
  description: The events intake API is the internal protocol that APM agents use to talk to the APM Server.
  name: Elastic Observability event intake API
  slug: elastic-observability-event-intake-api
- baseURL: https://{deployment}.apm.{region}.cloud.es.io:443
  baseurl_source: declared
  description: The OpenTelemetry intake API uses the OpenTelemetry Protocol (OTLP) to send traces, metrics, and logs to APM Server. OTLP is the default transfer protocol for OpenTelemetry and is supported natively b
  name: Elastic Observability opentelemetry intake API
  slug: elastic-observability-opentelemetry-intake-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Elastic Observability (APM Server) Agent Configuration API
  slug: open-elastic-observability-agent-configuration-api
- collection_type: open
  name: Elastic Observability (APM Server) Agent Configuration Intake API
  slug: open-elastic-observability-intake-api
- collection_type: open
  name: Elastic Observability (APM Server) Agent Configuration OpenTelemetry API
  slug: open-elastic-observability-opentelemetry-api
- collection_type: open
  name: Elastic Observability (APM Server) Agent Configuration Server Info API
  slug: open-elastic-observability-server-info-api
- collection_type: open
  name: Elastic Observability (APM Server) API
  slug: open-elastic-observability
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elastic-observability-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/elastic-observability-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elastic-observability-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elastic-observability-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.elastic.co/observability
- group: docs
  title: ''
  type: Documentation
  url: https://www.elastic.co/docs/solutions/observability
- group: build
  title: ''
  type: Packages
  url: packages/elastic-observability-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/elastic-observability-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/elastic-observability-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/elastic-observability-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/elastic-observability-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/elastic-observability-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elastic-observability-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/elastic-observability-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/elastic-observability-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/elastic-observability-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/elastic-observability-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elastic.co
- group: operate
  title: ''
  type: Deprecation
  url: https://www.elastic.co/support/eol
- group: design
  title: ''
  type: Conventions
  url: conventions/elastic-observability-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/elastic-observability-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/elastic-observability-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/elastic-observability-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/elastic-observability-sandbox.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/elastic-observability-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.elastic.co/product-security
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/elastic-observability-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elastic-observability-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/elastic-observability-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.elastic.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.elastic.co/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.elastic.co/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.elastic.co/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://discuss.elastic.co
- group: company
  title: ''
  type: Blog
  url: https://www.elastic.co/observability-labs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elastic
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elastic.co/pricing/serverless-observability
- group: start
  title: ''
  type: SignUp
  url: https://cloud.elastic.co/registration
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elastic.co/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elastic.co/legal/privacy-statement
created: '2026-03-27'
description: 'Elastic Observability is Elastic''s unified logs, metrics, traces and profiling solution, built on the Elastic Stack. Its published machine-readable contract is the Observability Intake API served by APM Server: a newline-delimited JSON event intake for Elastic APM agents, a central agent-configuration endpoint, and native OpenTelemetry Protocol ingest over both OTLP/HTTP and OTLP/gRPC. Analysis of the telemetry once it has landed happens through Kibana and, for agents, through the Elastic Agent Builder MCP server, which exposes sixteen observability.* tools over a deployment-scoped endpoint.'
finops:
- name: Elastic Observability Finops
  service_category: API
  slug: elastic-observability-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elastic-observability.png
layout: provider
mcp_servers:
- description: ''
  name: Elastic Agent Builder MCP Server
  slug: elastic-agent-builder-mcp-server
modified: '2026-08-29'
name: Elastic Observability
nav: Providers
network: true
overview: 'Elastic Observability publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Server Info API, agent config API, event intake API, and 1 more. Tagged areas include AIOps, Observability, APM, Logging, and Metrics.


  Elastic Observability''s developer surface includes authentication, documentation, changelog, CLI, sandbox, API reference, getting-started guide, and 34 more developer resources.'
plans:
- name: Elastic Observability Plans Pricing
  plan_count: 2
  slug: elastic-observability-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Elastic Observability Rate Limits
  slug: elastic-observability-rate-limits
score:
  band: strong
  composite: 59.1
  coverage:
    artifact_dirs: 25
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 48.2
    developer_ergonomics: 80.4
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elastic-observability/refs/heads/main/screenshots/elastic-observability-2026-06-20T180529.png
security:
- kind: authentication
  name: Elastic Observability Authentication
  slug: elastic-observability-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Elastic Observability Domain Security
  slug: elastic-observability-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Elastic Observability Vulnerability Disclosure
  slug: elastic-observability-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Elastic Observability Trust Center
  slug: elastic-observability-trust-center
  summary_line: FedRAMP High, FedRAMP Moderate, PCI DSS (Level 1 Service Provider), CSA STAR, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, SOC 2, SOC 3, TISAX, HIPAA, Cyber Essentials Plus, IRAP Assessed — Protected B, CyberGRX, GDPR
slug: elastic-observability
tags:
- AIOps
- Observability
- APM
- Logging
- Metrics
- Tracing
- OpenTelemetry
- Monitoring
- Telemetry
website: https://www.elastic.co/observability
---
