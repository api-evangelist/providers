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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Konfig's developer platform for generating, validating, and publishing SDKs, API reference documentation, and interactive tutorials from OpenAPI specifications and Postman Collections. Delivered prima
  name: Konfig SDK Generation Platform (Sunset)
  slug: konfig-sdk-generation
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/konfig-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://konfigthis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://konfigthis.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://konfigthis.com/docs/getting-started/openapi-specification/
- group: company
  title: ''
  type: Blog
  url: https://konfigthis.com/blog/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/konfig-dev
- group: build
  title: ''
  type: GitHub Generator
  url: https://github.com/konfig-dev/konfig
- group: build
  title: ''
  type: GitHub Automation
  url: https://github.com/konfig-dev/automation
- group: build
  title: ''
  type: GitHub Backstage Plugin
  url: https://github.com/konfig-dev/backstage-plugin-konfig
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/konfig
- group: start
  title: ''
  type: Schedule Demo
  url: https://konfigthis.com/schedule-demo/
- group: other
  title: ''
  type: ClosureAnnouncement
  url: https://dylanhuang.com/blog/closing-my-startup/
- group: commercial
  title: ''
  type: Plans
  url: plans/konfig-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/konfig-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/konfig-finops.yml
created: '2026-03-16'
deprecated: true
deprecated_note: Konfig's API has been sunset. Retained for historical reference.
description: Konfig was a developer-tools startup that generated SDKs, API documentation, interactive demos, and tutorials from OpenAPI Specifications and Postman Collections, delivered primarily through the konfig-cli command-line interface and GitHub Actions automation. The company was sunset in December 2024; founder Dylan Huang announced the closure in a "Closing My Startup" blog post on November 25, 2024. The flagship konfig generator repository's GitHub description now reads "SDK & API Docs Generator. Sunset as of December 2024." This index is retained as a historical record of the platform and the consolidation of the SDK-generation category around Stainless, Fern, and Speakeasy.
finops:
- name: Konfig Finops
  service_category: API
  slug: konfig-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/konfig.png
layout: provider
modified: '2026-05-22'
name: Konfig
nav: Providers
network: true
overview: 'Konfig publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Documentation, CLI, Developer Tools, OpenAPI, and Postman.


  Konfig''s developer surface includes documentation, getting-started guide, engineering blog, GitHub presence, and 11 more developer resources.'
plans:
- name: Konfig Plans Pricing
  plan_count: 3
  slug: konfig-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Konfig Rate Limits
  slug: konfig-rate-limits
score:
  band: emerging
  composite: 23.0
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 25.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/konfig/refs/heads/main/screenshots/konfig-2026-06-20T184127.png
security:
- kind: domain-security
  name: Konfig Domain Security
  slug: konfig-domain-security
  summary_line: TLSv1.3 · DMARC
slug: konfig
tags:
- API Documentation
- CLI
- Developer Tools
- OpenAPI
- Postman
- SDK Generation
- Sunset
website: https://konfigthis.com/
---
