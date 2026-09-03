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
  band: human-only
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
    error_semantics: false
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
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: VIA Rail's complete national timetable published as a static General Transit Feed Specification (GTFS) archive, offered for download from the VIA Rail Developer Resources page with no registration, no
  name: VIA Rail GTFS Schedule Feed
  slug: via-rail-gtfs-schedule-feed
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/via-rail-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/via-rail-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/via-rail-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/via-rail-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/via-rail-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/via-rail-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.viarail.ca/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.viarail.ca/en/developer-resources
- group: docs
  title: ''
  type: Documentation
  url: https://www.viarail.ca/en/developer-resources
- group: operate
  title: ''
  type: Support
  url: https://www.viarail.ca/en/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VIARailCanada
- group: docs
  title: ''
  type: DocumentationFrench
  url: https://www.viarail.ca/fr/ressources-developpeurs
- group: other
  title: ''
  type: Corporate
  url: https://corpo.viarail.ca/en
- group: company
  title: ''
  type: Newsroom
  url: https://media.viarail.ca/en
- group: start
  title: ''
  type: TravelAgentPortal
  url: https://reservia.viarail.ca/en/booking/agent/login
- group: start
  title: ''
  type: PartnerPortal
  url: https://reservia.viarail.ca/en/booking/contra/login
- group: other
  title: ''
  type: TravelAgentRegistration
  url: https://www.viarail.ca/en/travel-agents/travel-agent-registration
- group: other
  title: ''
  type: TourOperatorRegistration
  url: https://www.viarail.ca/en/travel-agents/tour-operator-registration
- group: operate
  title: ''
  type: FAQ
  url: https://www.viarail.ca/en/travel-agents/travel-agent-faq
- group: operate
  title: ''
  type: FAQ
  url: https://www.viarail.ca/en/travel-agents/tour-operator-faq
- group: other
  title: ''
  type: Policy
  url: https://www.viarail.ca/en/travel-agents/ad75-conditions
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.viarail.ca/en/terms-and-conditions
- group: other
  title: ''
  type: Policy
  url: https://www.viarail.ca/en/conditions-contract
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.viarail.ca/en/our-privacy-policy
- group: commercial
  title: ''
  type: License
  url: https://open.canada.ca/en/open-government-licence-canada
- group: other
  title: ''
  type: Governance
  url: https://corpo.viarail.ca/en/company/governance-ethics
- group: other
  title: ''
  type: AccessToInformation
  url: https://www.viarail.ca/sites/all/files/media/pdfs/access-to-information/en_entr_access_info_form.pdf
- group: other
  title: ''
  type: Loyalty
  url: https://www.viapreference.com/en/home
- group: other
  title: ''
  type: Booking
  url: https://reservia.viarail.ca/
- group: operate
  title: ''
  type: Status
  url: https://tsimobile.viarail.ca/
- group: company
  title: ''
  type: Blog
  url: https://www.viarail.ca/en/blog
- group: company
  title: ''
  type: Careers
  url: https://careers.viarail.ca/?locale=en_US
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/via-rail-canada
created: '2026-07-28'
description: 'VIA Rail Canada Inc. is the federal Crown corporation that operates Canada''s national intercity passenger rail network, headquartered in Montreal and reporting to Parliament through the Minister of Transport. It runs the Quebec City - Windsor corridor plus long-distance and regional services including The Canadian (Toronto - Vancouver), The Ocean (Montreal - Halifax), Winnipeg - Churchill, Jasper - Prince Rupert, Sudbury - White River, and the jointly operated Toronto - New York Maple Leaf. In the distribution chain VIA Rail is a direct-only supplier: it sells through viarail.ca, its mobile app, its call centre, and its own Travel Agency and Tour Operator portals on reservia.viarail.ca. There is no GDS channel, no NDC, no OSDM, and no reseller API. VIA Rail''s API posture is honestly stated as an open-standard data feed and nothing else. It publishes a real, ungated Developer Resources page offering a static GTFS schedule feed licensed under the Open Government Licence - Canada
  2.0, with a dev@viarail.ca contact address - one of the very few genuinely self-serve, commercially reusable machine-readable contracts in Canadian travel. Everything transactional is unpublished: the reservation platform is Sqills S3 Passenger integrated by CGI, its API gateway at api.reservia.viarail.ca answers 403 "Missing Authentication Token" with no documentation, no terms and no published contract, and agency access is gated behind approval plus a registered IATA number, while tour operators must commit to a CAD $25,000 per year minimum revenue and may not sell VIA tickets outside packaged travel.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: VIA Rail GTFS Schedule Feed
  property_count: 12
  slug: via-rail-gtfs
layout: provider
modified: '2026-07-28'
name: VIA Rail Canada
nav: Providers
network: true
overview: 'VIA Rail Canada publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Canada, Rail, Passenger Rail, and Transit.


  VIA Rail Canada''s developer surface includes authentication, documentation, support, FAQ, status page, engineering blog, and 27 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 8.0
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 25.3
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/via-rail/refs/heads/main/screenshots/via-rail-2026-09-02T165836.png
security:
- kind: authentication
  name: Via Rail Authentication
  slug: via-rail-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Via Rail Domain Security
  slug: via-rail-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: via-rail
tags:
- Travel
- Canada
- Rail
- Passenger Rail
- Transit
- GTFS
- Open Data
- Booking
- Distribution
- Travel Agents
- Crown Corporation
- Loyalty
website: https://www.viarail.ca/en
---
