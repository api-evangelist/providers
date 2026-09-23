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
  scored_at: '2026-09-23'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://airvine.com/
- group: docs
  title: ''
  type: Documentation
  url: https://airvine.com/support/technical-documentation/
- group: operate
  title: ''
  type: Support
  url: https://airvine.com/support/
- group: company
  title: ''
  type: Blog
  url: https://airvine.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://airvine.com/feed/
- group: company
  title: ''
  type: Newsroom
  url: https://airvine.com/news-events/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airvine.com/privacy-policy/
- group: commercial
  title: ''
  type: License
  url: https://airvine.com/eula/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://cousides.sirv.com/collateral/Airvine-VineOS-Release-Notes.pdf
- group: company
  title: ''
  type: About
  url: https://airvine.com/company/
- group: company
  title: ''
  type: Careers
  url: https://airvine.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://airvine.com/contact/
- group: company
  title: ''
  type: Partners
  url: https://airvine.com/partners/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airvine
- group: other
  title: ''
  type: X
  url: https://x.com/wavetunnel
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airvine/refs/heads/main/security/airvine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airvine-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/airvine/refs/heads/main/regulatory/airvine-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/airvine-regulatory-posture.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airvine/refs/heads/main/llms/airvine-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airvine-llms.txt
coverage:
  checked: '2026-09-19'
  detail: The public WaveTunnel user manual lists an "Open API" and SNMP management interface and the WaveCore configuration guide describes a per-device RESTAPI Authentication Key, but both refer readers to separate "API/SNMP documents" that are absent from the public Technical Documentation page, whose only other document channel is the partner portal login at partner.airvine.com; airvine.com/api, /docs and /openapi.json all 404 and no developer, docs or api subdomain resolves.
  evidence:
  - status: 200
    url: https://cousides.sirv.com/collateral/Airvine-User-Manual-Configuration-Guide-Wave-Tunnel.pdf
  - status: 200
    url: https://media.airvine.com/collateral/Airvine-Configuration-Guide-WaveCore.pdf
  - status: 200
    url: https://airvine.com/support/technical-documentation/
  - status: 200
    url: https://partner.airvine.com/wp-login.php
  - status: 404
    url: https://airvine.com/api
  - status: 404
    url: https://airvine.com/openapi.json
  - status: 404
    url: https://airvine.com/.well-known/agent-card.json
  - status: 404
    url: https://airvine.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-09-19'
description: 'Airvine Scientific is a Silicon Valley maker of indoor 60 GHz millimeter-wave wireless backhaul hardware. Its WaveTunnel modules deliver a multi-gigabit, non-line-of-sight, beam-steering indoor Ethernet backbone in a resilient ring topology, and the WaveCore and WaveCore Flex products extend that wireless gigabit backbone; all run on the VineSuite software platform (VineOS on the device, the browser-based VineManager, the AirvineMobile app and the VineCalculator planning tool). The products are sold into multi-dwelling units, hospitality, education, industrial and large-venue networks through distributors, certified resellers and certified installers. Airvine publishes no public API: the device manuals name an Open API, SNMP and CLI management surface with a per-device REST API authentication key, but the API/SNMP documents they refer to are not published on the public technical documentation page and there is no developer portal or machine-readable contract.'
image: https://airvine.com/wp-content/uploads/airvine-logo.svg
layout: provider
modified: '2026-09-19'
name: Airvine
nav: Providers
network: true
overview: 'Airvine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wireless Networking, Networking Hardware, Telecommunications, and Millimeter Wave.


  Airvine''s developer surface includes documentation, support, engineering blog, release notes, and 14 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    operational_transparency: 15.8
  previous_composite: 10.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 13.9
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airvine Domain Security
  slug: airvine-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airvine
tags:
- Company
- Wireless Networking
- Networking Hardware
- Telecommunications
- Millimeter Wave
- Broadband
- Enterprise Networking
- Network Equipment
website: https://airvine.com/
---
