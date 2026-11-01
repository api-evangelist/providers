---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/voice-school-com/llms/voice-school-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/voice-school-com-llms.txt
- group: other
  href: https://artifacts.apis.io/voice-school-com/hosts/voice-school-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/voice-school-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/voice-school-com/vendors/voice-school-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/voice-school-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/voice-school-com/security/voice-school-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/voice-school-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://voice-school.com/
- group: docs
  title: ''
  type: Documentation
  url: https://voice-school.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://voice-school.com/en/privacy/
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's documented API hosts.
  evidence:
  - status: 502
    url: https://api.voice-school.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Voice School provides online singing lessons with vocal coaches via a web platform. Students can book trial lessons, single sessions, or courses, choosing teachers and lesson types for kids, teens, adults, or beginners. The service offers flexible scheduling, Zoom-based instruction, and a range of pricing options. The company’s website presents detailed information about teachers, lesson formats, pricing, and regional availability, positioning itself as a global provider of personalized vocal training.
layout: provider
modified: '2026-10-30'
name: voice-school-com
nav: Providers
network: true
overview: 'voice-school-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Music, OnlineLearning, and VocalCoaching.


  voice-school-com''s developer surface includes documentation and 6 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Voice School Com Domain Security
  slug: voice-school-com-domain-security
  summary_line: TLSv1.3
slug: voice-school-com
tags:
- Company
- Education
- Music
- OnlineLearning
- VocalCoaching
website: https://voice-school.com/
---
