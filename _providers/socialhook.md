---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Provides webhook aggregation for social media platforms. Documentation at https://socialhook.io/en/docs. No machine‑readable contract discovered.
  name: Socialhook API
  slug: socialhook-api-2
- baseURL: https://api.socialhook.io
  baseurl_source: declared
  description: 'Lead Lock Systems API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Lead Lock Systems API
  slug: socialhook-api
artifact_total: 9
asyncapis:
- description: ''
  name: Socialhook Webhooks
  slug: socialhook-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/socialhook/rate-limits/socialhook-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/socialhook-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/socialhook/plans/socialhook-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/socialhook-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/socialhook/rules/socialhook-rules.yml
  title: ''
  type: Spectral
  url: rules/socialhook-rules.yml
- group: design
  href: https://artifacts.apis.io/socialhook/vocabulary/socialhook-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/socialhook-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/socialhook/asyncapi/socialhook-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/socialhook-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/socialhook/changelog/socialhook-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/socialhook-changelog.yml
- group: auth
  href: https://artifacts.apis.io/socialhook/authentication/socialhook-authentication.yml
  title: ''
  type: Authentication
  url: authentication/socialhook-authentication.yml
- group: design
  href: https://artifacts.apis.io/socialhook/conformance/socialhook-conformance.yml
  title: ''
  type: Conformance
  url: conformance/socialhook-conformance.yml
- group: agent
  href: https://artifacts.apis.io/socialhook/llms/socialhook-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/socialhook-llms.txt
- group: other
  href: https://artifacts.apis.io/socialhook/hosts/socialhook-hosts.yml
  title: ''
  type: Hosts
  url: hosts/socialhook-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://socialhook.io/en/security
- group: start
  title: ''
  type: Login
  url: https://socialhook.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://socialhook.io/en/changelog
- group: auth
  href: https://artifacts.apis.io/socialhook/security/socialhook-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/socialhook-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/socialhook/security/socialhook-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/socialhook-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://socialhook.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://socialhook.io/en/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://socialhook.io/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://socialhook.io/en/blog
- group: operate
  title: ''
  type: Support
  url: https://socialhook.io/en/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://socialhook.io/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://socialhook.io/en/privacy
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on api.socialhook.io or socialhook.io despite probing known spec endpoints.
  evidence:
  - status: 404
    url: https://api.socialhook.io/openapi.json
  - status: 404
    url: https://api.socialhook.io/openapi.yaml
  - status: 307
    url: https://socialhook.io/openapi.json
  - status: 307
    url: https://socialhook.io/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Lead Lock Systems provides a platform that aggregates and forwards webhooks from major social media channels such as Facebook, Instagram, and WhatsApp to a user‑specified endpoint. It enables businesses to receive real‑time messaging events, automate workflows, and integrate with CRM or AI systems without building direct connections to each social network. The service offers instant webhook delivery, a simple pricing model, and a developer‑friendly documentation site covering quickstart, payload reference, and security guidelines.
image: https://socialhook.io/favicon.ico
layout: provider
modified: '2026-10-18'
name: Lead Lock Systems
nav: Providers
network: true
overview: 'Lead Lock Systems is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Webhook, Social Media, Integration, and Automation.


  The Lead Lock Systems catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Lead Lock Systems'' developer surface includes changelog, authentication, getting-started guide, pricing, engineering blog, support, and 16 more developer resources.'
plans:
- name: Socialhook Plans Pricing
  plan_count: 1
  slug: socialhook-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Socialhook Rate Limits
  slug: socialhook-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Lead Lock Systems API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: socialhook-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 53.8
    catalog_earned_first_party: 16.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 19.1
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 55.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
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
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Socialhook Authentication
  slug: socialhook-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Socialhook Domain Security
  slug: socialhook-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Socialhook Vulnerability Disclosure
  slug: socialhook-vulnerability-disclosure
  summary_line: no policy recorded
slug: socialhook
tags:
- Company
- Webhook
- Social Media
- Integration
- Automation
website: https://socialhook.io/
---
