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
api_count: 0
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/zovo-one/llms/zovo-one-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zovo-one-llms.txt
- group: agent
  href: https://artifacts.apis.io/zovo-one/mcp/zovo-one-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/zovo-one-mcp.yml
- group: agent
  href: https://artifacts.apis.io/zovo-one/well-known/zovo-one-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zovo-one-well-known.yml
- group: other
  href: https://artifacts.apis.io/zovo-one/hosts/zovo-one-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zovo-one-hosts.yml
- group: other
  href: https://artifacts.apis.io/zovo-one/vendors/zovo-one-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zovo-one-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://zovo.one/support
- group: operate
  title: ''
  type: Roadmap
  url: https://zovo.one/roadmap
- group: docs
  title: ''
  type: Documentation
  url: https://zovo.one/guides
- group: operate
  title: ''
  type: ChangeLog
  url: https://zovo.one/changelog
- group: auth
  href: https://artifacts.apis.io/zovo-one/security/zovo-one-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zovo-one-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zovo.one/
- group: company
  title: ''
  type: Blog
  url: https://zovo.one/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://zovo.one/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/theluckystrike
coverage:
  checked: '2026-10-29'
  detail: Zovo provides free browser tools and Chrome extensions but does not offer a public developer API.
  evidence:
  - status: 200
    url: https://zovo.one/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Zovo publishes 108 Chrome extensions and free online tools, serving over 150,000 users. Built and maintained by a single developer, Michael Lip, the extensions cover productivity, privacy, and developer utilities. Free features run locally in the browser, while optional Pro upgrades unlock additional capabilities for a monthly or lifetime fee. The site also offers browser-based tools such as calculators, converters, and editors, all accessible without installation. Zovo’s open‑source code is hosted on GitHub under the MIT licence.
image: https://zovo.one/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.zovo.one requiring an API key.
  name: zovo-one MCP Server
  slug: zovo-one-mcp-yml
modified: '2026-10-29'
name: zovo-one
nav: Providers
network: true
overview: 'zovo-one is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chrome Extensions, Productivity, Privacy, and Free Tools.


  zovo-one''s developer surface includes support, documentation, changelog, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Zovo One Plans Pricing
  plan_count: 0
  slug: zovo-one-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Zovo One Rate Limits
  slug: zovo-one-rate-limits
scopes:
- name: Zovo One Scopes
  scope_count: 0
  slug: zovo-one-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 58.3
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.7
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/zovo-one/zovo-one-2026-11-03T150544.png
security:
- kind: authentication
  name: Zovo One Authentication
  slug: zovo-one-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Zovo One Domain Security
  slug: zovo-one-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zovo-one
tags:
- Company
- Chrome Extensions
- Productivity
- Privacy
- Free Tools
- Developers
website: https://zovo.one/
---
