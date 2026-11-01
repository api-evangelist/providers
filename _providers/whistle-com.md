---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/whistle-com/plans/whistle-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/whistle-com-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://tractive.com/en/l/vulnerability-disclosure
- group: agent
  href: https://artifacts.apis.io/whistle-com/llms/whistle-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/whistle-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/whistle-com/well-known/whistle-com-tractive-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/whistle-com-tractive-security.txt
- group: agent
  href: https://artifacts.apis.io/whistle-com/well-known/whistle-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/whistle-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/whistle-com/hosts/whistle-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/whistle-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/whistle-com/vendors/whistle-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/whistle-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assets.tractive.com/static/legal/en-us/terms-of-service.pdf
- group: operate
  title: ''
  type: Support
  url: https://help.tractive.com/hc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://assets.tractive.com/static/legal/en/privacy-policy.pdf
- group: commercial
  title: ''
  type: Pricing
  url: https://tractive.com/en/c/plans
- group: company
  title: ''
  type: Newsroom
  url: https://tractive.com/en/pr/press
- group: company
  title: ''
  type: Blog
  url: https://tractive.com/blog/en/
- group: docs
  title: ''
  type: Documentation
  url: https://help.tractive.com/
- group: auth
  href: https://artifacts.apis.io/whistle-com/security/whistle-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/whistle-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/whistle-com/security/whistle-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whistle-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whistle.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://whistle.com/mcp
  - status: 401
    url: https://help.tractive.com/mcp
  - status: 200
    url: https://whistle.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Tractive sells GPS tracking and health monitoring devices for dogs and cats. The smart trackers provide real‑time location, virtual fences, health insights, bark and scratch monitoring, and waterproof designs for pets of various sizes. Tractive markets these products directly to pet owners worldwide.
image: https://assets.tractive.com/assets/image/shop-frontend/og-images/tractive-dog-4-og.jpg
layout: provider
modified: '2026-10-24'
name: whistle
nav: Providers
network: true
overview: 'whistle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pet GPS, Pet Health Monitoring, Animal Tracking, and Pet Safety.


  whistle''s developer surface includes support, pricing, engineering blog, documentation, and 13 more developer resources.'
plans:
- name: Whistle Com Plans Pricing
  plan_count: 9
  slug: whistle-com-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 41.1
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Whistle Com Domain Security
  slug: whistle-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Whistle Com Vulnerability Disclosure
  slug: whistle-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: whistle-com
tags:
- Pet GPS
- Pet Health Monitoring
- Animal Tracking
- Pet Safety
website: https://whistle.com
---
