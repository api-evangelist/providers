---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
  scored_at: '2026-09-04'
api_count: 8
apis:
- description: 'Partner-facing developer portal hosted at developer.devops.chvac.trane.com for Trane Commercial HVAC ("CHVAC") cloud and controls APIs. The portal is gated and surfaces API design, documentation, and '
  name: Trane Developer Portal
  slug: trane-developer-portal
- description: Trane Connect is the secure, cloud-based customer portal that lets building owners and service technicians remotely monitor and manage Trane-connected building systems, automate routine maintenance, v
  name: Trane Connect
  slug: trane-connect
- description: 'Tracer SC+ is Trane''s commercial building automation system controller. It is built on open, industry-standard protocols — BACnet/IP, BACnet MS/TP, BACnet Secure Connect, Modbus (RTU and TCP/IP), and '
  name: Tracer SC+ Building Automation System
  slug: tracer-sc-plus
- description: Symbio is Trane's portfolio of digital equipment controllers (chillers, rooftop units, air handlers) providing remote monitoring, diagnostics, and connectivity. Symbio communicates over BACnet (MS/TP,
  name: Trane Symbio Digital Equipment Controllers
  slug: symbio-controllers
- description: Thermo King TracKing is the flagship telematics platform for transport refrigeration units (TRUs) — trailers, trucks, vans, and rail — exposing reefer setpoints, return / supply air temperatures, alar
  name: Thermo King TracKing Telematics
  slug: thermo-king-tracking
- description: ConnectedSuite is Thermo King's umbrella of connected products — TracKing telematics, TracKing Pro (energy usage), TracKing Smart Trailer Telematics, and the Remote Operating Center — that surface fle
  name: Thermo King ConnectedSuite
  slug: thermo-king-connectedsuite
- description: 'Residential connected-home line including ComfortLink II XL1050, ComfortLink II XL850, LINK UX360, XL824, and XR724 smart thermostats. Trane does not publish a public consumer developer API for these '
  name: Trane Residential Connected Thermostats
  slug: trane-residential-connected
- description: BrainBox AI is the autonomous HVAC-optimization AI platform operated under Trane Technologies, which opened the BrainBox AI Lab in Montreal to accelerate AI-driven building optimization. BrainBox AI e
  name: BrainBox AI (Trane Technologies)
  slug: brainbox-ai
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trane-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tranetechnologies.com/
- group: other
  title: ''
  type: CommercialSite
  url: https://www.trane.com/commercial/
- group: other
  title: ''
  type: ResidentialSite
  url: https://www.trane.com/residential/
- group: other
  title: ''
  type: BrandSite
  url: https://www.thermoking.com/na/en.html
- group: other
  title: ''
  type: BrandSite
  url: https://www.americanstandardair.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.devops.chvac.trane.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.trane.com/commercial/north-america/us/en/services/operate-maintain-repair/connectivity-and-cloud-services.html
- group: build
  title: ''
  type: SystemsIntegration
  url: https://www.trane.com/commercial/north-america/us/en/services/operate-maintain-repair/connectivity-and-cloud-services/systems-integration.html
- group: build
  title: ''
  type: ELibrary
  url: https://elibrary.tranetechnologies.com/
- group: other
  title: ''
  type: SoftwareDownloads
  url: https://www.trane.com/commercial/north-america/us/en/products-systems/building-management---automation/trane-controls-software-downloads.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Trane-Technologies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trane-technologies/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/TraneTech
- group: company
  title: ''
  type: NewsRoom
  url: https://www.tranetechnologies.com/en/index/news-and-events.html
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.tranetechnologies.com/en/index/investor-relations.html
- group: other
  title: ''
  type: Sustainability
  url: https://www.tranetechnologies.com/en/index/sustainability.html
- group: company
  title: ''
  type: Careers
  url: https://careers.tranetechnologies.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.tranetechnologies.com/en/index/contact-us.html
- group: commercial
  title: ''
  type: Plans
  url: plans/trane-technologies-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trane-technologies-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/trane-technologies-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/trane-technologies-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/trane-technologies-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tranetechnologies.com/en/index/blog.html
created: '2026-05-23'
description: 'Trane Technologies plc (NYSE: TT) is an Ireland-domiciled global climate innovator that designs, manufactures, sells, and services heating, ventilation, air conditioning (HVAC), transport refrigeration, and building-automation systems. The company operates through two reportable segments — the Americas and EMEA / Asia Pacific — under the Trane, Thermo King, and American Standard Heating & Air Conditioning brands. Spun off from Ingersoll-Rand in 2020, Trane Technologies reported approximately US$23.9B in 2025 revenue, ~45,000 employees, and operations across 61 countries. Its digital surface centers on Trane Connect (cloud building portal), Tracer SC+ / Symbio controllers for commercial building automation, and the Thermo King TracKing / ConnectedSuite telematics platform for transport refrigeration.'
finops:
- name: Trane Technologies Finops
  service_category: HVAC / IoT Platform
  slug: trane-technologies-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trane-technologies.png
jsonld:
- class_count: 0
  name: Trane Technologies Context
  property_count: 16
  slug: trane-technologies-context
layout: provider
modified: '2026-05-23'
name: Trane Technologies
nav: Providers
network: true
overview: 'Trane Technologies publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include HVAC, Cold Chain, Telematics, Building Automation, and IoT.


  The Trane Technologies catalog on APIs.io includes 1 JSON-LD context.


  Trane Technologies'' developer surface includes documentation, engineering blog, and 23 more developer resources.'
plans:
- name: Trane Technologies Plans Pricing
  plan_count: 4
  slug: trane-technologies-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Trane Technologies Rate Limits
  slug: trane-technologies-rate-limits
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 75.0
    catalog_earned_first_party: 0.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 15.2
    contract_quality: 10.7
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 15.2
    operational_transparency: 50.0
  previous_composite: 31.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trane-technologies/refs/heads/main/screenshots/trane-technologies-2026-06-20T195537.png
security:
- kind: domain-security
  name: Trane Technologies Domain Security
  slug: trane-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: trane-technologies
tags:
- HVAC
- Cold Chain
- Telematics
- Building Automation
- IoT
- Refrigeration
- Transport Refrigeration
- BACnet
- Smart Buildings
- Fortune 500
website: https://www.tranetechnologies.com/
---
