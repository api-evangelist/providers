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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Aserto Agentic Access
  operation_count: 36
  slug: aserto-agentic-access
  summary_line: 36 operations · 21 acting
api_count: 3
apis:
- baseURL: https://console.aserto.com
  baseurl_source: declared
  description: 'Collects and surfaces a complete audit trail of authorization decisions made by connected Authorizer instances. Supports compliance, debugging, and analytics use cases by recording who was authorized '
  name: Aserto Decision Logs API
  slug: aserto-decision-logs-api
- description: Management API for the Aserto SaaS control plane (wound down May 2025, succeeded by the open-source Topaz project). Provided lifecycle management of policies, Edge Authorizer instances, tenants, and c
  name: Aserto Control Plane API
  slug: aserto-control-plane-api
- baseURL: https://authorizer.prod.aserto.com
  baseurl_source: declared
  description: The Authorizer API from Aserto — 4 operation(s) for authorizer.
  name: Aserto Authorizer API
  slug: aserto-authorizer-api
- baseURL: https://authorizer.prod.aserto.com
  baseurl_source: declared
  description: The authzen API from Aserto — 5 operation(s) for authzen.
  name: Aserto authzen API
  slug: aserto-authzen-api
- baseURL: https://authorizer.prod.aserto.com
  baseurl_source: declared
  description: The decision_logs API from Aserto — 6 operation(s) for decision_logs.
  name: Aserto decision_logs API
  slug: aserto-decision-logs-api
- baseURL: https://authorizer.prod.aserto.com
  baseurl_source: declared
  description: The directory API from Aserto — 14 operation(s) for directory.
  name: Aserto directory API
  slug: aserto-directory-api
- baseURL: https://authorizer.prod.aserto.com
  baseurl_source: declared
  description: The Info API from Aserto — 1 operation(s) for info.
  name: Aserto Info API
  slug: aserto-info-api
- baseURL: https://authorizer.prod.aserto.com
  baseurl_source: declared
  description: The Policy API from Aserto — 2 operation(s) for policy.
  name: Aserto Policy API
  slug: aserto-policy-api
artifact_total: 133
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: aserto//v2/.proto Authorizer API
  slug: open-aserto-authorizer-api
- collection_type: open
  name: aserto//v2/.proto Authorizer authzen API
  slug: open-aserto-authzen-api
- collection_type: open
  name: aserto//v2/.proto Authorizer decision_logs API
  slug: open-aserto-decision-logs-api
- collection_type: open
  name: aserto//v2/.proto Authorizer directory API
  slug: open-aserto-directory-api
- collection_type: open
  name: aserto//v2/.proto Authorizer Info API
  slug: open-aserto-info-api
- collection_type: open
  name: aserto//v2/.proto Authorizer Policy API
  slug: open-aserto-policy-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aserto-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aserto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aserto-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.aserto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aserto.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/aserto-dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aserto-com
- group: other
  title: ''
  type: X
  url: https://x.com/aserto_com
- group: company
  title: ''
  type: Blog
  url: https://www.aserto.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aserto.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aserto.com
- group: commercial
  title: ''
  type: Plans
  url: plans/aserto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aserto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aserto-finops.yml
created: '2026-06-13'
description: Aserto is a cloud-native authorization platform providing fine-grained, policy-based access control for applications and APIs. Built on Open Policy Agent (OPA) and a Google Zanzibar-inspired directory, Aserto exposes REST and gRPC APIs for the Authorizer (real-time authorization decisions), Directory (managing users, groups, objects, and relations), and Decision Logs (audit trails of authorization events). The open-source Topaz engine carries the technology forward after the commercial SaaS control plane was wound down in May 2025.
examples:
- key_count: 4
  name: Aserto Authorizer Examples
  slug: aserto-authorizer-examples
- key_count: 4
  name: Aserto Decision Logs Examples
  slug: aserto-decision-logs-examples
- key_count: 5
  name: Aserto Directory Examples
  slug: aserto-directory-examples
finops:
- name: Aserto Finops
  service_category: ''
  slug: aserto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aserto.png
json_schemas:
- name: apiIdentityContext
  property_count: 2
  slug: aserto-authorizer-apiidentitycontext
- name: apiIdentityType
  property_count: 0
  slug: aserto-authorizer-apiidentitytype
- name: apiModule
  property_count: 5
  slug: aserto-authorizer-apimodule
