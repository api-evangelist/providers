---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aerospacelab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aerospacelab.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aerospacelab.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.aerospacelab.com/blog/press-releases-1/feed
- group: operate
  title: ''
  type: Support
  url: https://www.aerospacelab.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aerospacelab.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.aerospacelab.com/coordinated-vulnerability-disclosure-policy
- group: company
  title: ''
  type: Partners
  url: https://www.aerospacelab.com/partners-suppliers
- group: company
  title: ''
  type: Careers
  url: https://www.aerospacelab.com/jobs
- group: other
  title: ''
  type: Events
  url: https://www.aerospacelab.com/events
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aerospacelab-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aerospacelab-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Aerospacelab is a satellite manufacturer that sells missions, not API calls — its own sitemap lists only marketing, blog, events, jobs and legal pages with no developer, docs or API section, and api./developer./docs.aerospacelab.com do not resolve at all.
  evidence:
  - status: 200
    url: https://www.aerospacelab.com/sitemap.xml
  - status: 404
    url: https://www.aerospacelab.com/developers
  - status: 404
    url: https://www.aerospacelab.com/openapi.json
  - status: 404
    url: https://www.aerospacelab.com/.well-known/agent-card.json
  - status: 0
    url: https://api.aerospacelab.com/
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Aerospacelab is a vertically integrated satellite manufacturer headquartered in Mont-Saint-Guibert, Belgium, founded in 2018 by Benoit Deper. The company designs, builds, tests and operates small-to-medium satellites — its Versatile Satellite Platform (VSP-50, VSP-150, VSP-300) family plus mission-specific payloads spanning very-high-resolution and multispectral/hyperspectral Earth observation, synthetic aperture radar, radio-frequency sensing, and narrowband/broadband telecommunications — for commercial, institutional and government customers, with an explicitly ITAR-free European supply chain. It is roughly 90% vertically integrated across platforms, payloads, avionics and subsystems, has flown eight satellites in under three years, acquired Belgian space-optics firm AMOS, and is building a European satellite megafactory targeting 500 satellites per year. Aerospacelab publishes no public developer program, API documentation or machine-readable API contract; its programmatic
  surfaces (mission control, tasking, image-processing pipeline and data platform built under the ESA InCubed MultiSpectral Companion Mission) are delivered to contracted mission customers rather than to self-serve developers.
image: https://www.aerospacelab.com/web/image/342190-68a123e8/Aerospacelab_VHR_20231221_0016%20%281%29-min.jpg
layout: provider
modified: '2026-08-06'
name: Aerospacelab
nav: Providers
network: true
overview: 'Aerospacelab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Satellites, Space, Earth Observation, and Aerospace.


  Aerospacelab''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 22.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aerospacelab/refs/heads/main/screenshots/aerospacelab-2026-08-07T161005.png
security:
- kind: domain-security
  name: Aerospacelab Domain Security
  slug: aerospacelab-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aerospacelab Vulnerability Disclosure
  slug: aerospacelab-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aerospacelab
tags:
- Company
- Satellites
- Space
- Earth Observation
- Aerospace
- Remote Sensing
- Satellite Manufacturing
- Telecommunications
- Defense
- Belgium
website: https://www.aerospacelab.com/
---
