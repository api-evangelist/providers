---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 269
  human_in_the_loop: 5
  name: Confluent The Data Streaming Platform Agentic Access
  operation_count: 523
  slug: confluent-the-data-streaming-platform-agentic-access
  summary_line: 523 operations · 269 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: The Confluent Cloud REST API is the management plane for Confluent Cloud. It is used to manage organizations, environments, Kafka and Flink clusters, service accounts, API keys, role bindings, network
  name: Confluent Cloud REST API
  slug: cloud-rest-api
- description: The Kafka REST API (Confluent REST Proxy in self-managed deployments, Kafka REST in Cloud) provides HTTP access to Apache Kafka topics, consumers, partitions, brokers, and ACLs. Clients without a nati
  name: Confluent Kafka REST API
  slug: kafka-rest-api
- description: The Schema Registry REST API stores and serves Avro, JSON Schema, and Protobuf schemas with versioning and compatibility enforcement. It is available both as a managed Confluent Cloud service and as a
  name: Confluent Schema Registry REST API
  slug: schema-registry-api
- description: The Kafka Connect REST API manages connectors, tasks, and worker configuration. Operators use it to deploy, configure, pause, resume, and delete source and sink connectors, inspect task status, and re
  name: Kafka Connect REST API
  slug: connect-rest-api
- description: The ksqlDB REST API exposes ksqlDB, Confluent's streaming SQL engine, over HTTP. Clients submit streaming SQL statements, query streams and tables (push and pull queries), and inspect server status.
  name: ksqlDB REST API
  slug: ksqldb-rest-api
- description: The Confluent Cloud for Apache Flink REST API manages Flink compute pools, statements, and workspaces for stateful stream processing on Confluent Cloud. It is part of the Confluent Cloud REST surface.
  name: Confluent Cloud for Apache Flink REST API
  slug: flink-rest-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: The API Keys API from Confluent | the Data Streaming Platform — 2 operation(s) for api keys.
  name: Confluent | the Data Streaming Platform API Keys API
  slug: confluent-the-data-streaming-platform-api-keys-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: The Clusters API from Confluent | the Data Streaming Platform — 2 operation(s) for clusters.
  name: Confluent | the Data Streaming Platform Clusters API
  slug: confluent-the-data-streaming-platform-clusters-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: The Environments API from Confluent | the Data Streaming Platform — 2 operation(s) for environments.
  name: Confluent | the Data Streaming Platform Environments API
  slug: confluent-the-data-streaming-platform-environments-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: The Organizations API from Confluent | the Data Streaming Platform — 2 operation(s) for organizations.
  name: Confluent | the Data Streaming Platform Organizations API
  slug: confluent-the-data-streaming-platform-organizations-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: The Service Accounts API from Confluent | the Data Streaming Platform — 2 operation(s) for service accounts.
  name: Confluent | the Data Streaming Platform Service Accounts API
  slug: confluent-the-data-streaming-platform-service-accounts-api
artifact_total: 41
asyncapis:
- description: ''
  name: Confluent The Data Streaming Platform Webhooks
  slug: confluent-the-data-streaming-platform-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Confluent Cloud REST API (selected) API Keys API
  slug: open-confluent-the-data-streaming-platform-api-keys-api
- collection_type: open
  name: Confluent Cloud REST API (selected) API Keys Clusters API
  slug: open-confluent-the-data-streaming-platform-clusters-api
- collection_type: open
  name: Confluent Cloud REST API (selected) API Keys Environments API
  slug: open-confluent-the-data-streaming-platform-environments-api
- collection_type: open
  name: Confluent Cloud REST API (selected) API Keys Organizations API
  slug: open-confluent-the-data-streaming-platform-organizations-api
- collection_type: open
  name: Confluent Cloud REST API (selected) API Keys Service Accounts API
  slug: open-confluent-the-data-streaming-platform-service-accounts-api
- collection_type: open
  name: Confluent Cloud REST API (selected)
  slug: open-confluent-the-data-streaming-platform
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/confluent-the-data-streaming-platform-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/confluent-the-data-streaming-platform-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/confluent-the-data-streaming-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/confluent-the-data-streaming-platform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/confluent-the-data-streaming-platform-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/confluentinc/agent-skills
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/confluent
- group: company
  title: ''
  type: Website
  url: https://www.confluent.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.confluent.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.confluent.io/
- group: docs
  title: ''
  type: Cloud API Reference
  url: https://docs.confluent.io/cloud/current/api.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/confluentinc
- group: company
  title: ''
  type: Blog
  url: https://www.confluent.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.confluent.io/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.confluent.cloud/
- group: start
  title: ''
  type: Login
  url: https://confluent.cloud/login
- group: other
  title: ''
  type: Marketplace
  url: https://www.confluent.io/hub/
