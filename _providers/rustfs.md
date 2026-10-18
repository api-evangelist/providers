---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-10-17'
api_count: 4
apis:
- baseURL: http://localhost:9000
  baseurl_source: declared
  description: The Health API from RustFS — 2 operation(s) for health.
  name: RustFS Health API
  slug: rustfs-health-api
- baseURL: http://localhost:9000
  baseurl_source: declared
  description: The Minio API from RustFS — 2 operation(s) for minio.
  name: RustFS Minio API
  slug: rustfs-minio-api
- baseURL: http://localhost:9000
  baseurl_source: declared
  description: The RustFS API API from RustFS — 3 operation(s) for rustfs api.
  name: RustFS RustFS API
  slug: rustfs-rustfs-api-api
- baseURL: http://localhost:9000
  baseurl_source: declared
  description: The Rustfs API from RustFS — 13 operation(s) for rustfs.
  name: RustFS Rustfs API
  slug: rustfs-rustfs-api
artifact_total: 17
asyncapis:
- description: ''
  name: Rustfs Webhooks
  slug: rustfs-webhooks
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/plans/rustfs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rustfs-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/rules/rustfs-rules.yml
  title: ''
  type: Spectral
  url: rules/rustfs-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/json-ld/rustfs-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rustfs-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/vocabulary/rustfs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rustfs-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/asyncapi/rustfs-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/rustfs-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/data-model/rustfs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rustfs-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/cli/rustfs-cli.yml
  title: ''
  type: CLI
  url: cli/rustfs-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/changelog/rustfs-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rustfs-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/authentication/rustfs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rustfs-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/conformance/rustfs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rustfs-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/llms/rustfs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rustfs-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/mcp/rustfs-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rustfs-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/hosts/rustfs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rustfs-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/integrations/rustfs-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/rustfs-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/vendors/rustfs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rustfs-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/packages/rustfs-packages.yml
  title: ''
  type: SDKs
  url: packages/rustfs-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/packages/rustfs-packages.yml
  title: ''
  type: Packages
  url: packages/rustfs-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rustfs.com/en/installation/linux/quick-start
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rustfs/refs/heads/main/security/rustfs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rustfs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rustfs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rustfs.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rustfs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/rustfs/rustfs
- group: company
  title: ''
  type: Blog
  url: https://rustfs.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://rustfs.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rustfs.com/privacy-policy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://rustfs.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: 'RustFS is an Apache-2.0, Rust-built, S3-compatible distributed object storage system. It is self-hosted: each deployment serves the S3 API (plus admin API and health endpoints) on port 9000 and an embedded web console on port 9001, with an optional OpenStack Swift API, STS/OIDC identity, bucket event notifications, a Kubernetes operator and an MCP server.'
json_schemas:
- name: GetHealthResponse
  property_count: 1
  slug: rustfs-get-health-response
- name: GetRustfsAdminV3OidcProvidersResponse
  property_count: 1
  slug: rustfs-get-rustfs-admin-v3-oidc-providers-response
- name: PostRustfsAdminV3IdpBuiltinPolicyPolicyidRequest
  property_count: 3
  slug: rustfs-post-rustfs-admin-v3-idp-builtin-policy-policyid-request
- name: PostRustfsAdminV3RebalanceRebalanceidResponse
  property_count: 1
  slug: rustfs-post-rustfs-admin-v3-rebalance-rebalanceid-response
- name: PostRustfsAdminV3V3IdRequest
  property_count: 9
  slug: rustfs-post-rustfs-admin-v3-v3-id-request
- name: PutRustfsAdminV3V3IdRequest
  property_count: 1
  slug: rustfs-put-rustfs-admin-v3-v3-id-request
jsonld:
- class_count: 7
  name: Rustfs Context
  property_count: 17
  slug: rustfs-context
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 6 tools listed.
  name: RustFS MCP Server
  slug: rustfs-mcp-server
modified: '2026-10-13'
name: RustFS
nav: Providers
network: true
overview: 'RustFS is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Health API, Minio API, RustFS API, and 1 more. Tagged areas include Company, Object Storage, S3, Open Source, and Storage.


  The RustFS catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  RustFS''s developer surface includes CLI, changelog, authentication, getting-started guide, documentation, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Rustfs Plans Pricing
  plan_count: 2
  slug: rustfs-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: RustFS API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: rustfs-rules
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 66.8
    catalog_earned_first_party: 8.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 31.3
    developer_ergonomics: 50.0
    discoverability: 65.0
    operational_transparency: 28.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Rustfs Authentication
  slug: rustfs-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Rustfs Domain Security
  slug: rustfs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rustfs
tags:
- Company
- Object Storage
- S3
- Open Source
- Storage
website: https://rustfs.com
---
