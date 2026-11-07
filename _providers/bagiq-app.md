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
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: BagIQ offers a disc‑golf bag builder and analysis tool; its API is exposed via an MCP endpoint.
  name: BagIQ API
  slug: bagiq-api
artifact_total: 8
common:
- group: operate
  href: https://artifacts.apis.io/bagiq-app/changelog/bagiq-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bagiq-app-changelog.yml
- group: auth
  href: https://artifacts.apis.io/bagiq-app/security/bagiq-app-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bagiq-app-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/bagiq-app/llms/bagiq-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bagiq-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/bagiq-app/mcp/bagiq-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bagiq-app-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bagiq-app/well-known/bagiq-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bagiq-app-security.txt
- group: agent
  href: https://artifacts.apis.io/bagiq-app/well-known/bagiq-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bagiq-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/bagiq-app/hosts/bagiq-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bagiq-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/bagiq-app/vendors/bagiq-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bagiq-app-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://bagiq.app/release-notes
- group: auth
  href: https://artifacts.apis.io/bagiq-app/security/bagiq-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bagiq-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bagiq-app/security/bagiq-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bagiq-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bagiq.app/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bagiq.app/privacy.html
- group: company
  title: ''
  type: Blog
  url: https://bagiq.app/release-notes.html
coverage:
  checked: '2026-11-02'
  detail: The provider's public website and docs contain no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://bagiq.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BagIQ is a free disc‑golf bag builder and gap‑analysis tool that helps players identify missing or overlapping disc slots in their bag. Using real flight data from DiscList™, the app analyses a user’s throws to suggest which discs would improve coverage, highlights redundant discs, and offers live retailer pricing. The service runs entirely in the browser with optional cloud sync via a short bag code, requires no account, and is available on desktop and mobile devices.
image: https://app.bagiq.app/assets/images/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at data.bagiq.app.
  name: BagIQ MCP Server
  slug: bagiq-app-mcp-yml
modified: '2026-11-02'
name: BagIQ
nav: Providers
network: true
overview: 'BagIQ is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Disc Golf, Bag Builder, Sports, and Artificial Intelligence.


  BagIQ''s developer surface includes changelog, engineering blog, and 12 more developer resources.'
plans:
- name: Bagiq App Plans Pricing
  plan_count: 0
  slug: bagiq-app-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Bagiq App Rate Limits
  slug: bagiq-app-rate-limits
scopes:
- name: Bagiq App Scopes
  scope_count: 0
  slug: bagiq-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 56.7
    operational_transparency: 18.4
  previous_composite: 13.8
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bagiq App Authentication
  slug: bagiq-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bagiq App Domain Security
  slug: bagiq-app-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bagiq App Vulnerability Disclosure
  slug: bagiq-app-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bagiq-app
tags:
- Disc Golf
- Bag Builder
- Sports
- Artificial Intelligence
website: https://bagiq.app/
---
