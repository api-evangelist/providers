---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 59.6
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 70
  human_in_the_loop: 0
  name: Apex27 Agentic Access
  operation_count: 129
  slug: apex27-agentic-access
  summary_line: 129 operations · 70 acting
api_count: 2
apis:
- description: 'The Apex27 CRM API is the vendor''s REST interface over the estate agency CRM, covering contacts, leads, listings and their media, rooms, keys, notes, offers, viewings, valuations, inspections, issues '
  name: Apex27 CRM API
  slug: apex27-crm-api
- description: The Apex27 Portal API is the per-tenant, website-facing API that drives search and enquiry on Apex27-built agency websites. Its documented operations are get-listings, get-listing, get-search-options,
  name: Apex27 Portal API
  slug: apex27-portal-api
artifact_total: 6
asyncapis:
- description: ''
  name: Apex27 Webhooks
  slug: apex27-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apex27-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apex27-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apex27-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://apex27.co.uk/
- group: start
  title: ''
  type: SignUp
  url: https://apex27.co.uk/estate-agent-software-sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://apex27.co.uk/estate-agent-software-pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://apex27.co.uk/crm-changelog
- group: company
  title: ''
  type: Blog
  url: https://apex27.co.uk/estate-agency-blog
- group: operate
  title: ''
  type: Support
  url: https://apex27.co.uk/contact-apex27
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apex27.co.uk/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apex27.co.uk/privacy-policy
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://apex27.co.uk/acceptable-use-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apex27
- group: build
  title: ''
  type: Packages
  url: packages/apex27-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apex27-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/apex27-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apex27-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apex27-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apex27-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/apex27-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apex27-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apex27-vocabulary.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/apex27-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-26'
description: Apex27 Limited is a United Kingdom estate agency CRM vendor, founded in 2019 and headquartered in the UK, selling cloud software to sales, lettings and commercial agents for £35 per user per month. It sits in the middle of the UK residential value chain — between the agent and the portals — capturing leads, applicants, listings, viewings, valuations, offers, sales progression and tenancies, then syndicating listings out to Rightmove, Zoopla, OnTheMarket and others. Because the UK has no MLS and no cooperative listing database, that CRM seat is the only practical route a listing takes to market, and Apex27 is one of the private gatekeepers of it. Apex27 does operate two real HTTP APIs — the Apex27 CRM API at api.apex27.co.uk and a per-tenant Portal API that powers agency websites — but neither has a public developer portal. The documentation URL that Apex27's own published n8n node points at, docs.apex27.co.uk, returns 404, and every CRM endpoint returns 401 Unauthorised without
  a key issued inside a paid tenant. Access is customer-only, not self-serve. RESO does not apply — no RESO Web API or Data Dictionary certification exists for Apex27 or for the UK market at all, since RESO is a NAR/MLS construct with no UK counterpart. Apex27 publishes no open data; the UK's open property layer belongs to HM Land Registry and Ordnance Survey, not to the CRM vendors.
image: https://apex27.co.uk/img/icon.png
layout: provider
modified: '2026-07-26'
name: Apex27
nav: Providers
network: true
overview: 'Apex27 publishes 2 APIs on the [APIs.io](https://apis.io/) network: CRM API and Portal API. Tagged areas include Real Estate, United Kingdom, PropTech, Property Listings, and CRM.


  The Apex27 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Apex27''s developer surface includes authentication, signup flow, pricing, changelog, engineering blog, support, and 18 more developer resources.'
random_paper: 59
score:
  band: thin
  composite: 44.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 66.8
    developer_ergonomics: 23.9
    discoverability: 92.5
    governance: 13.2
    operational_transparency: 23.7
  previous_composite: 44.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Apex27 Authentication
  slug: apex27-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Apex27 Domain Security
  slug: apex27-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: apex27
tags:
- Real Estate
- United Kingdom
- PropTech
- Property Listings
- CRM
- Estate Agency
- Lettings
- Rentals
- Property Management
- Valuation
- Tenancy
- Conveyancing
website: https://apex27.co.uk/
---