- name: apiPolicyContext
  property_count: 2
  slug: aserto-authorizer-apipolicycontext
- name: apiPolicyInstance
  property_count: 2
  slug: aserto-authorizer-apipolicyinstance
- name: authorizerv2Decision
  property_count: 2
  slug: aserto-authorizer-authorizerv2decision
- name: protobufAny
  property_count: 1
  slug: aserto-authorizer-protobufany
- name: protobufNullValue
  property_count: 0
  slug: aserto-authorizer-protobufnullvalue
- name: rpcStatus
  property_count: 3
  slug: aserto-authorizer-rpcstatus
- name: v2CompileRequest
  property_count: 9
  slug: aserto-authorizer-v2compilerequest
- name: v2CompileResponse
  property_count: 4
  slug: aserto-authorizer-v2compileresponse
- name: v2DecisionTreeOptions
  property_count: 1
  slug: aserto-authorizer-v2decisiontreeoptions
- name: v2DecisionTreeRequest
  property_count: 5
  slug: aserto-authorizer-v2decisiontreerequest
- name: v2DecisionTreeResponse
  property_count: 2
  slug: aserto-authorizer-v2decisiontreeresponse
- name: v2GetPolicyResponse
  property_count: 1
  slug: aserto-authorizer-v2getpolicyresponse
- name: v2InfoResponse
  property_count: 5
  slug: aserto-authorizer-v2inforesponse
- name: v2IsRequest
  property_count: 4
  slug: aserto-authorizer-v2isrequest
- name: v2IsResponse
  property_count: 1
  slug: aserto-authorizer-v2isresponse
- name: v2ListPoliciesResponse
  property_count: 1
  slug: aserto-authorizer-v2listpoliciesresponse
- name: "- PATH_SEPARATOR_UNKNOWN: Value not set.\n - PATH_SEPARATOR_DOT: Dot \".\" path separator\n - PATH_SEPARATOR_SLASH: Slash \"/\" path separtor"
  property_count: 0
  slug: aserto-authorizer-v2pathseparator
- name: v2QueryOptions
  property_count: 4
  slug: aserto-authorizer-v2queryoptions
- name: v2QueryRequest
  property_count: 7
  slug: aserto-authorizer-v2queryrequest
- name: v2QueryResponse
  property_count: 4
  slug: aserto-authorizer-v2queryresponse
- name: "- TRACE_LEVEL_UNKNOWN: Value not set.\n - TRACE_LEVEL_OFF: ExplainOffV1   ExplainModeV1 = \"off\"\n - TRACE_LEVEL_FULL: ExplainFullV1  ExplainModeV1 = \"full\"\n - TRACE_LEVEL_NOTES: ExplainNotesV1 ExplainModeV1 = \"notes\"\n - TRACE_LEVEL_FAILS: ExplainFailsV1 ExplainModeV1 = \"fails\""
  property_count: 0
  slug: aserto-authorizer-v2tracelevel
- name: protobufAny
  property_count: 2
  slug: aserto-decision-logs-protobufany
- name: protobufNullValue
  property_count: 0
  slug: aserto-decision-logs-protobufnullvalue
- name: rpcStatus
  property_count: 3
  slug: aserto-decision-logs-rpcstatus
- name: represents a decision that an authorizer performed in the past
  property_count: 9
  slug: aserto-decision-logs-v2decision
- name: v2DecisionLog
  property_count: 1
  slug: aserto-decision-logs-v2decisionlog
- name: v2DecisionLogItem
  property_count: 1
  slug: aserto-decision-logs-v2decisionlogitem
- name: information about a policy used in a decision
  property_count: 6
  slug: aserto-decision-logs-v2decisionpolicy
- name: information about a user on behalf of whom a decision was made
  property_count: 3
  slug: aserto-decision-logs-v2decisionuser
- name: v2ExecuteQueryRequest
  property_count: 4
  slug: aserto-decision-logs-v2executequeryrequest
- name: v2ExecuteQueryResponse
  property_count: 2
  slug: aserto-decision-logs-v2executequeryresponse
- name: v2GetDecisionLogResponse
  property_count: 1
  slug: aserto-decision-logs-v2getdecisionlogresponse
- name: v2GetDecisionsResponse
  property_count: 1
  slug: aserto-decision-logs-v2getdecisionsresponse
- name: v2GetUserResponse
  property_count: 1
  slug: aserto-decision-logs-v2getuserresponse
