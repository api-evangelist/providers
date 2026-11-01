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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 18.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/daxko/authentication/daxko-authentication.yml
  title: ''
  type: Authentication
  url: authentication/daxko-authentication.yml
- group: auth
  href: https://artifacts.apis.io/daxko/well-known/daxko-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/daxko-status-security.txt
- group: agent
  href: https://artifacts.apis.io/daxko/well-known/daxko-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/daxko-well-known.yml
- group: other
  href: https://artifacts.apis.io/daxko/hosts/daxko-hosts.yml
  title: ''
  type: Hosts
  url: hosts/daxko-hosts.yml
- group: other
  href: https://artifacts.apis.io/daxko/vendors/daxko-vendors.yml
  title: ''
  type: Vendors
  url: vendors/daxko-vendors.yml
- group: build
  href: https://artifacts.apis.io/daxko/packages/daxko-packages.yml
  title: ''
  type: SDKs
  url: packages/daxko-packages.yml
- group: build
  href: https://artifacts.apis.io/daxko/packages/daxko-packages.yml
  title: ''
  type: Packages
  url: packages/daxko-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.daxko.com/s/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.daxko.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.partners.daxko.com/tutorials/club_automation_getting_started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.partners.daxko.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/daxko
- group: auth
  href: https://artifacts.apis.io/daxko/security/daxko-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daxko-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://daxko.com/
created: '2026-10-27'
description: Daxko provides cloud‑based software solutions for YMCAs, community centers, and other nonprofit fitness organizations. Its platform includes membership management, facility scheduling, payments, marketing automation, and analytics, helping operators streamline operations and improve member experiences. Daxko serves a broad range of clients across the United States, offering integrated tools for clubs, gyms, and wellness programs.
image: https://daxkocms.wpenginepowered.com/wp-content/uploads/2024/06/old-logo.png
layout: provider
modified: '2026-10-27'
name: Daxko
nav: Providers
network: true
overview: 'Daxko is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, Fitness, Nonprofit, and SaaS.


  Daxko''s developer surface includes authentication, support, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 48.2
    operational_transparency: 31.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Daxko Authentication
  slug: daxko-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Daxko Domain Security
  slug: daxko-domain-security
  summary_line: TLSv1.3 · DMARC
slug: daxko
tags:
- Company
- Software
- Fitness
- Nonprofit
- SaaS
website: https://daxko.com/
---
