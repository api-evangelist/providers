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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Hotjar Agentic Access
  operation_count: 5
  slug: hotjar-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 7
apis:
- description: The Hotjar Events API is a client-side JavaScript API that allows developers to send custom events to Hotjar when specific actions take place on a website. These events can be used to filter collected
  name: Hotjar Events API
  slug: events-api
- description: The Hotjar Identify API is a client-side JavaScript API that allows developers to pass user data to Hotjar, saving it as User Attributes. These attributes enable advanced filtering and segmentation of
  name: Hotjar Identify API
  slug: identify-api
- description: The Hotjar JavaScript SDK (@hotjar/browser) is an npm package that provides a programmatic interface for integrating Hotjar directly into JavaScript applications. It allows developers to initialize Ho
  name: Hotjar JavaScript SDK
  slug: javascript-sdk
- description: OAuth 2.0 client credentials authentication endpoints for obtaining access tokens.
  name: hotjar Authentication API
  slug: hotjar-authentication-api
- description: Endpoints for exporting and listing survey response data with cursor-based pagination.
  name: hotjar Survey Responses API
  slug: hotjar-survey-responses-api
- description: Endpoints for listing surveys and retrieving survey details for a specific site.
  name: hotjar Surveys API
  slug: hotjar-surveys-api
- description: Endpoints for looking up user data and submitting deletion requests for GDPR compliance.
  name: hotjar User Lookup API
  slug: hotjar-user-lookup-api
artifact_total: 46
collections:
- collection_type: open
  name: Hotjar REST API
  slug: open-hotjar-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hotjar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hotjar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hotjar-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hotjar
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hotjar-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hotjar-survey-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hotjar-survey-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hotjar-user-lookup-schema.json
description: Hotjar is a behavior analytics and user feedback platform that helps businesses understand how users interact with their website through heatmaps, session recordings, surveys, and feedback widgets.
features:
- 'Free: 5,000 monthly sessions on new Contentsquare platform'
- 'Growth: $49/month annual'
- Legacy Observe Plus $32/mo (100 daily sessions)
- Legacy Observe Business $80/mo (500 daily sessions)
- Legacy Observe Scale $171/mo
- 'Pro / Enterprise: custom pricing'
- Heatmaps (click, scroll, move)
- Session replay (anonymized)
- Surveys and feedback widgets
- Funnels and conversion tracking
- Engage product for moderated user interviews
- Insights API at insights.hotjar.com
- OAuth + API tokens
- Webhooks via Insights
- Privacy controls (PII masking, IP suppression)
- Migration to unified Contentsquare platform through 2026
finops:
- name: Hotjar Finops
  service_category: Digital Experience
  slug: hotjar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hotjar.png
json_schemas:
- name: Error
  property_count: 2
  slug: hotjar-error
- name: OAuthToken
  property_count: 3
  slug: hotjar-oauthtoken
- name: Hotjar Survey Response
  property_count: 4
  slug: hotjar-survey-response
- name: Hotjar Survey
  property_count: 9
  slug: hotjar-survey
- name: SurveyAnswer
  property_count: 2
  slug: hotjar-surveyanswer
- name: SurveyListResponse
  property_count: 2
  slug: hotjar-surveylistresponse
- name: SurveyQuestion
  property_count: 7
  slug: hotjar-surveyquestion
- name: SurveyResponse
  property_count: 4
  slug: hotjar-surveyresponse
- name: SurveyResponseListResponse
  property_count: 2
  slug: hotjar-surveyresponselistresponse
- name: SurveyResponseTag
  property_count: 1
  slug: hotjar-surveyresponsetag
- name: Hotjar User Lookup Request
  property_count: 3
  slug: hotjar-user-lookup
- name: UserLookupRequest
  property_count: 3
  slug: hotjar-userlookuprequest
- name: UserLookupResponse
  property_count: 2
  slug: hotjar-userlookupresponse
json_structures:
- name: Hotjar Structure
  property_count: 0
  slug: hotjar-structure
jsonld:
- class_count: 0
  name: Hotjar Context
  property_count: 7
  slug: hotjar-context
layout: provider
modified: '2026-05-19'
name: hotjar
nav: Providers
network: true
overview: 'hotjar publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Survey Responses API, Surveys API, and 1 more.


  The hotjar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  hotjar''s developer surface includes authentication and 7 more developer resources.'
plans:
- name: Hotjar Plans Pricing
  plan_count: 6
  slug: hotjar-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 2
  name: Hotjar Rate Limits
  slug: hotjar-rate-limits
rules:
- name: hotjar API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: hotjar-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.6
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 66.4
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hotjar/refs/heads/main/screenshots/hotjar-2026-06-20T182845.png
security:
- kind: authentication
  name: Hotjar Authentication
  slug: hotjar-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hotjar Domain Security
  slug: hotjar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hotjar
---
