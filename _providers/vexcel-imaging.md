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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vexcel-imaging/refs/heads/main/llms/vexcel-imaging-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vexcel-imaging-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vexcel-imaging/refs/heads/main/hosts/vexcel-imaging-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vexcel-imaging-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vexcel-imaging/refs/heads/main/vendors/vexcel-imaging-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vexcel-imaging-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.vexcel-imaging.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vexcel-imaging.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.vexcel-imaging.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.vexcel-imaging.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vexcel-imaging/refs/heads/main/security/vexcel-imaging-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vexcel-imaging-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vexcel-imaging.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.vexcel-imaging.com/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Vexcel Imaging provides professional aerial imaging and photogrammetry solutions, including the UltraCam series of high‑resolution cameras and the UltraMap processing software suite. The company serves mapping agencies, survey firms, and defense customers worldwide, delivering accurate, reliable airborne data for large‑scale mapping projects.
image: https://www.vexcel-imaging.com/wp-content/uploads/2024/08/website_image_dragon4-1_graz_1000x500px_signet.jpg
layout: provider
modified: '2026-10-13'
name: Vexcel Imaging
nav: Providers
network: true
overview: 'Vexcel Imaging is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerial Imaging, Photogrammetry, Mapping, and UltraCam.


  Vexcel Imaging''s developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Vexcel Imaging Domain Security
  slug: vexcel-imaging-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vexcel-imaging
tags:
- Company
- Aerial Imaging
- Photogrammetry
- Mapping
- UltraCam
website: https://www.vexcel-imaging.com/
---
