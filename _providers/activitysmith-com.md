---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Send push notifications and Live Activities to your own devices via a single API key.
  name: ActivitySmith API
  slug: activitysmith-api
artifact_total: 7
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://activitysmith.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://activitysmith.com/legal/privacy-policy
- group: operate
  href: https://artifacts.apis.io/activitysmith-com/rate-limits/activitysmith-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/activitysmith-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/activitysmith-com/plans/activitysmith-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/activitysmith-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/activitysmith-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/activitysmith-com/conventions/activitysmith-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/activitysmith-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/activitysmith-com/security/activitysmith-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/activitysmith-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/activitysmith-com/conformance/activitysmith-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/activitysmith-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/activitysmith-com/llms/activitysmith-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/activitysmith-com-llms.txt
- group: build
  href: https://artifacts.apis.io/activitysmith-com/mcp/activitysmith-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/activitysmith-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/activitysmith-com/mcp/activitysmith-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/activitysmith-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/activitysmith-com/well-known/activitysmith-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/activitysmith-com-security.txt
- group: agent
  href: https://artifacts.apis.io/activitysmith-com/well-known/activitysmith-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/activitysmith-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/activitysmith-com/hosts/activitysmith-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/activitysmith-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/activitysmith-com/vendors/activitysmith-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/activitysmith-com-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://activitysmith.com/playground
- group: build
  title: ''
  type: SDKs
  url: https://activitysmith.com/sdks
- group: company
  title: ''
  type: Newsroom
  url: https://activitysmith.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ActivitySmithHQ
- group: operate
  title: ''
  type: ChangeLog
  url: https://activitysmith.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://activitysmith.com/docs/mcp-server
- group: docs
  title: ''
  type: APIReference
  url: https://activitysmith.com/docs/api-reference/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://activitysmith.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://activitysmith.com/lifetime-membership
- group: operate
  title: ''
  type: Support
  url: https://activitysmith.com/contact
- group: company
  title: ''
  type: Blog
  url: https://activitysmith.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://activitysmith.com/lifetime-membership
- group: auth
  href: https://artifacts.apis.io/activitysmith-com/security/activitysmith-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/activitysmith-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/activitysmith-com/security/activitysmith-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/activitysmith-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://activitysmith.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://activitysmith.com/openapi.json
  - status: 401
    url: https://activitysmith.com/api/mcp
  - status: 200
    url: https://activitysmith.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: ActivitySmith provides iPhone push notifications for AI agents, scripts, and backend processes. Users receive alerts when tasks finish, fail, make a sale, or need approval, all via Live Activities. The service includes a dedicated iOS app, no need for custom app development or Apple certificates, and offers developer and team lifetime membership plans.
image: https://cdn.activitysmith.com/og/main.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.activitysmith.com requiring OAuth.
  name: ActivitySmith MCP Server
  slug: activitysmith-com-mcp-yml
modified: '2026-10-31'
name: ActivitySmith
nav: Providers
network: true
overview: 'ActivitySmith is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mobile Notifications, Live Activities, AI Agent Integration, Backend Monitoring, and Deployment Alerts.


  ActivitySmith''s developer surface includes sandbox, changelog, getting-started guide, API reference, documentation, pricing, support, and 23 more developer resources.'
plans:
- name: Activitysmith Com Plans Pricing
  plan_count: 11
  slug: activitysmith-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Activitysmith Com Rate Limits
  slug: activitysmith-com-rate-limits
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.8
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.0
    discoverability: 65.8
    operational_transparency: 42.1
  previous_composite: 42.9
  provenance:
    conformance: derived
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Activitysmith Com Domain Security
  slug: activitysmith-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Activitysmith Com Vulnerability Disclosure
  slug: activitysmith-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: push-notification
  slug: activitysmith-com-push-notification
slug: activitysmith-com
tags:
- Mobile Notifications
- Live Activities
- AI Agent Integration
- Backend Monitoring
- Deployment Alerts
website: https://activitysmith.com/
---
