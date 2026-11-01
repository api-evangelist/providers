---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Symbl.ai provides AI‑powered conversation intelligence APIs for real‑time speech‑to‑text, topic detection, sentiment analysis, and actionable insights.
  name: Symbl Conversation API
  slug: symbl-conversation-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/rammer-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/rammer-ai/hosts/rammer-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rammer-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/rammer-ai/vendors/rammer-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rammer-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/rammer-ai/security/rammer-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rammer-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rammer.ai/
coverage:
  checked: '2026-10-29'
  detail: All attempts to fetch documentation and contract files returned HTTP 500, indicating the site is protected and no machine‑readable spec is available.
  evidence:
  - status: 500
    url: https://symbl.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Symbl.ai provides AI-powered conversation intelligence APIs that enable developers to add real-time speech-to-text, topic detection, sentiment analysis, and actionable insights to voice, video, and messaging applications. Their platform processes live and recorded audio, delivering structured data such as speaker identification, intent extraction, and summary generation, helping businesses automate note-taking, improve customer experiences, and build intelligent communication tools. The company is backed by Techstars and positioned in the conversational AI market.
image: https://symbl.ai/assets/logo.png
layout: provider
modified: '2026-10-29'
name: Symbl.ai
nav: Providers
network: true
overview: Symbl.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Conversation, Speech, and NLP.
plans:
- name: Rammer Ai Plans Pricing
  plan_count: 0
  slug: rammer-ai-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Rammer Ai Rate Limits
  slug: rammer-ai-rate-limits
scopes:
- name: Rammer Ai Scopes
  scope_count: 0
  slug: rammer-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Rammer Ai Authentication
  slug: rammer-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rammer Ai Domain Security
  slug: rammer-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rammer-ai
tags:
- Company
- AI
- Conversation
- Speech
- NLP
- Real-time
- Communication
website: https://rammer.ai/
---
