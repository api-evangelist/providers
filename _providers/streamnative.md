---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Streamnative Agentic Access
  operation_count: 59
  slug: streamnative-agentic-access
  summary_line: 59 operations · 32 acting
api_count: 20
apis:
- baseURL: https://api.streamnative.cloud
  baseurl_source: declared
  description: The cloudStreamnativeIo_v1alpha1 API from StreamNative — 20 operation(s) for cloudstreamnativeio_v1alpha1.
  name: StreamNative Cloud Streamnative Io V1alpha1 API
  slug: streamnative-cloudstreamnativeio-v1alpha1-api
- baseURL: https://api.streamnative.cloud
  baseurl_source: declared
  description: The ksn-consumer-group API from StreamNative — 4 operation(s) for ksn-consumer-group.
  name: StreamNative Ksn Consumer Group API
  slug: streamnative-ksn-consumer-group-api
- baseURL: https://api.streamnative.cloud
  baseurl_source: declared
  description: The ksn-topics API from StreamNative — 5 operation(s) for ksn-topics.
  name: StreamNative Ksn Topics API
  slug: streamnative-ksn-topics-api
artifact_total: 38
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/agentic-access/streamnative-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/streamnative-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/plans/streamnative-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/streamnative-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/rules/streamnative-rules.yml
  title: ''
  type: Spectral
  url: rules/streamnative-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/json-ld/streamnative-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/streamnative-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/vocabulary/streamnative-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/streamnative-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/data-model/streamnative-data-model.yml
  title: ''
  type: DataModel
  url: data-model/streamnative-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/authentication/streamnative-authentication.yml
  title: ''
  type: Authentication
  url: authentication/streamnative-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/errors/streamnative-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/streamnative-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/conformance/streamnative-conformance.yml
  title: ''
  type: Conformance
  url: conformance/streamnative-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/llms/streamnative-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/streamnative-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/a2a/streamnative-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/streamnative-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/mcp/streamnative-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/streamnative-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/well-known/streamnative-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/streamnative-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/hosts/streamnative-hosts.yml
  title: ''
  type: Hosts
  url: hosts/streamnative-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/vendors/streamnative-vendors.yml
  title: ''
  type: Vendors
  url: vendors/streamnative-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.streamnative.io/
- group: company
  title: ''
  type: Newsroom
  url: https://streamnative.io/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/streamnative/refs/heads/main/security/streamnative-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/streamnative-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://streamnative.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.streamnative.io/home
- group: docs
  title: ''
  type: APIReference
  url: https://docs.streamnative.io/api-references/cloudapi/cloud-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.streamnative.io/cloud/get-started/quickstart-kafka
- group: operate
  title: ''
  type: Support
  url: https://support.streamnative.io/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.streamnative.io/
- group: company
  title: ''
  type: Blog
  url: https://streamnative.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/streamnative
- group: commercial
  title: ''
  type: Pricing
  url: https://streamnative.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.streamnative.cloud/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://streamnative.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://streamnative.io/privacy
created: '2026-10-13'
description: StreamNative is the company founded by the original creators of Apache Pulsar, offering StreamNative Cloud - a managed data streaming platform that runs Apache Pulsar and Apache Kafka-compatible (Kafka protocol) clusters as Serverless, Dedicated, BYOC and self-managed Private Cloud deployments, with Lakehouse storage integration, connectors and Pulsar Functions. It publishes a Kubernetes-style Cloud API at api.streamnative.cloud for managing API keys, service accounts, Pulsar instances, clusters and gateways, a Kafka REST API, and an MCP server.
image: https://streamnative.io/imgs/og-default.webp
json_schemas:
- name: cloud.v1alpha1.APIKeyList
  property_count: 4
  slug: streamnative-cloud-v1alpha1-apikey-list
- name: cloud.v1alpha1.APIKey
  property_count: 5
  slug: streamnative-cloud-v1alpha1-apikey
- name: cloud.v1alpha1.CloudConnectionList
  property_count: 4
  slug: streamnative-cloud-v1alpha1-cloud-connection-list
- name: cloud.v1alpha1.CloudConnection
  property_count: 5
  slug: streamnative-cloud-v1alpha1-cloud-connection
- name: cloud.v1alpha1.CloudEnvironmentList
  property_count: 4
  slug: streamnative-cloud-v1alpha1-cloud-environment-list
