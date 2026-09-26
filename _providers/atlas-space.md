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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlas-space/refs/heads/main/hosts/atlas-space-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlas-space-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlas-space/refs/heads/main/security/atlas-space-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlas-space-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlasground.com/
- group: company
  title: ''
  type: Blog
  url: https://atlasspace.com/news/
- group: operate
  title: ''
  type: Support
  url: https://atlasspace.com/contact/
- group: docs
  title: ''
  type: Documentation
  url: https://atlasspace.com/solutions/
- group: start
  title: ''
  type: GettingStarted
  url: https://atlasspace.com/apply/
coverage:
  checked: 2026-09-23
  detail: Provider documentation is HTML only with no OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts discovered.
  evidence:
  - status: 200
    url: https://atlasspace.com/solutions/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-23'
description: ATLAS Space Operations provides a federated ground network and software-as-a-service solutions for satellite operations, including launch and early orbit phase (LEOP) support, commercial, civil, and federal space missions. The company offers Freedom Ground Software as a Service™ and a collaborative platform to manage ground station resources, enabling customers to streamline mission control, data downlink, and operational workflows across a global network.
image: https://atlasspace.com/wp-content/uploads/2023/08/ATLAS-Featured-Image-08_12_2023.png
layout: provider
modified: '2026-09-23'
name: ATLAS Space Operations
nav: Providers
network: true
overview: 'ATLAS Space Operations is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Software-as-a-Service, Ground-Network, and Satellite Operations.


  ATLAS Space Operations'' developer surface includes engineering blog, support, documentation, getting-started guide, and 3 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 10.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atlas Space Domain Security
  slug: atlas-space-domain-security
  summary_line: TLSv1.3 · HSTS
slug: atlas-space
tags:
- Company
- Space
- Software-as-a-Service
- Ground-Network
- Satellite Operations
website: https://atlasground.com/
---
