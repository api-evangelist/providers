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
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 9.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ''
  name: Magic Teams API
  slug: magic-teams-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/magicteams-ai/conventions/magicteams-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/magicteams-ai-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://magicteams.ai/privacy
- group: auth
  href: https://artifacts.apis.io/magicteams-ai/authentication/magicteams-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/magicteams-ai-authentication.yml
- group: agent
  href: https://artifacts.apis.io/magicteams-ai/llms/magicteams-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/magicteams-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/magicteams-ai/a2a/magicteams-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/magicteams-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/magicteams-ai/mcp/magicteams-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/magicteams-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/magicteams-ai/well-known/magicteams-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/magicteams-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/magicteams-ai/well-known/magicteams-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/magicteams-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/magicteams-ai/hosts/magicteams-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/magicteams-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/magicteams-ai/vendors/magicteams-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/magicteams-ai-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://magicteams.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://blog.magicteams.ai
- group: auth
  href: https://artifacts.apis.io/magicteams-ai/security/magicteams-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/magicteams-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/magicteams-ai/security/magicteams-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/magicteams-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://magicteams.ai/
coverage:
  checked: '2026-10-29'
  detail: Documentation is publicly available at https://docs.magicteams.ai/ but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other spec is published.
  evidence:
  - status: 200
    url: https://docs.magicteams.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Magic Teams AI provides an AI Operating System (AIOS) for founders, delivering a daily brief, approved follow‑through, and a unified operating layer across inboxes, meetings, and files. It also offers a voice conversation platform with real‑time transcription, call management, campaign automation, and webhook events, powered by edge computing, Supabase, and Twilio integration.
image: data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='30' fill='%23F3EFE8'/%3E%3Ccircle cx='50' cy='50' r='17' fill='%23FF6A00'/%3E%3C/svg%3E
layout: provider
mcp_servers:
- description: Remote MCP server at ai-ready.magicteams.ai.
  name: magicteams-ai MCP Server
  slug: magicteams-ai-mcp-yml
modified: '2026-10-29'
name: magicteams-ai
nav: Providers
network: true
overview: 'magicteams-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Productivity, Automation, Voice, and Startups.


  magicteams-ai''s developer surface includes authentication, engineering blog, and 13 more developer resources.'
plans:
- name: Magicteams Ai Plans Pricing
  plan_count: 0
  slug: magicteams-ai-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Magicteams Ai Rate Limits
  slug: magicteams-ai-rate-limits
scopes:
- name: Magicteams Ai Scopes
  scope_count: 0
  slug: magicteams-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 66.7
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.1
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/magicteams-ai/magicteams-ai-2026-11-03T135222.png
security:
- kind: authentication
  name: Magicteams Ai Authentication
  slug: magicteams-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Magicteams Ai Domain Security
  slug: magicteams-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Magicteams Ai Vulnerability Disclosure
  slug: magicteams-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: magicteams-ai
tags:
- Artificial Intelligence
- Productivity
- Automation
- Voice
- Startups
website: https://magicteams.ai/
---
