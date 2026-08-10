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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Detectlanguage Agentic Access
  operation_count: 4
  slug: detectlanguage-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 3
apis:
- description: Account status and usage information.
  name: DetectLanguage Account API
  slug: detectlanguage-account-api
- description: Language detection endpoints for single and batch text analysis.
  name: DetectLanguage Detection API
  slug: detectlanguage-detection-api
- description: Retrieve the list of supported languages.
  name: DetectLanguage Languages API
  slug: detectlanguage-languages-api
artifact_total: 18
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/detectlanguage-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/detectlanguage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/detectlanguage-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://detectlanguage.com
- group: docs
  title: ''
  type: Documentation
  url: https://detectlanguage.com/documentation/v3
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/detectlanguage
- group: commercial
  title: ''
  type: Pricing
  url: https://detectlanguage.com/plans
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/detectlanguage/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/detectlanguage/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/detectlanguage/refs/heads/main/finops/finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://detectlanguage.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://detectlanguage.com/privacy_policy
- group: start
  title: ''
  type: Signup
  url: https://detectlanguage.com/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://detectlanguage.com/users/sign_in
- group: operate
  title: ''
  type: Contact
  url: https://detectlanguage.com/contact
created: '2026-06-13'
description: DetectLanguage is a language detection REST API that analyzes text samples and returns the identified language along with a confidence score. Supporting 216 languages, the API enables developers to identify languages from brief phrases to full documents, with batch processing support for multiple texts in a single request. It offers SDKs for Ruby, Python, Node.js, Go, Java, PHP, and .NET, making integration straightforward across technology stacks.
examples:
- key_count: 4
  name: Account Status
  slug: account-status
- key_count: 4
  name: Detect Batch
  slug: detect-batch
- key_count: 4
  name: Detect Single
  slug: detect-single
- key_count: 4
  name: Languages List
  slug: languages-list
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/detectlanguage.png
json_schemas:
- name: Account Status
  property_count: 8
  slug: account-status
- name: Language Candidate
  property_count: 2
  slug: language-candidate
- name: Language
  property_count: 2
  slug: language
jsonld:
- class_count: 0
  name: context Context
  property_count: 17
  slug: context
layout: provider
modified: '2026-06-13'
name: DetectLanguage
nav: Providers
network: true
overview: 'DetectLanguage publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Detection API, and Languages API. Tagged areas include Language Detection, Natural Language Processing, Text Analysis, Machine Learning, and Multilingual.


  The DetectLanguage catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DetectLanguage''s developer surface includes authentication, documentation, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 7
  slug: plans
random_paper: 77
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: DetectLanguage API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: detectlanguage-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.2
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 73.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/detectlanguage/refs/heads/main/screenshots/detectlanguage-2026-06-20T175940.png
security:
- kind: authentication
  name: Detectlanguage Authentication
  slug: detectlanguage-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Detectlanguage Domain Security
  slug: detectlanguage-domain-security
  summary_line: TLSv1.3 · DMARC
slug: detectlanguage
tags:
- Language Detection
- Natural Language Processing
- Text Analysis
- Machine Learning
- Multilingual
website: https://detectlanguage.com
---
