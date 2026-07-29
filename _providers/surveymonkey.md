---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Surveymonkey Agentic Access
  operation_count: 30
  slug: surveymonkey-agentic-access
  summary_line: 30 operations · 6 acting
api_count: 8
apis:
- description: The Collectors API from SurveyMonkey — 3 operation(s) for collectors.
  name: SurveyMonkey Collectors API
  slug: surveymonkey-collectors-api
- description: The Contacts API from SurveyMonkey — 3 operation(s) for contacts.
  name: SurveyMonkey Contacts API
  slug: surveymonkey-contacts-api
- description: The Groups API from SurveyMonkey — 4 operation(s) for groups.
  name: SurveyMonkey Groups API
  slug: surveymonkey-groups-api
- description: The Responses API from SurveyMonkey — 4 operation(s) for responses.
  name: SurveyMonkey Responses API
  slug: surveymonkey-responses-api
- description: The Survey Structure API from SurveyMonkey — 4 operation(s) for survey structure.
  name: SurveyMonkey Survey Structure API
  slug: surveymonkey-survey-structure-api
- description: The Surveys API from SurveyMonkey — 3 operation(s) for surveys.
  name: SurveyMonkey Surveys API
  slug: surveymonkey-surveys-api
- description: The Users API from SurveyMonkey — 3 operation(s) for users.
  name: SurveyMonkey Users API
  slug: surveymonkey-users-api
- description: The Workgroups API from SurveyMonkey — 2 operation(s) for workgroups.
  name: SurveyMonkey Workgroups API
  slug: surveymonkey-workgroups-api
artifact_total: 19
asyncapis:
- description: AsyncAPI 2.6 description of the SurveyMonkey v3 webhook surface. SurveyMonkey delivers events as HTTP POST requests to a `subscription_url` that the consumer registers via the REST endpoint `POST /v3/
  name: SurveyMonkey Webhooks
  slug: surveymonkey-asyncapi
collections:
- collection_type: open
  name: SurveyMonkey API v3
  slug: open-surveymonkey
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/surveymonkey-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/surveymonkey-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/surveymonkey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/surveymonkey-authentication.yml
- group: auth
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
- name: Surveymonkey Finops
  service_category: Surveys / Feedback
  slug: surveymonkey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/surveymonkey.png
layout: provider
modified: '2026-05-30'
name: SurveyMonkey
nav: Providers
network: true
overview: 'SurveyMonkey publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Collectors API, Contacts API, Groups API, and 5 more. Tagged areas include Surveys, Market Research, Feedback, NPS, and Forms.


  The SurveyMonkey catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  SurveyMonkey''s developer surface includes authentication, engineering blog, and 4 more developer resources.'
plans:
- name: Surveymonkey Plans Pricing
  plan_count: 5
  slug: surveymonkey-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Surveymonkey Rate Limits
  slug: surveymonkey-rate-limits
rules:
- name: SurveyMonkey API Rules
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
  band: developing
  composite: 44.5
  delta: -3.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 63.6
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 31.6
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/surveymonkey/refs/heads/main/screenshots/surveymonkey-2026-06-20T194739.png
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
---
