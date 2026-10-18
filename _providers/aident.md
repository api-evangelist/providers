---
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Aident Loadout provides an API platform for third‑party app integration.
  name: Loadout API
  slug: loadout-api
artifact_total: 4
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aident/refs/heads/main/authentication/aident-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aident-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aident/refs/heads/main/llms/aident-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aident-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aident/refs/heads/main/a2a/aident-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aident-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aident/refs/heads/main/mcp/aident-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aident-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aident/refs/heads/main/well-known/aident-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aident-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aident/refs/heads/main/hosts/aident-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aident-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aident/refs/heads/main/vendors/aident-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aident-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loadout.aident.ai/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://aident.ai/skills/signup-flow-cro-4af1168c-a99d-511d-bb6a-2a32f9d575b4
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loadout.aident.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://aident.ai/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aident-AI
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aident.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://aident.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aident.ai/loadout/setup-agents
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aident/refs/heads/main/security/aident-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aident-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aident.ai
- group: docs
  title: ''
  type: Documentation
  url: https://loadout.aident.ai/mcp
coverage:
  checked: '2026-10-05'
  detail: MCP endpoint requires authentication (401 Unauthorized)
  evidence:
  - status: 401
    url: https://loadout.aident.ai/mcp
  reason: partner-login
  state: gated
created: '2026-10-05'
description: Aident Loadout provides a unified gateway for AI agents to securely access over 1,000 third‑party applications. Users connect each app once, then agents can invoke actions across services without handling raw credentials. The platform offers built‑in skills, balance management, and a dashboard for monitoring usage, aiming to simplify AI‑driven workflows in enterprise and developer contexts.
image: https://aident.ai/assets/loadout/hero-ui@2x.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.aident.ai.
  name: Aident Loadout MCP Server
  slug: aident-mcp-yml
modified: '2026-10-05'
name: Aident Loadout
nav: Providers
network: true
overview: 'Aident Loadout is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Integration, Automation, and Platform.


  Aident Loadout''s developer surface includes authentication, signup flow, pricing, changelog, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 66.7
    operational_transparency: 21.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aident Authentication
  slug: aident-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aident Domain Security
  slug: aident-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aident
tags:
- Company
- Artificial Intelligence
- Integration
- Automation
- Platform
website: https://aident.ai
---
