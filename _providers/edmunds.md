---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Edmunds Agentic Access
  operation_count: 5
  slug: edmunds-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: The Edmunds Dealership API is a tool that provides real-time access to data on cars for sale at dealerships across the country. By connecting to the API, users can search for specific makes and models
  name: Edmunds Dealership API
  slug: edmunds
- description: 'Edmunds API is a robust software interface that provides access to a vast database of automotive information and data. With this API, users can access details on car specifications, pricing, reviews, '
  name: Edmunds API
  slug: edmunds
- description: The Vehicle API from Edmunds — 5 operation(s) for vehicle.
  name: Edmunds Vehicle API
  slug: edmunds-vehicle-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Edmunds Vehicle API
  slug: open-edmunds-vehicle-api
- collection_type: open
  name: Edmunds Vehicle API
  slug: open-edmunds
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/edmunds-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edmunds-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/edmunds-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edmunds
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/edmunds-com
- group: start
  title: ''
  type: Portal
  url: https://developer.edmunds.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.edmunds.com/terms_of_service.html
- group: other
  title: ''
  type: Branding
  url: https://developer.edmunds.com/api_branding_guide.html
- group: operate
  title: ''
  type: FAQ
  url: https://developer.edmunds.com/faq.html
- group: operate
  title: ''
  type: Contact
  url: https://developer.edmunds.com/contact_us.html
- group: build
  title: ''
  type: SDKs
  url: https://developer.edmunds.com/api-documentation/overview/#sec-9
created: '2024-07-11T00:00:00.000Z'
description: Edmunds is a popular automotive resource website that provides consumers with valuable information and tools to help them make informed decisions about buying and selling cars. They offer expert reviews, comparison tools, price guides, and a variety of resources to help users research and find the perfect vehicle for their needs.
finops:
- name: Edmunds Finops
  service_category: API
  slug: edmunds-finops
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/edmunds-developer-network-welcome-to-the-edmunds-api-edmunds-developer-portal.png
layout: provider
modified: '2026-04-28'
name: Edmunds
nav: Providers
network: true
overview: 'Edmunds publishes 1 API on the [APIs.io](https://apis.io/) network: Vehicle API. Tagged areas include Automobiles, Cars, and Vehicles.


  Edmunds'' developer surface includes authentication, developer portal, FAQ, and 8 more developer resources.'
plans:
- name: Edmunds Plans Pricing
  plan_count: 3
  slug: edmunds-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Edmunds Rate Limits
  slug: edmunds-rate-limits
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 38.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/edmunds/refs/heads/main/screenshots/edmunds-2026-06-20T180456.png
security:
- kind: authentication
  name: Edmunds Authentication
  slug: edmunds-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Edmunds Domain Security
  slug: edmunds-domain-security
  summary_line: TLSv1.3
slug: edmunds
tags:
- Automobiles
- Cars
- Vehicles
website: https://developer.edmunds.com/
---
