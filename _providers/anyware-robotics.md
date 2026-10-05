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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anyware-robotics/refs/heads/main/hosts/anyware-robotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anyware-robotics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anyware-robotics/refs/heads/main/vendors/anyware-robotics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anyware-robotics-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://anyware-robotics.com/news/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.anyware-robotics.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anyware-robotics/refs/heads/main/security/anyware-robotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anyware-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anyware-robotics.com
coverage:
  checked: '2026-09-25'
  detail: The provider's website offers only marketing pages and no publicly accessible OpenAPI, GraphQL, or other machine‑readable API specifications.
  evidence:
  - status: 404
    url: https://anyware-robotics.com/openapi.json
  - status: 302
    url: https://dev.anyware-robotics.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Anyware Robotics builds and deploys advanced physical AI robots designed for the toughest industrial tasks. Their AnywareOS platform combines perception, motion planning, and autonomous decision‑making, allowing robots to collaborate safely with human workers, adapt to dynamic environments, and continuously learn from each operation. Solutions include palletizing, case picking, trailer loading, machine tending, and custom automation, all aimed at cutting labor costs, boosting productivity, and enhancing workplace safety across manufacturing, logistics, and warehousing sectors. The company also offers integration services, remote monitoring, and a developer ecosystem to extend robot capabilities.
layout: provider
modified: '2026-09-25'
name: Anyware Robotics
nav: Providers
network: true
overview: 'Anyware Robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Artificial Intelligence, Industrial Automation, Deployable Robots, and Manufacturing.


  Anyware Robotics'' developer surface includes documentation and 5 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anyware Robotics Domain Security
  slug: anyware-robotics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: anyware-robotics
tags:
- Robotics
- Artificial Intelligence
- Industrial Automation
- Deployable Robots
- Manufacturing
website: https://anyware-robotics.com
---
