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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/deepstream/hosts/deepstream-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepstream-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepstream/vendors/deepstream-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepstream-vendors.yml
- group: build
  href: https://artifacts.apis.io/deepstream/packages/deepstream-packages.yml
  title: ''
  type: SDKs
  url: packages/deepstream-packages.yml
- group: build
  href: https://artifacts.apis.io/deepstream/packages/deepstream-packages.yml
  title: ''
  type: Packages
  url: packages/deepstream-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepstreamIO
- group: start
  title: ''
  type: GettingStarted
  url: https://deepstream.io/tutorials/getting-started/javascript/
- group: docs
  title: ''
  type: Documentation
  url: https://deepstream.io/docs/
- group: company
  title: ''
  type: Blog
  url: https://deepstream.io/blog/
- group: auth
  href: https://artifacts.apis.io/deepstream/security/deepstream-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepstream-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deepstream.io/
coverage:
  checked: '2026-10-20'
  detail: The provider’s documentation site offers only HTML pages with no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://deepstream.io/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: deepstreamHub GmbH provides deepstream.io, an open‑source real‑time server for mobile, web and IoT applications. It enables clients and backend services to sync data, publish events, perform RPCs and monitor presence with a strong focus on security and scalability. The platform supports multiple client libraries (JavaScript, Java, HTTP) and integrates with various databases, caches and message buses, offering flexible configuration without writing extensive code.
layout: provider
modified: '2026-10-20'
name: deepstreamhub
nav: Providers
network: true
overview: 'deepstreamhub is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Time, Open Source, Data Sync, IoT, and Security.


  deepstreamhub''s developer surface includes getting-started guide, documentation, engineering blog, and 7 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 0
  name: Deepstream Rate Limits
  slug: deepstream-rate-limits
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 44.6
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
  name: Deepstream Domain Security
  slug: deepstream-domain-security
  summary_line: TLSv1.3
slug: deepstream
tags:
- Real-Time
- Open Source
- Data Sync
- IoT
- Security
website: https://deepstream.io/
---
