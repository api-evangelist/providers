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
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/withpoly-com/well-known/withpoly-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/withpoly-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/withpoly-com/hosts/withpoly-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/withpoly-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/withpoly-com/vendors/withpoly-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/withpoly-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/withpoly-com/packages/withpoly-com-packages.yml
  title: ''
  type: SDKs
  url: packages/withpoly-com-packages.yml
- group: build
  href: https://artifacts.apis.io/withpoly-com/packages/withpoly-com-packages.yml
  title: ''
  type: Packages
  url: packages/withpoly-com-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://poly.app/privacy
- group: start
  title: ''
  type: Login
  url: https://poly.app/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withpoly
- group: auth
  href: https://artifacts.apis.io/withpoly-com/security/withpoly-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/withpoly-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://withpoly.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://withpoly.com
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Poly is a technology company offering a collaborative platform that enables users to create, share, and interact with immersive 3D experiences. The service provides tools for building virtual environments, integrating multimedia content, and connecting with audiences in real time. Poly focuses on simplifying complex workflows for creators, developers, and enterprises, delivering APIs and SDKs that facilitate seamless integration of 3D assets into applications, games, and social platforms. Backed by notable investors, Poly aims to democratize immersive content creation and distribution across the web and emerging metaverse ecosystems.
image: https://poly.app/og-social.jpg
layout: provider
modified: '2026-10-21'
name: Poly
nav: Providers
network: true
overview: Poly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Collaboration, 3D, Immersive, and Platform.
random_paper: 12
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Withpoly Com Domain Security
  slug: withpoly-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: withpoly-com
tags:
- Company
- Collaboration
- 3D
- Immersive
- Platform
website: https://withpoly.com
---
