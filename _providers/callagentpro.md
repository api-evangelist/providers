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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: 'REST API for everything the callagent.pro dashboard does: agents, test-chat and test-call, numbers, SIP accounts and trunks, calls and live calls, knowledge, contacts, do-not-call, and billing includi'
  name: callagent.pro Agent API
  slug: agent-api
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.callagent.pro/
- group: company
  title: ''
  type: Blog
  url: https://www.callagent.pro/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.callagent.pro/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.callagent.pro/policy
created: '2026-09-23'
description: callagent.pro provides human-like AI phone agents that answer and place real phone calls. Its REST Agent API (Bearer keys prefixed cak_live_, base https://www.callagent.pro) covers building agents, assigning numbers and SIP trunks, test chats and test calls, call transcripts, recordings and summaries, contacts, do-not-call lists, and billing, including x402 USDC top-ups on Base. Submitted through apis.io/add.
layout: provider
modified: '2026-09-23'
name: callagent.pro
nav: Providers
network: true
overview: 'callagent.pro publishes 1 API on the [APIs.io](https://apis.io/) network: Agent API. Tagged areas include AI Agents, Voice, Telephony, Phone Agents, and SIP.


  callagent.pro''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 1
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 11.9
    discoverability: 66.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: callagentpro
tags:
- AI Agents
- Voice
- Telephony
- Phone Agents
- SIP
- x402
- Call Automation
website: https://www.callagent.pro/
---
