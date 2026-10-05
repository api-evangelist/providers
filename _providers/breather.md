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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/breather/refs/heads/main/plans/breather-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/breather-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breather/refs/heads/main/hosts/breather-hosts.yml
  title: ''
  type: Hosts
  url: hosts/breather-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breather/refs/heads/main/vendors/breather-vendors.yml
  title: ''
  type: Vendors
  url: vendors/breather-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.breather.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.breather.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/breather
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breather/refs/heads/main/security/breather-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breather-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.breather.com
- group: other
  title: ''
  type: Image
  url: https://www.breather.com/assets/svg/breather_logo.svg
coverage:
  checked: '2026-10-03'
  detail: No public developer program or API documentation was found on breather.com.
  evidence:
  - status: 200
    url: https://www.breather.com
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Breather provides on-demand access to a global network of coworking spaces, meeting rooms, and private offices. Users can book desks, conference rooms, or entire offices by the hour, day, or month across more than 260 cities in 20 countries. The platform offers flexible pricing, a seamless reservation experience, and integrates with Deskpass for unified account management, catering to individuals, small businesses, and large enterprises seeking productive work environments.
image: https://transforms.breather.com/production/gen/breather-socialshare.jpg?w=1200&h=630&q=82&auto=format%2Cavif&fit=crop&dm=1721599804&s=3fedc8f615db2e868218fd304bb6bdac
layout: provider
modified: '2026-10-03'
name: Breather
nav: Providers
network: true
overview: 'Breather is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workspace, Booking, On-Demand, and Global.


  Breather''s developer surface includes pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Breather Plans Pricing
  plan_count: 3
  slug: breather-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Breather Domain Security
  slug: breather-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: breather
tags:
- Company
- Workspace
- Booking
- On-Demand
- Global
website: https://www.breather.com
---
