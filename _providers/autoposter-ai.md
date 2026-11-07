---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Automated social media publishing, scheduling, draft creation, and receipt tracking for AI assistants (ChatGPT, Claude, Cursor, OpenClaw).
  name: Autoposter AI Agent API
  slug: autoposter-ai-agent-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/autoposter-ai/plans/autoposter-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autoposter-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/autoposter-ai/conformance/autoposter-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autoposter-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/autoposter-ai/llms/autoposter-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autoposter-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/autoposter-ai/mcp/autoposter-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/autoposter-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/autoposter-ai/well-known/autoposter-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autoposter-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/autoposter-ai/hosts/autoposter-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autoposter-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/autoposter-ai/vendors/autoposter-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autoposter-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autoposter.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autoposter.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vladilins
- group: auth
  href: https://artifacts.apis.io/autoposter-ai/security/autoposter-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autoposter-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autoposter.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://agent.autoposter.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://autoposter.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://autoposter.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://autoposter.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://autoposter.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://autoposter.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.autoposter.ai/signup
created: '2026-11-02'
description: Auto Poster AI is a social media scheduling platform powered by AI tools that helps creators, businesses, and agencies automate content creation, scheduling, and posting across multiple platforms such as Instagram, TikTok, Facebook, LinkedIn, and X. It offers AI-generated captions, brand voice customization, multi‑workspace collaboration, and a link‑in‑bio feature, aiming to streamline social media workflows and boost engagement.
image: https://autoposter.ai/og-homepage.png
layout: provider
mcp_servers:
- description: Remote MCP server at agent.autoposter.ai.
  name: Auto Poster AI MCP Server
  slug: autoposter-ai-mcp-yml
modified: '2026-11-02'
name: Auto Poster AI
nav: Providers
network: true
overview: 'Auto Poster AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media, Artificial Intelligence, Automation, Marketing, and Scheduler.


  Auto Poster AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Autoposter Ai Plans Pricing
  plan_count: 6
  slug: autoposter-ai-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 31.3
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autoposter Ai Domain Security
  slug: autoposter-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: autoposter-ai
tags:
- Social Media
- Artificial Intelligence
- Automation
- Marketing
- Scheduler
website: https://autoposter.ai/
---
