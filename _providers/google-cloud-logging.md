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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.8
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Google Cloud Logging Agentic Access
  operation_count: 15
  slug: google-cloud-logging-agentic-access
  summary_line: 15 operations · 10 acting
api_count: 1
apis:
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Bucket API from Google Cloud Logging — 1 operation(s) for bucket.
  name: Google Cloud Logging Bucket API
  slug: google-cloud-logging-bucket-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Buckets API from Google Cloud Logging — 1 operation(s) for buckets.
  name: Google Cloud Logging Buckets API
  slug: google-cloud-logging-buckets-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Entries:copy API from Google Cloud Logging — 1 operation(s) for entries:copy.
  name: Google Cloud Logging Entries:copy API
  slug: google-cloud-logging-entries-copy-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Entries:list API from Google Cloud Logging — 1 operation(s) for entries:list.
  name: Google Cloud Logging Entries:list API
  slug: google-cloud-logging-entries-list-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Entries:tail API from Google Cloud Logging — 1 operation(s) for entries:tail.
  name: Google Cloud Logging Entries:tail API
  slug: google-cloud-logging-entries-tail-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Entries:write API from Google Cloud Logging — 1 operation(s) for entries:write.
  name: Google Cloud Logging Entries:write API
  slug: google-cloud-logging-entries-write-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Exclusions API from Google Cloud Logging — 1 operation(s) for exclusions.
  name: Google Cloud Logging Exclusions API
  slug: google-cloud-logging-exclusions-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Google Cloud Logging API API from Google Cloud Logging — 1 operation(s) for google cloud logging api.
  name: Google Cloud Logging Google Cloud Logging API
  slug: google-cloud-logging-google-cloud-logging-api-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Sinks API from Google Cloud Logging — 1 operation(s) for sinks.
  name: Google Cloud Logging Sinks API
  slug: google-cloud-logging-sinks-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Logging Bucket API
  slug: open-google-cloud-logging-bucket-api
- collection_type: open
  name: Google Cloud Logging Bucket Buckets API
  slug: open-google-cloud-logging-buckets-api
- collection_type: open
  name: Google Cloud Logging Bucket Entries:copy API
  slug: open-google-cloud-logging-entries-copy-api
- collection_type: open
  name: Google Cloud Logging Bucket Entries:list API
  slug: open-google-cloud-logging-entries-list-api
- collection_type: open
  name: Google Cloud Logging Bucket Entries:tail API
  slug: open-google-cloud-logging-entries-tail-api
- collection_type: open
  name: Google Cloud Logging Bucket Entries:write API
  slug: open-google-cloud-logging-entries-write-api
- collection_type: open
  name: Google Cloud Logging Bucket Exclusions API
  slug: open-google-cloud-logging-exclusions-api
- collection_type: open
  name: Google Cloud Logging Bucket Google Cloud Logging API API
  slug: open-google-cloud-logging-google-cloud-logging-api-api
- collection_type: open
  name: Google Cloud Logging Bucket Sinks API
  slug: open-google-cloud-logging-sinks-api
- collection_type: open
  name: Google Cloud Logging API
  slug: open-google-cloud-logging
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/agentic-access/google-cloud-logging-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-logging-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/security/google-cloud-logging-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-logging-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/security/google-cloud-logging-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-logging-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/authentication/google-cloud-logging-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-logging-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/scopes/google-cloud-logging-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-logging-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://console.cloud.google.com
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/logging/docs/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/support
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/operations
- group: operate
  title: ''
  type: ChangeLog
  url: https://cloud.google.com/logging/docs/release-notes
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/logging/docs
- group: operate
  title: ''
  type: RateLimits
  url: https://cloud.google.com/logging/quotas
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/logs
- group: company
  title: ''
  type: Website
  url: https://cloud.google.com
- group: start
  title: ''
  type: Login
  url: https://console.cloud.google.com/
- group: start
  title: ''
  type: Signup
  url: https://console.cloud.google.com/freetrial
