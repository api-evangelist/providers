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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-19'
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
artifact_total: 28
asyncapis:
- description: AsyncAPI 2.6 description of the SurveyMonkey v3 webhook surface. SurveyMonkey delivers events as HTTP POST requests to a `subscription_url` that the consumer registers via the REST endpoint `POST /v3/
  name: SurveyMonkey Webhooks
  slug: surveymonkey-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
random_paper: 1
rate_limits:
- limit_count: 3
  name: Surveymonkey Rate Limits
  slug: surveymonkey-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: SurveyMonkey API Rules
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
  composite: 32.4
  delta: -4.4
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 11.4
    contract_quality: 60.1
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 11.4
    operational_transparency: 7.9
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