- name: cloud.v1alpha1.CloudEnvironment
  property_count: 5
  slug: streamnative-cloud-v1alpha1-cloud-environment
- name: cloud.v1alpha1.PulsarClusterList
  property_count: 4
  slug: streamnative-cloud-v1alpha1-pulsar-cluster-list
- name: cloud.v1alpha1.PulsarCluster
  property_count: 5
  slug: streamnative-cloud-v1alpha1-pulsar-cluster
- name: cloud.v1alpha1.PulsarGatewayList
  property_count: 4
  slug: streamnative-cloud-v1alpha1-pulsar-gateway-list
- name: cloud.v1alpha1.PulsarGateway
  property_count: 5
  slug: streamnative-cloud-v1alpha1-pulsar-gateway
- name: cloud.v1alpha1.PulsarInstanceList
  property_count: 4
  slug: streamnative-cloud-v1alpha1-pulsar-instance-list
- name: cloud.v1alpha1.PulsarInstance
  property_count: 5
  slug: streamnative-cloud-v1alpha1-pulsar-instance
- name: cloud.v1alpha1.SecretList
  property_count: 4
  slug: streamnative-cloud-v1alpha1-secret-list
- name: cloud.v1alpha1.Secret
  property_count: 10
  slug: streamnative-cloud-v1alpha1-secret
- name: cloud.v1alpha1.ServiceAccountBindingList
  property_count: 4
  slug: streamnative-cloud-v1alpha1-service-account-binding-list
- name: cloud.v1alpha1.ServiceAccountBinding
  property_count: 5
  slug: streamnative-cloud-v1alpha1-service-account-binding
- name: cloud.v1alpha1.ServiceAccountList
  property_count: 4
  slug: streamnative-cloud-v1alpha1-service-account-list
- name: cloud.v1alpha1.ServiceAccount
  property_count: 5
  slug: streamnative-cloud-v1alpha1-service-account
- name: cloud.v1alpha1.UserList
  property_count: 4
  slug: streamnative-cloud-v1alpha1-user-list
- name: cloud.v1alpha1.User
  property_count: 5
  slug: streamnative-cloud-v1alpha1-user
- name: io.k8s.apimachinery.pkg.apis.meta.v1.Patch
  property_count: 0
  slug: streamnative-io-k8s-apimachinery-pkg-apis-meta-v1-patch
- name: io.k8s.apimachinery.pkg.apis.meta.v1.Status
  property_count: 8
  slug: streamnative-io-k8s-apimachinery-pkg-apis-meta-v1-status
- name: KafkaConsumerGroupList
  property_count: 3
  slug: streamnative-kafka-consumer-group-list
- name: KafkaConsumerGroup
  property_count: 7
  slug: streamnative-kafka-consumer-group
- name: KafkaConsumerLagList
  property_count: 3
  slug: streamnative-kafka-consumer-lag-list
- name: KafkaConsumerList
  property_count: 3
  slug: streamnative-kafka-consumer-list
- name: KafkaTopicList
  property_count: 3
  slug: streamnative-kafka-topic-list
- name: TopicMessageEventDTO
  property_count: 4
  slug: streamnative-topic-message-event-dto
jsonld:
- class_count: 101
  name: Streamnative Context
  property_count: 200
  slug: streamnative-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.streamnative.io.
  name: StreamNative MCP Servers
  slug: streamnative-mcp-servers
modified: '2026-10-13'
name: StreamNative
nav: Providers
network: true
overview: 'StreamNative publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Cloud Streamnative Io V1alpha1 API, Ksn Consumer Group API, and Ksn Topics API. Tagged areas include Company, Data Streaming, Apache Pulsar, Apache Kafka, and Messaging.


  The StreamNative catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  StreamNative''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Streamnative Plans Pricing
  plan_count: 3
  slug: streamnative-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: StreamNative API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 3
  slug: streamnative-rules
score:
  band: developing
  composite: 53.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 58.1
    developer_ergonomics: 47.6
    discoverability: 81.7
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Streamnative Authentication
  slug: streamnative-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Streamnative Domain Security
  slug: streamnative-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: streamnative
tags:
- Company
- Data Streaming
- Apache Pulsar
- Apache Kafka
- Messaging
- Event Streaming
- Cloud
website: https://streamnative.io
---
