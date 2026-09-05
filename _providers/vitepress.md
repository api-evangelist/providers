---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: The VitePress Runtime API provides Vue composition functions and helper utilities for use in custom themes, Vue components, and Markdown pages. Key composables include useData() for accessing site and
  name: VitePress Runtime API
  slug: runtime-api
- description: The VitePress site configuration system exported from .vitepress/config.[js|ts]. Defines all settings controlling site metadata, routing, theming, Markdown processing, Vite and Vue integration, and bu
  name: VitePress Site Configuration
  slug: site-config
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vitepress-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vitepress.dev
- group: docs
  title: ''
  type: Documentation
  url: https://vitepress.dev/guide/getting-started
- group: build
  title: ''
  type: GitHub
  url: https://github.com/vuejs/vitepress
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/vitepress-config-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/vitepress-frontmatter-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/vitepress-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/vitepress-config-structure.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vitepress-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://vitepress.dev/llms.txt
created: '2026-03-18'
description: VitePress is a Vite and Vue powered static site generator widely used for developer documentation. It converts Markdown content into fast, beautiful documentation sites with support for Vue components embedded directly in Markdown pages. VitePress ships a polished default theme with built-in dark mode, mobile-responsive layout, full-text local search, Algolia DocSearch integration, internationalization, and automatic sitemap generation. VitePress is the official documentation framework used by Vue, Vite, Rollup, Pinia, and many CNCF and open source projects.
examples:
- key_count: 5
  name: Vitepress Config Example
  slug: vitepress-config-example
- key_count: 5
  name: Vitepress Frontmatter Example
  slug: vitepress-frontmatter-example
finops:
- name: Vitepress Finops
  service_category: API
  slug: vitepress-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vitepress.png
json_schemas:
- name: VitePress Site Configuration
  property_count: 26
  slug: vitepress-config
- name: VitePress Page Frontmatter
  property_count: 15
  slug: vitepress-frontmatter
json_structures:
- name: Vitepress Config Structure
  property_count: 0
  slug: vitepress-config-structure
jsonld:
- class_count: 0
  name: Vitepress Context
  property_count: 9
  slug: vitepress-context
layout: provider
modified: '2026-05-03'
name: VitePress
nav: Providers
network: true
overview: 'VitePress publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Documentation, Markdown, Open-Source, Static Site Generator, and Vite.


  The VitePress catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  VitePress'' developer surface includes documentation, GitHub presence, and 8 more developer resources.'
plans:
- name: Vitepress Plans Pricing
  plan_count: 3
  slug: vitepress-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Vitepress Rate Limits
  slug: vitepress-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: VitePress API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: vitepress-jsonschema-spectral-rules
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 59.3
    catalog_earned_first_party: 0.0
    catalog_gap: 55.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 6.7
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 25.0
    operational_transparency: 13.2
  previous_composite: 20.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vitepress/refs/heads/main/screenshots/vitepress-2026-06-20T201107.png
security:
- kind: domain-security
  name: Vitepress Domain Security
  slug: vitepress-domain-security
  summary_line: TLSv1.3 · HSTS
slug: vitepress
tags:
- Documentation
- Markdown
- Open-Source
- Static Site Generator
- Vite
- Vue
website: https://vitepress.dev
---
