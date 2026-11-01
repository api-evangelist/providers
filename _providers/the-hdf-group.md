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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: http://hsdshdflab.hdfgroup.org
  baseurl_source: declared
  description: RESTful API for HDF Scalable Data Service (HSDS)
  name: HSDS REST API
  slug: hsds-rest-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/the-hdf-group/llms/the-hdf-group-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/the-hdf-group-llms.txt
- group: auth
  href: https://artifacts.apis.io/the-hdf-group/well-known/the-hdf-group-hdfgroup-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/the-hdf-group-hdfgroup-security.txt
- group: agent
  href: https://artifacts.apis.io/the-hdf-group/well-known/the-hdf-group-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/the-hdf-group-well-known.yml
- group: other
  href: https://artifacts.apis.io/the-hdf-group/hosts/the-hdf-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/the-hdf-group-hosts.yml
- group: other
  href: https://artifacts.apis.io/the-hdf-group/vendors/the-hdf-group-vendors.yml
  title: ''
  type: Vendors
  url: vendors/the-hdf-group-vendors.yml
- group: build
  href: https://artifacts.apis.io/the-hdf-group/packages/the-hdf-group-packages.yml
  title: ''
  type: SDKs
  url: packages/the-hdf-group-packages.yml
- group: build
  href: https://artifacts.apis.io/the-hdf-group/packages/the-hdf-group-packages.yml
  title: ''
  type: Packages
  url: packages/the-hdf-group-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hdfgroup.org/status/services
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/HDFGroup/hsds/releases
- group: auth
  href: https://artifacts.apis.io/the-hdf-group/security/the-hdf-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-hdf-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hdfgroup.org
- group: docs
  title: ''
  type: Documentation
  url: https://support.hdfgroup.org/documentation/
- group: company
  title: ''
  type: Blog
  url: https://www.hdfgroup.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HDFGroup
- group: operate
  title: ''
  type: Support
  url: https://support.hdfgroup.org
- group: docs
  title: ''
  type: APIReference
  url: https://support.hdfgroup.org/documentation/hdf5/latest/
created: '2026-10-28'
description: The HDF Group is a nonprofit organization dedicated to ensuring long‑term access and usability of HDF data. It develops and maintains the HDF5® library, HDF5® Server, HDF® View, and related tools, providing services such as priority support, training, cloud‑native HDF5 (HSDS), data conversion, and consulting. With over 25 years of experience, the group supports a global community of scientists and engineers through open‑source software, documentation, webinars, and community forums, fostering efficient and equitable data management across platforms.
layout: provider
modified: '2026-10-28'
name: The HDF Group
nav: Providers
network: true
overview: 'The HDF Group is listed with 1 API on the [APIs.io](https://apis.io/) network: HSDS REST API. Tagged areas include Company, Data Management, Open Source, Scientific Computing, and Nonprofit.


  The HDF Group''s developer surface includes changelog, documentation, engineering blog, support, API reference, and 11 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 37.6
    developer_ergonomics: 31.0
    discoverability: 62.5
    operational_transparency: 47.4
  provenance:
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
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: The Hdf Group Domain Security
  slug: the-hdf-group-domain-security
  summary_line: TLSv1.3 · DMARC
slug: the-hdf-group
tags:
- Company
- Data Management
- Open Source
- Scientific Computing
- Nonprofit
website: https://www.hdfgroup.org
---
