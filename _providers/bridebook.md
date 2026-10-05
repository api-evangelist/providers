---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.4
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Bridebook provides a wedding planning platform; API documentation is currently inaccessible due to Cloudflare access protection.
  name: Bridebook API
  slug: bridebook-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bridebook/refs/heads/main/llms/bridebook-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bridebook-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bridebook/refs/heads/main/well-known/bridebook-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bridebook-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bridebook/refs/heads/main/hosts/bridebook-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bridebook-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bridebook/refs/heads/main/vendors/bridebook-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bridebook-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.bridebook.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bridebook.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bridebook
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bridebook/refs/heads/main/security/bridebook-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bridebook-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bridebook.com
created: '2026-10-03'
description: Bridebook is a free online wedding planning platform that helps couples plan their weddings across 185 countries. It offers tools for budgeting, guest list management, vendor selection, and timeline creation. The service is featured by major media outlets such as Apple, The New York Times, and the BBC, and operates as a SaaS solution for the wedding industry.
image: https://media.bridebook.com/assets/bblogo_fb.jpg
layout: provider
modified: '2026-10-03'
name: Bridebook
nav: Providers
network: true
overview: 'Bridebook publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Wedding Planning, Online Planner, Free App, and Couples.


  Bridebook''s developer surface includes support, documentation, and 7 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bridebook Domain Security
  slug: bridebook-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bridebook
tags:
- Wedding Planning
- Online Planner
- Free App
- Couples
website: https://bridebook.com
---
