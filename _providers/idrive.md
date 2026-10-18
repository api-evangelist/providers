---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.9
  scored_at: '2026-10-17'
api_count: 2
apis:
- baseURL: https://api.idrivee2.com/api
  baseurl_source: declared
  description: The Reseller API from IDrive — 24 operation(s) for reseller.
  name: IDrive Reseller API
  slug: idrive-reseller-api
- baseURL: https://api.idrivee2.com/api
  baseurl_source: declared
  description: The Subusers API from IDrive — 9 operation(s) for subusers.
  name: IDrive Subusers API
  slug: idrive-subusers-api
artifact_total: 16
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/idrive/refs/heads/main/rules/idrive-rules.yml
  title: ''
  type: Spectral
  url: rules/idrive-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/idrive/refs/heads/main/json-ld/idrive-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/idrive-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/idrive/refs/heads/main/vocabulary/idrive-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/idrive-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/idrive/refs/heads/main/data-model/idrive-data-model.yml
  title: ''
  type: DataModel
  url: data-model/idrive-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.idrive.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/idrive/refs/heads/main/authentication/idrive-authentication.yml
  title: ''
  type: Authentication
  url: authentication/idrive-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/idrive/refs/heads/main/scopes/idrive-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/idrive-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/idrive/refs/heads/main/conformance/idrive-conformance.yml
  title: ''
  type: Conformance
  url: conformance/idrive-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/idrive/refs/heads/main/mcp/idrive-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/idrive-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/idrive/refs/heads/main/well-known/idrive-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/idrive-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/idrive/refs/heads/main/hosts/idrive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/idrive-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/idrive/refs/heads/main/vendors/idrive-vendors.yml
  title: ''
  type: Vendors
  url: vendors/idrive-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.idrive.com/endpoint-backup/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.idrive.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.idrive.com/s3-storage-e2/media
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/idrive/refs/heads/main/security/idrive-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/idrive-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/idrive/refs/heads/main/security/idrive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/idrive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.idrive.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.idrive.com/s3-storage-e2/developer-guide
- group: docs
  title: ''
  type: Documentation
  url: https://www.idrive.com/s3-storage-e2/developer-guide
- group: docs
  title: ''
  type: APIReference
  url: https://www.idrive.com/s3-storage-e2/reseller-api
- group: operate
  title: ''
  type: Support
  url: https://www.idrive.com/s3-storage-e2/support
- group: operate
  title: ''
  type: FAQ
  url: https://www.idrive.com/s3-storage-e2/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://www.idrive.com/s3-storage-e2/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.idrivee2.com/signup
- group: start
  title: ''
  type: Login
  url: https://console.idrivee2.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.idrive.com/s3-storage-e2/terms
- group: company
  title: ''
  type: Blog
  url: https://blog.idrive.com/
created: '2026-10-13'
description: IDrive Inc. provides cloud backup and IDrive e2, an S3-compatible object storage service. For developers it publishes the IDrive e2 Reseller API (a REST/JSON API at api.idrivee2.com for managing users, regions, access keys, CNAME whitelabeling and subusers, authenticated with an API key sent in a token header), the S3-compatible storage endpoints themselves, and IDrive e2 MCP, an OAuth-protected hosted Model Context Protocol server at mcp.idrivee2.com/s3 (with a self-hosted option) exposing 65 bucket and object tools to AI clients.
image: https://static.idriveonlinebackup.com/include/images/idrive-image.png
json_schemas:
- name: PostApiResellerV1EditUserResponse
  property_count: 1
  slug: idrive-post-api-reseller-v1-edit-user-response
- name: PostApiResellerV1RemoveAccessKeyResponse
  property_count: 3
  slug: idrive-post-api-reseller-v1-remove-access-key-response
- name: PostApiResellerV1StorageBucketStatsResponse
  property_count: 3
  slug: idrive-post-api-reseller-v1-storage-bucket-stats-response
- name: PostApiResellerV1StorageCnameAddRequest
  property_count: 7
  slug: idrive-post-api-reseller-v1-storage-cname-add-request
- name: PostApiResellerV1StorageCnameResponse
  property_count: 1
  slug: idrive-post-api-reseller-v1-storage-cname-response
- name: PostApiResellerV1StorageCnameUpdateResponse
  property_count: 1
  slug: idrive-post-api-reseller-v1-storage-cname-update-response
jsonld:
- class_count: 27
  name: Idrive Context
  property_count: 21
  slug: idrive-context
layout: provider
mcp_servers:
- description: IDrive e2 MCP connects IDrive e2 object storage to MCP clients (Claude, Cursor, Codex, ChatGPT, Grok). Hosted endpoint https://mcp.idrivee2.com/s3 is OAuth-protected (RFC 9728 metadata served; anonymo
  name: IDrive MCP Server
  slug: idrive-e2
modified: '2026-10-13'
name: IDrive
nav: Providers
network: true
overview: 'IDrive is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Reseller API and Subusers API. Tagged areas include Company, Object Storage, S3 Compatible, Cloud Storage, and Backup.


  The IDrive catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  IDrive''s developer surface includes authentication, documentation, API reference, support, FAQ, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Idrive Plans
  plan_count: 11
  slug: idrive-plans
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: IDrive API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: idrive-rules
scopes:
- name: Idrive Scopes
  scope_count: 3
  slug: idrive-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 26.5
    developer_ergonomics: 45.2
    discoverability: 70.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Idrive Authentication
  slug: idrive-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Idrive Domain Security
  slug: idrive-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Idrive Trust Center
  slug: idrive-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: idrive
tags:
- Company
- Object Storage
- S3 Compatible
- Cloud Storage
- Backup
- Reseller
- MCP
website: https://www.idrive.com
---
