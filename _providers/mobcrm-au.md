---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://mobcrm.au/api/v1
  baseurl_source: declared
  description: Public REST API for Mob CRM, providing access to contacts, notes, and relationships.
  name: Mob CRM API
  slug: mob-crm-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/mobcrm-au/conformance/mobcrm-au-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mobcrm-au-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mobcrm-au/well-known/mobcrm-au-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mobcrm-au-well-known.yml
- group: other
  href: https://artifacts.apis.io/mobcrm-au/hosts/mobcrm-au-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mobcrm-au-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://mobcrm.au/web/login
- group: auth
  href: https://artifacts.apis.io/mobcrm-au/security/mobcrm-au-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mobcrm-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mobcrm.au/
- group: docs
  title: ''
  type: Documentation
  url: https://mobcrm.au/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://mobcrm.au/#pricing
- group: operate
  title: ''
  type: Support
  url: mailto:mobsupport@benkaiser.dev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/benkaiser/mob-mcp-crm
created: '2026-10-30'
description: Mob is a personal customer relationship management (CRM) platform that helps users capture and organize information about the people in their lives—notes, reminders, birthdays, and relationships—using natural language input. It includes native MCP (Mobile Cloud Platform) support, allowing seamless integration with mobile devices. The service offers documentation, pricing plans, and open‑source code on GitHub, providing a comprehensive tool for personal productivity and contact management.
image: https://mobcrm.au/app/icons/icon.svg
layout: provider
modified: '2026-10-30'
name: mobcrm-au
nav: Providers
network: true
overview: 'mobcrm-au is listed with 1 API on the [APIs.io](https://apis.io/) network: Mob CRM API. Tagged areas include CRM, Personal Productivity, Mobile, Open Source, and Contact Management.


  mobcrm-au''s developer surface includes documentation, pricing, support, and 7 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 32.9
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mobcrm Au Domain Security
  slug: mobcrm-au-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mobcrm-au
tags:
- CRM
- Personal Productivity
- Mobile
- Open Source
- Contact Management
website: https://mobcrm.au/
---
