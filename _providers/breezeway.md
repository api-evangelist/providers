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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Breezeway Webhooks
  slug: breezeway-webhooks
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/breezeway/refs/heads/main/plans/breezeway-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/breezeway-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/breezeway/refs/heads/main/asyncapi/breezeway-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/breezeway-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breezeway/refs/heads/main/authentication/breezeway-authentication.yml
  title: ''
  type: Authentication
  url: authentication/breezeway-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/breezeway/refs/heads/main/llms/breezeway-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/breezeway-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breezeway/refs/heads/main/well-known/breezeway-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/breezeway-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/breezeway/refs/heads/main/well-known/breezeway-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/breezeway-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breezeway/refs/heads/main/hosts/breezeway-hosts.yml
  title: ''
  type: Hosts
  url: hosts/breezeway-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breezeway/refs/heads/main/vendors/breezeway-vendors.yml
  title: ''
  type: Vendors
  url: vendors/breezeway-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/breezeway/refs/heads/main/packages/breezeway-packages.yml
  title: ''
  type: SDKs
  url: packages/breezeway-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/breezeway/refs/heads/main/packages/breezeway-packages.yml
  title: ''
  type: Packages
  url: packages/breezeway-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.breezeway.io/terms?hsLang=en
- group: operate
  title: ''
  type: Support
  url: https://help.breezeway.io/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.breezeway.io/privacy?hsLang=en
- group: company
  title: ''
  type: Newsroom
  url: https://www.breezeway.io/it/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.breezeway.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.breezeway.io/it/blog
- group: docs
  title: ''
  type: APIReference
  url: https://developer.breezeway.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.breezeway.io/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.breezeway.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breezeway/refs/heads/main/security/breezeway-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breezeway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.breezeway.io
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://developer.breezeway.io/mcp
  - status: 403
    url: https://www.breezeway.io/mcp
  - status: 403
    url: https://app.breezeway.io/mcp
  - status: 403
    url: https://equityzen.com/company/breezeway
  reason: partner-login
  state: gated
created: '2026-10-03'
description: Breezeway provides a property care, operations, and messaging platform for short‑term rentals, hotels, and corporate housing. Their SaaS solution automates tasks such as cleaning checklists, maintenance work orders, guest verification, inventory tracking, payments to cleaners, and integrates with smart locks and other property tech. The platform aims to streamline operations, improve guest experience, and give property managers real‑time insights and reporting.
layout: provider
modified: '2026-10-03'
name: Breezeway
nav: Providers
network: true
overview: 'Breezeway is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Software-as-a-Service, Operations Automation, Guest Experience, and Real Estate.


  The Breezeway catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Breezeway''s developer surface includes authentication, support, changelog, engineering blog, API reference, getting-started guide, documentation, and 14 more developer resources.'
plans:
- name: Breezeway Plans Pricing
  plan_count: 6
  slug: breezeway-plans-pricing
random_paper: 6
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 54.8
    discoverability: 53.6
    operational_transparency: 23.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Breezeway Authentication
  slug: breezeway-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Breezeway Domain Security
  slug: breezeway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: breezeway
tags:
- Property Management
- Software-as-a-Service
- Operations Automation
- Guest Experience
- Real Estate
website: https://www.breezeway.io
---
