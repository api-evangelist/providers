---
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Australian address autocomplete, validation and geocoding API.
  name: Locio API
  slug: locio-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/locio/refs/heads/main/plans/locio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/locio-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/locio/refs/heads/main/authentication/locio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/locio-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/locio/refs/heads/main/conformance/locio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/locio-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/locio/refs/heads/main/llms/locio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/locio-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/locio/refs/heads/main/mcp/locio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/locio-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/locio/refs/heads/main/well-known/locio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/locio-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/locio/refs/heads/main/hosts/locio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/locio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/locio/refs/heads/main/vendors/locio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/locio-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/locio/refs/heads/main/packages/locio-packages.yml
  title: ''
  type: SDKs
  url: packages/locio-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/locio/refs/heads/main/packages/locio-packages.yml
  title: ''
  type: Packages
  url: packages/locio-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.locio.com.au</code
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/locio/refs/heads/main/security/locio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/locio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://locio.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://locio.com.au/docs
- group: docs
  title: ''
  type: APIReference
  url: https://locio.com.au/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://locio.com.au/guides
- group: operate
  title: ''
  type: Support
  url: https://locio.com.au/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://locio.com.au/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://locio.com.au/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://locio.com.au/pricing
- group: start
  title: ''
  type: SignUp
  url: https://locio.com.au/account/api
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.locio.com.au/v1/openapi.json
  - status: 401
    url: https://api.locio.com.au/mcp
  reason: partner-login
  state: gated
created: '2026-10-02'
description: Locio provides an Australian address API and MCP server offering G-NAF lookup, geocoding, address autocomplete, and validation. It returns structured address fields, coordinates, and mesh block data, and supports AI agents via MCP integration. Free tier includes 10,000 lookups per month with no credit card required.
image: https://locio.com.au/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.locio.com.au.
  name: Locio MCP Server
  slug: locio-mcp-yml
modified: '2026-10-02'
name: Locio
nav: Providers
network: true
overview: 'Locio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Address, Geocoding, and MCP.


  Locio''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Locio Plans Pricing
  plan_count: 4
  slug: locio-plans-pricing
random_paper: 6
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 66.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Locio Authentication
  slug: locio-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Locio Domain Security
  slug: locio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: locio
tags:
- Company
- Address
- Geocoding
- MCP
website: https://locio.com.au/
---
