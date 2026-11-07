---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: quarter
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Guesty Agentic Access
  operation_count: 10
  slug: guesty-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 5
apis:
- baseURL: https://open-api.guesty.com
  baseurl_source: declared
  description: Listing availability and pricing
  name: Guesty Calendars API
  slug: guesty-calendars-api
- baseURL: https://open-api.guesty.com
  baseurl_source: declared
  description: Guest communication threads
  name: Guesty Conversations API
  slug: guesty-conversations-api
- baseURL: https://open-api.guesty.com
  baseurl_source: declared
  description: Guest profiles
  name: Guesty Guests API
  slug: guesty-guests-api
- baseURL: https://open-api.guesty.com
  baseurl_source: declared
  description: Property listings
  name: Guesty Listings API
  slug: guesty-listings-api
- baseURL: https://open-api.guesty.com
  baseurl_source: declared
  description: Bookings and reservations
  name: Guesty Reservations API
  slug: guesty-reservations-api
artifact_total: 19
collections:
- collection_type: open
  name: Guesty Open Calendars API
  slug: open-guesty-calendars-api
- collection_type: open
  name: Guesty Open Calendars Conversations API
  slug: open-guesty-conversations-api
- collection_type: open
  name: Guesty Open Calendars Guests API
  slug: open-guesty-guests-api
- collection_type: open
  name: Guesty Open Calendars Listings API
  slug: open-guesty-listings-api
- collection_type: open
  name: Guesty Open Calendars Reservations API
  slug: open-guesty-reservations-api
- collection_type: open
  name: Guesty Open API
  slug: open-guesty
common:
- group: commercial
  href: https://artifacts.apis.io/guesty/plans/guesty-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/guesty-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/guesty/rate-limits/guesty-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/guesty-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/guesty/finops/guesty-finops.yml
  title: ''
  type: FinOps
  url: finops/guesty-finops.yml
- group: other
  href: https://artifacts.apis.io/guesty/capabilities/guesty-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/guesty-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/guesty/agentic-access/guesty-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/guesty-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/guesty/security/guesty-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/guesty-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/guesty/authentication/guesty-authentication.yml
  title: ''
  type: Authentication
  url: authentication/guesty-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/guestyorg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/guesty
- group: start
  title: ''
  type: Portal
  url: https://open-api-docs.guesty.com/
- group: company
  title: ''
  type: Website
  url: https://www.guesty.com/
- group: start
  title: ''
  type: Signup
  url: https://app.guesty.com/register
- group: operate
  title: ''
  type: Support
  url: https://help.guesty.com/
- group: company
  title: ''
  type: Blog
  url: https://www.guesty.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://open-api-docs.guesty.com/reference
- group: agent
  title: ''
  type: LlmsText
  url: https://open-api-docs.guesty.com/llms.txt
created: '2025-02-12'
description: Guesty is a property management platform for short-term rental businesses. The Guesty Open API provides programmatic access to manage properties, reservations, guests, and operations across multiple listing channels.
finops:
- has_sources: false
  method: generated
  name: Guesty Finops
  primary_unit: request
  service_category: API
  slug: guesty-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/guesty.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.guesty.com over HTTP; 138 tools listed.
  name: Guesty MCP Server
  slug: guesty
modified: '2026-05-19'
name: Guesty
nav: Providers
network: true
overview: 'Guesty is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Calendars API, Conversations API, Guests API, and 2 more. Tagged areas include Booking, Hospitality, Property Management, Reservations, and Short-Term Rental.


  The Guesty catalog on APIs.io includes 1 Spectral governance ruleset.


  Guesty''s developer surface includes authentication, developer portal, signup flow, support, engineering blog, API reference, and 10 more developer resources.'
plans:
- name: Guesty Plans Pricing
  plan_count: 3
  slug: guesty-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Guesty Rate Limits
  slug: guesty-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Guesty API Rules
  rule_count: 59
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 1
  slug: guesty-rules
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 50.5
    catalog_earned_first_party: 0.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.7
  facets:
    access_clarity: 21.1
    contract_governance: 13.6
    contract_quality: 46.0
    developer_ergonomics: 45.2
    discoverability: 80.0
    operational_transparency: 26.3
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/guesty/guesty-2026-06-20T182431.png
security:
- kind: authentication
  name: Guesty Authentication
  slug: guesty-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Guesty Domain Security
  slug: guesty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: guesty
tags:
- Booking
- Hospitality
- Property Management
- Reservations
- Short-Term Rental
- Vacation Rentals
website: https://www.guesty.com/
---
