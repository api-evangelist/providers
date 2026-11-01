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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/onevizion/well-known/onevizion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/onevizion-well-known.yml
- group: other
  href: https://artifacts.apis.io/onevizion/hosts/onevizion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/onevizion-hosts.yml
- group: other
  href: https://artifacts.apis.io/onevizion/vendors/onevizion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/onevizion-vendors.yml
- group: build
  href: https://artifacts.apis.io/onevizion/packages/onevizion-packages.yml
  title: ''
  type: SDKs
  url: packages/onevizion-packages.yml
- group: build
  href: https://artifacts.apis.io/onevizion/packages/onevizion-packages.yml
  title: ''
  type: Packages
  url: packages/onevizion-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onevizion.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://onevizion.com/press/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.onevizion.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Onevizion
- group: auth
  href: https://artifacts.apis.io/onevizion/security/onevizion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onevizion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onevizion.com/
coverage:
  checked: '2026-10-21'
  detail: OneVizion's website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://onevizion.com
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: OneVizion provides an AI‑ready operations platform that serves as the operational backbone for telecom and utility infrastructure programs worldwide. It eliminates fragmented data, creates full program visibility, and enables efficient management of critical infrastructure deployments and maintenance across the nation.
image: https://onevizion.com/wp-content/uploads/2026/06/Social-Homepage.jpg
layout: provider
modified: '2026-10-21'
name: OneVizion
nav: Providers
network: true
overview: 'OneVizion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Infrastructure, Telecommunications, and Utilities.


  OneVizion''s developer surface includes documentation and 10 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 12.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Onevizion Domain Security
  slug: onevizion-domain-security
  summary_line: TLSv1.3 · DMARC
slug: onevizion
tags:
- Company
- Artificial Intelligence
- Infrastructure
- Telecommunications
- Utilities
website: https://onevizion.com/
---
