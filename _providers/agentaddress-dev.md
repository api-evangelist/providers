---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    event_surface_described: unknown
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provision a persistent return address for an ephemeral AI agent.
  name: AgentAddress API
  slug: agentaddress-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/agentaddress-dev/plans/agentaddress-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentaddress-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentaddress-dev/conformance/agentaddress-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentaddress-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentaddress-dev/llms/agentaddress-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentaddress-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/agentaddress-dev/hosts/agentaddress-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentaddress-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentaddress-dev/vendors/agentaddress-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentaddress-dev-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://agentaddress.dev/webhooks
- group: auth
  href: https://artifacts.apis.io/agentaddress-dev/security/agentaddress-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentaddress-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentaddress.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://agentaddress.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://agentaddress.dev/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentaddress.dev/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentaddress.dev/terms
created: '2026-10-31'
description: AgentAddress provides a return address service for AI agents, offering a write‑only HTTPS inbox and inbound email address that feed a private, ordered queue. It enables agents to receive webhooks, callbacks, and human replies without running their own server, supporting event queues, read tokens, and secure message handling.
image: https://agentaddress.dev/opengraph-image?9437a4080f6b5df1
layout: provider
modified: '2026-10-31'
name: AgentAddress
nav: Providers
network: true
overview: 'AgentAddress is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Webhook, Email, and Agents.


  AgentAddress'' developer surface includes documentation, pricing, and 10 more developer resources.'
plans:
- name: Agentaddress Dev Plans Pricing
  plan_count: 2
  slug: agentaddress-dev-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 66.1
    operational_transparency: 3.9
  previous_composite: 20.9
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentaddress Dev Domain Security
  slug: agentaddress-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: agentaddress-dev
tags:
- Company
- Artificial Intelligence
- Webhook
- Email
- Agents
website: https://agentaddress.dev/
---
