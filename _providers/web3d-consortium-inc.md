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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/web3d-consortium-inc/conformance/web3d-consortium-inc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/web3d-consortium-inc-conformance.yml
- group: other
  href: https://artifacts.apis.io/web3d-consortium-inc/hosts/web3d-consortium-inc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/web3d-consortium-inc-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.web3d.org/user/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.web3d.org/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.web3d.org/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.web3d.org/press/releases
- group: auth
  href: https://artifacts.apis.io/web3d-consortium-inc/security/web3d-consortium-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/web3d-consortium-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.web3d.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.web3d.org/getting-started-x3d
- group: company
  title: ''
  type: Blog
  url: https://www.web3d.org/blogs/general
- group: docs
  title: ''
  type: APIReference
  url: https://www.web3d.org/x3d/what-x3d
coverage:
  checked: '2026-10-30'
  detail: The provider's website offers documentation but no discoverable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://www.web3d.org/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Web3D Consortium, Inc. is a non‑profit standards organization that develops and promotes open standards for real‑time 3D communication on the web and other platforms. It maintains the X3D specification, provides resources, tools, and documentation for developers, and fosters a community through working groups, events, and educational materials. The consortium aims to enable interoperable 3D content across browsers, devices, and applications, supporting use cases such as virtual reality, augmented reality, gaming, scientific visualization, and digital heritage.
layout: provider
modified: '2026-10-28'
name: Web3D Consortium, Inc.
nav: Providers
network: true
overview: 'Web3D Consortium, Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Standards, 3D, OpenSource, and Community.


  Web3D Consortium, Inc.''s developer surface includes signup flow, changelog, documentation, engineering blog, API reference, and 6 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 46.4
    operational_transparency: 15.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Web3D Consortium Inc Domain Security
  slug: web3d-consortium-inc-domain-security
  summary_line: TLSv1.3
slug: web3d-consortium-inc
tags:
- Company
- Standards
- 3D
- OpenSource
- Community
website: https://www.web3d.org/
---