- name: v2IdentityContext
  property_count: 2
  slug: aserto-decision-logs-v2identitycontext
- name: v2IdentityType
  property_count: 0
  slug: aserto-decision-logs-v2identitytype
- name: v2ListDecisionLogsResponse
  property_count: 2
  slug: aserto-decision-logs-v2listdecisionlogsresponse
- name: v2ListUsersResponse
  property_count: 2
  slug: aserto-decision-logs-v2listusersresponse
- name: v2PaginationRequest
  property_count: 2
  slug: aserto-decision-logs-v2paginationrequest
- name: v2PaginationResponse
  property_count: 3
  slug: aserto-decision-logs-v2paginationresponse
- name: v2PolicyContext
  property_count: 2
  slug: aserto-decision-logs-v2policycontext
- name: v2PolicyInstance
  property_count: 2
  slug: aserto-decision-logs-v2policyinstance
- name: v2Result
  property_count: 2
  slug: aserto-decision-logs-v2result
- name: v2User
  property_count: 1
  slug: aserto-decision-logs-v2user
- name: v2UserItem
  property_count: 2
  slug: aserto-decision-logs-v2useritem
- name: protobufAny
  property_count: 1
  slug: aserto-directory-protobufany
- name: protobufNullValue
  property_count: 0
  slug: aserto-directory-protobufnullvalue
- name: rpcStatus
  property_count: 3
  slug: aserto-directory-rpcstatus
- name: https://openid.github.io/authzen/#name-action
  property_count: 2
  slug: aserto-directory-v1action
- name: https://openid.github.io/authzen/#name-the-action-search-api-reque
  property_count: 5
  slug: aserto-directory-v1actionsearchrequest
- name: https://openid.github.io/authzen/#name-the-action-search-api-respo
  property_count: 2
  slug: aserto-directory-v1actionsearchresponse
- name: https://openid.github.io/authzen/#name-the-access-evaluation-api-r
  property_count: 4
  slug: aserto-directory-v1evaluationrequest
- name: https://openid.github.io/authzen/#name-the-access-evaluation-api-re
  property_count: 2
  slug: aserto-directory-v1evaluationresponse
- name: https://openid.github.io/authzen/#name-the-access-evaluations-api-
  property_count: 6
  slug: aserto-directory-v1evaluationsrequest
- name: https://openid.github.io/authzen/#name-access-evaluations-api-resp
  property_count: 1
  slug: aserto-directory-v1evaluationsresponse
- name: v1Page
  property_count: 1
  slug: aserto-directory-v1page
- name: https://openid.github.io/authzen/#name-resource
  property_count: 3
  slug: aserto-directory-v1resource
- name: https://openid.github.io/authzen/#name-the-resource-search-api-req
  property_count: 5
  slug: aserto-directory-v1resourcesearchrequest
- name: https://openid.github.io/authzen/#name-the-resource-search-api-res
  property_count: 2
  slug: aserto-directory-v1resourcesearchresponse
- name: https://openid.github.io/authzen/#name-subject
  property_count: 3
  slug: aserto-directory-v1subject
- name: https://openid.github.io/authzen/#name-the-subject-search-api-requ
  property_count: 5
  slug: aserto-directory-v1subjectsearchrequest
- name: https://openid.github.io/authzen/#name-the-subject-search-api-resp
  property_count: 2
  slug: aserto-directory-v1subjectsearchresponse
- name: v3Assert
  property_count: 6
  slug: aserto-directory-v3assert
- name: v3Body
  property_count: 1
  slug: aserto-directory-v3body
- name: v3CheckPermissionRequest
  property_count: 6
  slug: aserto-directory-v3checkpermissionrequest
- name: v3CheckPermissionResponse
  property_count: 2
  slug: aserto-directory-v3checkpermissionresponse
- name: v3CheckRelationRequest
  property_count: 6
  slug: aserto-directory-v3checkrelationrequest
- name: v3CheckRelationResponse
  property_count: 2
  slug: aserto-directory-v3checkrelationresponse
- name: v3CheckRequest
  property_count: 6
  slug: aserto-directory-v3checkrequest
- name: v3CheckResponse
  property_count: 3
  slug: aserto-directory-v3checkresponse
- name: EXPERIMENTAL
  property_count: 2
  slug: aserto-directory-v3checksrequest
- name: EXPERIMENTAL
  property_count: 1
  slug: aserto-directory-v3checksresponse
