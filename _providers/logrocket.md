---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Logrocket Agentic Access
  operation_count: 5
  slug: logrocket-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.logrocket.com/v1
  baseurl_source: declared
  description: Retrieve exported session data files from storage buckets.
  name: LogRocket Data Export API
  slug: logrocket-data-export-api
- baseURL: https://api.logrocket.com/v1
  baseurl_source: declared
  description: Access Galileo AI-generated session highlights and summaries.
  name: LogRocket Highlights API
  slug: logrocket-highlights-api
- baseURL: https://api.logrocket.com/v1
  baseurl_source: declared
  description: Manage user identification and traits for session context.
  name: LogRocket Users API
  slug: logrocket-users-api
- baseURL: https://api.logrocket.com
  baseurl_source: declared
  description: GraphQL endpoint for querying session replay and analytics data.
  name: LogRocket Graph QL API
  slug: logrocket-graph-ql-api
artifact_total: 36
asyncapis:
- description: The LogRocket Galileo Highlights webhook delivers AI-generated session highlights to a customer-specified URL when processing completes. When a highlights request includes a webhookURL parameter, LogR
  name: LogRocket Galileo Highlights Webhook
  slug: logrocket-highlights-webhook-asyncapi
collections:
- collection_type: open
  name: LogRocket GraphQL Data Export API
  slug: open-logrocket-data-export-api
- collection_type: open
  name: LogRocket Data Export GraphQL API
  slug: open-logrocket-graphql-api
- collection_type: open
  name: LogRocket GraphQL Data Export Highlights API
  slug: open-logrocket-highlights-api
- collection_type: open
  name: LogRocket REST API
  slug: open-logrocket-rest-api
- collection_type: open
  name: LogRocket GraphQL Data Export Users API
  slug: open-logrocket-users-api
common:
- group: agent
  href: https://artifacts.apis.io/logrocket/agentic-access/logrocket-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/logrocket-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/logrocket/security/logrocket-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/logrocket-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/logrocket/security/logrocket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/logrocket-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/logrocket/authentication/logrocket-authentication.yml
  title: ''
  type: Authentication
  url: authentication/logrocket-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LogRocket
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/logrocket
- group: company
  title: ''
  type: Website
  url: https://logrocket.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.logrocket.com/reference
- group: commercial
  href: https://artifacts.apis.io/logrocket/plans/logrocket-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/logrocket-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/logrocket/rate-limits/logrocket-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/logrocket-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/logrocket/finops/logrocket-finops.yml
  title: ''
  type: FinOps
  url: finops/logrocket-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.logrocket.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.logrocket.com/feed/
created: '2026-05-08'
description: LogRocket is a session replay, product analytics, and frontend monitoring platform that captures user sessions, errors, and performance data.
finops:
- has_sources: true
  method: generated
  name: Logrocket Finops
  primary_unit: ''
  service_category: Observability
  slug: logrocket-finops
  template: false
graphqls:
- description: LogRocket GraphQL API for querying session, event, error, and analytics data with flexible field selection.
  name: LogRocket GraphQL API
  slug: logrocket-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logrocket.png
json_schemas:
- name: LogRocket Data Export Record
  property_count: 8
  slug: logrocket-data-export
- name: DataExportResponse
  property_count: 2
  slug: logrocket-dataexportresponse
- name: ExportedSession
  property_count: 1
  slug: logrocket-exportedsession
- name: GraphQLError
  property_count: 4
  slug: logrocket-graphqlerror
- name: GraphQLRequest
  property_count: 3
  slug: logrocket-graphqlrequest
- name: GraphQLResponse
  property_count: 2
  slug: logrocket-graphqlresponse
- name: HighlightsRequest
  property_count: 4
  slug: logrocket-highlightsrequest
- name: HighlightsResponse
  property_count: 4
  slug: logrocket-highlightsresponse
- name: HighlightsResult
  property_count: 2
  slug: logrocket-highlightsresult
- name: LogRocket Session
  property_count: 20
  slug: logrocket-session
- name: SessionHighlight
  property_count: 2
  slug: logrocket-sessionhighlight
- name: User
  property_count: 4
  slug: logrocket-user
- name: UserIdentificationRequest
  property_count: 3
  slug: logrocket-useridentificationrequest
json_structures:
- name: Logrocket Structure
  property_count: 0
  slug: logrocket-structure
jsonld:
- class_count: 0
  name: Logrocket Context
  property_count: 6
  slug: logrocket-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.logrocket.com over HTTP.
  name: LogRocket MCP Server
  slug: logrocket
modified: '2026-05-19'
name: LogRocket
nav: Providers
network: true
overview: 'LogRocket publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data Export API, Highlights API, Users API, and 1 more. Tagged areas include Session Replay, Product Analytics, Frontend Monitoring, Logging, and Errors.


  The LogRocket catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  LogRocket''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Logrocket Plans Pricing
  plan_count: 1
  slug: logrocket-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Logrocket Rate Limits
  slug: logrocket-rate-limits
rules:
- authorship: generated
  effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: LogRocket — asyncapi rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: logrocket-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: LogRocket — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: logrocket-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.2
  facets:
    access_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 62.1
    developer_ergonomics: 23.8
    discoverability: 66.7
    operational_transparency: 7.9
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/logrocket/logrocket-2026-06-20T184701.png
security:
- kind: authentication
  name: Logrocket Authentication
  slug: logrocket-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Logrocket Domain Security
  slug: logrocket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Logrocket Trust Center
  slug: logrocket-trust-center
  summary_line: SOC 2, GDPR
slug: logrocket
tags:
- Session Replay
- Product Analytics
- Frontend Monitoring
- Logging
- Errors
website: https://logrocket.com/
---
