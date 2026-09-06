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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/peloton-interactive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peloton-interactive-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/peloton-interactive-
- group: company
  title: ''
  type: Website
  url: https://www.onepeloton.com
created: '2026-05-04'
description: Peloton Interactive is a connected fitness company that produces interactive exercise equipment and a streaming subscription service. The company sells connected stationary bikes, treadmills, rowers, and a digital app offering live and on-demand fitness classes. Peloton has built a large community of members who participate in instructor-led workouts and track performance metrics through its platform.
layout: provider
modified: '2026-05-04'
name: Peloton Interactive
nav: Providers
network: true
overview: Peloton Interactive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fitness, Connected Fitness, Consumer Hardware, Streaming, and Health and Wellness.
random_paper: 1
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 2
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peloton-interactive/refs/heads/main/screenshots/peloton-interactive-2026-06-20T191540.png
security:
- kind: domain-security
  name: Peloton Interactive Domain Security
  slug: peloton-interactive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Peloton Interactive Vulnerability Disclosure
  slug: peloton-interactive-vulnerability-disclosure
  summary_line: Hackerone
slug: peloton-interactive
tags:
- Fitness
- Connected Fitness
- Consumer Hardware
- Streaming
- Health and Wellness
website: https://www.onepeloton.com
---
