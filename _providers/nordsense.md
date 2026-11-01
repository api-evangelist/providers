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
  href: https://artifacts.apis.io/nordsense/vendors/nordsense-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nordsense-vendors.yml
- group: other
  href: https://artifacts.apis.io/nordsense/hosts/nordsense-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nordsense-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nordsense.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://nordsense.com/press/
- group: start
  title: ''
  type: Login
  url: https://nordsense.com/log-in/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.nordsense.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nordsense
- group: auth
  href: https://artifacts.apis.io/nordsense/security/nordsense-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nordsense-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nordsense.com
coverage:
  checked: '2026-10-22'
  detail: The provider's website does not expose any machine‑readable API contract such as OpenAPI, GraphQL SDL, or WSDL.
  evidence:
  - status: 200
    url: https://nordsense.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Nordsense provides smart sensor solutions for waste management, delivering real‑time data insights to municipalities and businesses. Their IoT‑enabled smart bin sensors track fill levels, location, and routing, helping reduce carbon emissions, increase recycling rates, and improve operational transparency. By digitizing waste collection, Nordsense enables data‑driven decisions that optimize routes, lower fuel use, and enhance sustainability outcomes across urban environments.
image: https://nordsense.com/wp-content/uploads/2023/05/Site-Image.png
layout: provider
modified: '2026-10-22'
name: Nordsense
nav: Providers
network: true
overview: 'Nordsense is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sensors, WasteManagement, IoT, and DataInsights.


  Nordsense''s developer surface includes documentation and 8 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 5.3
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
  name: Nordsense Domain Security
  slug: nordsense-domain-security
  summary_line: TLSv1.2
slug: nordsense
tags:
- Company
- Sensors
- WasteManagement
- IoT
- DataInsights
website: https://nordsense.com
---
