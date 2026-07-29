---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_access: derived
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Radio Co Agentic Access
  operation_count: 3
  slug: radio-co-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- description: Station status and metadata endpoints
  name: Radio.co Station API
  slug: radio-co-station-api
- description: Currently playing track information
  name: Radio.co Track API
  slug: radio-co-track-api
artifact_total: 8
collections:
- collection_type: open
  name: Radio.co Public API
  slug: open-radio-co
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/radio-co-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/radio-co-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/radiodotco
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/radio-co
- group: agent
  title: ''
  type: LlmsText
  url: https://www.radio.co/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.radio.co/blog
created: '2025-02-12'
description: Your toolset for creating bespoke players. Showcase your station to fit your website, apps, and beyond.
finops:
- name: Radio Co Finops
  service_category: API
  slug: radio-co-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/radio-co.png
layout: provider
modified: '2026-05-19'
name: Radio.co
nav: Providers
network: true
overview: 'Radio.co publishes 2 APIs on the [APIs.io](https://apis.io/) network: Station API and Track API. Tagged areas include Radio, Streaming, Audio, and Music.


  Radio.co''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Radio Co Plans Pricing
  plan_count: 3
  slug: radio-co-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Radio Co Rate Limits
  slug: radio-co-rate-limits
score:
  band: thin
  composite: 30.0
  delta: -1.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 47.5
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/radio-co/refs/heads/main/screenshots/radio-co-2026-06-20T192532.png
security:
- kind: domain-security
  name: Radio Co Domain Security
  slug: radio-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: radio-co
tags:
- Radio
- Streaming
- Audio
- Music
---
