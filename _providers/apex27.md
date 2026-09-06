---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 70
  human_in_the_loop: 0
  name: Apex27 Agentic Access
  operation_count: 129
  slug: apex27-agentic-access
  summary_line: 129 operations · 70 acting
api_count: 2
apis:
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Appointment availability for valuations and viewings.
  name: Apex27 Availability API
  slug: apex27-availability-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Agency branches within the tenant.
  name: Apex27 Branches API
  slug: apex27-branches-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Telephone activity recorded against a contact.
  name: Apex27 Call Logs API
  slug: apex27-call-logs-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Client-portal authentication and sign-in links.
  name: Apex27 Client Portal API
  slug: apex27-client-portal-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Sales completions and progression.
  name: Apex27 Completions API
  slug: apex27-completions-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Orders placed against a contact.
  name: Apex27 Contact Orders API
  slug: apex27-contact-orders-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Referrals raised against a contact (conveyancing, mortgage, survey).
  name: Apex27 Contact Referrals API
  slug: apex27-contact-referrals-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Applicants, vendors, landlords, tenants and buyers held in the CRM.
  name: Apex27 Contacts API
  slug: apex27-contacts-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Documents attached to listings or contacts.
  name: Apex27 Documents API
  slug: apex27-documents-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Website enquiries and valuation requests.
  name: Apex27 Enquiries API
  slug: apex27-enquiries-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Saved listings for a portal contact.
  name: Apex27 Favourites API
  slug: apex27-favourites-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Cross-entity search.
  name: Apex27 Global Search API
  slug: apex27-global-search-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Property inspections (lettings management).
  name: Apex27 Inspections API
  slug: apex27-inspections-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Inbound leads and their pipeline status.
  name: Apex27 Leads API
  slug: apex27-leads-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Maintenance issues raised against a listing.
  name: Apex27 Listing Issues API
  slug: apex27-listing-issues-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Key sets held for a listing, including check-out and check-in.
  name: Apex27 Listing Keys API
  slug: apex27-listing-keys-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Virtual tours, videos, EPC reports and brochure links on a listing.
  name: Apex27 Listing Links API
  slug: apex27-listing-links-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Images, EPCs, floorplans, brochures and videos on a listing.
  name: Apex27 Listing Media API
  slug: apex27-listing-media-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Room-by-room detail on a listing.
  name: Apex27 Listing Rooms API
  slug: apex27-listing-rooms-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Saved applicant listing searches used for matching and alerts.
  name: Apex27 Listing Searches API
  slug: apex27-listing-searches-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Sales, lettings, land and commercial property records.
  name: Apex27 Listings API
  slug: apex27-listings-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Free-text notes attached to a contact or a listing.
  name: Apex27 Notes API
  slug: apex27-notes-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: In-app notifications to users, branches, listings or contacts.
  name: Apex27 Notifications API
  slug: apex27-notifications-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Offers made against listings.
  name: Apex27 Offers API
  slug: apex27-offers-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Compliance and onboarding checklists on a listing.
  name: Apex27 Onboarding Checks API
  slug: apex27-onboarding-checks-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Named geographic search regions.
  name: Apex27 Search Regions API
  slug: apex27-search-regions-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Portal inventory statistics.
  name: Apex27 Statistics API
  slug: apex27-statistics-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Work items assigned to users.
  name: Apex27 Tasks API
  slug: apex27-tasks-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Tenancy agreements and their lifecycle.
  name: Apex27 Tenancies API
  slug: apex27-tenancies-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: CRM users within the tenant.
  name: Apex27 Users API
  slug: apex27-users-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Market appraisals and valuation appointments.
  name: Apex27 Valuations API
  slug: apex27-valuations-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Viewing appointments.
  name: Apex27 Viewings API
  slug: apex27-viewings-api
- baseURL: https://api.apex27.co.uk
  baseurl_source: declared
  description: Webhook subscription management.
  name: Apex27 Webhooks API
  slug: apex27-webhooks-api
artifact_total: 39
asyncapis:
- description: ''
  name: Apex27 Webhooks
  slug: apex27-webhooks
collections:
- collection_type: open
  name: Apex27 CRM API
  slug: open-apex27-crm-api
- collection_type: open
  name: Apex27 Portal API
  slug: open-apex27-portal-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/apex27-crm-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/apex27-portal-api-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/apex27-mcp.yml
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
overview: 'Apex27 publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Branches API, Call Logs API, and 30 more. Tagged areas include Real-Estate, United Kingdom, PropTech, Property Listings, and CRM.


  The Apex27 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Apex27''s developer surface includes authentication, signup flow, pricing, changelog, engineering blog, support, and 21 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 38.3
    catalog_earned_first_party: 0.0
    catalog_gap: 76.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 8.3
    contract_quality: 25.4
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 8.3
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 33
      marker_coverage: 100.0
      total: 33
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apex27/refs/heads/main/screenshots/apex27-2026-08-07T161440.png
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
- Real-Estate
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
