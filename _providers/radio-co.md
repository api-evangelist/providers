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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Radio Co Agentic Access
  operation_count: 3
  slug: radio-co-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://public.radio.co
  baseurl_source: declared
  description: Station status and metadata endpoints
  name: Radio.co Station API
  slug: radio-co-station-api
- baseURL: https://public.radio.co
  baseurl_source: declared
  description: Currently playing track information
  name: Radio.co Track API
  slug: radio-co-track-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Radio.co Public Station API
  slug: open-radio-co-station-api
- collection_type: open
  name: Radio.co Public Station Track API
  slug: open-radio-co-track-api
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
random_paper: 5
rate_limits:
- limit_count: 5
  name: Radio Co Rate Limits
  slug: radio-co-rate-limits
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 70.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 20.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
