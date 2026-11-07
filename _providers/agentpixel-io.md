---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Consent-first website pixel API for creating pixels and managing contacts.
  name: AgentPixel API
  slug: agentpixel-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/agentpixel-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/agentpixel-io/authentication/agentpixel-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentpixel-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentpixel-io/conformance/agentpixel-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentpixel-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentpixel-io/llms/agentpixel-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentpixel-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentpixel-io/mcp/agentpixel-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentpixel-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentpixel-io/well-known/agentpixel-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentpixel-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentpixel-io/hosts/agentpixel-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentpixel-io-hosts.yml
- group: start
  title: ''
  type: Sandbox
  url: https://agentpixel.io/console
- group: start
  title: ''
  type: GettingStarted
  url: https://agentpixel.io/docs/setup
- group: docs
  title: ''
  type: APIReference
  url: https://agentpixel.io/docs
- group: auth
  href: https://artifacts.apis.io/agentpixel-io/security/agentpixel-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentpixel-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentpixel.io/
created: '2026-11-01'
description: AgentPixel provides a consent-first website pixel that transforms visitor clicks on an Accept button into identifiable contacts. By installing a simple tag, businesses can capture visitor details such as name, job title, company, and email, turning anonymous traffic into actionable leads. The service offers a 30‑day free trial, then charges $1 per account per month, supporting up to three pixels and 500 new contacts monthly. It integrates with AI agents like Claude Code, Cursor, VS Code, Gemini CLI, and Cline, enabling automated contact retrieval without requiring user accounts or API keys.
layout: provider
mcp_servers:
- description: Remote MCP server at agentpixel.io.
  name: AgentPixel MCP Server
  slug: agentpixel-io-mcp-yml
modified: '2026-11-01'
name: AgentPixel
nav: Providers
network: true
overview: 'AgentPixel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consent, Marketing, Lead Generation, and AI Integration.


  AgentPixel''s developer surface includes authentication, sandbox, getting-started guide, API reference, and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 31.4
    discoverability: 61.7
    operational_transparency: 0.0
  previous_composite: 15.9
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentpixel Io Authentication
  slug: agentpixel-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentpixel Io Domain Security
  slug: agentpixel-io-domain-security
  summary_line: TLSv1.3
slug: agentpixel-io
tags:
- Company
- Consent
- Marketing
- Lead Generation
- AI Integration
website: https://agentpixel.io/
---
