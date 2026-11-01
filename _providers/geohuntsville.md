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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API information not publicly documented
  name: GEOHuntsville API
  slug: geohuntsville-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/geohuntsville/llms/geohuntsville-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/geohuntsville-llms.txt
- group: other
  href: https://artifacts.apis.io/geohuntsville/hosts/geohuntsville-hosts.yml
  title: ''
  type: Hosts
  url: hosts/geohuntsville-hosts.yml
- group: other
  href: https://artifacts.apis.io/geohuntsville/vendors/geohuntsville-vendors.yml
  title: ''
  type: Vendors
  url: vendors/geohuntsville-vendors.yml
- group: auth
  href: https://artifacts.apis.io/geohuntsville/security/geohuntsville-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geohuntsville-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.geohuntsville.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.geohuntsville.org/about
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.geohuntsville.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.geohuntsville.org/conference
coverage:
  checked: '2026-10-26'
  detail: The provider's website returns HTML without machine‑readable API specifications or documentation pages.
  evidence:
  - status: 200
    url: https://www.geohuntsville.org/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: GEOHuntsville is a nonprofit organization based in Huntsville, Alabama, dedicated to advancing geospatial innovation, workforce development, and practical solutions for the community and nation. Founded in 2012 as part of the Exemplar City initiative, it unites government, industry, and academia to foster collaboration, education, and economic growth through geospatial technologies, supporting initiatives like the Blueprint for Safety and hosting events such as the GEOHuntsville Summit.
image: https://static.wixstatic.com/media/ebdde2_4a8ce921ed59402e898e4ab645c091d2%7Emv2.png/v1/fit/w_2500,h_1330,al_c/ebdde2_4a8ce921ed59402e898e4ab645c091d2%7Emv2.png
layout: provider
modified: '2026-10-26'
name: GEOHuntsville
nav: Providers
network: true
overview: 'GEOHuntsville is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geospatial, Nonprofit, Community, and Innovation.


  GEOHuntsville''s developer surface includes documentation, getting-started guide, and 6 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 10.5
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
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Geohuntsville Domain Security
  slug: geohuntsville-domain-security
  summary_line: TLSv1.3 · HSTS
slug: geohuntsville
tags:
- Company
- Geospatial
- Nonprofit
- Community
- Innovation
website: https://www.geohuntsville.org/
---
