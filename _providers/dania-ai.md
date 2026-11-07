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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/dania-ai/llms/dania-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dania-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/dania-ai/well-known/dania-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dania-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/dania-ai/hosts/dania-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dania-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/dania-ai/security/dania-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dania-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dania.ai/
- group: company
  title: ''
  type: Blog
  url: https://dania.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dania.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dania.ai/privacy
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was found on any discovered host.
  evidence:
  - status: 0
    url: https://api.dania.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: DANIA.AI provides AI‑powered online presence management for businesses, offering intelligent website chat, Google Maps review integration, social media management, and marketing tools from a single dashboard. Plans start at $99 USD per month with no long‑term contracts, targeting local businesses seeking to increase customers through automated AI services.
image: https://dania.ai/og/dania-default.jpg
layout: provider
modified: '2026-11-04'
name: DANIA.AI
nav: Providers
network: true
overview: 'DANIA.AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, Software-as-a-Service, OnlinePresence, and BusinessTools.


  DANIA.AI''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dania Ai Domain Security
  slug: dania-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dania-ai
tags:
- Artificial Intelligence
- Marketing
- Software-as-a-Service
- OnlinePresence
- BusinessTools
website: https://dania.ai/
---
