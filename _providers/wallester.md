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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: Wallester provides card issuing and payment APIs as described on their pricing page.
  name: Wallester API
  slug: wallester-api
artifact_total: 2
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wallester.com/legal-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wallester.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wallester.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://wallester.com/business/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://wallester.com/media
- group: start
  title: ''
  type: Login
  url: https://wallester.com/sign-in
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wallester/refs/heads/main/llms/wallester-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wallester-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wallester/refs/heads/main/security/wallester-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wallester-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wallester.com/
coverage:
  checked: 2026-09-20
  detail: Pricing page loads a heavy JavaScript app with no direct OpenAPI spec discovered.
  evidence:
  - status: 404
    url: https://api.wallester.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-20'
description: Wallester provides a modern card issuing platform that enables businesses to embed financial services directly into their products. Through a robust set of APIs, Wallester offers virtual and physical card issuance, transaction processing, compliance, and risk management tools. Their solution targets fintechs, marketplaces, and SaaS platforms seeking to integrate payment capabilities without building banking infrastructure from scratch. With global coverage and customizable workflows, Wallester aims to simplify the complexities of card issuance and payments for developers and enterprises alike.
layout: provider
modified: '2026-09-20'
name: Wallester
nav: Providers
network: true
overview: 'Wallester publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Card Issuing, Fintech, and API Platform.


  Wallester''s developer surface includes pricing and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 7.5
    developer_ergonomics: 0.0
    discoverability: 55.6
    operational_transparency: 15.8
  previous_composite: 16.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Wallester Domain Security
  slug: wallester-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: wallester
tags:
- Company
- Payments
- Card Issuing
- Fintech
- API Platform
website: https://wallester.com/
---