- name: v3DeleteAssertionResponse
  property_count: 1
  slug: aserto-directory-v3deleteassertionresponse
- name: v3DeleteManifestResponse
  property_count: 1
  slug: aserto-directory-v3deletemanifestresponse
- name: v3DeleteObjectResponse
  property_count: 1
  slug: aserto-directory-v3deleteobjectresponse
- name: v3DeleteRelationResponse
  property_count: 1
  slug: aserto-directory-v3deleterelationresponse
- name: v3ExportResponse
  property_count: 3
  slug: aserto-directory-v3exportresponse
- name: v3GetAssertionResponse
  property_count: 1
  slug: aserto-directory-v3getassertionresponse
- name: v3GetGraphResponse
  property_count: 3
  slug: aserto-directory-v3getgraphresponse
- name: v3GetManifestResponse
  property_count: 3
  slug: aserto-directory-v3getmanifestresponse
- name: v3GetObjectManyResponse
  property_count: 1
  slug: aserto-directory-v3getobjectmanyresponse
- name: v3GetObjectResponse
  property_count: 3
  slug: aserto-directory-v3getobjectresponse
- name: v3GetObjectsResponse
  property_count: 2
  slug: aserto-directory-v3getobjectsresponse
- name: v3GetRelationResponse
  property_count: 2
  slug: aserto-directory-v3getrelationresponse
- name: v3GetRelationsResponse
  property_count: 3
  slug: aserto-directory-v3getrelationsresponse
- name: v3ImportCounter
  property_count: 5
  slug: aserto-directory-v3importcounter
- name: v3ImportRequest
  property_count: 3
  slug: aserto-directory-v3importrequest
- name: v3ImportResponse
  property_count: 4
  slug: aserto-directory-v3importresponse
- name: v3ImportStatus
  property_count: 3
  slug: aserto-directory-v3importstatus
- name: v3ListAssertionsResponse
  property_count: 2
  slug: aserto-directory-v3listassertionsresponse
- name: v3Metadata
  property_count: 2
  slug: aserto-directory-v3metadata
- name: v3Object
  property_count: 7
  slug: aserto-directory-v3object
- name: Object identifier
  property_count: 2
  slug: aserto-directory-v3objectidentifier
- name: v3Opcode
  property_count: 0
  slug: aserto-directory-v3opcode
- name: Pagination request
  property_count: 2
  slug: aserto-directory-v3paginationrequest
- name: Pagination response
  property_count: 1
  slug: aserto-directory-v3paginationresponse
- name: v3Relation
  property_count: 9
  slug: aserto-directory-v3relation
- name: v3SetAssertionRequest
  property_count: 1
  slug: aserto-directory-v3setassertionrequest
- name: v3SetAssertionResponse
  property_count: 1
  slug: aserto-directory-v3setassertionresponse
- name: v3SetManifestResponse
  property_count: 1
  slug: aserto-directory-v3setmanifestresponse
- name: v3SetObjectRequest
  property_count: 1
  slug: aserto-directory-v3setobjectrequest
- name: v3SetObjectResponse
  property_count: 1
  slug: aserto-directory-v3setobjectresponse
- name: v3SetRelationRequest
  property_count: 1
  slug: aserto-directory-v3setrelationrequest
- name: v3SetRelationResponse
  property_count: 1
  slug: aserto-directory-v3setrelationresponse
jsonld:
- class_count: 52
  name: Aserto Context
  property_count: 3
  slug: aserto-context
layout: provider
modified: '2026-06-13'
name: Aserto
nav: Providers
network: true
overview: 'Aserto publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Decision Logs API, Authorizer API, authzen API, and 4 more. Tagged areas include Authorization, Fine-Grained Access Control, RBAC, ABAC, and ReBAC.


  The Aserto catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aserto''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Aserto Plans Pricing
  plan_count: 3
  slug: aserto-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Aserto Rate Limits
  slug: aserto-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Aserto API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aserto-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 66.3
    catalog_earned_first_party: 0.0
    catalog_gap: 48.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 54.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aserto/refs/heads/main/screenshots/aserto-2026-06-20T172456.png
security:
- kind: authentication
  name: Aserto Authentication
  slug: aserto-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Aserto Domain Security
  slug: aserto-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aserto
tags:
- Authorization
- Fine-Grained Access Control
- RBAC
- ABAC
- ReBAC
- Policy
- Open Policy Agent
- OPA
- Cloud-Native
- Security
website: https://www.aserto.com/
---
