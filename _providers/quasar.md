---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Quasar Agentic Access
  operation_count: 12
  slug: quasar-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 1
apis:
- baseURL: https://quasar.ai
  baseurl_source: declared
  description: Operational statistics about the QuasarDB cluster
  name: Quasar cluster API
  slug: quasar-cluster-api
- baseURL: https://quasar.ai
  baseurl_source: declared
  description: The Login API from Quasar — 1 operation(s) for login.
  name: Quasar Login API
  slug: quasar-login-api
- baseURL: https://quasar.ai
  baseurl_source: declared
  description: The max-in-buffer-size API from Quasar — 1 operation(s) for max-in-buffer-size.
  name: Quasar max-in-buffer-size API
  slug: quasar-max-in-buffer-size-api
- baseURL: https://quasar.ai
  baseurl_source: declared
  description: The option API from Quasar — 2 operation(s) for option.
  name: Quasar option API
  slug: quasar-option-api
- baseURL: https://quasar.ai
  baseurl_source: declared
  description: The parallelism API from Quasar — 1 operation(s) for parallelism.
  name: Quasar parallelism API
  slug: quasar-parallelism-api
- baseURL: https://quasar.ai
  baseurl_source: declared
  description: The Prometheus API from Quasar — 2 operation(s) for prometheus.
  name: Quasar Prometheus API
  slug: quasar-prometheus-api
- baseURL: https://quasar.ai
  baseurl_source: declared
  description: The query API from Quasar — 1 operation(s) for query.
  name: Quasar query API
  slug: quasar-query-api
- baseURL: https://quasar.ai
  baseurl_source: declared
  description: The Status API from Quasar — 2 operation(s) for status.
  name: Quasar Status API
  slug: quasar-status-api
- baseURL: https://quasar.ai
  baseurl_source: declared
  description: The Tables API from Quasar — 1 operation(s) for tables.
  name: Quasar Tables API
  slug: quasar-tables-api
- baseURL: https://quasar.ai
  baseurl_source: declared
  description: The tags API from Quasar — 1 operation(s) for tags.
  name: Quasar tags API
  slug: quasar-tags-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: QuasarDB cluster API
  slug: open-quasar-cluster-api
- collection_type: open
  name: QuasarDB cluster Login API
  slug: open-quasar-login-api
- collection_type: open
  name: QuasarDB cluster max-in-buffer-size API
  slug: open-quasar-max-in-buffer-size-api
- collection_type: open
  name: QuasarDB cluster option API
  slug: open-quasar-option-api
- collection_type: open
  name: QuasarDB cluster parallelism API
  slug: open-quasar-parallelism-api
- collection_type: open
  name: QuasarDB cluster Prometheus API
  slug: open-quasar-prometheus-api
- collection_type: open
  name: QuasarDB cluster query API
  slug: open-quasar-query-api
- collection_type: open
  name: QuasarDB cluster Status API
  slug: open-quasar-status-api
- collection_type: open
  name: QuasarDB cluster Tables API
  slug: open-quasar-tables-api
- collection_type: open
  name: QuasarDB cluster tags API
  slug: open-quasar-tags-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/quasar-rest-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.quasar.ai/master/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.quasar.ai/master/
- group: docs
  title: ''
  type: APIReference
  url: https://doc.quasar.ai/master/user-guide/api/rest.html
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.quasar.ai/master/user-guide/howto/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bureau14
- group: company
  title: ''
  type: Blog
  url: https://quasar.ai/blog-news/
- group: commercial
  title: ''
  type: Pricing
  url: https://quasar.ai/deployment-pricing/
- group: operate
  title: ''
  type: Support
  url: https://quasar.ai/support-services/
- group: build
  title: ''
  type: Packages
  url: packages/quasar-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/quasar-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/quasar-cli.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/quasar-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quasar-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/quasar-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/quasar-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/quasar-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/quasar-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/quasar-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/quasar-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.quasar.ai/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quasar-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/quasar-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quasar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quasar.ai/
created: '2026-07-17'
description: Quasar (QuasarDB, by Bureau 14) is a distributed, high-performance time-series database built for the hardest data problems, where precision, speed, scale, and accuracy must hold at the same time. It combines live ingestion, lossless-compressed historical retention, and heavy analytics on a single distributed system, deployed in cloud, edge, and appliance form across aerospace and defense, finance, industrial operations, and scientific research. QuasarDB exposes a JWT-authenticated REST API plus native client libraries in Python, Java, Go, .NET, C, PHP, R, and Ruby, and integrates with Grafana, Kafka, Spark, NATS, Prometheus, and Dask.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quasar.png
layout: provider
modified: '2026-07-20'
name: Quasar
nav: Providers
network: true
overview: 'Quasar publishes 10 APIs on the [APIs.io](https://apis.io/) network, including cluster API, Login API, max-in-buffer-size API, and 7 more. Tagged areas include Company, Time Series Database, Database, Analytics, and Infrastructure.


  Quasar''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, CLI, and 19 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 41.2
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quasar/refs/heads/main/screenshots/quasar-2026-09-02T152632.png
security:
- kind: authentication
  name: Quasar Authentication
  slug: quasar-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Quasar Domain Security
  slug: quasar-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Quasar Trust Center
  slug: quasar-trust-center
  summary_line: SOC 2
slug: quasar
tags:
- Company
- Time Series Database
- Database
- Analytics
- Infrastructure
- Real-Time Data
- Aerospace
- Finance
website: https://quasar.ai/
---
