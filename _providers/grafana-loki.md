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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.6
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: The Grafana Loki HTTP API — 40 documented endpoints for pushing logs (native and OTLP), querying with LogQL over instants and ranges, discovering labels, series, patterns and detected fields, streamin
  name: Loki HTTP API
  slug: loki-http-api
- description: 'Grafana Cloud Logs is the fully managed Grafana Loki service. It serves the same Loki HTTP API on a per-stack host of the form logs-prod-<cluster>.grafana.net, authenticated with HTTP Basic where the '
  name: Grafana Cloud Logs API
  slug: grafana-cloud-logs-api
- description: Grafana Loki reaches MCP clients through the Grafana Labs MCP servers, which register a Loki tool family (query_loki_logs, list_loki_label_names, list_loki_label_values, query_loki_stats, query_loki_p
  name: Grafana MCP Server — Loki tools
  slug: grafana-mcp-loki-tools
artifact_total: 11
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/grafana/loki/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://grafana.com/oss/loki/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://grafana.com/docs/loki/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/loki/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://grafana.com/docs/loki/latest/reference/loki-http-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://grafana.com/docs/loki/latest/get-started/
- group: operate
  title: ''
  type: Support
  url: https://community.grafana.com/
- group: company
  title: ''
  type: Blog
  url: https://grafana.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/grafana
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/loki
- group: commercial
  title: ''
  type: Pricing
  url: https://grafana.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://grafana.com/auth/sign-up/create-user
- group: commercial
  title: ''
  type: TermsOfService
  url: https://grafana.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://grafana.com/legal/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://grafana.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://grafana.com/legal/security-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: security/grafana-loki-trust-center.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.grafana.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/grafana-loki-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/grafana-loki-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/grafana-loki-changelog.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/grafana-loki-push.proto
- group: auth
  title: ''
  type: Authentication
  url: authentication/grafana-loki-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/grafana-loki-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/grafana-loki-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/grafana-loki-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/grafana-loki-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/grafana-loki-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/grafana-loki-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/grafana-loki-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/grafana-loki-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/grafana-loki-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/grafana-loki-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/grafana-loki-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/grafana-loki-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grafana-loki-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/grafana-loki-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/grafana-loki-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/grafana-loki-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/grafana-loki-query-logs.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/grafana-loki-push-logs.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/grafana-loki-delete-logs.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/grafana-loki-manage-alerting-rules.md
created: '2026-08-27'
description: Grafana Loki is Grafana Labs' open source log aggregation system — "like Prometheus, but for logs." Rather than full-text indexing log contents, Loki indexes only a small set of labels per log stream and stores the compressed lines in object storage, which is what makes it cheap to run at scale. It is queried with LogQL, a Prometheus-inspired query language, over an HTTP API that covers ingestion, querying, label and pattern discovery, live tailing over WebSocket, a Prometheus-compatible ruler for alerting and recording rules, and a cancellable log deletion API. Loki accepts native pushes and OpenTelemetry OTLP/HTTP logs, publishes proto3 gRPC service definitions for its push and query paths, and ships a first-party CLI (LogCLI), Helm charts, a Kubernetes operator, and Docker images. It is licensed AGPL-3.0 and self-hosted; the same engine is sold as the managed Grafana Cloud Logs service and as the self-managed Grafana Enterprise Logs distribution.
image: https://grafana.com/media/docs/loki/logo-grafana-loki.png
layout: provider
mcp_servers:
- description: 'Grafana Loki does not itself ship an MCP server. The Loki query surface reaches MCP clients through the Grafana Labs MCP servers, which expose Loki as a datasource: the open-source grafana/mcp-grafana'
  name: Grafana MCP server (Loki tools)
  slug: grafana-mcp-server-loki-tools
modified: '2026-08-27'
name: Grafana Loki
nav: Providers
network: true
overview: 'Grafana Loki publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logs, Logging, Log Aggregation, and Observability.


  Grafana Loki''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Grafana Loki Plans Pricing
  plan_count: 3
  slug: grafana-loki-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 14
  name: Grafana Loki Rate Limits
  slug: grafana-loki-rate-limits
scopes:
- name: Grafana Loki Scopes
  scope_count: 0
  slug: grafana-loki-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 80.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 84.2
  previous_composite: 62.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grafana-loki/refs/heads/main/screenshots/grafana-loki-2026-09-02T145629.png
security:
- kind: authentication
  name: Grafana Loki Authentication
  slug: grafana-loki-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Grafana Loki Domain Security
  slug: grafana-loki-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Grafana Loki Vulnerability Disclosure
  slug: grafana-loki-vulnerability-disclosure
  summary_line: Intigriti · contact published
- kind: trust-center
  name: Grafana Loki Trust Center
  slug: grafana-loki-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, PCI DSS, FedRAMP High, GDPR, CSA STAR, EU-US / Swiss-US Data Privacy Framework
slug: grafana-loki
tags:
- Company
- Logs
- Logging
- Log Aggregation
- Observability
- Monitoring
- Open-Source
- LogQL
- OpenTelemetry
- Telemetry
- Kubernetes
- Cloud-Native
website: https://grafana.com/oss/loki/
---
