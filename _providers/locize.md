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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Locize REST API enables developers to programmatically manage translation namespaces, keys, languages, and versions. It supports fetching and updating translations via CDN endpoints, reporting mis
  name: Locize REST API
  slug: locize-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/locize-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.locize.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.locize.com/docs/integration/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/locize
- group: company
  title: ''
  type: Blog
  url: https://www.locize.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.locize.com/pricing/
- group: other
  title: ''
  type: X
  url: https://x.com/locize
- group: commercial
  title: ''
  type: Plans
  url: plans/locize-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/locize-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/locize-finops.yml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/locize-context.jsonld
created: '2026-06-13'
description: Locize is a localization-as-a-service platform built by the creators of i18next that connects developers, product managers, and translators to deliver translation updates continuously without requiring app redeployment. The platform provides a comprehensive REST API for managing translation namespaces, keys, importing and exporting translations, and version management across multiple languages and environments. Locize supports native i18next integration along with any i18n library and workflow, and offers CLI tooling, CDN delivery, AI-assisted translation, and in-context editing for a complete developer-friendly localization lifecycle.
finops:
- name: Locize Finops
  service_category: ''
  slug: locize-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/locize.png
jsonld:
- class_count: 30
  name: Locize Context
  property_count: 0
  slug: locize-context
layout: provider
modified: '2026-06-13'
name: Locize
nav: Providers
network: true
overview: 'Locize publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Localization, Internationalization, i18n, Translation Management, and Translation.


  The Locize catalog on APIs.io includes 1 JSON-LD context.


  Locize''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Locize Plans Pricing
  plan_count: 7
  slug: locize-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Locize Rate Limits
  slug: locize-rate-limits
score:
  band: thin
  composite: 35.1
  delta: -4.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/locize/refs/heads/main/screenshots/locize-2026-06-20T184640.png
security:
- kind: domain-security
  name: Locize Domain Security
  slug: locize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: locize
tags:
- Localization
- Internationalization
- i18n
- Translation Management
- Translation
- i18next
- Developer Tools
- CDN
- SaaS
website: https://www.locize.com/
---
