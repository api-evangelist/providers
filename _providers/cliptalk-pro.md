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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
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
  score: 34.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ''
  name: ClipTalk API v1
  slug: cliptalk-api-v1
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/cliptalk-pro/conventions/cliptalk-pro-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cliptalk-pro-conventions.yml
- group: design
  href: https://artifacts.apis.io/cliptalk-pro/conventions/cliptalk-pro-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cliptalk-pro-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/payamsaremi/cliptalk-mcp/blob/main/SECURITY.md
- group: auth
  href: https://artifacts.apis.io/cliptalk-pro/authentication/cliptalk-pro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cliptalk-pro-authentication.yml
- group: design
  href: https://artifacts.apis.io/cliptalk-pro/errors/cliptalk-pro-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cliptalk-pro-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cliptalk-pro/conformance/cliptalk-pro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cliptalk-pro-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cliptalk-pro/llms/cliptalk-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cliptalk-pro-llms.txt
- group: other
  href: https://artifacts.apis.io/cliptalk-pro/a2a/cliptalk-pro-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cliptalk-pro-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cliptalk-pro/mcp/cliptalk-pro-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cliptalk-pro-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cliptalk-pro/well-known/cliptalk-pro-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cliptalk-pro-security.txt
- group: auth
  href: https://artifacts.apis.io/cliptalk-pro/well-known/cliptalk-pro-cliptalk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cliptalk-pro-cliptalk-security.txt
- group: agent
  href: https://artifacts.apis.io/cliptalk-pro/well-known/cliptalk-pro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cliptalk-pro-well-known.yml
- group: other
  href: https://artifacts.apis.io/cliptalk-pro/hosts/cliptalk-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cliptalk-pro-hosts.yml
- group: other
  href: https://artifacts.apis.io/cliptalk-pro/vendors/cliptalk-pro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cliptalk-pro-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cliptalk-pro/security/cliptalk-pro-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cliptalk-pro-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cliptalk-pro/security/cliptalk-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cliptalk-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cliptalk.pro
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cliptalk.pro/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://www.cliptalk.pro/api/v1
- group: docs
  title: ''
  type: APIReference
  url: https://www.cliptalk.pro/api/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cliptalk.pro/api/v1
- group: operate
  title: ''
  type: Support
  url: https://www.cliptalk.pro/contact
- group: company
  title: ''
  type: Blog
  url: https://www.cliptalk.pro/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cliptalk.pro/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.cliptalk.pro/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cliptalk.pro/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cliptalk.pro/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: API reference is provided as markdown at https://www.cliptalk.pro/api/v1 but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable spec is published.
  evidence:
  - status: 200
    url: https://www.cliptalk.pro/api/v1
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: ClipTalk provides an AI-powered video creation platform that instantly generates short-form videos for Instagram Reels, YouTube Shorts, TikTok, and other social media. Users describe a concept or provide media, and the service automatically scripts, selects visuals, adds voiceovers, captions, and music, delivering a ready-to-post MP4. The platform also offers a suite of AI tools for content creators, marketers, and developers via a REST API and MCP integration, enabling automated video production at scale.
image: https://www.cliptalk.pro/cliptalk-og.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.cliptalk.pro requiring OAuth.
  name: ClipTalk MCP Server
  slug: cliptalk-pro-mcp-yml
modified: '2026-10-29'
name: ClipTalk
nav: Providers
network: true
overview: 'ClipTalk is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Video, Social Media, and Automation.


  ClipTalk''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Cliptalk Pro Plans Pricing
  plan_count: 0
  slug: cliptalk-pro-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Cliptalk Pro Rate Limits
  slug: cliptalk-pro-rate-limits
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 22.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 75.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 33.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cliptalk-pro/cliptalk-pro-2026-11-03T124443.png
security:
- kind: authentication
  name: Cliptalk Pro Authentication
  slug: cliptalk-pro-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cliptalk Pro Domain Security
  slug: cliptalk-pro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cliptalk Pro Vulnerability Disclosure
  slug: cliptalk-pro-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cliptalk-pro
tags:
- Company
- Artificial Intelligence
- Video
- Social Media
- Automation
website: https://cliptalk.pro
---
