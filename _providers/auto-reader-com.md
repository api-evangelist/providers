---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Auto Reader Com Agentic Access
  operation_count: 32
  slug: auto-reader-com-agentic-access
  summary_line: 32 operations · 26 acting
api_count: 1
apis:
- description: Multilingual OCR (Arabic-first, manga-aware), translation, and vision escalation.
  name: OCR & Translate API
  slug: ocr-translate-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Ask API from Auto Reader — 1 operation(s) for ask.
  name: Auto Reader Ask API
  slug: auto-reader-com-ask-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Book API from Auto Reader — 3 operation(s) for book.
  name: Auto Reader Book API
  slug: auto-reader-com-book-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Correct API from Auto Reader — 1 operation(s) for correct.
  name: Auto Reader Correct API
  slug: auto-reader-com-correct-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Data API from Auto Reader — 1 operation(s) for data.
  name: Auto Reader Data API
  slug: auto-reader-com-data-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Detect API from Auto Reader — 2 operation(s) for detect.
  name: Auto Reader Detect API
  slug: auto-reader-com-detect-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Document API from Auto Reader — 1 operation(s) for document.
  name: Auto Reader Document API
  slug: auto-reader-com-document-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Export API from Auto Reader — 1 operation(s) for export.
  name: Auto Reader Export API
  slug: auto-reader-com-export-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Extract API from Auto Reader — 2 operation(s) for extract.
  name: Auto Reader Extract API
  slug: auto-reader-com-extract-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Feedback API from Auto Reader — 1 operation(s) for feedback.
  name: Auto Reader Feedback API
  slug: auto-reader-com-feedback-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Glossary API from Auto Reader — 1 operation(s) for glossary.
  name: Auto Reader Glossary API
  slug: auto-reader-com-glossary-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Health API from Auto Reader — 2 operation(s) for health.
  name: Auto Reader Health API
  slug: auto-reader-com-health-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Internal API from Auto Reader — 1 operation(s) for internal.
  name: Auto Reader Internal API
  slug: auto-reader-com-internal-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Jobs API from Auto Reader — 1 operation(s) for jobs.
  name: Auto Reader Jobs API
  slug: auto-reader-com-jobs-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Manga API from Auto Reader — 2 operation(s) for manga.
  name: Auto Reader Manga API
  slug: auto-reader-com-manga-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Ocr API from Auto Reader — 2 operation(s) for ocr.
  name: Auto Reader Ocr API
  slug: auto-reader-com-ocr-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Ocr Translate API from Auto Reader — 2 operation(s) for ocr translate.
  name: Auto Reader Ocr Translate API
  slug: auto-reader-com-ocr-translate-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Reduce API from Auto Reader — 1 operation(s) for reduce.
  name: Auto Reader Reduce API
  slug: auto-reader-com-reduce-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Rewrite API from Auto Reader — 1 operation(s) for rewrite.
  name: Auto Reader Rewrite API
  slug: auto-reader-com-rewrite-api
- baseURL: https://api.auto-reader.com
  baseurl_source: declared
  description: The Translate API from Auto Reader — 2 operation(s) for translate.
  name: Auto Reader Translate API
  slug: auto-reader-com-translate-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/auto-reader-com/agentic-access/auto-reader-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/auto-reader-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/auto-reader-com/rules/auto-reader-com-rules.yml
  title: ''
  type: Spectral
  url: rules/auto-reader-com-rules.yml
- group: design
  href: https://artifacts.apis.io/auto-reader-com/json-ld/auto-reader-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/auto-reader-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/auto-reader-com/vocabulary/auto-reader-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/auto-reader-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/auto-reader-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/auto-reader-com/data-model/auto-reader-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/auto-reader-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/auto-reader-com/errors/auto-reader-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/auto-reader-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/auto-reader-com/conformance/auto-reader-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/auto-reader-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/auto-reader-com/llms/auto-reader-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auto-reader-com-llms.txt
- group: other
  href: https://artifacts.apis.io/auto-reader-com/hosts/auto-reader-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auto-reader-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/auto-reader-com/vendors/auto-reader-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auto-reader-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/auto-reader-com/authentication/auto-reader-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/auto-reader-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/auto-reader-com/security/auto-reader-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auto-reader-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auto-reader.com/
- group: docs
  title: ''
  type: Documentation
  url: https://auto-reader.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ocr.auto-reader.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://auto-reader.com/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auto-reader.com/eula.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auto-reader.com/privacy
created: '2026-11-02'
description: Auto Reader provides a mobile app that turns books, manga, and PDFs into spoken audio using on-device lifelike voices. The service works offline, ensuring privacy, and offers free basic features with premium options for higher quality voices and additional formats. It supports multiple languages and integrates with popular e‑book libraries, delivering a hands‑free reading experience for commuters, visually impaired users, and anyone who prefers listening to reading.
image: https://auto-reader.com/assets/og-cover.png
jsonld:
- class_count: 21
  name: Auto Reader Com Context
  property_count: 42
  slug: auto-reader-com-context
layout: provider
modified: '2026-11-02'
name: Auto Reader
nav: Providers
network: true
overview: 'Auto Reader publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ask API, Book API, Correct API, and 17 more. Tagged areas include Mobile, Accessibility, Audio, eBook, and Offline.


  The Auto Reader catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Auto Reader''s developer surface includes authentication, documentation, API reference, pricing, and 15 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Auto Reader API Rules
  rule_count: 52
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 5
  slug: auto-reader-com-rules
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 28.5
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 55.9
    developer_ergonomics: 22.0
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 3.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Auto Reader Com Authentication
  slug: auto-reader-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Auto Reader Com Domain Security
  slug: auto-reader-com-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: auto-reader-com-book-processing
  slug: auto-reader-com-book-processing
slug: auto-reader-com
tags:
- Mobile
- Accessibility
- Audio
- eBook
- Offline
website: https://auto-reader.com/
---
