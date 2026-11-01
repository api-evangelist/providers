---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 100
  human_in_the_loop: 2
  name: Sapling Agentic Access
  operation_count: 116
  slug: sapling-agentic-access
  summary_line: 116 operations · 100 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.sapling.ai
  baseurl_source: declared
  description: API key status, usage and quota reporting.
  name: Sapling Account API
  slug: sapling-account-api
- baseURL: https://api.sapling.ai
  baseurl_source: declared
  description: Tone, sentiment, readability, quality, SEO, classification, extraction, style-guide compliance, and inclusive language.
  name: Sapling Analysis API
  slug: sapling-analysis-api
- baseURL: https://api.sapling.ai
  baseurl_source: declared
  description: AI-content, language, PII, named-entity, and unsafe-content detection.
  name: Sapling Detection API
  slug: sapling-detection-api
- baseURL: https://api.sapling.ai
  baseurl_source: declared
  description: PDF/Word text extraction and text chunking.
  name: Sapling Files API
  slug: sapling-files-api
- baseURL: https://api.sapling.ai
  baseurl_source: declared
  description: Text rewriting, summarization, translation, and completion.
  name: Sapling Generation API
  slug: sapling-generation-api
- baseURL: https://api.sapling.ai
  baseurl_source: declared
  description: Grammar and spelling correction.
  name: Sapling Proofreading API
  slug: sapling-proofreading-api
- baseURL: https://api.sapling.ai
  baseurl_source: declared
  description: Health and version probes (no API key).
  name: Sapling Service API
  slug: sapling-service-api
artifact_total: 18
common:
- group: auth
  href: https://artifacts.apis.io/sapling/well-known/sapling-sapling-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sapling-sapling-security.txt
- group: agent
  href: https://artifacts.apis.io/sapling/agentic-access/sapling-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sapling-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/sapling/rate-limits/sapling-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sapling-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sapling/plans/sapling-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sapling-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sapling/rules/sapling-rules.yml
  title: ''
  type: Spectral
  url: rules/sapling-rules.yml
- group: design
  href: https://artifacts.apis.io/sapling/json-ld/sapling-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sapling-context.jsonld
- group: design
  href: https://artifacts.apis.io/sapling/vocabulary/sapling-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sapling-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sapling/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sapling/data-model/sapling-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sapling-data-model.yml
- group: design
  href: https://artifacts.apis.io/sapling/components/sapling-components.yml
  title: ''
  type: Components
  url: components/sapling-components.yml
- group: auth
  title: ''
  type: Compliance
  url: https://sapling.ai/security
- group: auth
  href: https://artifacts.apis.io/sapling/authentication/sapling-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sapling-authentication.yml
- group: design
  href: https://artifacts.apis.io/sapling/errors/sapling-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sapling-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sapling/conformance/sapling-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sapling-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sapling/llms/sapling-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sapling-llms.txt
- group: agent
  href: https://artifacts.apis.io/sapling/well-known/sapling-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sapling-well-known.yml
- group: other
  href: https://artifacts.apis.io/sapling/hosts/sapling-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sapling-hosts.yml
- group: other
  href: https://artifacts.apis.io/sapling/vendors/sapling-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sapling-vendors.yml
- group: build
  href: https://artifacts.apis.io/sapling/packages/sapling-packages.yml
  title: ''
  type: Packages
  url: packages/sapling-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://sapling.statuspage.io
- group: auth
  title: ''
  type: Security
  url: https://sapling.ai/security
- group: build
  title: ''
  type: SDKs
  url: https://sapling.ai/llm/libraries
- group: operate
  title: ''
  type: ChangeLog
  url: https://sapling.ai/security/changelog
- group: auth
  href: https://artifacts.apis.io/sapling/security/sapling-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sapling-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/sapling/security/sapling-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sapling-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sapling/security/sapling-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sapling-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sapling.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sapling.ai/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://sapling.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://sapling.ai/docs/api/
- group: operate
  title: ''
  type: Support
  url: https://sapling.ai/docs/help/
- group: company
  title: ''
  type: Blog
  url: https://sapling.ai/devblog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/saplingai
- group: commercial
  title: ''
  type: Pricing
  url: https://sapling.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sapling.ai/user/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sapling.ai/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sapling.ai/privacy
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/20248607-4e2eafd4-e941-4d52-88a8-b4bb90c1d26a?action=collection%2Ffork&collection-url=entityId%3D20248607-4e2eafd4-e941-4d52-88a8-b4bb90c1d26a%26entityType%3Dcollection%26workspaceId%3Dcea8d224-5c5e-4604-a8f6-46f228f46f78
created: '2026-10-29'
description: Sapling provides a language model API toolkit and copilot for enterprise tasks, offering APIs and SDKs for grammar and spell checking, autocomplete, AI detection, paraphrasing, sentiment analysis, and more. The platform enables developers to integrate real‑time writing assistance and AI‑powered content generation into their applications, with customizable models, self‑hosting options, and extensive documentation for enterprise use cases.
image: https://sapling.ai/static/img/sapling-logo-horizontal.png
jsonld:
- class_count: 1
  name: Sapling Context
  property_count: 1
  slug: sapling-context
layout: provider
modified: '2026-10-29'
name: Sapling
nav: Providers
network: true
overview: 'Sapling publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Analysis API, Detection API, and 4 more. Tagged areas include AI, Language-Model, API, Enterprise, and Productivity.


  The Sapling catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sapling''s developer surface includes authentication, changelog, documentation, API reference, support, engineering blog, pricing, and 31 more developer resources.'
plans:
- name: Sapling Plans Pricing
  plan_count: 1
  slug: sapling-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Sapling Rate Limits
  slug: sapling-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Sapling API Rules
  rule_count: 18
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 2
  slug: sapling-rules
scopes:
- name: Sapling Scopes
  scope_count: 0
  slug: sapling-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 63.8
    catalog_earned_first_party: 16.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    contract_governance: 35.6
    contract_quality: 53.3
    developer_ergonomics: 63.6
    discoverability: 66.1
    operational_transparency: 68.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 41.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sapling Authentication
  slug: sapling-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Sapling Domain Security
  slug: sapling-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sapling Vulnerability Disclosure
  slug: sapling-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Sapling Trust Center
  slug: sapling-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR
skill_count: 1
skills:
- name: autocomplete
  slug: sapling-autocomplete
slug: sapling
tags:
- AI
- Language-Model
- API
- Enterprise
- Productivity
website: https://sapling.ai/
---
