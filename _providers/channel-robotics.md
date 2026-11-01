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
- group: agent
  href: https://artifacts.apis.io/channel-robotics/llms/channel-robotics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/channel-robotics-llms.txt
- group: other
  href: https://artifacts.apis.io/channel-robotics/hosts/channel-robotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/channel-robotics-hosts.yml
- group: other
  href: https://artifacts.apis.io/channel-robotics/vendors/channel-robotics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/channel-robotics-vendors.yml
- group: auth
  href: https://artifacts.apis.io/channel-robotics/security/channel-robotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/channel-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://channelrobotics.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://channelrobotics.com/mcp
  - status: 403
    url: https://www.channelrobotics.com/mcp
  - status: 200
    url: https://channelrobotics.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Channel Robotics builds advanced robotic automation solutions for industrial and logistics environments. Leveraging AI-driven perception and modular hardware, they enable flexible, scalable automation that integrates with existing workflows. Their platform offers remote monitoring, real-time analytics, and easy-to-deploy robot cells, helping manufacturers increase efficiency, reduce downtime, and accelerate digital transformation. Backed by True Ventures, they serve enterprises seeking cutting-edge automation technology.
image: https://static.wixstatic.com/media/2075ef_9fff35569fd14bbeaca435959d9873f4~mv2.png/v1/fill/w_260,h_68,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/Channel%20Robotics%20Logo%20Blue.png
layout: provider
modified: '2026-10-24'
name: Channel Robotics
nav: Providers
network: true
overview: Channel Robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Automation, AI, and Industrial.
random_paper: 11
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Channel Robotics Domain Security
  slug: channel-robotics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: channel-robotics
tags:
- Company
- Robotics
- Automation
- AI
- Industrial
website: https://channelrobotics.com
---
