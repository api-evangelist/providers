---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: 'REST API (formerly Applanga) for mobile app and software string localization, supporting upload/download of source and translated entries, tags, screenshots, projects, branches, orders, and webhooks, '
  name: GlobalLink Strings API
  slug: globallink-strings
- description: Open-source PHP Drupal module exposing GlobalLink translation submission and retrieval inside Drupal sites, with sub-modules for blocks, entities, menus, taxonomy, and webforms, configured via GlobalL
  name: GlobalLink Drupal Connector
  slug: globallink-drupal
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transperfect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.transperfect.com/
- group: other
  title: ''
  type: GlobalLinkSuite
  url: https://globallink.transperfect.com/
- group: other
  title: ''
  type: Products
  url: https://globallink.transperfect.com/products
- group: company
  title: ''
  type: Blog
  url: https://www.transperfect.com/blog
- group: company
  title: ''
  type: News
  url: https://www.transperfect.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.transperfect.com/about/leadership
- group: company
  title: ''
  type: About
  url: https://www.transperfect.com/about
- group: operate
  title: ''
  type: ContactSales
  url: https://www.transperfect.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://www.transperfect.com/careers
- group: build
  title: ''
  type: GitHub
  url: https://github.com/TransPerfect
- group: build
  title: ''
  type: AppsGitHub
  url: https://github.com/applanga
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/transperfect
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/transperfect
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/TransPerfectVideo
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/transperfect-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/transperfect-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/transperfect-translation-entry-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/transperfect-translation-entry-structure.json
created: '2026-05-23'
description: TransPerfect is the world's largest privately held provider of language and AI services, delivering translation, localization, interpretation, AI training data, and content technology through the GlobalLink platform suite, DataForce data services, and a global production network spanning 200+ languages and 160+ offices, with 2025 billed revenues of $1.32 billion serving over 6,000 organizations including 90% of the Fortune 500.
graphqls:
- description: TransPerfect does not currently publish a native GraphQL API. Their public-facing API surface consists of the GlobalLink Strings REST API (formerly Applanga) at `https://api.globallinkstrings.com/v1/a
  name: TransPerfect GraphQL
  slug: transperfect-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transperfect.png
json_schemas:
- name: GlobalLink Translation Entry
  property_count: 14
  slug: transperfect-translation-entry
json_structures:
- name: Transperfect Translation Entry Structure
  property_count: 0
  slug: transperfect-translation-entry-structure
jsonld:
- class_count: 62
  name: Transperfect Context
  property_count: 8
  slug: transperfect-context
layout: provider
modified: '2026-05-23'
name: TransPerfect
nav: Providers
network: true
overview: 'TransPerfect publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Translation, Localization, Language Services, Translation Management, and Machine Translation.


  The TransPerfect catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TransPerfect''s developer surface includes engineering blog, product news, GitHub presence, YouTube channel, and 15 more developer resources.'
random_paper: 21
rules:
- name: TransPerfect API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: transperfect-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 58.0
    developer_ergonomics: 2.2
    discoverability: 53.7
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 29.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transperfect/refs/heads/main/screenshots/transperfect-2026-06-20T195557.png
security:
- kind: domain-security
  name: Transperfect Domain Security
  slug: transperfect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: transperfect
tags:
- Translation
- Localization
- Language Services
- Translation Management
- Machine Translation
- AI Translation
- Interpretation
- Content Localization
- Mobile App Localization
- Globalization
- Multilingual
website: https://www.transperfect.com/
---
