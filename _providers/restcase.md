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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: RestCase provides a design-first API development platform with tools for API design, documentation, testing, and governance.
  name: RestCase API
  slug: restcase-api
artifact_total: 2
common:
- group: company
  title: ''
  type: Blog
  url: https://blog.restcase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.restcase.com/
- group: other
  href: https://artifacts.apis.io/restcase/hosts/restcase-hosts.yml
  title: ''
  type: Hosts
  url: hosts/restcase-hosts.yml
- group: other
  href: https://artifacts.apis.io/restcase/vendors/restcase-vendors.yml
  title: ''
  type: Vendors
  url: vendors/restcase-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Restcase
- group: auth
  href: https://artifacts.apis.io/restcase/security/restcase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/restcase-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://restcase.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.restcase.com/
coverage:
  checked: '2026-10-21'
  detail: OpenAPI spec endpoint https://api.restcase.com/openapi.json returned HTTP 530, no machine‑readable contract found.
  evidence:
  - status: 530
    url: https://api.restcase.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: RestCase provides a design-first API development platform that supercharges the API development process, resulting in improved team collaboration, reduced development time, better testing, and increased overall productivity. It offers tools for API design, documentation, testing, and governance, helping teams build high-quality APIs faster.
image: https://www.restcase.com/assets/images/restcase_post_logo.png
layout: provider
modified: '2026-10-21'
name: Guy Levin
nav: Providers
network: true
overview: 'Guy Levin is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Development, Design-First, Collaboration, Productivity, and Platform.


  Guy Levin''s developer surface includes engineering blog, documentation, and 6 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Restcase Domain Security
  slug: restcase-domain-security
  summary_line: TLSv1.3
slug: restcase
tags:
- API Development
- Design-First
- Collaboration
- Productivity
- Platform
- Company
website: https://restcase.com/
---
