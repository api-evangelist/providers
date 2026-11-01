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
api_count: 1
apis:
- description: The FamilySearch API provides programmatic access to genealogical data, records search, and family tree management as documented on the developer portal.
  name: FamilySearch API
  slug: familysearch-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/familysearch/vendors/familysearch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/familysearch-vendors.yml
- group: agent
  href: https://artifacts.apis.io/familysearch/llms/familysearch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/familysearch-llms.txt
- group: agent
  href: https://artifacts.apis.io/familysearch/well-known/familysearch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/familysearch-well-known.yml
- group: other
  href: https://artifacts.apis.io/familysearch/hosts/familysearch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/familysearch-hosts.yml
- group: build
  href: https://artifacts.apis.io/familysearch/packages/familysearch-packages.yml
  title: ''
  type: SDKs
  url: packages/familysearch-packages.yml
- group: build
  href: https://artifacts.apis.io/familysearch/packages/familysearch-packages.yml
  title: ''
  type: Packages
  url: packages/familysearch-packages.yml
- group: start
  title: ''
  type: Login
  url: https://community.familysearch.org/en/discussions/tagged/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://developers.familysearch.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FamilySearch
- group: auth
  href: https://artifacts.apis.io/familysearch/security/familysearch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/familysearch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://familysearch.org/
coverage:
  checked: '2026-10-28'
  detail: Developer portal at https://developers.familysearch.org/ is a React app with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://developers.familysearch.org/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: FamilySearch provides a free, nonprofit genealogy platform that allows users to build, share, and explore family trees. It offers access to billions of historical records and a suite of tools for family history research. The service includes APIs that enable developers to integrate FamilySearch data and functionality into applications, supporting tasks such as searching records, retrieving person information, and managing family tree data.
layout: provider
modified: '2026-10-28'
name: FamilySearch Family Tree download + WebHints
nav: Providers
network: true
overview: 'FamilySearch Family Tree download + WebHints is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Genealogy, Family History, Nonprofit, API, and Data.


  FamilySearch Family Tree download + WebHints'' developer surface includes documentation and 10 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 53.6
    operational_transparency: 5.3
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
  name: Familysearch Domain Security
  slug: familysearch-domain-security
  summary_line: TLSv1.2 · DMARC
slug: familysearch
tags:
- Genealogy
- Family History
- Nonprofit
- API
- Data
website: https://familysearch.org/
---
