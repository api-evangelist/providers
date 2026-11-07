---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
- description: Public developer portal for Akiflow, but no machine‑readable API specification is published.
  name: Akiflow API
  slug: akiflow-api
artifact_total: 8
common:
- group: build
  href: https://artifacts.apis.io/akiflow-com/cli/akiflow-com-cli.yml
  title: ''
  type: CLI
  url: cli/akiflow-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/akiflow-com/security/akiflow-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/akiflow-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/akiflow-com/llms/akiflow-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/akiflow-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/akiflow-com/mcp/akiflow-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/akiflow-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/akiflow-com/well-known/akiflow-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/akiflow-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/akiflow-com/hosts/akiflow-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/akiflow-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/akiflow-com/vendors/akiflow-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/akiflow-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/akiflow-com/packages/akiflow-com-packages.yml
  title: ''
  type: SDKs
  url: packages/akiflow-com-packages.yml
- group: build
  href: https://artifacts.apis.io/akiflow-com/packages/akiflow-com-packages.yml
  title: ''
  type: Packages
  url: packages/akiflow-com-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://product.akiflow.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://product.akiflow.com/p/inline-subtask-creation-during-new-task-setup
- group: auth
  href: https://artifacts.apis.io/akiflow-com/security/akiflow-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/akiflow-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/akiflow-com/security/akiflow-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/akiflow-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://akiflow.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://akiflow.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://akiflow.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://akiflow.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://akiflow.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://akiflow.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://web.akiflow.com/auth/register
- group: operate
  title: ''
  type: Support
  url: https://product.akiflow.com/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://akiflow.com/terms-of-service
coverage:
  checked: '2026-11-01'
  detail: Developer portal provides documentation but no machine‑readable API specification is published.
  evidence:
  - status: 200
    url: https://akiflow.com/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Akiflow brings tasks, calendars, and AI into one time‑blocking planner, helping busy professionals plan focused days and follow through. From a simple idea to an all‑in‑one platform, Akiflow is building the ultimate time‑blocking app, imagining the future of work together.
image: https://framerusercontent.com/assets/4Gxi74kOT8XyoFWliuXnlk3LC4.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.akiflow.com.
  name: Akiflow MCP Server
  slug: akiflow-com-mcp-yml
modified: '2026-11-01'
name: Akiflow
nav: Providers
network: true
overview: 'Akiflow is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Productivity, Calendar, Task Management, Time Blocking, and Artificial Intelligence.


  Akiflow''s developer surface includes CLI, changelog, getting-started guide, documentation, pricing, engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Akiflow Com Plans Pricing
  plan_count: 0
  slug: akiflow-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Akiflow Com Rate Limits
  slug: akiflow-com-rate-limits
scopes:
- name: Akiflow Com Scopes
  scope_count: 0
  slug: akiflow-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 56.7
    operational_transparency: 18.4
  previous_composite: 31.1
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Akiflow Com Authentication
  slug: akiflow-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Akiflow Com Domain Security
  slug: akiflow-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Akiflow Com Vulnerability Disclosure
  slug: akiflow-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: akiflow-com
tags:
- Productivity
- Calendar
- Task Management
- Time Blocking
- Artificial Intelligence
website: https://akiflow.com/
---
