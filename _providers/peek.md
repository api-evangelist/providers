---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-09-14'
api_count: 2
apis:
- description: Peek Pro's implementation of the OCTO API specification, the open API standard for the experiences industry. Resellers list a supplier's products, check the availability calendar and per-departure ava
  name: Peek Reseller API (OCTO)
  slug: peek-reseller-api-octo
- description: A free, public, anonymous remote MCP server that gives AI assistants access to Peek.com's catalog of 300,000+ verified experiences with real-time availability and pricing. Six tools cover experience s
  name: Peek Experiences MCP Server
  slug: peek-experiences-mcp-server
artifact_total: 9
asyncapis:
- description: ''
  name: Peek Octo Webhooks
  slug: peek-octo-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.peek.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://octodocs.peek.com/
- group: docs
  title: ''
  type: Documentation
  url: https://octodocs.peek.com/
- group: docs
  title: ''
  type: APIReference
  url: https://octodocs.peek.com/booking-flow/products
- group: start
  title: ''
  type: GettingStarted
  url: https://octodocs.peek.com/getting-started/basics
- group: start
  title: ''
  type: SignUp
  url: https://www.peekpro.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.peekpro.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.peekpro.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/peek-travel
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.peekpro.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.peekpro.com/privacy-policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/llms/peek-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/peek-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/mcp/peek-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/peek-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/packages/peek-packages.yml
  title: ''
  type: Packages
  url: packages/peek-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/packages/peek-packages.yml
  title: ''
  type: SDKs
  url: packages/peek-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/cli/peek-cli.yml
  title: ''
  type: CLI
  url: cli/peek-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/well-known/peek-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/peek-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/well-known/peek-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/peek-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/security/peek-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/peek-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/security/peek-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/peek-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/security/peek-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/peek-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/conformance/peek-conformance.yml
  title: ''
  type: Conformance
  url: conformance/peek-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/authentication/peek-authentication.yml
  title: ''
  type: Authentication
  url: authentication/peek-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/errors/peek-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/peek-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/lifecycle/peek-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/peek-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/conventions/peek-conventions.yml
  title: ''
  type: Conventions
  url: conventions/peek-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/asyncapi/peek-octo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/peek-octo-webhooks.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/plans/peek-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/peek-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/rate-limits/peek-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/peek-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/data-model/peek-data-model.yml
  title: ''
  type: DataModel
  url: data-model/peek-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/changelog/peek-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/peek-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/sandbox/peek-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/peek-sandbox.yml
created: '2026-08-26'
description: 'Peek is a San Francisco-based travel technology company founded in 2012 by Ruzwana Bashir and Oskar Bruening. It operates two connected surfaces: peek.com, a consumer marketplace of 300,000+ bookable tours, activities, rentals and attractions, and Peek Pro, the booking and back-office operating system used by tour, activity, rental and attraction operators for reservations, capacity and inventory, waivers, payments, dynamic pricing and reporting. Its public API surface is the Peek Reseller API — an implementation of the OCTO (Open Connectivity for Tourism) open standard for the experiences industry, covering products, availability, booking, pricing and booking webhooks — plus a free public remote MCP server at mcp.peek.com that gives AI assistants live experience search, detail and availability, and a Developer Hub with app SDKs, a CLI and an n8n connector for building apps embedded inside Peek Pro.'
image: https://cdn.prod.website-files.com/63c9874aa33ce9a6f0ab0e91/63c9874aa33ce95c4eab0ecc_peek-pro-logo.svg
layout: provider
mcp_servers:
- description: Build travel itineraries with Peek's 300k+ experiences. Search, details, and availability.
  name: Experiences MCP
  slug: experiences-mcp
modified: '2026-08-26'
name: Peek
nav: Providers
network: true
overview: 'Peek publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Tourism, Booking, and Reservations.


  The Peek catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Peek''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, CLI, and 25 more developer resources.'
plans:
- name: Peek Plans Pricing
  plan_count: 0
  slug: peek-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Peek Rate Limits
  slug: peek-rate-limits
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 78.6
    discoverability: 75.9
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 49.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/peek/refs/heads/main/screenshots/peek-2026-09-02T150936.png
security:
- kind: authentication
  name: Peek Authentication
  slug: peek-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Peek Domain Security
  slug: peek-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Peek Vulnerability Disclosure
  slug: peek-vulnerability-disclosure
  summary_line: Hackerone
slug: peek
tags:
- Company
- Travel
- Tourism
- Booking
- Reservations
- Experience
- Tours and Activities
- Payments
- Marketplace
- MCP
- OCTO
- Software-as-a-Service
website: https://www.peek.com/
---
