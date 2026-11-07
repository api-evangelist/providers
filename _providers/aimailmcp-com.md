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
    agent_card: flavored
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
  score: 23.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/aimailmcp-com/llms/aimailmcp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aimailmcp-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aimailmcp-com/a2a/aimailmcp-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aimailmcp-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/aimailmcp-com/well-known/aimailmcp-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aimailmcp-com-security.txt
- group: agent
  href: https://artifacts.apis.io/aimailmcp-com/well-known/aimailmcp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aimailmcp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aimailmcp-com/hosts/aimailmcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aimailmcp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aimailmcp-com/vendors/aimailmcp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aimailmcp-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://aimailmcp.com/status
- group: auth
  title: ''
  type: Security
  url: https://aimailmcp.com/security
- group: auth
  href: https://artifacts.apis.io/aimailmcp-com/security/aimailmcp-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aimailmcp-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aimailmcp-com/security/aimailmcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aimailmcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aimailmcp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aimailmcp.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://aimailmcp.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aimailmcp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aimailmcp.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://aimailmcp.com/support
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://aimailmcp.com/mcp
  - status: 200
    url: https://aimailmcp.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: AI Mail MCP provides a unified email inbox for AI agents, enabling them to receive, sort, draft, and manage messages across multiple roles such as support, sales, billing, legal, and HR. The platform offers tools for DNS security, documentation, pricing, and account management, with a sandbox environment for free trials. It emphasizes security with token scoping, audit logs, and outgoing guard mechanisms, and supports custom domains and integrations via MCP endpoints. Pricing is usage‑based, with per‑mailbox and per‑recipient rates, and data is automatically deleted after the trial period unless extended.
image: https://aimailmcp.com/og-image.png
layout: provider
modified: '2026-11-01'
name: AI Mail MCP
nav: Providers
network: true
overview: 'AI Mail MCP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Email, Artificial Intelligence, MCP, Software-as-a-Service, and Inbox.


  AI Mail MCP''s developer surface includes documentation, pricing, support, and 13 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 13.2
  previous_composite: 18.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aimailmcp Com Domain Security
  slug: aimailmcp-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Aimailmcp Com Vulnerability Disclosure
  slug: aimailmcp-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aimailmcp-com
tags:
- Email
- Artificial Intelligence
- MCP
- Software-as-a-Service
- Inbox
website: https://aimailmcp.com/
---
