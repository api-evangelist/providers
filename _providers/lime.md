---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lime Agentic Access
  operation_count: 6
  slug: lime-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL_template: https://data.lime.bike/api/partners/v2/gbfs/{city}
  baseurl_source: spec_template
  description: The Free Bike Status API from Lime — 1 operation(s) for free bike status.
  name: Lime Free Bike Status API
  slug: lime-free-bike-status-api
- baseURL_template: https://data.lime.bike/api/partners/v2/gbfs/{city}
  baseurl_source: spec_template
  description: The Gbfs.json API from Lime — 1 operation(s) for gbfs.json.
  name: Lime Gbfs.json API
  slug: lime-gbfs-json-api
- baseURL_template: https://data.lime.bike/api/partners/v2/gbfs/{city}
  baseurl_source: spec_template
  description: The Station Information API from Lime — 1 operation(s) for station information.
  name: Lime Station Information API
  slug: lime-station-information-api
- baseURL_template: https://data.lime.bike/api/partners/v2/gbfs/{city}
  baseurl_source: spec_template
  description: The Station Status API from Lime — 1 operation(s) for station status.
  name: Lime Station Status API
  slug: lime-station-status-api
- baseURL_template: https://data.lime.bike/api/partners/v2/gbfs/{city}
  baseurl_source: spec_template
  description: The System Information API from Lime — 1 operation(s) for system information.
  name: Lime System Information API
  slug: lime-system-information-api
- baseURL_template: https://data.lime.bike/api/partners/v2/gbfs/{city}
  baseurl_source: spec_template
  description: The Vehicle Types API from Lime — 1 operation(s) for vehicle types.
  name: Lime Vehicle Types API
  slug: lime-vehicle-types-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lime GBFS Public Feed Free Bike Status API
  slug: open-lime-free-bike-status-api
- collection_type: open
  name: Lime GBFS Public Feed Free Bike Status Gbfs.json API
  slug: open-lime-gbfs-json-api
- collection_type: open
  name: Lime GBFS Public Feed
  slug: open-lime-gbfs
- collection_type: open
  name: Lime GBFS Public Feed Free Bike Status Station Information API
  slug: open-lime-station-information-api
- collection_type: open
  name: Lime GBFS Public Feed Free Bike Status Station Status API
  slug: open-lime-station-status-api
- collection_type: open
  name: Lime GBFS Public Feed Free Bike Status System Information API
  slug: open-lime-system-information-api
- collection_type: open
  name: Lime GBFS Public Feed Free Bike Status Vehicle Types API
  slug: open-lime-vehicle-types-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lime-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lime-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lime-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lime-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.li.me
- group: company
  title: ''
  type: About
  url: https://www.li.me/about
- group: company
  title: ''
  type: Newsroom
  url: https://www.li.me/newsroom
- group: company
  title: ''
  type: Careers
  url: https://www.li.me/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.li.me/contact-us
- group: operate
  title: ''
  type: Support
  url: https://help.li.me
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.li.me/legal/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.li.me/legal/privacy-policy
- group: commercial
  title: ''
  type: GBFSTerms
  url: https://www.li.me/legal/public-gbfs-terms
- group: other
  title: ''
  type: Sustainability
  url: https://www.li.me/sustainability
- group: other
  title: ''
  type: Safety
  url: https://www.li.me/safety
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/limebike
- group: other
  title: ''
  type: DataSharing
  url: https://github.com/limebike/data-sharing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/limebike
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/limebike
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/li.me
created: '2026-05-25'
description: Lime is a San Francisco–based shared electric vehicle company that operates e-scooters and e-bikes across more than 280 cities in 30+ countries. Riders unlock and pay for vehicles through the Lime mobile app; cities and transit agencies receive operational data via standardized public feeds. Lime publishes per-city public GBFS (General Bikeshare Feed Specification) 2.2 feeds covering system information, station information, station status, free (dockless) bike status, and vehicle types under the Lime Public GBFS Terms. Lime also publishes MDS Extensions on GitHub — an open-source aggregation layer that sits on top of the MDS Provider standard for sharing k-anonymized operational data with regulators. There is no public, commercially licensable rider/booking API; the rider-facing endpoints at web-production.lime.bike are private to the Lime app. Integrations with trip-planning surfaces (Google Maps, Uber, Moovit, Citymapper) and city permit dashboards are delivered through the
  GBFS and MDS feeds.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lime.png
layout: provider
modified: '2026-05-25'
name: Lime
nav: Providers
network: true
overview: 'Lime publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Free Bike Status API, Gbfs.json API, Station Information API, and 3 more. Tagged areas include Shared Mobility, Micromobility, Electric Scooters, Electric Bikes, and E-Bikes.


  Lime''s developer surface includes support and 19 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 14.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lime/refs/heads/main/screenshots/lime-2026-06-20T184529.png
security:
- kind: domain-security
  name: Lime Domain Security
  slug: lime-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Lime Vulnerability Disclosure
  slug: lime-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lime
tags:
- Shared Mobility
- Micromobility
- Electric Scooters
- Electric Bikes
- E-Bikes
- E-Scooters
- Transportation
- Urban Mobility
- GBFS
- MDS
- Smart Cities
- Transit
website: https://www.li.me
---
