---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Vividcortex Agentic Access
  operation_count: 20
  slug: vividcortex-agentic-access
  summary_line: 20 operations · 7 acting
api_count: 1
apis:
- baseURL: https://app.vividcortex.com/api/v2
  baseurl_source: declared
  description: Alert configuration, destinations, and integrations.
  name: VividCortex Alerts API
  slug: vividcortex-alerts-api
- baseURL: https://app.vividcortex.com/api/v2
  baseurl_source: declared
  description: Events and annotations on the DPM timeline.
  name: VividCortex Events API
  slug: vividcortex-events-api
- baseURL: https://app.vividcortex.com/api/v2
  baseurl_source: declared
  description: Managing the database and OS hosts monitored by DPM agents.
  name: VividCortex Hosts API
  slug: vividcortex-hosts-api
- baseURL: https://app.vividcortex.com/api/v2
  baseurl_source: declared
  description: Active metric discovery and time-series data.
  name: VividCortex Metrics API
  slug: vividcortex-metrics-api
- baseURL: https://app.vividcortex.com/api/v2
  baseurl_source: declared
  description: Observed queries, query digests, and query samples.
  name: VividCortex Queries API
  slug: vividcortex-queries-api
artifact_total: 22
asyncapis:
- description: ''
  name: Vividcortex Alerts Webhooks
  slug: vividcortex-alerts-webhooks
collections:
- collection_type: postman
  name: VividCortex (SolarWinds Database Performance Monitor) Alerts API
  slug: postman-vividcortex-alerts-api
- collection_type: postman
  name: VividCortex (SolarWinds Database Performance Monitor) Alerts Events API
  slug: postman-vividcortex-events-api
- collection_type: postman
  name: VividCortex (SolarWinds Database Performance Monitor) Alerts Hosts API
  slug: postman-vividcortex-hosts-api
- collection_type: postman
  name: VividCortex (SolarWinds Database Performance Monitor) Alerts Metrics API
  slug: postman-vividcortex-metrics-api
- collection_type: postman
  name: VividCortex (SolarWinds Database Performance Monitor) Alerts Queries API
  slug: postman-vividcortex-queries-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VividCortex (SolarWinds Database Performance Monitor) Alerts API
  slug: open-vividcortex-alerts-api
- collection_type: open
  name: VividCortex (SolarWinds Database Performance Monitor) Alerts Events API
  slug: open-vividcortex-events-api
- collection_type: open
  name: VividCortex (SolarWinds Database Performance Monitor) Alerts Hosts API
  slug: open-vividcortex-hosts-api
- collection_type: open
  name: VividCortex (SolarWinds Database Performance Monitor) Alerts Metrics API
  slug: open-vividcortex-metrics-api
- collection_type: open
  name: VividCortex (SolarWinds Database Performance Monitor) Alerts Queries API
  slug: open-vividcortex-queries-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/vividcortex/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.vividcortex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vividcortex.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vividcortex.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vividcortex.com/how-to-use-vividcortex/quick-start-guide/
- group: operate
  title: ''
  type: StatusPage
  url: https://dpm.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.vividcortex.com/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VividCortex
- group: start
  title: ''
  type: SignUp
  url: https://app.vividcortex.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.vividcortex.com/login
- group: operate
  title: ''
  type: Support
  url: https://docs.vividcortex.com/getting-started/troubleshooting/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solarwinds.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solarwinds.com/legal/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/vividcortex-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vividcortex-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vividcortex-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vividcortex-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vividcortex-changelog.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/vividcortex-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vividcortex-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/vividcortex-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/vividcortex-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vividcortex-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/vividcortex-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vividcortex-alerts-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vividcortex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vividcortex-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/vividcortex-packages.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vividcortex-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.solarwinds.com/information-security/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/vividcortex-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.solarwinds.com/trust-center
- group: commercial
  title: ''
  type: Pricing
  url: https://www.solarwinds.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.solarwinds.com/blog
created: '2026-07-17'
description: VividCortex is a SaaS database performance monitoring platform, now part of SolarWinds and marketed as SolarWinds Database Performance Monitor (DPM). It uses lightweight per-host agents to capture and analyze every query executed against MySQL, PostgreSQL, MongoDB, Redis, Amazon Aurora, and SQL Server workloads with sub-second, always-on visibility and minimal overhead. DPM surfaces query analysis, profiling, fault detection, adaptive alerting, and time-series metrics through a web application and a public REST API (v2) that exposes hosts, metrics and series data, observed queries and samples, timeline events, and alert configuration. VividCortex was acquired by SolarWinds in December 2019; this profile was surfaced as a portfolio company of Battery Ventures and enriched by the API Evangelist pipeline from the provider's live public documentation at docs.vividcortex.com.
image: https://avatars.githubusercontent.com/u/2809667?v=4
layout: provider
modified: '2026-07-21'
name: VividCortex
nav: Providers
network: true
overview: 'VividCortex publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Events API, Hosts API, and 2 more. Tagged areas include Company, Database, Performance Monitoring, Observability, and Monitoring.


  The VividCortex catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  VividCortex''s developer surface includes documentation, API reference, getting-started guide, changelog, signup flow, support, authentication, and 28 more developer resources.'
random_paper: 10
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 66.4
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vividcortex/refs/heads/main/screenshots/vividcortex-2026-08-17T082806.png
security:
- kind: authentication
  name: Vividcortex Authentication
  slug: vividcortex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vividcortex Domain Security
  slug: vividcortex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vividcortex Vulnerability Disclosure
  slug: vividcortex-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Vividcortex Trust Center
  slug: vividcortex-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: vividcortex
tags:
- Company
- Database
- Performance Monitoring
- Observability
- Monitoring
- APM
- Database Performance
- SQL
- DevOps
- SolarWinds
website: https://docs.vividcortex.com/
---
