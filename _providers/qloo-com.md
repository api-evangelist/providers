---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Qloo Com Agentic Access
  operation_count: 10
  slug: qloo-com-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- description: Qloo API provides cultural intelligence insights and recommendations via REST endpoints.
  name: Qloo API
  slug: qloo-api
- baseURL: https://api.qloo.com
  baseurl_source: spec
  description: Features for anaylzing and comparing entities.
  name: Qloo Analysis API
  slug: qloo-com-analysis-api
- baseURL: https://api.qloo.com
  baseurl_source: spec
  description: Segment and filter by audience groupings
  name: Qloo Audiences API
  slug: qloo-com-audiences-api
- baseURL: https://api.qloo.com
  baseurl_source: spec
  description: Retrieve entity data
  name: Qloo Entities API
  slug: qloo-com-entities-api
- baseURL: https://api.qloo.com
  baseurl_source: spec
  description: General API information
  name: Qloo Info API
  slug: qloo-com-info-api
- baseURL: https://api.qloo.com
  baseurl_source: spec
  description: Returns high-level insights across entities
  name: Qloo Insights API
  slug: qloo-com-insights-api
- baseURL: https://api.qloo.com
  baseurl_source: spec
  description: Search across entities
  name: Qloo Search API
  slug: qloo-com-search-api
- baseURL: https://api.qloo.com
  baseurl_source: spec
  description: Tag-based filtering and classification
  name: Qloo Tags API
  slug: qloo-com-tags-api
- baseURL: https://api.qloo.com
  baseurl_source: spec
  description: Features involving trend data
  name: Qloo Trends API
  slug: qloo-com-trends-api
artifact_total: 13
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qloo.com/reference/api-onboarding
- group: agent
  href: https://artifacts.apis.io/qloo-com/agentic-access/qloo-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/qloo-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/qloo-com/rules/qloo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/qloo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/qloo-com/vocabulary/qloo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/qloo-com-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/qloo-com/authentication/qloo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qloo-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/qloo-com/errors/qloo-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/qloo-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/qloo-com/conformance/qloo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qloo-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/qloo-com/hosts/qloo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qloo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/qloo-com/vendors/qloo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qloo-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qloo.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.qloo.com/company/press
- group: auth
  href: https://artifacts.apis.io/qloo-com/security/qloo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qloo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qloo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.qloo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qloo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qloo.com/reference
- group: operate
  title: ''
  type: Support
  url: https://www.qloo.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qloo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qloo.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qloo.com/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/qloo/workspace
coverage:
  checked: '2026-10-21'
  detail: Docs at https://docs.qloo.com/reference provide API information but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts are available.
  evidence:
  - status: 200
    url: https://docs.qloo.com/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Qloo provides an AI-driven cultural intelligence platform that aggregates and analyzes taste and preference data across categories to help businesses deliver personalized experiences. Leveraging a vast cultural graph, Qloo offers APIs for insights, audience segmentation, and recommendation services, enabling integration of cultural context into products, marketing, and user experiences. The platform serves sectors such as entertainment, travel, retail, and media, delivering data-driven recommendations and analytics to enhance engagement and decision-making.
layout: provider
modified: '2026-10-21'
name: Qloo
nav: Providers
network: true
overview: 'Qloo publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analysis API, Audiences API, Entities API, and 6 more. Tagged areas include Company, Artificial Intelligence, Cultural-Intelligence, Data Analytics, and Personalization.


  The Qloo catalog on APIs.io includes 1 Spectral governance ruleset.


  Qloo''s developer surface includes getting-started guide, authentication, documentation, API reference, support, and 16 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Qloo API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 3
  slug: qloo-com-rules
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 56.7
    developer_ergonomics: 35.7
    discoverability: 54.5
    operational_transparency: 10.5
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/qloo-com/qloo-com-2026-11-03T141750.png
security:
- kind: authentication
  name: Qloo Com Authentication
  slug: qloo-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Qloo Com Domain Security
  slug: qloo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qloo-com
tags:
- Company
- Artificial Intelligence
- Cultural-Intelligence
- Data Analytics
- Personalization
website: https://qloo.com/
---
