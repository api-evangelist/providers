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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/tildei/plans/tildei-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tildei-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/tildei/llms/tildei-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tildei-llms.txt
- group: auth
  href: https://artifacts.apis.io/tildei/well-known/tildei-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tildei-www-security.txt
- group: auth
  href: https://artifacts.apis.io/tildei/well-known/tildei-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tildei-help-security.txt
- group: auth
  href: https://artifacts.apis.io/tildei/well-known/tildei-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tildei-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/tildei/well-known/tildei-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tildei-app-security.txt
- group: agent
  href: https://artifacts.apis.io/tildei/well-known/tildei-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tildei-well-known.yml
- group: other
  href: https://artifacts.apis.io/tildei/hosts/tildei-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tildei-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tildei
- group: auth
  href: https://artifacts.apis.io/tildei/security/tildei-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tildei-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tildei.com/
- group: company
  title: ''
  type: Blog
  url: https://www.runhappy.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.runhappy.ai/how-it-works
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.runhappy.ai/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.runhappy.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.runhappy.ai/contact
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.runhappy.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.runhappy.ai/
coverage:
  checked: '2026-10-29'
  detail: Notion pricing and docs pages require JavaScript rendering, preventing machine-readable access.
  evidence:
  - status: 200
    url: https://www.notion.com/pricing
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Tildei Inc. provides a platform for event and birthday party booking services, offering tools for venues to manage inquiries, bookings, and guest communications across multiple channels. The company focuses on seamless integration, real-time ROI calculations, and comprehensive support for corporate, group, and wedding events. Backed by Gradient Ventures, Tildei leverages secure cloud infrastructure and AI-driven analytics to enhance the event planning experience.
image: https://framerusercontent.com/images/QfBwM0Qi84Ris4ToDIYwyDmMA.png
layout: provider
modified: '2026-10-29'
name: Tildei
nav: Providers
network: true
overview: 'Tildei is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Event Management, Booking Platform, SaaS, AI Analytics, and Secure Cloud.


  Tildei''s developer surface includes engineering blog, documentation, support, pricing, and 14 more developer resources.'
plans:
- name: Tildei Plans Pricing
  plan_count: 4
  slug: tildei-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 15.8
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
  name: Tildei Domain Security
  slug: tildei-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tildei
tags:
- Event Management
- Booking Platform
- SaaS
- AI Analytics
- Secure Cloud
website: https://www.tildei.com/
---
