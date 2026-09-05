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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Linear Agentic Access
  operation_count: 2
  slug: linear-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: Linear webhooks deliver HTTP push notifications whenever data is created, updated, or removed. Webhooks are organization-scoped and can be configured for all public teams or a single team, enabling in
  name: Linear Webhooks API
  slug: linear-webhooks-api
- baseURL: https://api.linear.app/graphql
  baseurl_source: declared
  description: File upload for issue and comment attachments
  name: linear Attachments API
  slug: linear-attachments-api
- baseURL: https://api.linear.app/graphql
  baseurl_source: declared
  description: Core GraphQL query and mutation endpoint
  name: linear GraphQL API
  slug: linear-graphql-api
artifact_total: 29
asyncapis:
- description: Linear webhooks deliver HTTP push notifications whenever data is created, updated, or removed. Webhooks are organization-scoped and can be configured for all public teams or a single team, enabling in
  name: Linear Webhooks API
  slug: linear-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Linear GraphQL Attachments API
  slug: open-linear-attachments-api
- collection_type: open
  name: Linear Attachments GraphQL API
  slug: open-linear-graphql-api
- collection_type: open
  name: Linear GraphQL API
  slug: open-linear-graphql
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/linear-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/linear-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/linear-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linear-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linear-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/linear-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://linear.app/rss/now.xml
description: Linear's public API is built using GraphQL. It's the same API we use internally for developing our applications. If you are new to GraphQL, Apollo has resources for beginners. The official GraphQL documentation is another good starting point.
examples:
- key_count: 6
  name: Linear Executegraphqlquery Example
  slug: linear-executegraphqlquery-example
finops:
- name: Linear Finops
  service_category: Issue Tracking
  slug: linear-finops
graphqls:
- description: Linear's public GraphQL API provides full access to create, read, update, and query issues, projects, cycles, roadmaps, and teams. It is the same API Linear uses internally for its own applications, s
  name: linear GraphQL API
  slug: linear-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linear.png
json_schemas:
- name: ErrorResponse
  property_count: 2
  slug: linear-errorresponse
- name: FileUploadResponse
  property_count: 3
  slug: linear-fileuploadresponse
- name: GraphQLError
  property_count: 4
  slug: linear-graphqlerror
- name: GraphQLRequest
  property_count: 3
  slug: linear-graphqlrequest
- name: GraphQLResponse
  property_count: 2
  slug: linear-graphqlresponse
- name: Linear Issue
  property_count: 23
  slug: linear-issue
json_structures:
- name: Linear Structure
  property_count: 0
  slug: linear-structure
jsonld:
- class_count: 17
  name: Linear Context
  property_count: 11
  slug: linear-context
layout: provider
modified: '2026-05-19'
name: Linear
nav: Providers
network: true
overview: 'Linear publishes 3 APIs on the [APIs.io](https://apis.io/) network: Webhooks API, Attachments API, and GraphQL API.


  The Linear catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Linear''s developer surface includes authentication, engineering blog, and 5 more developer resources.'
plans:
- name: Linear Plans Pricing
  plan_count: 4
  slug: linear-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Linear Rate Limits
  slug: linear-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Linear API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: linear-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Linear API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: linear-jsonschema-spectral-rules
scopes:
- name: Linear Scopes
  scope_count: 4
  slug: linear-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 59.5
    catalog_earned_first_party: 0.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 73.8
    developer_ergonomics: 42.9
    discoverability: 61.1
    governance: 13.6
    operational_transparency: 15.8
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linear/refs/heads/main/screenshots/linear-2026-06-20T184541.png
security:
- kind: authentication
  name: Linear Authentication
  slug: linear-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Linear Domain Security
  slug: linear-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Linear Vulnerability Disclosure
  slug: linear-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Linear Trust Center
  slug: linear-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: linear
---
