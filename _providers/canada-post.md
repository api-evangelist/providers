---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 10
apis:
- description: Returns available shipping services and their rates for a given origin postal code, destination, parcel weight, and dimensions. Supports domestic, US, and international destinations. Returns base cost
  name: Canada Post Rating Web Service
  slug: rating
- description: Enables commercial customers with a Canada Post parcel agreement to create domestic and international shipments, generate shipping labels (PDF or ZPL), retrieve shipment pricing, manage shipment group
  name: Canada Post Contract Shipping Web Service
  slug: contract-shipping
- description: 'Allows general businesses and VentureOne card holders to create domestic and international shipments and generate labels without a formal Canada Post parcel agreement. Charges are applied to a credit '
  name: Canada Post Non-Contract Shipping Web Service
  slug: non-contract-shipping
- description: Provides parcel tracking capabilities using a PIN (Parcel Identification Number), DNC (Delivery Notice Card), or customer reference number. Returns tracking summary (most recent event) or full trackin
  name: Canada Post Tracking Web Service
  slug: tracking
- description: Address validation and auto-complete web service backed by Canada Post's authoritative Canadian address database. Implements a two-step Find/Retrieve flow — Find returns up to 8 candidate matches on e
  name: Canada Post AddressComplete API
  slug: address-complete
- description: 'Enables e-commerce platforms to schedule, modify, retrieve, and cancel on-demand parcel pickups. Supports checking pickup availability and cut-off times by postal code. Pickups can be booked up to 30 '
  name: Canada Post Pickup Web Service
  slug: pickup
- description: Generates return shipping labels for authorized returns (pre-approved by merchant) and open returns (customer-initiated). Supports both REST and SOAP protocols. Return labels are retrievable for up to
  name: Canada Post Returns Web Service
  slug: returns
- description: Returns a list of Canada Post retail post office locations near a given postal code or address, including hours of operation and available services. Useful for presenting drop-off locations to custome
  name: Canada Post Find a Post Office API
  slug: find-post-office
- description: Allows customers to select a post office as the delivery destination instead of a residential or commercial address at checkout. Integrates with the Find a Post Office service to present eligible pick
  name: Canada Post Deliver to Post Office API
  slug: deliver-to-post-office
- description: Provides information about scheduled outages and service disruptions to Canada Post web services, enabling applications to surface maintenance windows to developers and end users.
  name: Canada Post Service Information API
  slug: service-info
artifact_total: 22
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canada-post-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.canadapost-postescanada.ca/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.canadapost-postescanada.ca/information/app/drc/home?execution=e1s1
- group: docs
  title: ''
  type: Documentation
  url: https://www.canadapost-postescanada.ca/info/mc/business/productsservices/developers/services/fundamentals.jsf
- group: start
  title: ''
  type: GettingStarted
  url: https://www.canadapost-postescanada.ca/info/mc/business/productsservices/developers/services/gettingstarted.jsf
- group: other
  title: ''
  type: Catalog
  url: https://www.canadapost-postescanada.ca/info/mc/business/productsservices/developers/services/default.jsf
- group: start
  title: ''
  type: Signup
  url: https://sso-osu.canadapost-postescanada.ca/pfe-pap/en/registration
- group: start
  title: ''
  type: Login
  url: https://sso-osu.canadapost-postescanada.ca/lfe-cap/en/login
- group: start
  title: ''
  type: Sandbox
  url: https://ct.soa-gw.canadapost.ca
- group: operate
  title: ''
  type: Forums
  url: https://www.canadapost-postescanada.ca/info/mc/business/productsservices/developers/services/default.jsf
- group: other
  title: ''
  type: IntegratePage
  url: https://www.canadapost-postescanada.ca/cpc/en/commercial/integrate-apis.page
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canada-post
created: '2026-06-13'
description: Canada Post is the primary postal operator in Canada, offering a developer platform with REST and SOAP web services for e-commerce merchants and solution providers. APIs cover shipping label generation, rate calculation, parcel tracking, address validation (AddressComplete), parcel pickup scheduling, returns management, post office location lookup, and service information.
features:
- Free developer program registration; API keys issued per environment (sandbox and production)
- REST and SOAP protocols supported across all services; XML request/response bodies
- Sandbox base URL https://ct.soa-gw.canadapost.ca; production base URL https://soa-gw.canadapost.ca
- Basic HTTP authentication (Base64-encoded API key) on all calls
- Rating and post office location calls are free; shipping label creation incurs standard Canada Post postage charges
- AddressComplete priced separately on a credit-based model (see plans)
- API throttle limits exist but are not publicly specified; contact Canada Post for quota details
- Code samples provided in Java, PHP, and C# for REST and SOAP
finops:
- name: Canada Post Finops
  service_category: Logistics / Shipping
  slug: canada-post-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canada-post.png
layout: provider
modified: '2026-06-13'
name: Canada Post
nav: Providers
network: true
overview: 'Canada Post publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Address Validation, E-Commerce, Labels, Logistics, and Pickup.


  Canada Post''s developer surface includes documentation, getting-started guide, signup flow, sandbox, and 8 more developer resources.'
plans:
- name: Canada Post Plans Pricing
  plan_count: 13
  slug: canada-post-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 8
  name: Canada Post Rate Limits
  slug: canada-post-rate-limits
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 56.6
    commercial_clarity: 56.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canada-post/refs/heads/main/screenshots/canada-post-2026-06-20T173916.png
security:
- kind: domain-security
  name: Canada Post Domain Security
  slug: canada-post-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: canada-post
tags:
- Address Validation
- E-Commerce
- Labels
- Logistics
- Pickup
- Postal
- Rating
- Returns
- Shipping
- Tracking
website: https://www.canadapost-postescanada.ca/
---
