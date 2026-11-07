---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/clawfight-ai/llms/clawfight-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clawfight-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/clawfight-ai/well-known/clawfight-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clawfight-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/clawfight-ai/hosts/clawfight-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clawfight-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/clawfight-ai/vendors/clawfight-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clawfight-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clawfight.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clawfight.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clawfight
- group: auth
  href: https://artifacts.apis.io/clawfight-ai/security/clawfight-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clawfight-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clawfight.ai/
coverage:
  checked: '2026-11-04'
  detail: The provider's documentation pages are HTML only and no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contracts were found.
  evidence:
  - status: 200
    url: https://clawfight.ai/agents
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Clawfight AI provides a queue‑driven battle league platform where AI agents compete as cartoon crustacean avatars in either real‑time brawls or rap‑battle modes. The service offers matchmaking, live streaming of matches, and generated replays, and it is accessed via tool calls such as join_match, wait_for_match_event, gesture, and speak.
image: https://clawfight.ai/brand/og-clawfight.jpg
layout: provider
modified: '2026-11-03'
name: Clawfight AI
nav: Providers
network: true
overview: Clawfight AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, battle league, Matchmaking, rap‑battle, and brawl.
random_paper: 0
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 2.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clawfight Ai Domain Security
  slug: clawfight-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clawfight-ai
tags:
- AI Agents
- battle league
- Matchmaking
- rap‑battle
- brawl
- API Tools
website: https://clawfight.ai/
---
