---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public documentation and tools are available at BacklinkGenie's website, but no machine‑readable API contract is published.
  name: BacklinkGenie API
  slug: backlinkgenie-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/backlinkgenie-com/plans/backlinkgenie-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/backlinkgenie-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/backlinkgenie-com/changelog/backlinkgenie-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/backlinkgenie-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/backlinkgenie-com/authentication/backlinkgenie-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/backlinkgenie-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/backlinkgenie-com/conformance/backlinkgenie-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/backlinkgenie-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/backlinkgenie-com/llms/backlinkgenie-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/backlinkgenie-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/backlinkgenie-com/mcp/backlinkgenie-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/backlinkgenie-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/backlinkgenie-com/well-known/backlinkgenie-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/backlinkgenie-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/backlinkgenie-com/hosts/backlinkgenie-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backlinkgenie-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/backlinkgenie-com/vendors/backlinkgenie-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backlinkgenie-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.backlinkgenie.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://backlinkgenie.com/guides/
- group: operate
  title: ''
  type: ChangeLog
  url: https://backlinkgenie.com/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://backlinkgenie.com/guides/link-outreach-deliverability/
- group: auth
  href: https://artifacts.apis.io/backlinkgenie-com/security/backlinkgenie-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backlinkgenie-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://backlinkgenie.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://backlinkgenie.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://backlinkgenie.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://backlinkgenie.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://backlinkgenie.com/privacy
coverage:
  checked: '2026-11-02'
  detail: Documentation pages exist but provide no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://backlinkgenie.com/guides/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BacklinkGenie is an AI‑powered link‑building outreach platform that automatically discovers relevant blog posts, round‑ups, comparison and resource pages, crafts personalized pitches, and sends them from a warmed‑up domain mailbox. Users approve each email, and the service follows up and tracks earned backlinks. Plans start at $99 per month and include a free prospect report, with higher tiers offering more outreach capacity.
image: https://backlinkgenie.com/brand/logo-mark.svg
layout: provider
mcp_servers:
- description: Remote MCP server at app.backlinkgenie.com.
  name: BacklinkGenie MCP Server
  slug: backlinkgenie-com-mcp-yml
modified: '2026-11-02'
name: BacklinkGenie
nav: Providers
network: true
overview: 'BacklinkGenie is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, SEO, Link Building, Marketing, and Automation.


  BacklinkGenie''s developer surface includes changelog, authentication, documentation, getting-started guide, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Backlinkgenie Com Plans Pricing
  plan_count: 3
  slug: backlinkgenie-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Backlinkgenie Com Rate Limits
  slug: backlinkgenie-com-rate-limits
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 56.7
    operational_transparency: 7.9
  previous_composite: 33.4
  provenance:
    conformance: first-party
    mcp: derived
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
- kind: authentication
  name: Backlinkgenie Com Authentication
  slug: backlinkgenie-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Backlinkgenie Com Domain Security
  slug: backlinkgenie-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: backlinkgenie-com
tags:
- Artificial Intelligence
- SEO
- Link Building
- Marketing
- Automation
website: https://backlinkgenie.com/
---
