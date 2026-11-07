---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 1Social provides an API to publish posts to multiple social networks via AI chat interfaces.
  name: 1Social API
  slug: 1social-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/1social-dev/plans/1social-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/1social-dev-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/1social-dev/authentication/1social-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/1social-dev-authentication.yml
- group: agent
  href: https://artifacts.apis.io/1social-dev/llms/1social-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/1social-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/1social-dev/mcp/1social-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/1social-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/1social-dev/well-known/1social-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/1social-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/1social-dev/hosts/1social-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/1social-dev-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1social.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://1social.dev/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://1social.dev/login
- group: auth
  href: https://artifacts.apis.io/1social-dev/security/1social-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/1social-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1social.dev/
- group: company
  title: ''
  type: Blog
  url: https://1social.dev/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://1social.dev/pricing
- group: operate
  title: ''
  type: Support
  url: https://1social.dev/support
coverage:
  checked: '2026-10-31'
  detail: The provider's website is publicly accessible but no machine‑readable API specification (OpenAPI, AsyncAPI, GraphQL, etc.) was found.
  evidence:
  - status: 200
    url: https://1social.dev/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 1Social enables publishing to major social networks directly from AI chat interfaces like ChatGPT and Claude. One message to your AI agent is sent to Instagram, TikTok, YouTube Shorts, LinkedIn, X, Bluesky, Threads and Facebook, with each caption automatically trimmed to fit. No dashboard, no copy‑paste, and scheduling is handled server‑side. The service respects your tokens, never stores them, and provides engagement metrics per network.
image: https://1social.dev/_og/d/c_Brand,title_Post+to+every+network+from+your+AI+chat.,subtitle_~SW5zdGFncmFtIMK3IFRpa1RvayDCtyBMaW5rZWRJbiDCtyBYIMK3IEJsdWVza3kgwrcgVGhyZWFkcyDCtyBGYWNlYm9vayDCtyBZb3VUdWJlIFNob3J0cw,s_8YGy0IqXIExpTTKB.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.1social.dev requiring OAuth.
  name: 1Social MCP Server
  slug: 1social-dev-mcp-yml
modified: '2026-10-31'
name: 1Social
nav: Providers
network: true
overview: '1Social is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media, AI Integration, Automation, Content Publishing, and ChatGPT.


  1Social''s developer surface includes authentication, engineering blog, pricing, support, and 10 more developer resources.'
plans:
- name: 1Social Dev Plans Pricing
  plan_count: 2
  slug: 1social-dev-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: 1Social Dev Rate Limits
  slug: 1social-dev-rate-limits
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 23.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 1Social Dev Authentication
  slug: 1social-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 1Social Dev Domain Security
  slug: 1social-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 1social-dev
tags:
- Social Media
- AI Integration
- Automation
- Content Publishing
- ChatGPT
website: https://1social.dev/
---
