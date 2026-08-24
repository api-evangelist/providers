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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Consul Agentic Access
  operation_count: 58
  slug: consul-agentic-access
  summary_line: 58 operations · 25 acting
api_count: 14
apis:
- description: Access Control List management
  name: HashiCorp Consul ACL API
  slug: consul-acl-api
- description: Interact with the local Consul agent
  name: HashiCorp Consul Agent API
  slug: consul-agent-api
- description: Register and query services and nodes
  name: HashiCorp Consul Catalog API
  slug: consul-catalog-api
- description: Centralized configuration entries
  name: HashiCorp Consul Config Entries API
  slug: consul-config-entries-api
- description: Service mesh / Connect CA and intentions
  name: HashiCorp Consul Connect API
  slug: consul-connect-api
- description: Network coordinate information
  name: HashiCorp Consul Coordinates API
  slug: consul-coordinates-api
- description: Fire and list custom user events
  name: HashiCorp Consul Events API
  slug: consul-events-api
- description: Query health check information
  name: HashiCorp Consul Health API
  slug: consul-health-api
- description: Key/Value store operations
  name: HashiCorp Consul KV Store API
  slug: consul-kv-store-api
- description: Cluster operator endpoints
  name: HashiCorp Consul Operator API
  slug: consul-operator-api
- description: Session management for distributed locking
  name: HashiCorp Consul Sessions API
  slug: consul-sessions-api
- description: Snapshot and restore operations
  name: HashiCorp Consul Snapshot API
  slug: consul-snapshot-api
- description: Cluster status information
  name: HashiCorp Consul Status API
  slug: consul-status-api
- description: Atomic key/value transactions
  name: HashiCorp Consul Transaction API
  slug: consul-transaction-api
artifact_total: 41
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HashiCorp Consul HTTP ACL API
  slug: open-consul-acl-api
- collection_type: open
  name: HashiCorp Consul HTTP ACL Agent API
  slug: open-consul-agent-api
- collection_type: open
  name: HashiCorp Consul HTTP ACL Catalog API
  slug: open-consul-catalog-api
- collection_type: open
  name: HashiCorp Consul HTTP ACL Config Entries API
  slug: open-consul-config-entries-api
- collection_type: open
  name: HashiCorp Consul HTTP ACL Connect API
  slug: open-consul-connect-api
- collection_type: open
  name: HashiCorp Consul HTTP ACL Coordinates API
  slug: open-consul-coordinates-api
- collection_type: open
  name: HashiCorp Consul HTTP ACL Events API
  slug: open-consul-events-api
- collection_type: open
  name: HashiCorp Consul HTTP ACL Health API
  slug: open-consul-health-api
- collection_type: open
  name: HashiCorp Consul HTTP API
  slug: open-consul-http-api
- collection_type: open
  name: HashiCorp Consul HTTP ACL KV Store API
  slug: open-consul-kv-store-api
- collection_type: open
  name: HashiCorp Consul HTTP ACL Operator API
  slug: open-consul-operator-api
- collection_type: open
  name: HashiCorp Consul HTTP ACL Sessions API
  slug: open-consul-sessions-api
- collection_type: open
  name: HashiCorp Consul HTTP ACL Snapshot API
  slug: open-consul-snapshot-api
- collection_type: open
  name: HashiCorp Consul HTTP ACL Status API
  slug: open-consul-status-api
- collection_type: open
  name: HashiCorp Consul HTTP ACL Transaction API
  slug: open-consul-transaction-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/hashicorp/consul/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/hashicorp/.github/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/hashicorp/consul/blob/main/.github/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/consul-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/consul-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/consul-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.consul.io
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hashicorp.com/consul
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.hashicorp.com/consul/tutorials/get-started-vms
- group: learn
  title: ''
  type: Tutorials
  url: https://developer.hashicorp.com/consul/tutorials
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hashicorp
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/hashicorp/consul
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/hashicorp/consul/releases
- group: company
  title: ''
  type: Blog
  url: https://www.hashicorp.com/blog/products/consul
- group: operate
  title: ''
  type: Community
  url: https://discuss.hashicorp.com/c/consul
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/HashiCorp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hashicorp.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hashicorp.com/privacy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/consul-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/consul-service-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/consul-kv-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/consul-rules.yml
created: '2024-01-01'
description: HashiCorp Consul is a distributed, highly available service-networking control plane that automates network configuration, discovers services, enables secure service-to-service communication, and exposes a strongly consistent key/value store. The Consul HTTP API is a REST + JSON service exposed by every Consul agent and server at /v1, gated by the X-Consul-Token header (apiKey) and ACL policies, supporting blocking queries via X-Consul-Index for streaming-style change detection.
finops:
- name: Consul Finops
  service_category: API
  slug: consul-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/consul.png
json_schemas:
- name: Consul KV Pair
  property_count: 9
  slug: consul-kv
- name: Consul Service Definition
  property_count: 16
  slug: consul-service
jsonld:
- class_count: 0
  name: Consul Context
  property_count: 6
  slug: consul-context
layout: provider
modified: '2026-05-19'
name: HashiCorp Consul
nav: Providers
network: true
overview: 'HashiCorp Consul publishes 14 APIs on the [APIs.io](https://apis.io/) network, including ACL API, Agent API, Catalog API, and 11 more. Tagged areas include ACL, Configuration, Health Checking, Key-Value Store, and Multi-Datacenter.


  The HashiCorp Consul catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  HashiCorp Consul''s developer surface includes authentication, documentation, getting-started guide, changelog, engineering blog, and 17 more developer resources.'
plans:
- name: Consul Plans Pricing
  plan_count: 3
  slug: consul-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Consul Rate Limits
  slug: consul-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: HashiCorp Consul API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: consul-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: HashiCorp Consul API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 3
  slug: consul-rules
score:
  band: thin
  composite: 38.3
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 52.0
    developer_ergonomics: 36.9
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/consul/refs/heads/main/screenshots/consul-2026-06-20T174916.png
security:
- kind: authentication
  name: Consul Authentication
  slug: consul-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Consul Domain Security
  slug: consul-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: consul
tags:
- ACL
- Configuration
- Health Checking
- Key-Value Store
- Multi-Datacenter
- Open-Source
- Service Discovery
- Service Mesh
website: https://www.consul.io
---
