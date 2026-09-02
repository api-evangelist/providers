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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://humatics.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/humatics-stock
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Humatics
- group: company
  title: ''
  type: Careers
  url: https://humatics.breezy.hr/
- group: operate
  title: ''
  type: Contact
  url: https://humatics.com/contact/
- group: company
  title: ''
  type: About
  url: https://humatics.com/about/
- group: other
  title: ''
  type: Product
  url: https://humatics.com/milo/
- group: other
  title: ''
  type: Product
  url: https://humatics.com/mobility/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://humatics.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://humatics.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/humatics-corporation/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/humatics-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/humatics-domain-security.yml
created: '2026-08-04'
description: 'Humatics Corporation is a Waltham, Massachusetts microlocation company founded in 2015 by MIT professor David Mindell and led by CEO James Kinsey. It builds radio-frequency positioning systems — ultra-wideband beacons, RF-pulse ranging, radar and inertial sensors fused in software — that locate people, vehicles and robots at centimeter- to millimeter-scale precision. Two product lines are on sale today: MILO, a sub-millimeter positioning system for industrial automation and in-motion robotics, advertised as compatible with Yaskawa, Mitsubishi Electric, FANUC, Universal Robots and KUKA; and Mobility, a rail and transit portfolio covering the FOCUS track-geometry monitoring kit and the Humatics Rail Navigation System (HRNS), used on New York City MTA subway signalling projects. Humatics publishes no developer portal, no API documentation and no machine-readable description of any product API. Two rounds of probing humatics.com returned HTTP 404 for every /.well-known/ path, /llms.txt,
  /openapi.json, /openapi.yaml, /swagger.json, /api-docs and /graphql; *.humatics.com is a DNS wildcard onto one retired address, so api., docs., developer., portal. and status. resolve but time out on connect. The only machine-readable HTTP interface on any Humatics host is the WordPress REST API of the marketing site itself at humatics.com/wp-json/ — 375 routes across 19 stock core and commercial-plugin namespaces, exposing pages and posts rather than positioning, and so recorded as evidence rather than catalogued as a Humatics API. The GitHub organization github.com/Humatics is real and public, but 31 of its 33 repositories are forks of third-party embedded and robotics open source (Fast-RTPS, Fast-CDR, FreeRTOS, Orange Pi BSP, Yocto meta-layers, EIPScanner, donkeycar); the two non-forks are internal tools. There is no first-party SDK, client library or specification, and no package named humatics exists on npm or PyPI. Marketing material for the earlier KinetIQ OS / Spatial Intelligence
  Platform referenced an "extensible API", but no public interface for it was ever documented, and the news host that carried those announcements (now.humatics.com) no longer answers.'
image: https://humatics.com/wp-content/uploads/2025/04/humatics.png
layout: provider
modified: '2026-08-04'
name: Humatics
nav: Providers
network: true
overview: Humatics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Positioning, Microlocation, Ultra-Wideband, and Sensors.
random_paper: 1
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/humatics/refs/heads/main/screenshots/humatics-2026-08-07T170400.png
security:
- kind: domain-security
  name: Humatics Domain Security
  slug: humatics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: humatics
tags:
- Company
- Positioning
- Microlocation
- Ultra-Wideband
- Sensors
- Navigation
- Robotics
- Industrial Automation
- Rail
- Transit
- Manufacturing
- Hardware
website: https://humatics.com/
---
