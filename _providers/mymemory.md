---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides translation, language detection, and glossary management via REST endpoints as described in the technical specifications page.
  name: MyMemory REST API
  slug: mymemory-rest-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/mymemory/hosts/mymemory-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mymemory-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mymemory.translated.net/terms-and-conditions
- group: auth
  href: https://artifacts.apis.io/mymemory/security/mymemory-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mymemory-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mymemory.translated.net/
- group: docs
  title: ''
  type: Documentation
  url: https://mymemory.translated.net/doc/
- group: docs
  title: ''
  type: APIReference
  url: https://mymemory.translated.net/doc/spec.php
- group: operate
  title: ''
  type: Support
  url: mailto:mymemory@translated.net?subject=MyMemory
coverage:
  checked: '2026-10-28'
  detail: Documentation page provides HTML specs but no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract.
  evidence:
  - status: 200
    url: https://mymemory.translated.net/doc/spec.php
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: MyMemory (Translated) provides a large collaborative translation memory service, offering both machine translation and human-contributed translations. It powers multilingual websites, applications, and content localization by allowing developers to access its Translation API for language detection, translation, and glossary management. The platform hosts the world’s largest public translation archive, enabling seamless integration of translation capabilities into software solutions.
layout: provider
modified: '2026-10-27'
name: MyMemory (Translated)
nav: Providers
network: true
overview: 'MyMemory (Translated) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Translation, Localization, and Machine Translation.


  MyMemory (Translated)''s developer surface includes documentation, API reference, support, and 4 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 10.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mymemory/mymemory-2026-11-03T135937.png
security:
- kind: domain-security
  name: Mymemory Domain Security
  slug: mymemory-domain-security
  summary_line: TLSv1.2 · DMARC
slug: mymemory
tags:
- Company
- Translation
- Localization
- Machine Translation
website: https://mymemory.translated.net/
---
