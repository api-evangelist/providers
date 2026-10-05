---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
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
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.3
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Neo4J Agentic Access
  operation_count: 21
  slug: neo4j-agentic-access
  summary_line: 21 operations · 14 acting
api_count: 2
apis:
- baseURL: http://localhost:7474
  baseurl_source: spec
  description: The Neo4j Query API enables the execution of Cypher statements against a Neo4j server through HTTP requests. It provides a streamlined interface for running graph database queries, supporting both sel
  name: Neo4j Query API
  slug: query-api
- description: The Neo4j GraphQL Library is an open source JavaScript library that enables rapid development of GraphQL APIs backed by a Neo4j graph database. It automatically generates a single optimized Cypher que
  name: Neo4j GraphQL Library
  slug: graphql-library
- description: The Neo4j Bolt Protocol is a binary application protocol designed for efficient execution of database queries using the Cypher query language. It operates over TCP or WebSocket connections on the defa
  name: Neo4j Bolt Protocol
  slug: bolt-protocol
- description: The Neo4j Python Driver is the official library for interacting with Neo4j graph databases from Python applications. It communicates using the Bolt protocol and supports both single instance and clust
  name: Neo4j Python Driver
  slug: python-driver
- description: The Neo4j Java Driver is the official library for connecting Java applications to Neo4j graph databases. Distributed via Maven, it uses the Bolt protocol for network communication and supports both si
  name: Neo4j Java Driver
  slug: java-driver
- description: The Neo4j JavaScript Driver is the official library for interacting with Neo4j graph databases from JavaScript and Node.js applications. It uses the Bolt protocol for efficient communication and can b
  name: Neo4j JavaScript Driver
  slug: javascript-driver
- baseURL: https://api.neo4j.io/v1
  baseurl_source: spec
  description: OAuth2 token management for authenticating API requests. Access tokens are temporary and expire after one hour.
  name: Neo4j Authentication API
  slug: neo4j-authentication-api
- baseURL: http://localhost:7474
  baseurl_source: spec
  description: Server discovery endpoint that returns available endpoints, server version, edition, and authentication configuration.
  name: Neo4j Discovery API
  slug: neo4j-discovery-api
- baseURL: https://api.neo4j.io/v1
  baseurl_source: spec
  description: Manage AuraDB cloud database instances including provisioning, configuration, lifecycle operations such as pause and resume, and deletion.
  name: Neo4j Instances API
  slug: neo4j-instances-api
- baseURL: https://api.neo4j.io/v1
  baseurl_source: spec
  description: Manage database snapshots which are point-in-time copies of instance data used for backup and restore operations.
  name: Neo4j Snapshots API
  slug: neo4j-snapshots-api
- baseURL: https://api.neo4j.io/v1
  baseurl_source: spec
  description: Manage tenants (projects) which organize multiple database instances under a single administrative unit for access control and configuration.
  name: Neo4j Tenants API
  slug: neo4j-tenants-api
- baseURL: http://localhost:7474
  baseurl_source: spec
  description: Manage explicit transactions with full control over the transaction lifecycle including open, run, commit, and rollback operations.
  name: Neo4j Transactions API
  slug: neo4j-transactions-api
artifact_total: 58
collections:
- collection_type: postman
  name: Neo4j Aura Authentication API
  slug: postman-neo4j-authentication-api
- collection_type: postman
  name: Neo4j Aura Authentication Discovery API
  slug: postman-neo4j-discovery-api
- collection_type: postman
  name: Neo4j Aura Authentication Instances API
  slug: postman-neo4j-instances-api
- collection_type: postman
  name: Neo4j Aura Authentication Query API
  slug: postman-neo4j-query-api
- collection_type: postman
  name: Neo4j Aura Authentication Snapshots API
  slug: postman-neo4j-snapshots-api
- collection_type: postman
  name: Neo4j Aura Authentication Tenants API
  slug: postman-neo4j-tenants-api
