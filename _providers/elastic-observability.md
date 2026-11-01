---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Elastic Observability Agentic Access
  operation_count: 14
  slug: elastic-observability-agentic-access
  summary_line: 14 operations · 9 acting
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
artifact_total: 24
collections:
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
- group: other
  href: https://artifacts.apis.io/elastic-observability/capabilities/elastic-observability-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/elastic-observability-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/elastic-observability/agentic-access/elastic-observability-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/elastic-observability-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/elastic-observability/security/elastic-observability-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/elastic-observability-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/elastic-observability/security/elastic-observability-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elastic-observability-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/elastic-observability/authentication/elastic-observability-authentication.yml
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
  href: https://artifacts.apis.io/elastic-observability/packages/elastic-observability-packages.yml
  title: ''
  type: Packages
  url: packages/elastic-observability-packages.yml
- group: build
  href: https://artifacts.apis.io/elastic-observability/packages/elastic-observability-packages.yml
  title: ''
  type: SDKs
  url: packages/elastic-observability-packages.yml
- group: agent
  href: https://artifacts.apis.io/elastic-observability/well-known/elastic-observability-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elastic-observability-well-known.yml
- group: auth
  href: https://artifacts.apis.io/elastic-observability/well-known/elastic-observability-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/elastic-observability-security.txt
- group: agent
  href: https://artifacts.apis.io/elastic-observability/mcp/elastic-observability-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/elastic-observability-mcp.yml
- group: build
  href: https://artifacts.apis.io/elastic-observability/mcp/elastic-observability-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/elastic-observability-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/elastic-observability/llms/elastic-observability-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elastic-observability-llms.txt
- group: design
  href: https://artifacts.apis.io/elastic-observability/conformance/elastic-observability-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elastic-observability-conformance.yml
- group: auth
  href: https://artifacts.apis.io/elastic-observability/conformance/elastic-observability-conformance.yml
  title: ''
  type: Compliance
  url: conformance/elastic-observability-conformance.yml
- group: design
  href: https://artifacts.apis.io/elastic-observability/errors/elastic-observability-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/elastic-observability-problem-types.yml
- group: design
  href: https://artifacts.apis.io/elastic-observability/lifecycle/elastic-observability-lifecycle.yml
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
  href: https://artifacts.apis.io/elastic-observability/conventions/elastic-observability-conventions.yml
  title: ''
  type: Conventions
  url: conventions/elastic-observability-conventions.yml
- group: operate
  href: https://artifacts.apis.io/elastic-observability/changelog/elastic-observability-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/elastic-observability-changelog.yml
- group: build
  href: https://artifacts.apis.io/elastic-observability/cli/elastic-observability-cli.yml
  title: ''
  type: CLI
  url: cli/elastic-observability-cli.yml
- group: design
  href: https://artifacts.apis.io/elastic-observability/data-model/elastic-observability-data-model.yml
  title: ''
  type: DataModel
  url: data-model/elastic-observability-data-model.yml
- group: start
  href: https://artifacts.apis.io/elastic-observability/sandbox/elastic-observability-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/elastic-observability-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/elastic-observability/security/elastic-observability-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/elastic-observability-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.elastic.co/product-security
- group: agent
  href: https://artifacts.apis.io/elastic-observability/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/elastic-observability/plans/elastic-observability-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elastic-observability-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/elastic-observability/rate-limits/elastic-observability-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elastic-observability-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/elastic-observability/finops/elastic-observability-finops.yml
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
- has_sources: true
  method: derived
  name: Elastic Observability Finops
  primary_unit: gb ingested
  service_category: ''
  slug: elastic-observability-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elastic-observability.png
layout: provider
mcp_servers:
- description: Remote MCP server at {KIBANA_URL} requiring an API key.
  name: Elastic Agent Builder MCP Server
  slug: elastic-agent-builder-mcp-server
modified: '2026-08-29'
name: Elastic Observability
nav: Providers
network: true
overview: 'Elastic Observability publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Server Info API, agent config API, event intake API, and 2 more. Tagged areas include AIOps, Observability, APM, Logging, and Metrics.


  Elastic Observability''s developer surface includes authentication, documentation, changelog, CLI, sandbox, API reference, getting-started guide, and 35 more developer resources.'
plans:
- name: Elastic Observability Plans Pricing
  plan_count: 17
  slug: elastic-observability-plans-pricing
- name: Elastic Observability Price Estimates
  plan_count: 0
  slug: elastic-observability-price-estimates
random_paper: 9
rate_limits:
- limit_count: 0
  name: Elastic Observability Rate Limits
  slug: elastic-observability-rate-limits
score:
  band: strong
  composite: 65.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.7
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 43.4
    developer_ergonomics: 80.4
    discoverability: 56.7
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 61.3
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/elastic-observability/elastic-observability-2026-06-20T180529.png
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
skill_count: 4
skills:
- name: elastic-observability-check-server-health
  slug: elastic-observability-check-server-health
- name: elastic-observability-export-otlp-telemetry
  slug: elastic-observability-export-otlp-telemetry
- name: elastic-observability-fetch-agent-config
  slug: elastic-observability-fetch-agent-config
- name: elastic-observability-send-apm-events
  slug: elastic-observability-send-apm-events
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
