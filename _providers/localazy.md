---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 2
  human_in_the_loop: 0
  name: Localazy Agentic Access
  operation_count: 7
  slug: localazy-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 4
apis:
- description: Download translated files for a specific language.
  name: Localazy Export API
  slug: localazy-export-api
- description: List files and read file content as keys and translations.
  name: Localazy Files API
  slug: localazy-files-api
- description: Import and upload source and translation content.
  name: Localazy Import API
  slug: localazy-import-api
- description: List and create projects, and read project languages.
  name: Localazy Projects API
  slug: localazy-projects-api
artifact_total: 11
collections:
- collection_type: open
  name: Localazy API
  slug: open-localazy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/localazy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/localazy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/localazy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/localazy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/localazy
- group: company
  title: ''
  type: Website
  url: https://localazy.com
- group: docs
  title: ''
  type: Documentation
  url: https://localazy.com/docs/api/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/localazy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/localazy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/localazy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://localazy.com/blog
created: '2026-06-21'
description: Localazy is a localization and translation management platform built for developers. Its REST API at https://api.localazy.com lets teams import and upload source content, export and download translated files, list and manage files, languages, and projects, and drive AI-assisted translation - all authenticated with project, translation, or organization tokens.
finops:
- name: Localazy Finops
  service_category: Localization and Translation
  slug: localazy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/localazy.png
layout: provider
modified: '2026-06-21'
name: Localazy
nav: Providers
network: true
overview: 'Localazy publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Export API, Files API, Import API, and 1 more. Tagged areas include Localization, Translation, Internationalization, i18n, and L10n.


  Localazy''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Localazy Plans Pricing
  plan_count: 5
  slug: localazy-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Localazy Rate Limits
  slug: localazy-rate-limits
score:
  band: thin
  composite: 39.5
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/localazy/refs/heads/main/screenshots/localazy-2026-07-25T225430.png
security:
- kind: authentication
  name: Localazy Authentication
  slug: localazy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Localazy Domain Security
  slug: localazy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: localazy
tags:
- Localization
- Translation
- Internationalization
- i18n
- L10n
- Translation Management
website: https://localazy.com
---
