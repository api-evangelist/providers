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
- group: other
  href: https://artifacts.apis.io/buildcon-org/hosts/buildcon-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildcon-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/buildcon-org/vendors/buildcon-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buildcon-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buildcon.org/terms.pdf
- group: auth
  href: https://artifacts.apis.io/buildcon-org/security/buildcon-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildcon-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildcon.org
- group: company
  title: ''
  type: Blog
  url: https://buildcontech.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://buildcontech.com
created: '2026-10-25'
description: 'Buildcon (brand: BuildconTech) provides digital construction and logistics solutions, offering the Buildx platform for project tracking, supply chain management, and data-driven decision making. The company leverages extensive industry expertise to deliver software that streamlines construction workflows and optimizes logistics operations, serving clients across the UK and Europe. Their services include construction project management tools, logistics coordination, and consulting for digital transformation in the built environment.'
image: https://buildcontech.com/images/buildcon-construction-and-logistics.jpg
layout: provider
modified: '2026-10-25'
name: Buildcon
nav: Providers
network: true
overview: 'Buildcon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Logistics, Software, and DigitalTransformation.


  Buildcon''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Buildcon Org Domain Security
  slug: buildcon-org-domain-security
  summary_line: TLSv1.3 · DMARC
slug: buildcon-org
tags:
- Company
- Construction
- Logistics
- Software
- DigitalTransformation
website: https://buildcon.org
---
