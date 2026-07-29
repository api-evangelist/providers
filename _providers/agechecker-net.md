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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Agechecker Net Agentic Access
  operation_count: 4
  slug: agechecker-net-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 3
apis:
- description: The Sessions API from AgeChecker.Net — 2 operation(s) for sessions.
  name: AgeChecker.Net Sessions API
  slug: agechecker-net-sessions-api
- description: The Verification API from AgeChecker.Net — 1 operation(s) for verification.
  name: AgeChecker.Net Verification API
  slug: agechecker-net-verification-api
- description: The Webhooks API from AgeChecker.Net — 1 operation(s) for webhooks.
  name: AgeChecker.Net Webhooks API
  slug: agechecker-net-webhooks-api
artifact_total: 31
collections:
- collection_type: postman
  name: AgeChecker.Net Age Verification Sessions API
  slug: postman-agechecker-net-sessions-api
- collection_type: postman
  name: AgeChecker.Net Age Sessions Verification API
  slug: postman-agechecker-net-verification-api
- collection_type: postman
  name: AgeChecker.Net Age Verification Sessions Webhooks API
  slug: postman-agechecker-net-webhooks-api
- collection_type: open
  name: AgeChecker.Net Age Verification API
  slug: open-agechecker-net-age-verification
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/agecheckernet/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agechecker-net-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agechecker-net-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agechecker-net-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agechecker
- group: start
  title: ''
  type: Portal
  url: https://agechecker.net
- group: start
  title: ''
  type: GettingStarted
  url: https://agechecker.net/age-verification-api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agechecker.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agechecker.net/privacy
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/rules/agechecker-net-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/json-schema/agechecker-verification-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/json-schema/agechecker-verification-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/json-schema/agechecker-session-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/json-ld/agechecker-verification-context.jsonld
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/examples/agechecker-verification-request-example.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/examples/agechecker-verification-response-example.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/examples/agechecker-session-example.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/vocabulary/agechecker-net-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://agechecker.net/llms.txt
created: '2025-01-07'
description: AgeChecker.Net provides age verification API services for e-commerce businesses selling age-restricted products such as alcohol, tobacco, cannabis, and firearms. The API enables seamless background verification for most customers and guided photo ID verification for those who cannot be automatically verified.
examples:
- key_count: 7
  name: Age Verification Session Example
  slug: age-verification-session-example
- key_count: 4
  name: Age Verification Session List Example
  slug: age-verification-session-list-example
- key_count: 12
  name: Age Verification Verification Request Example
  slug: age-verification-verification-request-example
- key_count: 6
  name: Age Verification Verification Response Example
  slug: age-verification-verification-response-example
- key_count: 5
  name: Age Verification Webhook Config Example
  slug: age-verification-webhook-config-example
finops:
- name: Agechecker Net Finops
  service_category: API
  slug: agechecker-net-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agechecker-net.png
json_schemas:
- name: SessionList
  property_count: 4
  slug: age-verification-session-list
- name: Session
  property_count: 7
  slug: age-verification-session
- name: VerificationRequest
  property_count: 12
  slug: age-verification-verification-request
- name: VerificationResponse
  property_count: 6
  slug: age-verification-verification-response
- name: WebhookConfig
  property_count: 5
  slug: age-verification-webhook-config
json_structures:
- name: Age Verification Session List Structure
  property_count: 4
  slug: age-verification-session-list-structure
- name: Age Verification Session Structure
  property_count: 7
  slug: age-verification-session-structure
- name: Age Verification Verification Request Structure
  property_count: 12
  slug: age-verification-verification-request-structure
- name: Age Verification Verification Response Structure
  property_count: 6
  slug: age-verification-verification-response-structure
- name: Age Verification Webhook Config Structure
  property_count: 5
  slug: age-verification-webhook-config-structure
jsonld:
- class_count: 8
  name: Agechecker Net Age Context
  property_count: 25
  slug: agechecker-net-age-context
layout: provider
modified: '2026-05-19'
name: AgeChecker.Net
nav: Providers
network: true
overview: 'AgeChecker.Net publishes 3 APIs on the [APIs.io](https://apis.io/) network: Sessions API, Verification API, and Webhooks API. Tagged areas include Age Verification, Identity, Compliance, Regulatory, and E-Commerce.


  The AgeChecker.Net catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AgeChecker.Net''s developer surface includes authentication, developer portal, getting-started guide, code examples, and 15 more developer resources.'
plans:
- name: Agechecker Net Plans Pricing
  plan_count: 3
  slug: agechecker-net-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Agechecker Net Rate Limits
  slug: agechecker-net-rate-limits
rules:
- name: AgeChecker.Net API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: agechecker-net-jsonschema-spectral-rules
- name: AgeChecker.Net API Rules
  rule_count: 29
  severity_counts:
    error: 14
    hint: 0
    info: 0
    warn: 15
  slug: agechecker-net-spectral-rules
score:
  band: strong
  composite: 57.2
  delta: -3.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 73.4
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 60.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/screenshots/agechecker-net-2026-06-20T165819.png
security:
- kind: authentication
  name: Agechecker Net Authentication
  slug: agechecker-net-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Agechecker Net Domain Security
  slug: agechecker-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agechecker-net
tags:
- Age Verification
- Identity
- Compliance
- Regulatory
- E-Commerce
website: https://agechecker.net
---
