---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/prospr/llms/prospr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/prospr-llms.txt
- group: other
  href: https://artifacts.apis.io/prospr/hosts/prospr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prospr-hosts.yml
- group: other
  href: https://artifacts.apis.io/prospr/vendors/prospr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prospr-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.prospr.work/
- group: auth
  href: https://artifacts.apis.io/prospr/security/prospr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prospr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prospr.work
- group: company
  title: ''
  type: Blog
  url: https://prospr.work/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://prospr.work/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://prospr.work/customer-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prospr.work/privacy
- group: operate
  title: ''
  type: Support
  url: https://help.prospr.work
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://prospr.work/mcp
  - status: 200
    url: https://prospr.work
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Prospr provides a frontline management toolkit for businesses, offering communication bulletins, ticketing, scheduling, knowledge base, and time‑tracking solutions. It serves retail, hospitality, food‑beverage, and other industries, enabling teams to collaborate, manage tasks, and streamline operations through a unified SaaS platform.
image: https://prospr.work/app_icon_rounded.png
layout: provider
modified: '2026-10-21'
name: Prospr
nav: Providers
network: true
overview: 'Prospr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SaaS, Frontline Management, Collaboration, and Scheduling.


  Prospr''s developer surface includes documentation, engineering blog, pricing, support, and 7 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Prospr Domain Security
  slug: prospr-domain-security
  summary_line: TLSv1.3
slug: prospr
tags:
- Company
- SaaS
- Frontline Management
- Collaboration
- Scheduling
website: https://prospr.work
---
