---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
- description: Control-plane API providing status and boundaries for the BlinkHost platform. Documented at https://blinkhost.me/docs/reference/control-plane-api. No public machine‑readable contract was found.
  name: BlinkHost Control-plane API
  slug: blinkhost-control-plane-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/blinkhost-me/plans/blinkhost-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blinkhost-me-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/blinkhost-me/changelog/blinkhost-me-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/blinkhost-me-changelog.yml
- group: agent
  href: https://artifacts.apis.io/blinkhost-me/llms/blinkhost-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blinkhost-me-llms.txt
- group: other
  href: https://artifacts.apis.io/blinkhost-me/hosts/blinkhost-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blinkhost-me-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blinkhost.me/legal/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://blinkhost.me/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blinkhost.me/legal/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.blinkhost.me/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blinkhost-ltd
- group: start
  title: ''
  type: DeveloperPortal
  url: https://blinkhost.me/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://blinkhost.me/docs/releases
- group: docs
  title: ''
  type: APIReference
  url: https://blinkhost.me/docs/reference/control-plane-api
- group: start
  title: ''
  type: GettingStarted
  url: https://blinkhost.me/docs/get-started/developer-quickstart
- group: auth
  href: https://artifacts.apis.io/blinkhost-me/security/blinkhost-me-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blinkhost-me-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blinkhost-me/security/blinkhost-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blinkhost-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blinkhost.me/
- group: docs
  title: ''
  type: Documentation
  url: https://blinkhost.me/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://blinkhost.me/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://blinkhost.me/status
created: '2026-10-30'
description: BlinkHost provides a full‑stack delivery platform for developers and agencies, offering integrated frontend, backend, data, and edge deployment tools. The service enables building, previewing, and deploying applications with managed runtimes for Rust, Go, and Python, custom domains, live‑stack previews, and comprehensive observability. It targets modern web developers seeking streamlined, end‑to‑end workflows across multiple regions.
image: https://blinkhost.me/opengraph-image?ec559ed6fc2d7201
layout: provider
modified: '2026-10-30'
name: blinkhost-me
nav: Providers
network: true
overview: 'blinkhost-me is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Platform, Full-Stack, Developer Tools, and Edge Deployment.


  blinkhost-me''s developer surface includes changelog, API reference, getting-started guide, documentation, pricing, and 14 more developer resources.'
plans:
- name: Blinkhost Me Plans Pricing
  plan_count: 4
  slug: blinkhost-me-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.9
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 23.7
  previous_composite: 35.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/blinkhost-me/blinkhost-me-2026-11-03T121935.png
security:
- kind: domain-security
  name: Blinkhost Me Domain Security
  slug: blinkhost-me-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Blinkhost Me Vulnerability Disclosure
  slug: blinkhost-me-vulnerability-disclosure
  summary_line: no policy recorded
slug: blinkhost-me
tags:
- Company
- Platform
- Full-Stack
- Developer Tools
- Edge Deployment
website: https://blinkhost.me/
---
