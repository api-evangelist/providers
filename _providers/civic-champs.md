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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Volunteer management platform API (no public machine-readable contract found)
  name: Civic Champs API
  slug: civic-champs-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/civic-champs/plans/civic-champs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/civic-champs-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/civic-champs/hosts/civic-champs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/civic-champs-hosts.yml
- group: other
  href: https://artifacts.apis.io/civic-champs/vendors/civic-champs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/civic-champs-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://www.civicchamps.com/libraries
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.civicchamps.com/privacypolicy
- group: auth
  href: https://artifacts.apis.io/civic-champs/security/civic-champs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/civic-champs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://civicchamps.com/
- group: company
  title: ''
  type: Blog
  url: https://www.civicchamps.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.civicchamps.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.civicchamps.com/
- group: operate
  title: ''
  type: Support
  url: https://www.civicchamps.com/faq
created: '2026-10-27'
description: Civic Champs provides volunteer management software that helps nonprofits recruit, engage, and coordinate volunteers. Their platform offers tools for scheduling, communication, reporting, and volunteer profile management, aiming to reduce recruitment effort by up to 85% and streamline volunteer operations for organizations of all sizes.
layout: provider
modified: '2026-10-27'
name: Civic Champs
nav: Providers
network: true
overview: 'Civic Champs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Volunteer Management, Nonprofit Software, SaaS, and Community.


  Civic Champs'' developer surface includes engineering blog, pricing, documentation, support, and 7 more developer resources.'
plans:
- name: Civic Champs Plans Pricing
  plan_count: 19
  slug: civic-champs-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 53.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Civic Champs Domain Security
  slug: civic-champs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: civic-champs
tags:
- Company
- Volunteer Management
- Nonprofit Software
- SaaS
- Community
website: https://civicchamps.com/
---
