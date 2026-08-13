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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Oso Agentic Access
  operation_count: 20
  slug: oso-agentic-access
  summary_line: 20 operations · 18 acting
api_count: 4
apis:
- description: The Centralized Authorization Data API from Oso Cloud — 6 operation(s) for centralized authorization data.
  name: Oso Cloud Centralized Authorization Data API
  slug: oso-centralized-authorization-data-api
- description: The Check API API from Oso Cloud — 6 operation(s) for check api.
  name: Oso Cloud Check API API
  slug: oso-check-api-api
- description: The Local Check API API from Oso Cloud — 4 operation(s) for local check api.
  name: Oso Cloud Local Check API API
  slug: oso-local-check-api-api
- description: The Policy API from Oso Cloud — 2 operation(s) for policy.
  name: Oso Cloud Policy API
  slug: oso-policy-api
artifact_total: 66
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oso-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/oso-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oso-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oso-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.osohq.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.osohq.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/osohq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/osohq
- group: company
  title: ''
  type: Blog
  url: https://www.osohq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.osohq.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://oso.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://x.com/osohq
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.osohq.com/docs/changelog/whats-new
- group: commercial
  title: ''
  type: Plans
  url: plans/oso-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/oso-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/oso-finops.yml
created: '2026-06-13'
description: Oso Cloud is an authorization-as-a-service platform that provides a REST API for defining and enforcing relationship-based access control policies. It enables developers to model RBAC, ReBAC, and ABAC authorization patterns, manage authorization facts, and query permissions at runtime with sub-10ms latency and 99.99% availability.
examples:
- key_count: 5
  name: Delete_Facts
  slug: delete_facts
- key_count: 5
  name: Get_Policy_Metadata
  slug: get_policy_metadata
- key_count: 5
  name: Post_Actions
  slug: post_actions
- key_count: 5
  name: Post_Actions_Query
  slug: post_actions_query
- key_count: 5
  name: Post_Authorize
  slug: post_authorize
- key_count: 5
  name: Post_Authorize_Query
  slug: post_authorize_query
- key_count: 5
  name: Post_Batch
  slug: post_batch
- key_count: 5
  name: Post_Evaluate_Query
  slug: post_evaluate_query
- key_count: 5
  name: Post_Evaluate_Query_Local
  slug: post_evaluate_query_local
- key_count: 5
  name: Post_Facts
  slug: post_facts
- key_count: 5
  name: Post_List
  slug: post_list
- key_count: 5
  name: Post_List_Query
  slug: post_list_query
- key_count: 5
  name: Post_Policy
  slug: post_policy
finops:
- name: Oso Finops
  service_category: ''
  slug: oso-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oso.png
json_schemas:
- name: ActionsQuery
  property_count: 5
  slug: ActionsQuery
- name: ActionsResult
  property_count: 1
  slug: ActionsResult
- name: ApiError
  property_count: 1
  slug: ApiError
- name: ApiResult
  property_count: 1
  slug: ApiResult
- name: AuthorizeQuery
  property_count: 6
  slug: AuthorizeQuery
- name: AuthorizeResourcesQuery
  property_count: 5
  slug: AuthorizeResourcesQuery
- name: AuthorizeResourcesResult
  property_count: 1
  slug: AuthorizeResourcesResult
- name: AuthorizeResult
  property_count: 1
  slug: AuthorizeResult
- name: Bulk
  property_count: 2
  slug: Bulk
- name: ConcreteFact
  property_count: 2
  slug: ConcreteFact
- name: Constraint
  property_count: 2
  slug: Constraint
- name: Fact
  property_count: 2
  slug: Fact
- name: FactChangeset
  property_count: 0
  slug: FactChangeset
- name: GetPolicyMetadataResult
  property_count: 1
  slug: GetPolicyMetadataResult
- name: GetPolicyResult
  property_count: 1
  slug: GetPolicyResult
- name: ListQuery
  property_count: 7
  slug: ListQuery
- name: ListResult
  property_count: 2
  slug: ListResult
- name: LocalActionsQuery
  property_count: 2
  slug: LocalActionsQuery
- name: LocalActionsResult
  property_count: 1
  slug: LocalActionsResult
- name: LocalAuthQuery
  property_count: 2
  slug: LocalAuthQuery
- name: LocalAuthResult
  property_count: 1
  slug: LocalAuthResult
- name: LocalListQuery
  property_count: 3
  slug: LocalListQuery
- name: LocalListResult
  property_count: 1
  slug: LocalListResult
- name: LocalQuery
  property_count: 3
  slug: LocalQuery
- name: LocalQueryMode
  property_count: 0
  slug: LocalQueryMode
- name: LocalQueryResult
  property_count: 1
  slug: LocalQueryResult
- name: Policy
  property_count: 2
  slug: Policy
- name: PolicyError
  property_count: 2
  slug: PolicyError
- name: PolicyFailure
  property_count: 0
  slug: PolicyFailure
- name: PolicyMetadata
  property_count: 1
  slug: PolicyMetadata
- name: PolicyTestResult
  property_count: 3
  slug: PolicyTestResult
- name: Query
  property_count: 4
  slug: Query
- name: QueryDeprecated
  property_count: 2
  slug: QueryDeprecated
- name: QueryResult
  property_count: 1
  slug: QueryResult
- name: QueryResultDeprecated
  property_count: 1
  slug: QueryResultDeprecated
- name: ResourceBlockData
  property_count: 3
  slug: ResourceBlockData
- name: SavePolicyError
  property_count: 0
  slug: SavePolicyError
- name: TestSummary
  property_count: 3
  slug: TestSummary
- name: TypedId
  property_count: 2
  slug: TypedId
- name: Value
  property_count: 2
  slug: Value
jsonld:
- class_count: 0
  name: Oso Context
  property_count: 41
  slug: oso-context
layout: provider
modified: '2026-06-13'
name: Oso Cloud
nav: Providers
network: true
overview: 'Oso Cloud publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Centralized Authorization Data API, Check API API, Local Check API API, and 1 more. Tagged areas include Authorization, Access Control, RBAC, ReBAC, and ABAC.


  The Oso Cloud catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Oso Cloud''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 11 more developer resources.'
plans:
- name: Oso Plans Pricing
  plan_count: 4
  slug: oso-plans-pricing
random_paper: 97
rate_limits:
- limit_count: 3
  name: Oso Rate Limits
  slug: oso-rate-limits
rules:
- name: Oso Cloud API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: oso-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.1
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 55.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 33.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oso/refs/heads/main/screenshots/oso-2026-06-20T191220.png
security:
- kind: authentication
  name: Oso Authentication
  slug: oso-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Oso Domain Security
  slug: oso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Oso Trust Center
  slug: oso-trust-center
  summary_line: SOC 2
slug: oso
tags:
- Authorization
- Access Control
- RBAC
- ReBAC
- ABAC
- Permissions
- Policy
- Security
- Identity
website: https://www.osohq.com
---
