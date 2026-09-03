---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: Versioned /v1 REST API for the Zenoss (Virtana Service Observability) platform. Covers the data receiver (metrics, events, entity models), event query and event management, model context (entity searc
  name: Virtana Service Observability API
  slug: zenoss
- description: First-party proto3 service contracts published at github.com/zenoss/zenoss-protobufs and released as a Go module (v1.5.5, 2026-07-27). DataReceiverService carries unary PutEvents, PutMetrics and PutMo
  name: Zenoss Cloud gRPC Services
  slug: zenoss-grpc
- description: The long-standing Zenoss JSON router API, still documented and supported for Zenoss Cloud Collection Zones and on-premises Zenoss Resource Manager / Service Dynamics. Every call is an HTTP POST of a J
  name: Zenoss API for Collection Zone and Resource Manager
  slug: zenoss-router-api
artifact_total: 10
asyncapis:
- description: ''
  name: Zenoss Webhooks
  slug: zenoss-webhooks
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/zenoss/zenoss-protobufs/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.zenoss.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zenoss.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zenoss.io/api/zenoss-api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zenoss.io/start/get-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zenoss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zenoss-inc-
- group: company
  title: ''
  type: Blog
  url: https://www.virtana.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.virtana.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.virtana.com/support/
- group: start
  title: ''
  type: Login
  url: https://app.cloud.virtana.com/ui/new-signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.virtana.com/legal-notices/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.virtana.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zenoss.io/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.zenoss.io/admin/updates/deprecation.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.zenoss.io/admin/updates/cloud-updates.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zenoss-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zenoss-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://docs.zenoss.io/glossary/glossary.html
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.virtana.com/trust/
- group: auth
  title: ''
  type: Compliance
  url: security/zenoss-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zenoss-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/zenoss-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zenoss-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zenoss-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zenoss-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zenoss-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zenoss-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zenoss-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zenoss-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zenoss-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zenoss-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenoss-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zenoss-llms.txt
created: '2026-03-27'
description: Zenoss is an AIOps and full-stack IT infrastructure monitoring platform, acquired by Virtana in May 2025 and now sold as Virtana Service Observability. It ingests metrics, events and entity models from hybrid estates — VMware, Nutanix, Kubernetes, AWS, Azure, GCP, network and storage — through on-premises Collection Zones, streaming agents and OpenTelemetry/OTLP, then applies dependency mapping, event correlation and anomaly detection to turn raw signal into service impact. The developer surface is a versioned /v1 REST API covering data ingest, event query and management, entity/model context, maintenance windows, the metric dictionary, notification Actions, credentials and user management, plus first-party proto3/gRPC contracts for the data receiver and data registry. API clients authenticate with a long-lived key in the zenoss-api-key header, issued per API Client from the console, and each tenant is assigned one of four regional endpoints.
finops:
- name: Zenoss Finops
  service_category: API
  slug: zenoss-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zenoss.png
layout: provider
modified: '2026-08-29'
name: Zenoss
nav: Providers
network: true
overview: 'Zenoss publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AIOps, Monitoring, Observability, Infrastructure, and Event Management.


  The Zenoss catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zenoss'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 28 more developer resources.'
plans:
- name: Zenoss Plans Pricing
  plan_count: 0
  slug: zenoss-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Zenoss Rate Limits
  slug: zenoss-rate-limits
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 20
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 33.3
    contract_quality: 41.6
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 33.3
    operational_transparency: 50.0
  previous_composite: 50.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zenoss/refs/heads/main/screenshots/zenoss-2026-06-20T201817.png
security:
- kind: authentication
  name: Zenoss Authentication
  slug: zenoss-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Zenoss Domain Security
  slug: zenoss-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zenoss Trust Center
  slug: zenoss-trust-center
  summary_line: SOC 2 Type II, CSA STAR Registry
slug: zenoss
tags:
- AIOps
- Monitoring
- Observability
- Infrastructure
- Event Management
- Hybrid Cloud
- OpenTelemetry
- gRPC
- Metrics
website: https://www.zenoss.com
---
