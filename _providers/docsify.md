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
    agent_skills: unknown
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Docsify is a lightweight, no-build documentation site generator that turns Markdown files into a website on the fly using client-side JavaScript rendering.
  name: Docsify
  slug: docsify
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/docsify/refs/heads/main/plans/docsify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docsify-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/docsify/refs/heads/main/rate-limits/docsify-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/docsify-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/docsify/refs/heads/main/finops/docsify-finops.yml
  title: ''
  type: FinOps
  url: finops/docsify-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/docsify/refs/heads/main/security/docsify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docsify-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/docsify
- group: company
  title: ''
  type: Website
  url: https://docsify.js.org
- group: docs
  title: ''
  type: Documentation
  url: https://docsify.js.org/#/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/docsifyjs
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/docsifyjs/docsify-skill
created: '2026-03-25'
description: Docsify is a lightweight, no-build documentation site generator that turns Markdown files into a website on the fly using client-side JavaScript rendering.
finops:
- has_sources: false
  method: generated
  name: Docsify Finops
  primary_unit: ''
  service_category: API
  slug: docsify-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/docsify.png
layout: provider
modified: '2026-05-19'
name: Docsify
nav: Providers
network: true
overview: 'Docsify is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Documentation and Static Site Generators.


  Docsify''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Docsify Plans Pricing
  plan_count: 3
  slug: docsify-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Docsify Rate Limits
  slug: docsify-rate-limits
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 28.0
    catalog_earned_first_party: 0.0
    catalog_gap: 87.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.1
    discoverability: 39.3
    operational_transparency: 10.5
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/docsify/refs/heads/main/screenshots/docsify-2026-06-20T180111.png
security:
- kind: domain-security
  name: Docsify Domain Security
  slug: docsify-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: docsify
  slug: docsify
slug: docsify
tags:
- Documentation
- Static Site Generators
website: https://docsify.js.org
---