- group: build
  title: ''
  type: SDKs
  url: https://cloud.google.com/logging/docs/reference/libraries
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/stackdriver/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/google-cloud-logging
- group: operate
  title: ''
  type: Issue Tracker
  url: https://cloud.google.com/support/docs/issue-trackers
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/discovery/google-cloud-logging-discovery-v2.json
  title: ''
  type: Discovery
  url: discovery/google-cloud-logging-discovery-v2.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/grpc/google-cloud-logging-logging.proto
  title: ''
  type: Protobuf
  url: grpc/google-cloud-logging-logging.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/grpc/google-cloud-logging-logging-config.proto
  title: ''
  type: Protobuf
  url: grpc/google-cloud-logging-logging-config.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/grpc/google-cloud-logging-logging-metrics.proto
  title: ''
  type: Protobuf
  url: grpc/google-cloud-logging-logging-metrics.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/grpc/google-cloud-logging-log-entry.proto
  title: ''
  type: Protobuf
  url: grpc/google-cloud-logging-log-entry.proto
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/mcp/google-cloud-logging-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/google-cloud-logging-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/mcp/google-cloud-logging-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/google-cloud-logging-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/packages/google-cloud-logging-packages.yml
  title: ''
  type: Packages
  url: packages/google-cloud-logging-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/packages/google-cloud-logging-packages.yml
  title: ''
  type: SDKs
  url: packages/google-cloud-logging-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/cli/google-cloud-logging-cli.yml
  title: ''
  type: CLI
  url: cli/google-cloud-logging-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/well-known/google-cloud-logging-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-cloud-logging-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/well-known/google-cloud-logging-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/google-cloud-logging-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/llms/google-cloud-logging-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-cloud-logging-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/conventions/google-cloud-logging-conventions.yml
  title: ''
  type: Conventions
  url: conventions/google-cloud-logging-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/conventions/google-cloud-logging-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/google-cloud-logging-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/errors/google-cloud-logging-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-cloud-logging-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/lifecycle/google-cloud-logging-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-cloud-logging-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://cloud.google.com/terms/deprecation
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/conformance/google-cloud-logging-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-cloud-logging-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cloud.google.com/security/compliance
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/security/google-cloud-logging-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/google-cloud-logging-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/data-model/google-cloud-logging-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-cloud-logging-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/sandbox/google-cloud-logging-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/google-cloud-logging-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/changelog/google-cloud-logging-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/google-cloud-logging-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/rate-limits/google-cloud-logging-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-logging-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/plans/google-cloud-logging-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-logging-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/finops/google-cloud-logging-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-logging-finops.yml
created: '2024-01-01'
description: Google Cloud Logging is a fully managed, real-time log management service that ingests, stores, searches, analyzes, routes and alerts on application and system log data at scale across Google Cloud, AWS and on-premises environments. The v2 API writes log entries and manages the configuration surface behind them — log buckets and views, Log Router sinks and exclusions, logs-based metrics, log scopes, linked BigQuery datasets and CMEK settings. Google publishes it as a Discovery document with 254 methods, as first-party gRPC service definitions, through seven official client libraries and the gcloud logging command group, and — since April 2026 — through a fully managed remote MCP server at logging.googleapis.com/mcp that exposes six read-only tools to agents.
finops:
- name: Google Cloud Logging Finops
  service_category: API
  slug: google-cloud-logging-finops
layout: provider
mcp_servers:
- description: ''
  name: Cloud Logging MCP server
  slug: cloud-logging-mcp-server
modified: '2026-09-16'
name: Google Cloud Logging
nav: Providers
network: true
overview: 'Google Cloud Logging publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Bucket API, Buckets API, Entries:copy API, and 6 more. Tagged areas include Cloud, Logging, Monitoring, Observability, and Telemetry.


  Google Cloud Logging''s developer surface includes authentication, developer portal, getting-started guide, support, engineering blog, changelog, documentation, and 47 more developer resources.'
plans:
- name: Google Cloud Logging Plans Pricing
  plan_count: 1
  slug: google-cloud-logging-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 8
  name: Google Cloud Logging Rate Limits
  slug: google-cloud-logging-rate-limits
scopes:
- name: Google Cloud Logging Scopes
  scope_count: 5
  slug: google-cloud-logging-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: strong
  composite: 64.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 58.0
    catalog_earned_first_party: 20.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 51.0
    developer_ergonomics: 82.7
    discoverability: 72.2
    operational_transparency: 84.2
  previous_composite: 64.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/screenshots/google-cloud-logging-2026-08-17T083131.png
security:
- kind: authentication
  name: Google Cloud Logging Authentication
  slug: google-cloud-logging-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Google Cloud Logging Domain Security
  slug: google-cloud-logging-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Logging Vulnerability Disclosure
  slug: google-cloud-logging-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Google Cloud Logging Trust Center
  slug: google-cloud-logging-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, ISO 22301, PCI DSS, HIPAA, FedRAMP, CSA STAR, BSI C5, IRAP
slug: google-cloud-logging
tags:
- Cloud
- Logging
- Monitoring
- Observability
- Telemetry
- Log Management
- SRE
- DevOps
- OpenTelemetry
- Google Cloud
website: https://cloud.google.com
---
