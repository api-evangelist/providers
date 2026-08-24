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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Riverside Agentic Access
  operation_count: 12
  slug: riverside-agentic-access
  summary_line: 12 operations · 3 acting
api_count: 4
apis:
- description: Export file management and downloads
  name: Riverside Exports API
  slug: riverside-exports-api
- description: Production workspace organization
  name: Riverside Productions API
  slug: riverside-productions-api
- description: Recording management and retrieval
  name: Riverside Recordings API
  slug: riverside-recordings-api
- description: Webinar registration management
  name: Riverside Webinars API
  slug: riverside-webinars-api
artifact_total: 26
collections:
- collection_type: postman
  name: Riverside Business Exports API
  slug: postman-riverside-exports-api
- collection_type: postman
  name: Riverside Business Exports Productions API
  slug: postman-riverside-productions-api
- collection_type: postman
  name: Riverside Business Exports Recordings API
  slug: postman-riverside-recordings-api
- collection_type: postman
  name: Riverside Business Exports Webinars API
  slug: postman-riverside-webinars-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Riverside Business API
  slug: open-riverside-business
- collection_type: open
  name: Riverside Business Exports API
  slug: open-riverside-exports-api
- collection_type: open
  name: Riverside Business Exports Productions API
  slug: open-riverside-productions-api
- collection_type: open
  name: Riverside Business Exports Recordings API
  slug: open-riverside-recordings-api
- collection_type: open
  name: Riverside Business Exports Webinars API
  slug: open-riverside-webinars-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/riverside/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/riverside-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/riverside-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/riverside-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/riversidefm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-riverside-company
- group: company
  title: ''
  type: Website
  url: https://riverside.fm
- group: docs
  title: ''
  type: Documentation
  url: https://docs.riverside.fm/
- group: operate
  title: ''
  type: Support
  url: https://support.riverside.fm
- group: commercial
  title: ''
  type: Pricing
  url: https://riverside.fm/pricing
- group: company
  title: ''
  type: Blog
  url: https://riverside.fm/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://riverside.fm/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://riverside.fm/terms-of-service
- group: start
  title: ''
  type: Signup
  url: https://riverside.fm/signup
- group: start
  title: ''
  type: Login
  url: https://riverside.fm/login
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/riverside/refs/heads/main/json-ld/riverside-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/riverside/refs/heads/main/vocabulary/riverside-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.riverside.fm/llms.txt
created: '2026-03-16'
description: Riverside is a professional podcast and video recording platform that enables remote studio-quality recording, AI-powered editing, and publishing. The Riverside Business API provides programmatic access to recordings, productions, studios, projects, exports, transcriptions, and webinar management for enterprise podcast production workflows. API access is available on Business plan only.
examples:
- key_count: 2
  name: Riverside List Recordings Example
  slug: riverside-list-recordings-example
finops:
- name: Riverside Finops
  service_category: API
  slug: riverside-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/riverside.png
json_schemas:
- name: Riverside Recording
  property_count: 10
  slug: riverside-recording
json_structures:
- name: Riverside Recording Structure
  property_count: 0
  slug: riverside-recording-structure
jsonld:
- class_count: 25
  name: Riverside Context
  property_count: 0
  slug: riverside-context
layout: provider
modified: '2026-05-19'
name: Riverside
nav: Providers
network: true
overview: 'Riverside publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Exports API, Productions API, Recordings API, and 1 more. Tagged areas include Podcast, Video Recording, Media, Content Creation, and Audio.


  The Riverside catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Riverside''s developer surface includes authentication, documentation, support, pricing, engineering blog, signup flow, and 12 more developer resources.'
plans:
- name: Riverside Plans Pricing
  plan_count: 3
  slug: riverside-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Riverside Rate Limits
  slug: riverside-rate-limits
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Riverside API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 0
    info: 4
    warn: 4
  slug: riverside-business-rules
- effective_rule_count: 5
  extends: []
  name: Riverside API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: riverside-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.1
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 69.7
    contract_quality: 67.7
    developer_ergonomics: 33.3
    discoverability: 81.5
    governance: 69.7
    operational_transparency: 10.5
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/riverside/refs/heads/main/screenshots/riverside-2026-06-20T193133.png
security:
- kind: authentication
  name: Riverside Authentication
  slug: riverside-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Riverside Domain Security
  slug: riverside-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: riverside
tags:
- Podcast
- Video Recording
- Media
- Content Creation
- Audio
website: https://riverside.fm
---
