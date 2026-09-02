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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Survicate Agentic Access
  operation_count: 9
  slug: survicate-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- description: The Survicate JavaScript SDK enables web-based feedback collection on websites and web applications. It provides methods to trigger surveys, set visitor traits, handle custom events, and control surve
  name: Survicate JavaScript SDK
  slug: survicate-javascript-sdk
- description: Survicate Mobile SDKs for iOS, Android, React Native, Flutter, and Unity enable in-app survey collection on mobile platforms with integrations for Segment, UXCam, and FullStory.
  name: Survicate Mobile SDK
  slug: survicate-mobile-sdk
- description: Survicate Webhooks enable real-time event-driven integrations by subscribing to events triggered by Survicate surveys such as new responses and survey completions.
  name: Survicate Webhooks
  slug: survicate-webhooks
- description: GDPR personal data management operations
  name: Survicate Personal Data API
  slug: survicate-personal-data-api
- description: Operations related to survey respondents
  name: Survicate Respondents API
  slug: survicate-respondents-api
- description: Operations related to survey responses
  name: Survicate Responses API
  slug: survicate-responses-api
- description: Operations related to surveys and their questions
  name: Survicate Surveys API
  slug: survicate-surveys-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Survicate Data Export Personal Data API
  slug: open-survicate-personal-data-api
- collection_type: open
  name: Survicate Data Export Personal Data Respondents API
  slug: open-survicate-respondents-api
- collection_type: open
  name: Survicate Data Export Personal Data Responses API
  slug: open-survicate-responses-api
- collection_type: open
  name: Survicate Data Export Personal Data Surveys API
  slug: open-survicate-surveys-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/survicate-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/survicate-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/survicate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/survicate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/survicate-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://survicate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.survicate.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Survicate
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/products/survicate/
- group: company
  title: ''
  type: Blog
  url: https://survicate.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://survicate.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.survicate.com/
- group: other
  title: ''
  type: X
  url: https://x.com/Survicate
- group: commercial
  title: ''
  type: Plans
  url: plans/survicate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/survicate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/survicate-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/survicate-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/survicate-context.jsonld
created: '2026-06-13'
description: Survicate is a customer feedback and survey platform with a REST API for managing surveys, collecting responses, segmenting audiences, and integrating feedback into CRM and analytics tools. The platform provides a Data Export API (v2) for retrieving survey data, a JavaScript SDK for web-based feedback collection, Mobile SDKs for iOS, Android, React Native, Flutter, and Unity, and Webhooks for event-driven integrations.
examples:
- key_count: 5
  name: List Surveys Example
  slug: list-surveys-example
- key_count: 5
  name: Survey Response Example
  slug: survey-response-example
finops:
- name: Survicate Finops
  service_category: ''
  slug: survicate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/survicate.png
json_schemas:
- name: Survicate Survey Response
  property_count: 5
  slug: survicate-response
- name: Survicate Survey
  property_count: 7
  slug: survicate-survey
jsonld:
- class_count: 27
  name: Survicate Context
  property_count: 5
  slug: survicate-context
layout: provider
modified: '2026-06-13'
name: Survicate
nav: Providers
network: true
overview: 'Survicate publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Personal Data API, Respondents API, Responses API, and 1 more. Tagged areas include Surveys, Customer Feedback, NPS, User Research, and Feedback Analytics.


  The Survicate catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Survicate''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Survicate Plans Pricing
  plan_count: 4
  slug: survicate-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Survicate Rate Limits
  slug: survicate-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Survicate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: survicate-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 38.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 59.4
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 42.1
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/survicate/refs/heads/main/screenshots/survicate-2026-06-20T194742.png
security:
- kind: authentication
  name: Survicate Authentication
  slug: survicate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Survicate Domain Security
  slug: survicate-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Survicate Vulnerability Disclosure
  slug: survicate-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Survicate Trust Center
  slug: survicate-trust-center
  summary_line: ISO 27001, PCI DSS, HIPAA, GDPR
slug: survicate
tags:
- Surveys
- Customer Feedback
- NPS
- User Research
- Feedback Analytics
- CRM Integration
- Customer Experience
website: https://survicate.com/
---
