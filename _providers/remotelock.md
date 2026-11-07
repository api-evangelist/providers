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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
  score: 28.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: RemoteLock API for managing locks, credentials, and access events.
  name: RemoteLock API
  slug: api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/remotelock/llms/remotelock-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/remotelock-llms.txt
- group: build
  href: https://artifacts.apis.io/remotelock/mcp/remotelock-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/remotelock-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/remotelock/mcp/remotelock-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/remotelock-mcp.yml
- group: agent
  href: https://artifacts.apis.io/remotelock/well-known/remotelock-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/remotelock-well-known.yml
- group: other
  href: https://artifacts.apis.io/remotelock/hosts/remotelock-hosts.yml
  title: ''
  type: Hosts
  url: hosts/remotelock-hosts.yml
- group: other
  href: https://artifacts.apis.io/remotelock/vendors/remotelock-vendors.yml
  title: ''
  type: Vendors
  url: vendors/remotelock-vendors.yml
- group: build
  href: https://artifacts.apis.io/remotelock/packages/remotelock-packages.yml
  title: ''
  type: SDKs
  url: packages/remotelock-packages.yml
- group: build
  href: https://artifacts.apis.io/remotelock/packages/remotelock-packages.yml
  title: ''
  type: Packages
  url: packages/remotelock-packages.yml
- group: auth
  href: https://artifacts.apis.io/remotelock/security/remotelock-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/remotelock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://remotelock.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://remotelock.com/product/developer-platform
- group: docs
  title: ''
  type: Documentation
  url: https://remotelock.com/product/developer-platform
- group: docs
  title: ''
  type: APIReference
  url: https://api.remotelock.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://remotelock.com/product/developer-platform
- group: operate
  title: ''
  type: Support
  url: https://support.remotelock.com/s/
- group: company
  title: ''
  type: Blog
  url: https://remotelock.com/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/remotelock
- group: commercial
  title: ''
  type: Pricing
  url: https://remotelock.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://remotelock.com/agreements-and-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://remotelock.com/legal/privacy-policy
coverage:
  checked: '2026-10-28'
  detail: Developer portal provides API information but no machine‑readable OpenAPI, GraphQL SDL, or AsyncAPI spec.
  evidence:
  - status: 200
    url: https://remotelock.com/product/developer-platform
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: RemoteLock provides a cloud-based smart access control platform that enables property owners and managers to control doors, locks, and credentials across multifamily, vacation rentals, and commercial properties. Their API allows developers to integrate lock management, schedule access, and receive real-time events via webhooks, supporting a wide range of hardware and software integrations.
image: https://cdn.prod.website-files.com/69b346cffdf59524de074ed0/6a4f8b637520fe47b60c0175_OG%20Image%20-%20Only%20Logo.webp
layout: provider
mcp_servers:
- description: Remote MCP server at shop.remotelock.com.
  name: RemoteLock MCP Server
  slug: remotelock-mcp-yml
modified: '2026-10-28'
name: RemoteLock
nav: Providers
network: true
overview: 'RemoteLock is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Access Control, IoT, smart-locks, and Property Management.


  RemoteLock''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 14 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 0
  name: Remotelock Rate Limits
  slug: remotelock-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 66.7
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.7
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
screenshot: https://apis.io/screenshots/remotelock/remotelock-2026-11-03T142139.png
security:
- kind: domain-security
  name: Remotelock Domain Security
  slug: remotelock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: remotelock
tags:
- Access Control
- IoT
- smart-locks
- Property Management
website: https://remotelock.com/
---
