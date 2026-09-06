---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Localazy Agentic Access
  operation_count: 7
  slug: localazy-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.localazy.com
  baseurl_source: declared
  description: Download translated files for a specific language.
  name: Localazy Export API
  slug: localazy-export-api
- baseURL: https://api.localazy.com
  baseurl_source: declared
  description: List files and read file content as keys and translations.
  name: Localazy Files API
  slug: localazy-files-api
- baseURL: https://api.localazy.com
  baseurl_source: declared
  description: Import and upload source and translation content.
  name: Localazy Import API
  slug: localazy-import-api
- baseURL: https://api.localazy.com
  baseurl_source: declared
  description: List and create projects, and read project languages.
  name: Localazy Projects API
  slug: localazy-projects-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Localazy Export API
  slug: open-localazy-export-api
- collection_type: open
  name: Localazy Export Files API
  slug: open-localazy-files-api
- collection_type: open
  name: Localazy Export Import API
  slug: open-localazy-import-api
- collection_type: open
  name: Localazy Export Projects API
  slug: open-localazy-projects-api
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
random_paper: 2
rate_limits:
- limit_count: 5
  name: Localazy Rate Limits
  slug: localazy-rate-limits
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.3
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
