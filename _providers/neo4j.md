---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Neo4J Agentic Access
  operation_count: 21
  slug: neo4j-agentic-access
  summary_line: 21 operations · 14 acting
api_count: 12
apis:
- description: The Neo4j Query API enables the execution of Cypher statements against a Neo4j server through HTTP requests. It provides a streamlined interface for running graph database queries, supporting both sel
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
- description: OAuth2 token management for authenticating API requests. Access tokens are temporary and expire after one hour.
  name: Neo4j Authentication API
  slug: neo4j-authentication-api
- description: Server discovery endpoint that returns available endpoints, server version, edition, and authentication configuration.
  name: Neo4j Discovery API
  slug: neo4j-discovery-api
- description: Manage AuraDB cloud database instances including provisioning, configuration, lifecycle operations such as pause and resume, and deletion.
  name: Neo4j Instances API
  slug: neo4j-instances-api
- description: Manage database snapshots which are point-in-time copies of instance data used for backup and restore operations.
  name: Neo4j Snapshots API
  slug: neo4j-snapshots-api
- description: Manage tenants (projects) which organize multiple database instances under a single administrative unit for access control and configuration.
  name: Neo4j Tenants API
  slug: neo4j-tenants-api
- description: Manage explicit transactions with full control over the transaction lifecycle including open, run, commit, and rollback operations.
  name: Neo4j Transactions API
  slug: neo4j-transactions-api
artifact_total: 43
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/neo4j/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/neo4j-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/neo4j-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/neo4j-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neo4j-domain-security.yml
- group: auth
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
- name: Neo4j Cypher Statement
  property_count: 4
  slug: neo4j-cypher-statement
- name: Neo4j Graph Elements
  property_count: 2
  slug: neo4j-graph-elements
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
overview: 'Neo4j publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Query API, Authentication API, Discovery API, and 4 more. Tagged areas include Graph Database, Cypher, Cloud, GraphQL, and Drivers.


  The Neo4j catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Neo4j''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 13 more developer resources.'
plans:
- name: Neo4J Plans Pricing
  plan_count: 8
  slug: neo4j-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 3
  name: Neo4J Rate Limits
  slug: neo4j-rate-limits
rules:
- name: Neo4j API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: neo4j-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.2
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 66.0
    developer_ergonomics: 45.7
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
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
- Graph Database
- Cypher
- Cloud
- GraphQL
- Drivers
- APIs
website: https://neo4j.com
---
