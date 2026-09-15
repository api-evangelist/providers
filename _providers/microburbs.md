---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-09-14'
api_count: 1
apis:
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: 'The Microburbs Property Data API: 173 metered, read-only REST operations for Australian property and suburb intelligence -- AVM valuations, sale/rent history, comparables, risk overlays, zoning, schoo'
  name: Microburbs API
  slug: microburbs-api
artifact_total: 6
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microburbs/refs/heads/main/security/microburbs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microburbs-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microburbs/refs/heads/main/authentication/microburbs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microburbs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.microburbs.com.au
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microburbs/refs/heads/main/well-known/microburbs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microburbs-well-known.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.microburbs.com.au/developers/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microburbs.com.au/api-access
- group: start
  title: ''
  type: SignUp
  url: https://www.microburbs.com.au/developers/keys
- group: operate
  title: ''
  type: Support
  url: https://www.microburbs.com.au/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microburbs.com.au/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.microburbs.com.au/privacy
- group: operate
  title: ''
  type: FAQ
  url: https://www.microburbs.com.au/faqs
created: '2026-09-14'
description: 'Microburbs is an Australian property and location-intelligence API: 173 read-only operations spanning property valuations (AVM), sale and rent history, comparable sales, environmental and neighbourhood risk overlays, zoning and development, schools, transport, demographics and suburb screening -- keyed to ABS statistical geography and G-NAF addresses, and mirrored as a hosted MCP server of 174 tools with per-call cent metering.'
layout: provider
mcp_servers:
- description: Australian property and suburb data as native MCP tools -- valuations, sale and rent history, comparables, risk overlays, zoning, schools, transport and demographics for every Australian address (GNAF
  name: Microburbs MCP Server
  slug: microburbs-mcp-server
modified: '2026-09-14'
name: Microburbs
nav: Providers
network: true
overview: 'Microburbs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Property Data, Real-Estate, Australia, Demographics, and Location Intelligence.


  Microburbs'' developer surface includes authentication, pricing, signup flow, support, FAQ, and 6 more developer resources.'
plans:
- name: Microburbs Plans Pricing
  plan_count: 0
  slug: microburbs-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Microburbs Rate Limits
  slug: microburbs-rate-limits
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 55.7
    developer_ergonomics: 44.6
    discoverability: 72.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Microburbs Authentication
  slug: microburbs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microburbs Domain Security
  slug: microburbs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microburbs
tags:
- Property Data
- Real-Estate
- Australia
- Demographics
- Location Intelligence
website: https://www.microburbs.com.au
---