- group: learn
  title: ''
  type: Training
  url: https://training.confluent.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.confluent.io/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.confluent.io/legal/confluent-privacy-notice/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.confluent.io/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/confluent-the-data-streaming-platform-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/confluent-the-data-streaming-platform-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/confluent-the-data-streaming-platform-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/confluent-the-data-streaming-platform-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/confluent-the-data-streaming-platform-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/confluent-the-data-streaming-platform-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/confluent-the-data-streaming-platform-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/confluent-the-data-streaming-platform-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.confluent.io/cloud/current/api.html#deprecation-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/confluent-the-data-streaming-platform-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/confluent-the-data-streaming-platform-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.confluent.io/trust-and-security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/confluent-the-data-streaming-platform-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.confluent.io/trust-and-security/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/confluent-the-data-streaming-platform-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/confluent-the-data-streaming-platform-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/confluent-the-data-streaming-platform-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/confluent-the-data-streaming-platform-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/confluent-the-data-streaming-platform-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/confluent-the-data-streaming-platform-rate-limits.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.confluent.io/cloud/current/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.confluent.io/cloud/current/get-started/index.html
- group: operate
  title: ''
  type: Support
  url: https://support.confluent.io/
- group: operate
  title: ''
  type: Community
  url: https://developer.confluent.io/community/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/confluentinc
- group: start
  title: ''
  type: SignUp
  url: https://www.confluent.io/confluent-cloud/tryfree/
created: '2025-08-19'
description: Confluent is a fully managed data streaming platform built by the original creators of Apache Kafka. It lets organizations stream, connect, process, and govern data in motion through a cloud-native service (Confluent Cloud) and the on-prem/self-managed Confluent Platform. Confluent's developer surface includes the Confluent Cloud REST API for managing clusters, environments, and access; the Kafka REST Proxy for producing and consuming events over HTTP; the Schema Registry REST API for governance of Avro, JSON Schema, and Protobuf schemas; the Kafka Connect REST API for managing connectors; the ksqlDB REST API for stream processing; and managed Apache Flink. Authentication is API-key based (Cloud) or HTTP/mTLS/OAuth (Platform).
finops:
- name: Confluent The Data Streaming Platform Finops
  service_category: API
  slug: confluent-the-data-streaming-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/confluent-the-data-streaming-platform.png
layout: provider
mcp_servers:
- description: ''
  name: Confluent managed MCP server
  slug: confluent-managed-mcp-server
modified: '2026-09-05'
name: Confluent | the Data Streaming Platform
nav: Providers
network: true
overview: 'Confluent | the Data Streaming Platform publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Confluent Cloud REST API, API Keys API, Clusters API, and 3 more. Tagged areas include Apache Flink, Apache Kafka, Confluent Cloud, Connectors, and Data Streaming.


  The Confluent | the Data Streaming Platform catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Confluent | the Data Streaming Platform''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, training material, CLI, and 41 more developer resources.'
plans:
- name: Confluent The Data Streaming Platform Plans Pricing
  plan_count: 5
  slug: confluent-the-data-streaming-platform-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Confluent The Data Streaming Platform Rate Limits
  slug: confluent-the-data-streaming-platform-rate-limits
scopes:
- name: Confluent The Data Streaming Platform Scopes
  scope_count: 5
  slug: confluent-the-data-streaming-platform-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: strong
  composite: 64.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 25.4
  facets:
    access_clarity: 72.4
    commercial_clarity: 72.4
    contract_governance: 18.2
    contract_quality: 59.6
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 63.2
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/screenshots/confluent-the-data-streaming-platform-2026-06-20T174902.png
security:
- kind: authentication
  name: Confluent The Data Streaming Platform Authentication
  slug: confluent-the-data-streaming-platform-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Confluent The Data Streaming Platform Domain Security
  slug: confluent-the-data-streaming-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Confluent The Data Streaming Platform Vulnerability Disclosure
  slug: confluent-the-data-streaming-platform-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Confluent The Data Streaming Platform Trust Center
  slug: confluent-the-data-streaming-platform-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, SOC 3, ISO 27001, ISO 27701, PCI DSS, CSA STAR Level 2, HITRUST CSF, TISAX
skill_count: 12
skills:
- name: Bad_Frontmatter
  slug: bad-frontmatter
- name: confluent-cloud-cdc-tableflow
  slug: confluent-cloud-cdc-tableflow
- name: confluent-skill-creator
  slug: confluent-skill-creator
- name: confluent-skill-reviewer
  slug: confluent-skill-reviewer
- name: developing-kafka-python-client
  slug: developing-kafka-python-client
- name: flink-udf
  slug: flink-udf
- name: good-skill
  slug: good-skill
- name: inlined-refs
  slug: inlined-refs
- name: kafka-schema-registry
  slug: kafka-schema-registry
- name: kafka-streams-programming
  slug: kafka-streams-programming
- name: stale-expectations
  slug: stale-expectations
- name: trigger-overlap
  slug: trigger-overlap
slug: confluent-the-data-streaming-platform
tags:
- Apache Flink
- Apache Kafka
- Confluent Cloud
- Connectors
- Data Streaming
- Event Streaming
- Kafka Connect
- ksqlDB
- Real-Time Data
- REST
- Schema Registry
- Stream Processing
website: https://www.confluent.io/
---
