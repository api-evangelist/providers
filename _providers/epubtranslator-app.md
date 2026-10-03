---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-10-03'
api_count: 2
apis:
- description: EPUB Translator provides AI-powered translation of entire EPUB books via a remote MCP server. Users upload an EPUB or PDF and receive a fully translated version in the target language.
  name: EPUB Translator API
  slug: epub-translator-api
- description: The Apis API from EPUB Translator — 1 operation(s) for apis.
  name: EPUB Translator APIs API
  slug: epubtranslator-app-apis-api
artifact_total: 7
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/epubtranslator-app/refs/heads/main/plans/epubtranslator-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/epubtranslator-app-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/epubtranslator-app/refs/heads/main/rules/epubtranslator-app-rules.yml
  title: ''
  type: Spectral
  url: rules/epubtranslator-app-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/epubtranslator-app/refs/heads/main/json-ld/epubtranslator-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/epubtranslator-app-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/epubtranslator-app/refs/heads/main/vocabulary/epubtranslator-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/epubtranslator-app-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/epubtranslator-app/refs/heads/main/data-model/epubtranslator-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/epubtranslator-app-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/epubtranslator-app/refs/heads/main/conformance/epubtranslator-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/epubtranslator-app-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/epubtranslator-app/refs/heads/main/llms/epubtranslator-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/epubtranslator-app-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/epubtranslator-app/refs/heads/main/well-known/epubtranslator-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/epubtranslator-app-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/epubtranslator-app/refs/heads/main/hosts/epubtranslator-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/epubtranslator-app-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/epubtranslator-app/refs/heads/main/vendors/epubtranslator-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/epubtranslator-app-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/epubtranslator-app/refs/heads/main/security/epubtranslator-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/epubtranslator-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://epubtranslator.app/
- group: docs
  title: ''
  type: Documentation
  url: https://epubtranslator.app/agent-skill
- group: commercial
  title: ''
  type: Pricing
  url: https://epubtranslator.app/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://epubtranslator.app/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://epubtranslator.app/en/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://epubtranslator.app/en/blog
- group: operate
  title: ''
  type: Support
  url: https://epubtranslator.app/en/faq/translation-reading
coverage:
  checked: '2026-10-02'
  detail: No OpenAPI or other machine‑readable contract is publicly available; only HTML docs and an MCP endpoint (401) exist.
  evidence:
  - status: 404
    url: https://api.epubtranslator.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: EPUB Translator provides AI-powered translation of entire EPUB books, preserving chapters, footnotes, and layout. Users upload an EPUB or PDF and receive a fully translated version in the target language, with context-aware chapter translation and original formatting retained. The service targets readers, researchers, and learners who own foreign language books and need accurate, formatted translations for personal use.
image: https://epubtranslator.app/opengraph-image
json_schemas:
- name: PostApisFileDownloadRequest
  property_count: 1
  slug: epubtranslator-app-post-apis-file-download-request
jsonld:
- class_count: 1
  name: Epubtranslator App Context
  property_count: 1
  slug: epubtranslator-app-context
layout: provider
modified: '2026-10-02'
name: EPUB Translator
nav: Providers
network: true
overview: 'EPUB Translator publishes 2 APIs on the [APIs.io](https://apis.io/) network, including APIs API, and 1 more. Tagged areas include Artificial Intelligence, Translation, EPUB, Book, and Software-as-a-Service.


  The EPUB Translator catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EPUB Translator''s developer surface includes documentation, pricing, engineering blog, support, and 14 more developer resources.'
plans:
- name: Epubtranslator App Plans Pricing
  plan_count: 1
  slug: epubtranslator-app-plans-pricing
random_paper: 0
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: EPUB Translator API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: epubtranslator-app-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 56.2
    catalog_earned_first_party: 8.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 35.6
    contract_quality: 16.4
    developer_ergonomics: 16.7
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Epubtranslator App Domain Security
  slug: epubtranslator-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: epubtranslator-app
tags:
- Artificial Intelligence
- Translation
- EPUB
- Book
- Software-as-a-Service
- Company
website: https://epubtranslator.app/
---
