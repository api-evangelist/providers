---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The Breeze Airways NDC gateway is the airline's direct-connect distribution API for accredited travel partners. It speaks IATA Offers and Orders (NDC) 21.3 XML over HTTPS on a Navitaire-hosted gateway
  name: Breeze Airways NDC Gateway
  slug: breeze-airways-ndc-gateway
artifact_total: 4
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/breeze-airways-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.flybreeze.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ndc.flybreeze.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ndc.flybreeze.com/docs/category/ndc-for-developers
- group: docs
  title: ''
  type: APIReference
  url: https://ndc.flybreeze.com/docs/category/ndc-shopping
- group: start
  title: ''
  type: GettingStarted
  url: https://ndc.flybreeze.com/docs/ndc-for-developers/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://ndc.flybreeze.com/docs/become-a-breeze-partner
- group: operate
  title: ''
  type: Support
  url: https://www.flybreeze.com/support
- group: company
  title: ''
  type: Blog
  url: https://ndc.flybreeze.com/news
- group: operate
  title: ''
  type: StatusPage
  url: https://ndc.flybreeze.com/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://ndc.flybreeze.com/news
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/breeze-airways-changelog.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flybreeze.com/page/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://media.flybreeze.com/docs/policies/privacypolicy.pdf
- group: company
  title: ''
  type: Careers
  url: https://jobs.flybreeze.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/breeze-airways-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/breeze-airways-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/breeze-airways-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/breeze-airways-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/breeze-airways-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/breeze-airways-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/breeze-airways-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/breeze-airways-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/breeze-airways-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/breeze-airways-domain-security.yml
created: '2026-08-01'
description: Breeze Airways (Breeze Aviation Group, Inc.) is an American low-cost point-to-point airline headquartered in Cottonwood Heights, Utah, founded by David Neeleman and flying since May 2021. Its distribution technology surface is a partner-facing IATA NDC gateway, documented at the Breeze B2B portal (ndc.flybreeze.com), which exposes IATA Offers and Orders 21.3 XML messages — AirlineProfile, AirShopping, OfferPrice, ServiceList, SeatAvailability and OrderCreate for shopping and selling, plus OrderRetrieve, OrderQuote, OrderReshop and OrderChange for servicing — over a Navitaire-hosted, IP-allowlisted gateway secured with a per-partner Azure API Management subscription key and a 30-minute session bearer token. Access is limited to accredited travel-agency partners (OTA, TMC and US federal government) with an IATA/ARC number and an executed commercial agreement; Breeze also distributes over Amadeus and Travelport GDS and via the TravelPro agent booking portal.
image: https://ndc.flybreeze.com/img/breeze-b2b-social-card.jpg
layout: provider
modified: '2026-08-01'
name: Breeze Airways
nav: Providers
network: true
overview: 'Breeze Airways publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Airlines, Travel, Aviation, and NDC.


  Breeze Airways'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, changelog, and 19 more developer resources.'
random_paper: 1
scopes:
- name: Breeze Airways Scopes
  scope_count: 0
  slug: breeze-airways-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 19.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/breeze-airways/refs/heads/main/screenshots/breeze-airways-2026-08-07T162755.png
security:
- kind: authentication
  name: Breeze Airways Authentication
  slug: breeze-airways-authentication
  summary_line: apiKey/http-basic/http-bearer/oauth2 · 4 schemes
- kind: domain-security
  name: Breeze Airways Domain Security
  slug: breeze-airways-domain-security
  summary_line: TLSv1.3 · DMARC
slug: breeze-airways
tags:
- Company
- Airlines
- Travel
- Aviation
- NDC
- Distribution
- Booking
- Reservations
- Travel Agencies
- IATA
website: https://www.flybreeze.com/
---
