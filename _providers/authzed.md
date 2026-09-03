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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Authzed Agentic Access
  operation_count: 27
  slug: authzed-agentic-access
  summary_line: 27 operations · 27 acting
api_count: 1
apis:
- description: The managed cloud offering of SpiceDB by Authzed, providing production-ready authorization infrastructure with hourly metered billing. Includes all SpiceDB API capabilities plus Authzed-specific featu
  name: Authzed Cloud API
  slug: authzed-cloud-api
- baseURL: https://grpc.authzed.com
  baseurl_source: declared
  description: Experimental and preview endpoints subject to change
  name: Authzed Experimental API
  slug: authzed-experimental-api
- baseURL: https://grpc.authzed.com
  baseurl_source: declared
  description: Check, expand, and lookup permissions on resources and subjects
  name: Authzed Permissions API
  slug: authzed-permissions-api
- baseURL: https://grpc.authzed.com
  baseurl_source: declared
  description: Read, write, delete, and bulk import/export relationship tuples
  name: Authzed Relationships API
  slug: authzed-relationships-api
- baseURL: https://grpc.authzed.com
  baseurl_source: declared
  description: Manage SpiceDB schema definitions, diff schemas, and reflect schema metadata
  name: Authzed Schema API
  slug: authzed-schema-api
- baseURL: https://grpc.authzed.com
  baseurl_source: declared
  description: Stream real-time relationship change updates
  name: Authzed Watch API
  slug: authzed-watch-api
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Authzed SpiceDB Permissions Experimental API
  slug: open-authzed-experimental-api
- collection_type: open
  name: Authzed SpiceDB Experimental Permissions API
  slug: open-authzed-permissions-api
- collection_type: open
  name: Authzed SpiceDB Permissions Experimental Relationships API
  slug: open-authzed-relationships-api
- collection_type: open
  name: Authzed SpiceDB Permissions Experimental Schema API
  slug: open-authzed-schema-api
- collection_type: open
  name: Authzed SpiceDB Permissions Experimental Watch API
  slug: open-authzed-watch-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/authzed/api/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/authzed/api/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/authzed/api/blob/main/CODE-OF-CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/authzed/api/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/authzed/api/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/authzed-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/authzed-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/authzed-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/authzed-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://authzed.com
- group: docs
  title: ''
  type: Documentation
  url: https://authzed.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/authzed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/authzed
- group: company
  title: ''
  type: Blog
  url: https://authzed.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://authzed.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.authzed.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/authzed
- group: commercial
  title: ''
  type: Plans
  url: plans/authzed-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/authzed-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/authzed-finops.yml
created: '2026-06-13'
description: Authzed is a SpiceDB-based authorization platform providing REST and gRPC APIs for Zanzibar-style relationship-based access control. It enables developers to manage schemas, write relationship tuples, and execute fine-grained permission checks at scale. Authzed Cloud delivers hosted SpiceDB infrastructure with pay-as-you-grow billing, processing tens of billions of permission checks daily across enterprise and AI-native applications.
examples:
- key_count: 4
  name: Check Permission Request
  slug: check-permission-request
- key_count: 2
  name: Check Permission Response
  slug: check-permission-response
- key_count: 4
  name: Lookup Resources Request
  slug: lookup-resources-request
- key_count: 1
  name: Write Relationships Request
  slug: write-relationships-request
- key_count: 1
  name: Write Schema Request
  slug: write-schema-request
finops:
- name: Authzed Finops
  service_category: ''
  slug: authzed-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/authzed.png
json_schemas:
- name: CheckPermissionRequest
  property_count: 6
  slug: CheckPermissionRequest
- name: CheckPermissionResponse
  property_count: 5
  slug: CheckPermissionResponse
- name: DeleteRelationshipsRequest
  property_count: 5
  slug: DeleteRelationshipsRequest
- name: DeleteRelationshipsResponse
  property_count: 3
  slug: DeleteRelationshipsResponse
- name: ObjectReference
  property_count: 2
  slug: ObjectReference
- name: PermissionRelationshipTree
  property_count: 4
  slug: PermissionRelationshipTree
- name: ReadRelationshipsRequest
  property_count: 4
  slug: ReadRelationshipsRequest
- name: ReadRelationshipsResponse
  property_count: 3
  slug: ReadRelationshipsResponse
- name: ReadSchemaResponse
  property_count: 2
  slug: ReadSchemaResponse
- name: Relationship
  property_count: 5
  slug: Relationship
- name: SubjectReference
  property_count: 2
  slug: SubjectReference
- name: WriteRelationshipsRequest
  property_count: 3
  slug: WriteRelationshipsRequest
- name: WriteRelationshipsResponse
  property_count: 1
  slug: WriteRelationshipsResponse
- name: WriteSchemaRequest
  property_count: 1
  slug: WriteSchemaRequest
- name: WriteSchemaResponse
  property_count: 1
  slug: WriteSchemaResponse
- name: ZedToken
  property_count: 1
  slug: ZedToken
jsonld:
- class_count: 4
  name: Authzed Context
  property_count: 34
  slug: authzed-context
layout: provider
modified: '2026-06-13'
name: Authzed
nav: Providers
network: true
overview: 'Authzed publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Experimental API, Permissions API, Relationships API, and 2 more. Tagged areas include Authorization, Access Control, Permissions, Zanzibar, and SpiceDB.


  The Authzed catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Authzed''s developer surface includes authentication, documentation, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Authzed Plans Pricing
  plan_count: 4
  slug: authzed-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Authzed Rate Limits
  slug: authzed-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Authzed API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: authzed-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 15
    catalog_gap: 39.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 56.5
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 68.4
  open_source:
    applies: true
    score: 65.0
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/authzed/refs/heads/main/screenshots/authzed-2026-06-20T172614.png
security:
- kind: authentication
  name: Authzed Authentication
  slug: authzed-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Authzed Domain Security
  slug: authzed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Authzed Trust Center
  slug: authzed-trust-center
  summary_line: SOC 2, GDPR
slug: authzed
tags:
- Authorization
- Access Control
- Permissions
- Zanzibar
- SpiceDB
- gRPC
- REST
- Relationship-Based Access Control
- ReBAC
- Fine-Grained Authorization
- Identity
- Security
website: https://authzed.com
---
