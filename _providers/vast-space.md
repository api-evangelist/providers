---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: 'Informational product surface for Haven-1, billed as the world''s first commercial space station - a standalone crewed station designed to host four crew with 45 cubic meters of habitable volume. This '
  name: Vast Haven-1 Station
  slug: haven-1-station
- description: Informational product surface for Haven-2, a larger multi-module station positioned as a successor to the International Space Station for continuous human presence in low-Earth orbit. Hardware/spacefl
  name: Vast Haven-2 Station
  slug: haven-2-station
- description: Informational surface for the Haven-1 Lab, an in-space microgravity research and manufacturing facility supporting up to ten payloads, each up to 30 kilograms and 100 watts of continuous power. Payloa
  name: Vast Haven-1 Lab
  slug: haven-1-lab
- description: Informational surface covering Vast's Request for Proposals (RFP) and payload-partner program for research on Haven-1 across life sciences, physical sciences, technology demonstrations, biotechnology,
  name: Vast Payload & Research Opportunities
  slug: payload-research-opportunities
artifact_total: 9
collections:
- collection_type: open
  name: Vast (Informational - No Public API)
  slug: open-vast-space
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vast-space-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vast-space
- group: company
  title: ''
  type: Website
  url: https://www.vastspace.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.vastspace.com/haven-1
- group: commercial
  title: ''
  type: Plans
  url: plans/vast-space-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vast-space-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vast-space-finops.yml
created: '2026-06-20'
description: Vast is a commercial space company building next-generation crewed space stations, beginning with Haven-1 (the first commercial space station, targeting a 2026 launch on a SpaceX Falcon 9) and the larger Haven-2. Vast is an aerospace hardware and human-spaceflight company; as of this writing it does not publish a public developer API. The surfaces catalogued here are informational product, research, and partnership pages rather than programmable HTTP APIs.
finops:
- name: Vast Space Finops
  service_category: Space and Aerospace
  slug: vast-space-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vast-space.png
layout: provider
modified: '2026-06-20'
name: Vast
nav: Providers
network: true
overview: 'Vast publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Haven-1 Station, Haven-2 Station, Haven-1 Lab, and 1 more. Tagged areas include Space, Aerospace, Space Station, Human Spaceflight, and Microgravity.


  Vast''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Vast Space Plans Pricing
  plan_count: 1
  slug: vast-space-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 2
  name: Vast Space Rate Limits
  slug: vast-space-rate-limits
score:
  band: emerging
  composite: 24.8
  delta: -3.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 32.3
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vast-space/refs/heads/main/screenshots/vast-space-2026-06-20T200831.png
security:
- kind: domain-security
  name: Vast Space Domain Security
  slug: vast-space-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: vast-space
tags:
- Space
- Aerospace
- Space Station
- Human Spaceflight
- Microgravity
- Research
- Informational
website: https://www.vastspace.com/
---
