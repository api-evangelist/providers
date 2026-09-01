---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
api_count: 5
apis:
- description: RESTful API that returns neutralized container and shipment milestones across Maersk's ocean network, enabling supply-chain visibility for shippers, BCOs, and downstream visibility platforms.
  name: Track and Trace API
  slug: tracking-and-trace
- description: Sailing schedules between origin and destination locations, including vessel, voyage, transshipment, and lead-time data; used for routing, booking, and supply-chain planning.
  name: Point-to-Point Schedules API
  slug: point-to-point-schedules
- description: Authoritative directory of Maersk service locations (ports, terminals, depots, inland points) with UN/LOCODE, geo-coordinates, and operational capabilities for use in upstream booking, routing, and sc
  name: Locations API
  slug: locations
- description: API for the Captain Peter remote-monitoring service for refrigerated containers; surfaces temperature, humidity, atmosphere, power, and alarm telemetry for perishables in transit.
  name: Captain Peter API
  slug: captain-peter
- description: Suite of pre-booking, booking, and post-booking APIs covering rate requests, booking creation, amendments, documentation, and shipment lifecycle management.
  name: Booking APIs
  slug: booking-apis
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/maersk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maersk-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MaerskTech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/maersk-group
- group: company
  title: ''
  type: Website
  url: https://www.maersk.com/
- group: company
  title: ''
  type: AboutUs
  url: https://www.maersk.com/about
- group: other
  title: ''
  type: Logistics
  url: https://www.maersk.com/logistics-explained
- group: other
  title: ''
  type: APMTerminals
  url: https://www.apmterminals.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.maersk.com/
- group: company
  title: ''
  type: News
  url: https://www.maersk.com/news
- group: other
  title: ''
  type: Sustainability
  url: https://www.maersk.com/sustainability
- group: company
  title: ''
  type: Careers
  url: https://www.maersk.com/careers
- group: start
  title: ''
  type: Portal
  url: https://developer.maersk.com/
- group: company
  title: ''
  type: Blog
  url: https://www.maersk.com/news
created: '2026-05-05'
description: A. P. Moller-Maersk is a Danish integrated logistics and container shipping company and one of the world's largest container shipping lines. Maersk operates ocean transport (Maersk Line), port and terminal operations (APM Terminals), supply-chain management, air cargo (Maersk Air Cargo), inland services, and customs solutions, connecting ports across more than 130 countries with end-to-end supply chain offerings. Maersk operates a public developer portal at developer.maersk.com that hosts APIs for shipping customers and partners covering tracking, schedules, rates, bookings, and related logistics workflows.
finops:
- name: Maersk Finops
  service_category: API
  slug: maersk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maersk.png
layout: provider
modified: '2026-05-23'
name: Maersk
nav: Providers
network: true
overview: 'Maersk publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Container Shipping, Freight, Logistics, Maritime, and Ports and Terminals.


  Maersk''s developer surface includes product news, developer portal, engineering blog, and 11 more developer resources.'
plans:
- name: Maersk Plans Pricing
  plan_count: 1
  slug: maersk-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Maersk Rate Limits
  slug: maersk-rate-limits
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 17.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maersk/refs/heads/main/screenshots/maersk-2026-06-20T184831.png
security:
- kind: domain-security
  name: Maersk Domain Security
  slug: maersk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Maersk Vulnerability Disclosure
  slug: maersk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: maersk
tags:
- Container Shipping
- Freight
- Logistics
- Maritime
- Ports and Terminals
- Shipping
- Supply Chain
website: https://www.maersk.com/
---
