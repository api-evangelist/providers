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
- description: Provides access to event details, RSVPs, tickets, menus, pricing, and music information.
  name: Details API
  slug: details-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/details-page/plans/details-page-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/details-page-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/details-page/llms/details-page-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/details-page-llms.txt
- group: other
  href: https://artifacts.apis.io/details-page/hosts/details-page-hosts.yml
  title: ''
  type: Hosts
  url: hosts/details-page-hosts.yml
- group: other
  href: https://artifacts.apis.io/details-page/vendors/details-page-vendors.yml
  title: ''
  type: Vendors
  url: vendors/details-page-vendors.yml
- group: auth
  href: https://artifacts.apis.io/details-page/security/details-page-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/details-page-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://details.page/
- group: commercial
  title: ''
  type: Pricing
  url: https://details.page/pricing
- group: start
  title: ''
  type: SignUp
  url: https://details.page/account/auth
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec was found on any discovered host.
  evidence:
  - status: 404
    url: https://details.page/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: details.page is a platform that aggregates and presents event details, RSVPs, tickets, menus, pricing, and music information on a single page. It offers free starter access and allows users to create and share detailed pages for various activities, integrating images and social sharing features. The service aims to simplify event management and information dissemination for organizers and attendees alike, providing a centralized hub for all relevant details.
image: https://details.page/images/heroes/og-home.png
layout: provider
modified: '2026-11-05'
name: details.page
nav: Providers
network: true
overview: 'details.page is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Platform, Event Management, Aggregator, RSVP, and Free.


  details.page''s developer surface includes pricing, signup flow, and 6 more developer resources.'
plans:
- name: Details Page Plans Pricing
  plan_count: 2
  slug: details-page-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Details Page Domain Security
  slug: details-page-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: details-page
tags:
- Platform
- Event Management
- Aggregator
- RSVP
- Free
website: https://details.page/
---
