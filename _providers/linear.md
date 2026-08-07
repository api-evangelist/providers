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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Linear Agentic Access
  operation_count: 2
  slug: linear-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 3
apis:
- description: Linear webhooks deliver HTTP push notifications whenever data is created, updated, or removed. Webhooks are organization-scoped and can be configured for all public teams or a single team, enabling in
  name: Linear Webhooks API
  slug: linear-webhooks-api
- description: File upload for issue and comment attachments
  name: linear Attachments API
  slug: linear-attachments-api
- description: Core GraphQL query and mutation endpoint
  name: linear GraphQL API
  slug: linear-graphql-api
artifact_total: 26
asyncapis:
- description: Linear webhooks deliver HTTP push notifications whenever data is created, updated, or removed. Webhooks are organization-scoped and can be configured for all public teams or a single team, enabling in
  name: Linear Webhooks API
  slug: linear-webhooks-asyncapi
collections:
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
name: linear
nav: Providers
network: true
overview: 'linear publishes 3 APIs on the [APIs.io](https://apis.io/) network: Webhooks API, Attachments API, and GraphQL API.


  The linear catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  linear''s developer surface includes authentication, engineering blog, and 5 more developer resources.'
plans:
- name: Linear Plans Pricing
  plan_count: 4
  slug: linear-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 3
  name: Linear Rate Limits
  slug: linear-rate-limits
rules:
- name: linear API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: linear-asyncapi-spectral-rules
- name: linear API Rules
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
  composite: 48.1
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 83.8
    developer_ergonomics: 13.0
    discoverability: 59.3
    governance: 41.7
    operational_transparency: 31.6
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