- collection_type: postman
  name: Neo4j Aura Authentication Transactions API
  slug: postman-neo4j-transactions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Neo4j Aura API
  slug: open-neo4j-aura-api
- collection_type: open
  name: Neo4j Aura Authentication API
  slug: open-neo4j-authentication-api
- collection_type: open
  name: Neo4j Aura Authentication Discovery API
  slug: open-neo4j-discovery-api
- collection_type: open
  name: Neo4j HTTP API
  slug: open-neo4j-http-api
- collection_type: open
  name: Neo4j Aura Authentication Instances API
  slug: open-neo4j-instances-api
- collection_type: open
  name: Neo4j Aura Authentication Query API
  slug: open-neo4j-query-api
- collection_type: open
  name: Neo4j Aura Authentication Snapshots API
  slug: open-neo4j-snapshots-api
- collection_type: open
  name: Neo4j Aura Authentication Tenants API
  slug: open-neo4j-tenants-api
- collection_type: open
  name: Neo4j Aura Authentication Transactions API
  slug: open-neo4j-transactions-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/finops/neo4j-finops.yml
  title: ''
  type: FinOps
  url: finops/neo4j-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/rate-limits/neo4j-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/neo4j-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/plans/neo4j-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/neo4j-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/rules/neo4j-rules.yml
  title: ''
  type: Spectral
  url: rules/neo4j-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/rules/neo4j-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/neo4j-jsonschema-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/json-ld/neo4j-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/neo4j-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/vocabulary/neo4j-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/neo4j-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/data-model/neo4j-data-model.yml
  title: ''
  type: DataModel
  url: data-model/neo4j-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/cli/neo4j-cli.yml
  title: ''
  type: CLI
  url: cli/neo4j-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/changelog/neo4j-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/neo4j-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.neo4j.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/errors/neo4j-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/neo4j-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/conformance/neo4j-conformance.yml
  title: ''
  type: Conformance
  url: conformance/neo4j-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/llms/neo4j-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/neo4j-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/well-known/neo4j-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/neo4j-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/well-known/neo4j-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/neo4j-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/well-known/neo4j-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/neo4j-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/hosts/neo4j-hosts.yml
  title: ''
  type: Hosts
  url: hosts/neo4j-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/vendors/neo4j-vendors.yml
  title: ''
  type: Vendors
  url: vendors/neo4j-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/packages/neo4j-packages.yml
  title: ''
  type: SDKs
  url: packages/neo4j-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/packages/neo4j-packages.yml
  title: ''
  type: Packages
  url: packages/neo4j-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://neo4j.com/blog/security/graphs-for-cybersecurity/
- group: commercial
  title: ''
  type: Pricing
  url: https://neo4j.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://neo4j.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://neo4j.com/leadership/
- group: operate
  title: ''
  type: ChangeLog
  url: https://neo4j.com/release-notes/
- group: docs
  title: ''
  type: APIReference
  url: https://neo4j.com/docs/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://neo4j.com/docs/getting-started/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/neo4j/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/agentic-access/neo4j-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/neo4j-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/security/neo4j-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/neo4j-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/security/neo4j-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/neo4j-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/security/neo4j-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/neo4j-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/authentication/neo4j-authentication.yml
  title: ''
  type: Authentication
  url: authentication/neo4j-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neo4j
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/neo4j
- group: start
  title: ''
  type: Portal
  url: https://neo4j.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://neo4j.com/docs/
- group: company
  title: ''
  type: Website
  url: https://neo4j.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://neo4j.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://neo4j.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://support.neo4j.com/
- group: company
  title: ''
  type: Blog
  url: https://neo4j.com/blog/
- group: start
  title: ''
  type: Login
  url: https://console.neo4j.io/
- group: agent
  title: ''
  type: AgentSkills
  url: https://neo4j.com/blog/developer/introducing-neo4j-agent-skills/
