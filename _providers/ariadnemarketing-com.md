---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/ariadnemarketing-com/llms/ariadnemarketing-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ariadnemarketing-com-llms.txt
- group: other
  href: https://artifacts.apis.io/ariadnemarketing-com/hosts/ariadnemarketing-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ariadnemarketing-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ariadnemarketing-com/vendors/ariadnemarketing-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ariadnemarketing-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ariadnemarketing-com/security/ariadnemarketing-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ariadnemarketing-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ariadnemarketing.com/
- group: company
  title: ''
  type: Blog
  url: https://ariadnemarketing.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ariadnemarketing.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ariadnemarketing.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://ariadnemarketing.com/login
- group: agent
  href: https://artifacts.apis.io/ariadnemarketing-com/mcp/ariadnemarketing-com-mcp.json
  title: ''
  type: MCPServer
  url: mcp/ariadnemarketing-com-mcp.json
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://therapists.ariadnemarketing.com/mcp
  - status: 200
    url: https://ariadnemarketing.com/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: 'Ariadne writes a week of marketing for therapists in private practice: Google Business posts, social, referral emails, and a monthly blog, in your voice, with nothing posted without your approval. Small-business version available too. Weekly marketing content written in your voice. Built for therapists in private practice and small businesses.'
image: https://ariadnemarketing.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Ariadne MCP Server
  slug: ariadnemarketing-com-mcp-json
modified: '2026-11-01'
name: Ariadne
nav: Providers
network: true
overview: 'Ariadne is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing, Therapists, Small Business, Automation, and Content.


  Ariadne''s developer surface includes engineering blog, signup flow, and 8 more developer resources.'
plans:
- name: Ariadnemarketing Com Plans Pricing
  plan_count: 0
  slug: ariadnemarketing-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Ariadnemarketing Com Rate Limits
  slug: ariadnemarketing-com-rate-limits
scopes:
- name: Ariadnemarketing Com Scopes
  scope_count: 0
  slug: ariadnemarketing-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 13.4
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ariadnemarketing Com Authentication
  slug: ariadnemarketing-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ariadnemarketing Com Domain Security
  slug: ariadnemarketing-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ariadnemarketing-com
tags:
- Marketing
- Therapists
- Small Business
- Automation
- Content
website: https://ariadnemarketing.com/
---
