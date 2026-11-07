---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/atlier-ai/plans/atlier-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/atlier-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/atlier-ai/llms/atlier-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlier-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/atlier-ai/well-known/atlier-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atlier-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/atlier-ai/hosts/atlier-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlier-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/atlier-ai/security/atlier-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlier-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlier.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://atlier.ai/guide
- group: commercial
  title: ''
  type: Pricing
  url: https://atlier.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atlier.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atlier.ai/privacy
- group: auth
  title: ''
  type: Trust
  url: https://atlier.ai/trust
- group: operate
  title: ''
  type: Support
  url: https://atlier.ai/support
- group: start
  title: ''
  type: DeveloperPortal
  url: https://atlier.ai/for-agents
- group: other
  title: ''
  type: OperatingContract
  url: https://atlier.ai/contract
- group: agent
  title: ''
  type: LLMs
  url: https://atlier.ai/llms.txt
coverage:
  checked: '2026-11-02'
  detail: Public website provides documentation but no machine‑readable API contract was found; all spec endpoints returned 401 unauthorized.
  evidence:
  - status: 401
    url: https://atlier.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Project Desk by Atlier is an AI‑first work‑management desk that provides a shared memory across AI sessions, keeping projects, queues, and handoffs truthful as agents do the work. Built and operated by Wilds, Inc., an independent company in Massachusetts, USA, it offers a beta‑stage product with transparent Terms of Service, Privacy Policy, and Trust & data‑handling pages. Users bring their own AI (Claude, Codex, etc.) and are never charged for agents; the service is free for solo builders and charges only for human seats in team plans.
layout: provider
modified: '2026-11-01'
name: Atlier
nav: Providers
network: true
overview: 'Atlier is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Project Management, Software-as-a-Service, Collaboration, and Productivity.


  Atlier''s developer surface includes documentation, pricing, support, and 12 more developer resources.'
plans:
- name: Atlier Ai Plans Pricing
  plan_count: 2
  slug: atlier-ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Atlier Ai Rate Limits
  slug: atlier-ai-rate-limits
scopes:
- name: Atlier Ai Scopes
  scope_count: 0
  slug: atlier-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 40.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 23.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atlier Ai Authentication
  slug: atlier-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atlier Ai Domain Security
  slug: atlier-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atlier-ai
tags:
- Artificial Intelligence
- Project Management
- Software-as-a-Service
- Collaboration
- Productivity
- Beta
website: https://atlier.ai/
---
