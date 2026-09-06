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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toytalk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pullstring.com
- group: build
  title: ''
  type: Packages
  url: packages/toytalk-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/toytalk-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/toytalk-llms.txt
created: '2026-07-17'
description: ToyTalk was a San Francisco conversational AI company founded in 2011 that built voice and chat characters for entertainment, rebranded as PullString in 2016, and was acquired by Apple in early 2019. Its developer platform - the PullString Web API plus Converse and Author tooling for authoring conversational experiences - was shut down after the acquisition. Today pullstring.com and toytalk.com no longer resolve and both domains are parked on Apple nameservers, the github.com/pullstring organization has been deleted, and the only surviving first-party developer artifact is the orphaned pullstring JavaScript SDK on npm. This profile records that historical developer surface; there is no live API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toytalk.png
layout: provider
modified: '2026-07-21'
name: ToyTalk
nav: Providers
network: true
overview: ToyTalk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Conversational AI, Voice, Chatbots, and Entertainment.
random_paper: 20
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Toytalk Domain Security
  slug: toytalk-domain-security
  summary_line: no transport/DNS hardening detected
slug: toytalk
tags:
- Company
- Conversational AI
- Voice
- Chatbots
- Entertainment
- Acquired
- Defunct
website: https://pullstring.com
---
