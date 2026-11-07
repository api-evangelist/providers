---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
- description: AxoWatch provides monitoring capabilities but no public machine‑readable API contract was found.
  name: AxoWatch API
  slug: axowatch-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/axowatch-com/plans/axowatch-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/axowatch-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/axowatch-com/changelog/axowatch-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/axowatch-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/axowatch-com/llms/axowatch-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/axowatch-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/axowatch-com/mcp/axowatch-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/axowatch-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/axowatch-com/well-known/axowatch-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/axowatch-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/axowatch-com/hosts/axowatch-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axowatch-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/axowatch-com/vendors/axowatch-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axowatch-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://axowatch.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://axowatch.com/changelog
- group: auth
  href: https://artifacts.apis.io/axowatch-com/security/axowatch-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axowatch-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axowatch.com/
- group: company
  title: ''
  type: Blog
  url: https://axowatch.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://axowatch.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://axowatch.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axowatch.com/privacy
coverage:
  checked: '2026-11-02'
  detail: Public website and marketing pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://axowatch.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: AxoWatch provides AI‑driven website monitoring that continuously watches your site’s user flows, uptime, page speed, and error events. It detects issues such as broken checkout steps, SSL certificate expiry, and performance slowdowns, then generates automated fix suggestions that can be reviewed and applied. The platform offers real‑time alerts, a guard that simulates real visitors, and integrates with tools like Sentry to streamline remediation for site owners and developers.
image: https://axowatch.com/media/63b6463a-d2ce-42a8-b2f1-007ac4914e81.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at axowatch.com.
  name: AxoWatch MCP Server
  slug: axowatch-com-mcp-yml
modified: '2026-11-02'
name: AxoWatch
nav: Providers
network: true
overview: 'AxoWatch is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Monitoring, Uptime, Performance, Error Tracking, and Artificial Intelligence.


  AxoWatch''s developer surface includes changelog, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Axowatch Com Plans Pricing
  plan_count: 4
  slug: axowatch-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Axowatch Com Rate Limits
  slug: axowatch-com-rate-limits
scopes:
- name: Axowatch Com Scopes
  scope_count: 0
  slug: axowatch-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 56.7
    operational_transparency: 7.9
  previous_composite: 25.3
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Axowatch Com Authentication
  slug: axowatch-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Axowatch Com Domain Security
  slug: axowatch-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: axowatch-com
tags:
- Monitoring
- Uptime
- Performance
- Error Tracking
- Artificial Intelligence
- Software-as-a-Service
website: https://axowatch.com/
---
