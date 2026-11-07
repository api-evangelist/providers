---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Langbly Com Agentic Access
  operation_count: 3
  slug: langbly-com-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.langbly.com
  baseurl_source: declared
  description: Translate text and detect languages
  name: langbly-com Translation API
  slug: langbly-com-translation-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/langbly-com/agentic-access/langbly-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/langbly-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/langbly-com/plans/langbly-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/langbly-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/langbly-com/rules/langbly-com-rules.yml
  title: ''
  type: Spectral
  url: rules/langbly-com-rules.yml
- group: design
  href: https://artifacts.apis.io/langbly-com/json-ld/langbly-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/langbly-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/langbly-com/vocabulary/langbly-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/langbly-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/langbly-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/langbly-com/data-model/langbly-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/langbly-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/langbly-com/conventions/langbly-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/langbly-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/langbly-com/conventions/langbly-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/langbly-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/langbly-com/authentication/langbly-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/langbly-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/langbly-com/errors/langbly-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/langbly-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/langbly-com/conformance/langbly-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/langbly-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/langbly-com/llms/langbly-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/langbly-com-llms.txt
- group: other
  href: https://artifacts.apis.io/langbly-com/hosts/langbly-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/langbly-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/langbly-com/vendors/langbly-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/langbly-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://langbly.com/status
- group: auth
  title: ''
  type: Security
  url: https://langbly.com/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://langbly.com/docs/changelog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.langbly.com</code
- group: auth
  href: https://artifacts.apis.io/langbly-com/security/langbly-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/langbly-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://langbly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://langbly.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://langbly.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://langbly.com/signup/
- group: operate
  title: ''
  type: Support
  url: https://langbly.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://langbly.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Langbly
- group: commercial
  title: ''
  type: Pricing
  url: https://langbly.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://langbly.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://langbly.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://langbly.com/privacy/
created: '2026-10-30'
description: Langbly provides an advanced translation API for developers, offering 500K characters included each month with pay-as-you-go pricing. The service is compatible with the Google Translate v2 endpoint shape, supports HTML-preserving translation, automatic language detection, formality control, and document translation for over 100 languages. It emphasizes privacy-first data handling, no request-body storage, encrypted traffic, EU data residency, and idempotency-safe retries. Langbly serves a range of industries from e-commerce to education, and offers SDKs for multiple platforms.
image: https://langbly.com/logo-32.png Langbly provides an advanced translation API for developers, offering 500K characters included each month with pay-as-you-go pricing. The service is compatible with the Google Translate v2 endpoint shape, supports HTML-preserving translation, automatic language detection, formality control, and document translation for over 100 languages. It emphasizes privacy-first data handling, no request-body storage, encrypted traffic, EU data residency, and idempotency-safe retries. Langbly serves a range of industries from e-commerce to education, and offers SDKs for multiple platforms.
json_schemas:
- name: DetectRequest
  property_count: 1
  slug: langbly-com-detect-request
- name: DetectResponse
  property_count: 1
  slug: langbly-com-detect-response
- name: LanguagesResponse
  property_count: 1
  slug: langbly-com-languages-response
- name: TranslateRequest
  property_count: 5
  slug: langbly-com-translate-request
- name: TranslateResponse
  property_count: 1
  slug: langbly-com-translate-response
jsonld:
- class_count: 6
  name: Langbly Com Context
  property_count: 7
  slug: langbly-com-context
layout: provider
modified: '2026-10-30'
name: langbly-com
nav: Providers
network: true
overview: 'langbly-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Translation API. Tagged areas include Company, Translation, Localization, Software-as-a-Service, and Machine Learning.


  The langbly-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  langbly-com''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 24 more developer resources.'
plans:
- name: Langbly Com Plans Pricing
  plan_count: 1
  slug: langbly-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Langbly Com Rate Limits
  slug: langbly-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: langbly-com API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: langbly-com-rules
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 67.8
    catalog_earned_first_party: 8.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.7
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 66.1
    developer_ergonomics: 41.0
    discoverability: 66.1
    operational_transparency: 23.7
  previous_composite: 59.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
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
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/langbly-com/langbly-com-2026-11-03T134632.png
security:
- kind: authentication
  name: Langbly Com Authentication
  slug: langbly-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Langbly Com Domain Security
  slug: langbly-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: translate-text
  slug: langbly-com-translate-text
slug: langbly-com
tags:
- Company
- Translation
- Localization
- Software-as-a-Service
- Machine Learning
website: https://langbly.com/
---