- group: agent
  title: ''
  type: LlmsText
  url: https://neo4j.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/capabilities/neo4j-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/neo4j-capability-edges.yml
created: '2025-03-05'
description: Neo4j is the leading graph database platform, enabling developers to build applications powered by connected data. Their developer platform provides HTTP, Query, and Aura cloud APIs alongside official drivers for Python, Java, and JavaScript, as well as a GraphQL library for rapid API development backed by the Neo4j graph database.
finops:
- name: Neo4J Finops
  service_category: Database
  slug: neo4j-finops
graphqls:
- description: The Neo4j GraphQL Library is an open source JavaScript library that enables rapid development of GraphQL APIs backed by a Neo4j graph database. It automatically generates a single optimized Cypher que
  name: Neo4j GraphQL API
  slug: neo4j-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neo4j.png
json_schemas:
- name: Neo4j Aura Instance
  property_count: 12
  slug: neo4j-aura-instance
- name: CreateInstanceRequest
  property_count: 7
  slug: neo4j-create-instance-request
- name: Neo4j Cypher Statement
  property_count: 4
  slug: neo4j-cypher-statement
- name: DiscoveryResponse
  property_count: 5
  slug: neo4j-discovery-response
- name: Neo4j Graph Elements
  property_count: 2
  slug: neo4j-graph-elements
- name: InstanceCreated
  property_count: 7
  slug: neo4j-instance-created
- name: Instance
  property_count: 12
  slug: neo4j-instance
- name: OverwriteInstanceRequest
  property_count: 2
  slug: neo4j-overwrite-instance-request
- name: QueryRequest
  property_count: 1
  slug: neo4j-query-request
- name: QueryResponse
  property_count: 2
  slug: neo4j-query-response
- name: RestoreSnapshotRequest
  property_count: 6
  slug: neo4j-restore-snapshot-request
- name: Snapshot
  property_count: 5
  slug: neo4j-snapshot
- name: Tenant
  property_count: 3
  slug: neo4j-tenant
- name: TokenResponse
  property_count: 3
  slug: neo4j-token-response
- name: TransactionRequest
  property_count: 1
  slug: neo4j-transaction-request
- name: TransactionResponse
  property_count: 4
  slug: neo4j-transaction-response
- name: UpdateInstanceRequest
  property_count: 2
  slug: neo4j-update-instance-request
jsonld:
- class_count: 0
  name: Neo4J Context
  property_count: 7
  slug: neo4j-context
layout: provider
modified: '2026-05-19'
name: Neo4j
nav: Providers
network: true
overview: 'Neo4j publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Query API, Authentication API, Discovery API, and 9 more. Tagged areas include Neo4j, Graph Database, Cypher, Cloud, and GraphQL.


  The Neo4j catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Neo4j''s developer surface includes CLI, changelog, pricing, API reference, getting-started guide, authentication, developer portal, and 41 more developer resources.'
plans:
- name: Neo4J Plans Pricing
  plan_count: 8
  slug: neo4j-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Neo4J Rate Limits
  slug: neo4j-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Neo4j API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: neo4j-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Neo4j API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: neo4j-rules
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 31
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 17.4
  facets:
    access_clarity: 69.7
    contract_governance: 22.0
    contract_quality: 64.0
    developer_ergonomics: 74.4
    discoverability: 67.9
    operational_transparency: 36.8
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/screenshots/neo4j-2026-08-17T124223.png
security:
- kind: authentication
  name: Neo4J Authentication
  slug: neo4j-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Neo4J Domain Security
  slug: neo4j-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Neo4J Vulnerability Disclosure
  slug: neo4j-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Neo4J Trust Center
  slug: neo4j-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR, CSA STAR
slug: neo4j
tags:
- Neo4j
- Graph Database
- Cypher
- Cloud
- GraphQL
- Drivers
- Database
website: https://neo4j.com
---
