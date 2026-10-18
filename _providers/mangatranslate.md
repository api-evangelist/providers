---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: MangaTranslate provides translation endpoints as listed in the API examples page.
  name: MangaTranslate API
  slug: mangatranslate-api
artifact_total: 3
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mangatranslate/refs/heads/main/llms/mangatranslate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mangatranslate-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mangatranslate/refs/heads/main/hosts/mangatranslate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mangatranslate-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mangatranslate/refs/heads/main/vendors/mangatranslate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mangatranslate-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mangatranslate.com/terms/
- group: auth
  title: ''
  type: Security
  url: https://www.mangatranslate.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mangatranslate.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://www.mangatranslate.com/ko/login/
- group: company
  title: ''
  type: Blog
  url: https://www.mangatranslate.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mangatranslate/refs/heads/main/security/mangatranslate-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mangatranslate-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mangatranslate/refs/heads/main/security/mangatranslate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mangatranslate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mangatranslate.com/ko/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mangatranslate.com/ko/api-examples/
coverage:
  checked: '2026-10-05'
  detail: API documentation page is a JavaScript-rendered SPA with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.mangatranslate.com/ko/api-examples/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-05'
description: MangaTranslate provides an AI-powered manga translation service that allows users to translate manga pages into multiple languages without requiring registration. The platform offers a web dashboard where users can upload images or PDFs, generate API keys, and manage translation credits. It supports over 30 source and target languages, boasts high accuracy, and is used by both individual readers and professional translators. The service includes detailed API documentation, pricing plans, and a community Discord for support.
image: https://www.mangatranslate.com/static/default/images/og-image.jpg
layout: provider
modified: '2026-10-05'
name: MangaTranslate
nav: Providers
network: true
overview: 'MangaTranslate is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Translation, and Manga.


  MangaTranslate''s developer surface includes engineering blog, documentation, and 10 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mangatranslate Domain Security
  slug: mangatranslate-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Mangatranslate Vulnerability Disclosure
  slug: mangatranslate-vulnerability-disclosure
  summary_line: no policy recorded
slug: mangatranslate
tags:
- Company
- Artificial Intelligence
- Translation
- Manga
website: https://www.mangatranslate.com/ko/
---
