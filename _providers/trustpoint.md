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
  band: agent-aware
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trustpoint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trustpointgps.com
- group: company
  title: ''
  type: Blog
  url: https://trustpointgps.com/news
- group: operate
  title: ''
  type: Contact
  url: https://trustpointgps.com/contact
- group: company
  title: ''
  type: Careers
  url: https://trustpoint.breezy.hr/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iubenda.com/privacy-policy/76230539/legal
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trustpoint-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trustpoint-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trustpoint-well-known.yml
created: '2026-07-17'
description: TrustPoint, Inc. is a space technology company building a fully commercial, next-generation global navigation satellite system (GNSS) — a C-band LEO microsatellite constellation delivering secure positioning, navigation, and timing (PNT) independent of GPS, with improved accuracy, faster time to first fix, and anti-jamming / anti-spoofing capabilities for automotive, aviation, critical infrastructure, and national security applications. Headquartered in Northern Virginia with an office in Mountain View, California, and backed by DCVC, TrustPoint does not currently publish a public API or developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trustpoint.png
layout: provider
mcp_servers:
- description: ''
  name: Wix Site MCP Server
  slug: wix-site-mcp-server
modified: '2026-07-21'
name: TrustPoint
nav: Providers
network: true
overview: 'TrustPoint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GNSS, Satellites, Navigation, and Positioning.


  TrustPoint''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.3
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
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.3
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trustpoint/refs/heads/main/screenshots/trustpoint-2026-09-02T164424.png
security:
- kind: domain-security
  name: Trustpoint Domain Security
  slug: trustpoint-domain-security
  summary_line: TLSv1.3 · HSTS
slug: trustpoint
tags:
- Company
- GNSS
- Satellites
- Navigation
- Positioning
- Timing
- PNT
- Space
- Aerospace
website: https://trustpointgps.com
---
