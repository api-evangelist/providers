---
access_model:
  confidence: medium
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Detectlanguage Agentic Access
  operation_count: 4
  slug: detectlanguage-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- baseURL: https://ws.detectlanguage.com/v3
  baseurl_source: declared
  description: Account status and usage information.
  name: DetectLanguage Account API
  slug: detectlanguage-account-api
- baseURL: https://ws.detectlanguage.com/v3
  baseurl_source: declared
  description: Language detection endpoints for single and batch text analysis.
  name: DetectLanguage Detection API
  slug: detectlanguage-detection-api
- baseURL: https://ws.detectlanguage.com/v3
  baseurl_source: declared
  description: Retrieve the list of supported languages.
  name: DetectLanguage Languages API
  slug: detectlanguage-languages-api
artifact_total: 21
collections:
- collection_type: open
  name: DetectLanguage Account API
  slug: open-detectlanguage-account-api
- collection_type: open
  name: DetectLanguage Account Detection API
  slug: open-detectlanguage-detection-api
- collection_type: open
  name: DetectLanguage Account Languages API
  slug: open-detectlanguage-languages-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/detectlanguage/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/detectlanguage
- group: auth
  title: ''
  type: Security
  url: https://detectlanguage.com/documentation#security
- group: operate
  title: ''
  type: FAQ
  url: https://detectlanguage.com/faq
- group: other
  title: ''
  type: Regions
  url: https://detectlanguage.com/regions
- group: agent
  href: https://artifacts.apis.io/detectlanguage/agentic-access/detectlanguage-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/detectlanguage-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/detectlanguage/security/detectlanguage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/detectlanguage-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/detectlanguage/authentication/detectlanguage-authentication.yml
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
- has_sources: false
  method: generated
  name: Finops
  primary_unit: ''
  service_category: ''
  slug: finops
  template: true
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
overview: 'DetectLanguage publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Account API, Detection API, and Languages API. Tagged areas include Language Detection, Natural Language Processing, Text Analysis, Machine Learning, and Multilingual.


  The DetectLanguage catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DetectLanguage''s developer surface includes FAQ, authentication, documentation, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Plans
  plan_count: 7
  slug: plans
random_paper: 5
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: DetectLanguage — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: detectlanguage-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 51.3
    catalog_earned_first_party: 0.0
    catalog_gap: 63.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 52.6
    contract_governance: 9.8
    contract_quality: 58.5
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 15.8
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/detectlanguage/detectlanguage-2026-06-20T175940.png
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
