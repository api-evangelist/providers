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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Collabora provides APIs for its open‑source solutions.
  name: Collabora API
  slug: collabora-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/collabora-ltd/well-known/collabora-ltd-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/collabora-ltd-well-known.yml
- group: other
  href: https://artifacts.apis.io/collabora-ltd/hosts/collabora-ltd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/collabora-ltd-hosts.yml
- group: other
  href: https://artifacts.apis.io/collabora-ltd/vendors/collabora-ltd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/collabora-ltd-vendors.yml
- group: build
  href: https://artifacts.apis.io/collabora-ltd/packages/collabora-ltd-packages.yml
  title: ''
  type: SDKs
  url: packages/collabora-ltd-packages.yml
- group: build
  href: https://artifacts.apis.io/collabora-ltd/packages/collabora-ltd-packages.yml
  title: ''
  type: Packages
  url: packages/collabora-ltd-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.collabora.com/otrs/customer.pl
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.collabora.com/privacy-notice.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/collabora
- group: auth
  href: https://artifacts.apis.io/collabora-ltd/security/collabora-ltd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/collabora-ltd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.collabora.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.collabora.com/sitemap.xml
coverage:
  checked: '2026-10-26'
  detail: Docs site renders content via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.collabora.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Collabora Ltd. is an open‑source software consulting company founded in 2005, helping clients across automotive, digital TV, silicon, OEM, and VR/AR industries to integrate, optimize, and maintain open‑source solutions. They provide services such as guide, train, build, integrate, optimize, and maintain, and contribute to projects like LibreOffice, GStreamer, Wayland, and Linux kernel.
image: https://www.collabora.com//assets/images/core/c_o.jpg
layout: provider
modified: '2026-10-26'
name: Collabora Ltd.
nav: Providers
network: true
overview: 'Collabora Ltd. is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OpenSource, Consulting, Software, and Services.


  Collabora Ltd.''s developer surface includes support, documentation, and 9 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
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
  name: Collabora Ltd Domain Security
  slug: collabora-ltd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: collabora-ltd
tags:
- Company
- OpenSource
- Consulting
- Software
- Services
website: https://www.collabora.com/
---
