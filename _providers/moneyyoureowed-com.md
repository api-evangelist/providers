---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-09-23'
api_count: 2
apis:
- description: Free public remote Model Context Protocol server (Streamable HTTP, protocol 2025-06-18, stateless, no authentication) exposing one read-only tool, answer_money_question, which takes a plain-language c
  name: Money You're Owed Catalog MCP Server
  slug: catalog-mcp-server
- description: A2A 1.0 agent ("Money You're Owed catalog agent", version 1.0.0) with a JSONRPC binding at https://agent.moneyyoureowed.com and one read-only skill, answer-money-questions, answering consumer question
  name: Money You're Owed Catalog Agent (A2A)
  slug: catalog-a2a-agent
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://moneyyoureowed.com/
- group: docs
  title: ''
  type: Documentation
  url: https://moneyyoureowed.com/connect
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moneyyoureowed.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moneyyoureowed.com/terms
- group: operate
  title: ''
  type: Contact
  url: mailto:hello@moneyyoureowed.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/mcp/moneyyoureowed-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/moneyyoureowed-com-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/a2a/moneyyoureowed-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/moneyyoureowed-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/well-known/moneyyoureowed-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/moneyyoureowed-com-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/llms/moneyyoureowed-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moneyyoureowed-com-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/authentication/moneyyoureowed-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/moneyyoureowed-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/conformance/moneyyoureowed-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moneyyoureowed-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/conventions/moneyyoureowed-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/moneyyoureowed-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/errors/moneyyoureowed-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moneyyoureowed-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/lifecycle/moneyyoureowed-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moneyyoureowed-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/rate-limits/moneyyoureowed-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/moneyyoureowed-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/plans/moneyyoureowed-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moneyyoureowed-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/data-model/moneyyoureowed-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moneyyoureowed-com-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/regulatory/moneyyoureowed-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/moneyyoureowed-com-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://moneyyoureowed.com/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://moneyyoureowed.com/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moneyyoureowed-com/refs/heads/main/security/moneyyoureowed-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moneyyoureowed-com-domain-security.yml
created: '2026-09-19'
description: 'Money You''re Owed publishes plain-English US consumer money-recovery help — free official-route checklists (unclaimed property, airline refunds, EITC, medical bills, property tax) and one-time-purchase self-help kits such as Deposit Defender and DenialFix — and exposes its source-cited fact catalog to AI assistants through two free, anonymous, read-only agent surfaces: a remote MCP server at mcp.moneyyoureowed.com with a single answer_money_question tool, and an A2A 1.0 agent whose card is served from agent.moneyyoureowed.com. There is no REST API, SDK or developer program; the machine surface is agent-native by design.'
image: https://moneyyoureowed.com/social-card.png
layout: provider
mcp_servers:
- description: ''
  name: Money You're Owed MCP Server
  slug: money-youre-owed-mcp-server
- description: ''
  name: Live MCP endpoint (Streamable HTTP)
  slug: live-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: Money You're Owed
nav: Providers
network: true
overview: 'Money You''re Owed publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Finance, Consumer Rights, Money Recovery, and Legal Self-Help.


  Money You''re Owed''s developer surface includes documentation, authentication, and 20 more developer resources.'
plans:
- name: Moneyyoureowed Com Plans Pricing
  plan_count: 0
  slug: moneyyoureowed-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Moneyyoureowed Com Rate Limits
  slug: moneyyoureowed-com-rate-limits
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 68.5
    operational_transparency: 0.0
  previous_composite: 20.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Moneyyoureowed Com Authentication
  slug: moneyyoureowed-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Moneyyoureowed Com Domain Security
  slug: moneyyoureowed-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: moneyyoureowed-com
tags:
- Company
- Consumer Finance
- Consumer Rights
- Money Recovery
- Legal Self-Help
- Education
- Agents
- MCP
- A2A
- Agent-Native
website: https://moneyyoureowed.com/
---
