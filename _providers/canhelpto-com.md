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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: documented
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
  score: 22.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Customer support API for MCP servers, providing ticket, reply, feedback and CSAT endpoints.
  name: canhelpto API
  slug: canhelpto-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/canhelpto-com/plans/canhelpto-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canhelpto-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/canhelpto-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/canhelpto-com/conformance/canhelpto-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canhelpto-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/canhelpto-com/llms/canhelpto-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canhelpto-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/canhelpto-com/well-known/canhelpto-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canhelpto-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/canhelpto-com/hosts/canhelpto-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canhelpto-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/canhelpto-com/vendors/canhelpto-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canhelpto-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://canhelpto.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://canhelpto.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://canhelpto.com/docs/agents
- group: auth
  href: https://artifacts.apis.io/canhelpto-com/security/canhelpto-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canhelpto-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canhelpto.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://canhelpto.com/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://canhelpto.com/openapi.json
  - status: 401
    url: https://canhelpto.com/api/mcp
  - status: 200
    url: https://canhelpto.com/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: 'Support where your users are: inside the AI agent. canhelpto provides customer support for MCP servers, offering three tools within the server: failure context attachment, a human inbox, and answer back in the conversation. It integrates with Claude, ChatGPT, and Cursor, and is free to start, aiming to streamline help desk operations directly in AI-powered workflows.'
layout: provider
modified: '2026-11-04'
name: canhelpto
nav: Providers
network: true
overview: 'canhelpto is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Service, AI Integration, MCP Server, Help Desk, and Automation.


  canhelpto''s developer surface includes API reference, pricing, and 11 more developer resources.'
plans:
- name: Canhelpto Com Plans Pricing
  plan_count: 2
  slug: canhelpto-com-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 5.4
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Canhelpto Com Domain Security
  slug: canhelpto-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: canhelpto-com-agent
  slug: canhelpto-com-agent
slug: canhelpto-com
tags:
- Customer Service
- AI Integration
- MCP Server
- Help Desk
- Automation
website: https://canhelpto.com/
---
