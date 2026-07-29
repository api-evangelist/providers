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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Run queries against data ingested into Devo. Supports synchronous JSON/CSV/TSV responses and asynchronous job-based delivery to repositories (HDFS, Amazon S3, Kafka). Job requests start, stop, check s
  name: Devo Query API
  slug: devo-query-api
- description: Create, read, update, delete, and manage Devo alert definitions and alert instances programmatically.
  name: Devo Alerts API
  slug: devo-alerts-api
- description: Programmatic management of Devo Activeboards (dashboards) — list, retrieve, and administer board definitions.
  name: Devo Activeboards API
  slug: devo-activeboards-api
- description: Manage lookup tables used to enrich queries and correlate data within the Devo platform.
  name: Devo Lookups API
  slug: devo-lookups-api
- description: Administrative provisioning of Devo domains, users, and platform resources.
  name: Devo Provisioning API
  slug: devo-provisioning-api
- description: Manage Devo Relay configuration for secure data forwarding into the platform.
  name: Devo Relay API
  slug: devo-relay-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.devo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.devo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.devo.com/space/latest/95128251/API+reference
- group: docs
  title: ''
  type: APIReference
  url: https://docs.devo.com/space/latest/95128251/API+reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.devo.com/space/latest/95128301/Running+queries+with+the+Query+API
- group: auth
  title: ''
  type: Authentication
  url: authentication/devo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DevoInc
- group: company
  title: ''
  type: Blog
  url: https://www.devo.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.devo.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.devo.com/demo/
- group: start
  title: ''
  type: Login
  url: https://www.devo.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.devo.com/legal-hub/devo-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.devo.com/privacy/
- group: auth
  title: ''
  type: TrustCenter
  url: security/devo-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.devo.com/trust-center/
- group: build
  title: ''
  type: Packages
  url: packages/devo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/devo-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/devo-cli.yml
- group: design
  title: ''
  type: Components
  url: components/devo-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/devo-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/devo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/devo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/devo-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/devo-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/devo-llms.txt
created: '2026-07-17'
description: 'Devo is a cloud-native security data platform delivering unified SIEM, security analytics, and threat detection at petabyte scale, powered by its HyperStream data engine for real-time ingestion and analytics. Devo exposes a public REST API surface for programmatic access to the platform: a Query API for running synchronous and asynchronous (job) queries against ingested data, an Alerts API for managing alert definitions and alert instances, plus Activeboards, Lookups, Provisioning, and Relay APIs. Authentication uses domain API key and secret credentials (HMAC-SHA256 request signing via x-logtrust-apikey / -timestamp / -sign headers) or standalone Bearer tokens. First-party SDKs are published for Python, Node.js, and the browser, alongside a Grafana datasource, a Fluentd plugin, an ML Model Manager client, and a JavaScript application-builder framework. Regional API endpoints are provided for the US (apiv2-us.devo.com) and EU (apiv2-eu.devo.com).'
image: https://www.devo.com/wp-content/themes/devo/assets/images/devo-logo.svg
layout: provider
modified: '2026-07-18'
name: Devo
nav: Providers
network: true
overview: 'Devo publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, SIEM, Security, and Security Data Platform.


  Devo''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, signup flow, and 18 more developer resources.'
random_paper: 45
score:
  band: thin
  composite: 34.5
  delta: 0.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 33.7
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/devo/refs/heads/main/screenshots/devo-2026-07-25T211822.png
security:
- kind: authentication
  name: Devo Authentication
  slug: devo-authentication
  summary_line: apiKey-hmac/http-bearer · 2 schemes
- kind: domain-security
  name: Devo Domain Security
  slug: devo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Devo Trust Center
  slug: devo-trust-center
  summary_line: SOC 2 Type II
slug: devo
tags:
- Company
- Cybersecurity
- SIEM
- Security
- Security Data Platform
- Threat Detection
- Log Management
- Analytics
- Observability
- Query API
website: https://www.devo.com/
---
