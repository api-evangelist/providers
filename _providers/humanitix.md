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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Public API for accessing events, orders, tickets and tags.
  name: Humanitix Public API
  slug: humanitix-public-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/humanitix/refs/heads/main/plans/humanitix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/humanitix-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/humanitix/refs/heads/main/conformance/humanitix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/humanitix-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/humanitix/refs/heads/main/llms/humanitix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/humanitix-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/humanitix/refs/heads/main/well-known/humanitix-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/humanitix-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/humanitix/refs/heads/main/well-known/humanitix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/humanitix-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/humanitix/refs/heads/main/hosts/humanitix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/humanitix-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/humanitix/refs/heads/main/vendors/humanitix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/humanitix-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.humanitix.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://humanitix.com/us/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://static.humanitix.com/pdfs/privacy_and_cookie_policy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://humanitix.com/us/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://humanitix.com/us/press
- group: company
  title: ''
  type: Blog
  url: https://humanitix.com/us/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.humanitix.com/en/articles/8889132-quick-start-guide-to-creating-an-event
- group: docs
  title: ''
  type: Documentation
  url: https://help.humanitix.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/humanitix/refs/heads/main/security/humanitix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/humanitix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://humanitix.com
created: '2026-10-13'
description: Humanitix is a ticketing platform that redirects 100% of booking fee profits to charitable causes, supporting education, health and community projects worldwide. Founded by Adam and Josh, it offers event organizers a socially responsible alternative, handling ticket sales, registrations and payments while providing a seamless experience for attendees. The service operates globally, with a focus on transparency, accessibility, and impact-driven events.
image: https://humanitix.com/social-sharing.jpg
layout: provider
modified: '2026-10-13'
name: Humanitix
nav: Providers
network: true
overview: 'Humanitix is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Ticketing, Non-Profit, Event, Platform, and Social Impact.


  Humanitix''s developer surface includes support, signup flow, pricing, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
plans:
- name: Humanitix Plans Pricing
  plan_count: 4
  slug: humanitix-plans-pricing
random_paper: 15
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Humanitix Domain Security
  slug: humanitix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: humanitix
tags:
- Ticketing
- Non-Profit
- Event
- Platform
- Social Impact
- Company
website: https://humanitix.com
---
