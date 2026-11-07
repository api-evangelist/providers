---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Surveymonkey Agentic Access
  operation_count: 30
  slug: surveymonkey-agentic-access
  summary_line: 30 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.surveymonkey.com/v3
  baseurl_source: declared
  description: The Collectors API from SurveyMonkey — 3 operation(s) for collectors.
  name: SurveyMonkey Collectors API
  slug: surveymonkey-collectors-api
- baseURL: https://api.surveymonkey.com/v3
  baseurl_source: declared
  description: The Contacts API from SurveyMonkey — 3 operation(s) for contacts.
  name: SurveyMonkey Contacts API
  slug: surveymonkey-contacts-api
- baseURL: https://api.surveymonkey.com/v3
  baseurl_source: declared
  description: The Groups API from SurveyMonkey — 4 operation(s) for groups.
  name: SurveyMonkey Groups API
  slug: surveymonkey-groups-api
- baseURL: https://api.surveymonkey.com/v3
  baseurl_source: declared
  description: The Responses API from SurveyMonkey — 4 operation(s) for responses.
  name: SurveyMonkey Responses API
  slug: surveymonkey-responses-api
- baseURL: https://api.surveymonkey.com/v3
  baseurl_source: declared
  description: The Survey Structure API from SurveyMonkey — 4 operation(s) for survey structure.
  name: SurveyMonkey Survey Structure API
  slug: surveymonkey-survey-structure-api
- baseURL: https://api.surveymonkey.com/v3
  baseurl_source: declared
  description: The Surveys API from SurveyMonkey — 3 operation(s) for surveys.
  name: SurveyMonkey Surveys API
  slug: surveymonkey-surveys-api
- baseURL: https://api.surveymonkey.com/v3
  baseurl_source: declared
  description: The Users API from SurveyMonkey — 3 operation(s) for users.
  name: SurveyMonkey Users API
  slug: surveymonkey-users-api
- baseURL: https://api.surveymonkey.com/v3
  baseurl_source: declared
  description: The Work Groups API from SurveyMonkey — 2 operation(s) for work groups.
  name: SurveyMonkey Work Groups API
  slug: surveymonkey-work-groups-api
artifact_total: 28
asyncapis:
- description: AsyncAPI 2.6 description of the SurveyMonkey v3 webhook surface. SurveyMonkey delivers events as HTTP POST requests to a `subscription_url` that the consumer registers via the REST endpoint `POST /v3/
  name: SurveyMonkey Webhooks
  slug: surveymonkey-asyncapi
collections:
- collection_type: open
  name: SurveyMonkey API v3 Collectors API
  slug: open-surveymonkey-collectors-api
- collection_type: open
  name: SurveyMonkey API v3 Collectors Contacts API
  slug: open-surveymonkey-contacts-api
- collection_type: open
  name: SurveyMonkey API v3 Collectors Groups API
  slug: open-surveymonkey-groups-api
- collection_type: open
  name: SurveyMonkey API v3 Collectors Responses API
  slug: open-surveymonkey-responses-api
- collection_type: open
  name: SurveyMonkey API v3 Collectors Survey Structure API
  slug: open-surveymonkey-survey-structure-api
- collection_type: open
  name: SurveyMonkey API v3 Collectors Surveys API
  slug: open-surveymonkey-surveys-api
- collection_type: open
  name: SurveyMonkey API v3 Collectors Users API
  slug: open-surveymonkey-users-api
- collection_type: open
  name: SurveyMonkey API v3 Collectors Workgroups API
  slug: open-surveymonkey-workgroups-api
- collection_type: open
  name: SurveyMonkey API v3
  slug: open-surveymonkey
common:
- group: commercial
  href: https://artifacts.apis.io/surveymonkey/plans/surveymonkey-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/surveymonkey-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/surveymonkey/rate-limits/surveymonkey-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/surveymonkey-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/surveymonkey/finops/surveymonkey-finops.yml
  title: ''
  type: FinOps
  url: finops/surveymonkey-finops.yml
- group: other
  href: https://artifacts.apis.io/surveymonkey/capabilities/surveymonkey-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/surveymonkey-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://surveymonkey.com
- group: agent
  href: https://artifacts.apis.io/surveymonkey/agentic-access/surveymonkey-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/surveymonkey-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/surveymonkey/security/surveymonkey-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/surveymonkey-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/surveymonkey/security/surveymonkey-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/surveymonkey-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/surveymonkey/authentication/surveymonkey-authentication.yml
  title: ''
  type: Authentication
  url: authentication/surveymonkey-authentication.yml
- group: auth
  href: https://artifacts.apis.io/surveymonkey/scopes/surveymonkey-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/surveymonkey-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://www.surveymonkey.com/feed/
created: '2026-05-08'
description: SurveyMonkey is a leading surveys and feedback platform. The SurveyMonkey API v3 is a REST API exposing surveys, pages, questions, collectors, contacts, responses, webhooks, users, teams, groups and benchmarks. Authenticated via OAuth 2.0 with scoped permissions.
finops:
- has_sources: true
  method: generated
  name: Surveymonkey Finops
  primary_unit: user-month / response
  service_category: Surveys / Feedback
  slug: surveymonkey-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/surveymonkey.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.surveymonkey.com over HTTP.
  name: SurveyMonkey MCP Server
  slug: surveymonkey
modified: '2026-09-16'
name: SurveyMonkey
nav: Providers
network: true
overview: 'SurveyMonkey publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Collectors API, Contacts API, Groups API, and 5 more. Tagged areas include Surveys, Market Research, Feedback, NPS, and Forms.


  The SurveyMonkey catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  SurveyMonkey''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: Surveymonkey Plans Pricing
  plan_count: 5
  slug: surveymonkey-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Surveymonkey Rate Limits
  slug: surveymonkey-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: SurveyMonkey — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: surveymonkey-asyncapi-spectral-rules
scopes:
- name: Surveymonkey Scopes
  scope_count: 7
  slug: surveymonkey-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 11.4
    contract_quality: 52.8
    developer_ergonomics: 31.0
    discoverability: 68.3
    operational_transparency: 15.8
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/surveymonkey/surveymonkey-2026-06-20T194739.png
security:
- kind: authentication
  name: Surveymonkey Authentication
  slug: surveymonkey-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Surveymonkey Domain Security
  slug: surveymonkey-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Surveymonkey Trust Center
  slug: surveymonkey-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, GDPR
slug: surveymonkey
tags:
- Surveys
- Market Research
- Feedback
- NPS
- Forms
- OAuth
- Authentication
website: https://surveymonkey.com
---
