---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Tolgee Agentic Access
  operation_count: 25
  slug: tolgee-agentic-access
  summary_line: 25 operations · 16 acting
api_count: 7
apis:
- description: Inspect the current API key.
  name: Tolgee API Keys API
  slug: tolgee-api-keys-api
- description: Export localization files and import translation data.
  name: Tolgee Import/Export API
  slug: tolgee-import-export-api
- description: Manage translation keys within a project.
  name: Tolgee Keys API
  slug: tolgee-keys-api
- description: Manage project languages (locales).
  name: Tolgee Languages API
  slug: tolgee-languages-api
- description: Create and manage localization projects.
  name: Tolgee Projects API
  slug: tolgee-projects-api
- description: Attach visual context screenshots to keys.
  name: Tolgee Screenshots API
  slug: tolgee-screenshots-api
- description: Read and write translations and their states.
  name: Tolgee Translations API
  slug: tolgee-translations-api
artifact_total: 14
collections:
- collection_type: open
  name: Tolgee API
  slug: open-tolgee
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tolgee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tolgee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tolgee-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tolgee
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tolgee
- group: company
  title: ''
  type: Website
  url: https://tolgee.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tolgee.io
- group: commercial
  title: ''
  type: Plans
  url: plans/tolgee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tolgee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tolgee-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://tolgee.io/blog
created: '2026-06-21'
description: Tolgee is an open-source localization platform for translating web and mobile applications. It provides in-context translation, AI-assisted machine translation, framework SDKs, a CLI, and a REST API. Teams can self-host the open-source platform for free via Docker or use Tolgee Cloud (app.tolgee.io). The REST API exposes projects, localization keys, translations, languages, import/export, and screenshots, authenticated with a project API key sent in the X-API-Key header.
finops:
- name: Tolgee Finops
  service_category: Developer Tools and Localization
  slug: tolgee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tolgee.png
layout: provider
modified: '2026-06-21'
name: Tolgee
nav: Providers
network: true
overview: 'Tolgee publishes 7 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Import/Export API, Keys API, and 4 more. Tagged areas include Localization, i18n, Translation, Open Source, and Developer Tools.


  Tolgee''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Tolgee Plans Pricing
  plan_count: 6
  slug: tolgee-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Tolgee Rate Limits
  slug: tolgee-rate-limits
score:
  band: thin
  composite: 37.8
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Tolgee Authentication
  slug: tolgee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tolgee Domain Security
  slug: tolgee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tolgee
tags:
- Localization
- i18n
- Translation
- Open Source
- Developer Tools
website: https://tolgee.io
---
