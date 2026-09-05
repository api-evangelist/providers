---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.morpheus.space/
- group: company
  title: ''
  type: About
  url: https://www.morpheus.space/company
- group: company
  title: ''
  type: Careers
  url: https://careers.morpheus.space/
- group: operate
  title: ''
  type: Support
  url: https://www.morpheus.space/contact-sales
- group: company
  title: ''
  type: Blog
  url: https://www.morpheus.space/media-newsroom
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.morpheus.space/privacy-cookie-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/morpheus-space
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/morpheus-space
- group: agent
  title: ''
  type: MCPServer
  url: mcp/morpheus-space-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/morpheus-space-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/morpheus-space-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/morpheus-space-domain-security.yml
created: '2026-07-17'
description: Morpheus Space is an in-space mobility company building electric propulsion systems and mission-design software for the New Space economy. Founded in 2018 out of the Technical University of Dresden, its second-generation GO-2 system uses FEEP (Field Emission Electric Propulsion) technology to deliver continuous, chemical-free thrust for satellite constellation deployment, station keeping, collision avoidance, repositioning, and deorbiting. The company also offers Journey, a mission simulation and design platform that matches simulated requirements to available satellite subsystems. Morpheus Space markets ITAR-free solutions and is backed by investors including Techstars, Alpine Space Ventures, Airbus Ventures, Lavrock Ventures, and In-Q-Tel. The company publishes no public developer API; its only machine-facing surface is a platform-hosted (Wix) site MCP endpoint and an auto-generated llms.txt for agent access to public marketing content.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/morpheus-space.png
layout: provider
mcp_servers:
- description: Wix-provided Site MCP server for morpheus.space. This is a platform-hosted (Wix) MCP endpoint auto-exposed for the marketing site, not a first-party product API from Morpheus Space. It surfaces public
  name: Morpheus Space Site MCP
  slug: morpheus-space-site-mcp
modified: '2026-07-20'
name: Morpheus Space
nav: Providers
network: true
overview: 'Morpheus Space is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Satellite, Propulsion, and Electric Propulsion.


  Morpheus Space''s developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.3
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/morpheus-space/refs/heads/main/screenshots/morpheus-space-2026-08-07T184310.png
security:
- kind: domain-security
  name: Morpheus Space Domain Security
  slug: morpheus-space-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: morpheus-space
tags:
- Company
- Space
- Satellite
- Propulsion
- Electric Propulsion
- Aerospace
- Mission Design
- New Space
website: https://www.morpheus.space/
---
