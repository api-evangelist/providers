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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Beleeg league management platform.
  name: Beleeg API
  slug: beleeg-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/beleeg-com/plans/beleeg-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beleeg-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/beleeg-com/llms/beleeg-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beleeg-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/beleeg-com/mcp/beleeg-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/beleeg-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/beleeg-com/well-known/beleeg-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beleeg-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/beleeg-com/hosts/beleeg-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beleeg-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/beleeg-com/vendors/beleeg-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beleeg-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beleeg.com/terms
- group: operate
  title: ''
  type: Support
  url: https://beleeg.com/help
- group: operate
  title: ''
  type: StatusPage
  url: https://beleeg.com/status
- group: start
  title: ''
  type: SignUp
  url: https://beleeg.com/admin/signup
- group: auth
  title: ''
  type: Security
  url: https://beleeg.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beleeg.com/privacy
- group: auth
  href: https://artifacts.apis.io/beleeg-com/security/beleeg-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/beleeg-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/beleeg-com/security/beleeg-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beleeg-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beleeg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://beleeg.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://beleeg.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://beleeg.com/pricing
coverage:
  checked: '2026-10-30'
  detail: API reference page https://beleeg.com/api returns a not-found page with no machine-readable specification.
  evidence:
  - status: 200
    url: https://beleeg.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Beleeg provides the easiest league software for sports organizations, offering scheduling, standings, scores, dues management, and a customizable website. Teams can quickly set up leagues, track results, collect payments, and engage members, with features like automated scheduling, real-time score updates, and integrated payment processing.
image: https://beleeg.com/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at beleeg.com.
  name: beleeg-com MCP Server
  slug: beleeg-com-mcp-yml
modified: '2026-10-29'
name: beleeg-com
nav: Providers
network: true
overview: 'beleeg-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, League-Management, Scheduling, and Payments.


  beleeg-com''s developer surface includes support, signup flow, documentation, API reference, pricing, and 13 more developer resources.'
plans:
- name: Beleeg Com Plans Pricing
  plan_count: 3
  slug: beleeg-com-plans-pricing
random_paper: 16
scopes:
- name: Beleeg Com Scopes
  scope_count: 0
  slug: beleeg-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 66.7
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.7
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 23.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/beleeg-com/beleeg-com-2026-11-03T121645.png
security:
- kind: authentication
  name: Beleeg Com Authentication
  slug: beleeg-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Beleeg Com Domain Security
  slug: beleeg-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Beleeg Com Vulnerability Disclosure
  slug: beleeg-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: beleeg-com
tags:
- Company
- Sports
- League-Management
- Scheduling
- Payments
- Web App
website: https://beleeg.com/
---
