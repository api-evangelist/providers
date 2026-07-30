---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Iceye Agentic Access
  operation_count: 14
  slug: iceye-agentic-access
  summary_line: 14 operations · 5 acting
api_count: 7
apis:
- description: Search, list, purchase, and retrieve products from ICEYE's archive of 60,000+ SAR scenes. Endpoints cover catalog item search, listing, purchase, and retrieval of purchased items for download.
  name: ICEYE Catalog API
  slug: catalog
- description: Direct tasking interface to the ICEYE SAR constellation. Create tasks up to 14 days in advance with no feasibility study, retrieve task status, list tasks, cancel tasks, fetch task scenes, and price t
  name: ICEYE Tasking API
  slug: tasking
- description: Account and company context API providing identity, entitlement, and organizational metadata that frames Catalog and Tasking calls.
  name: ICEYE Company API
  slug: company
- description: Web platform at platform.iceye.com for browsing catalog imagery, submitting tasking orders, monitoring task status, and downloading delivered SAR products through the same backend as the API Platform.
  name: ICEYE Platform
  slug: platform
- description: The Catalog API from ICEYE — 5 operation(s) for catalog.
  name: ICEYE Catalog API
  slug: iceye-catalog-api
- description: The Company API from ICEYE — 3 operation(s) for company.
  name: ICEYE Company API
  slug: iceye-company-api
- description: The Tasking API from ICEYE — 5 operation(s) for tasking.
  name: ICEYE Tasking API
  slug: iceye-tasking-api
artifact_total: 15
collections:
- collection_type: open
  name: ICEYE Constellation API
  slug: open-iceye
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/iceye-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/iceye-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iceye-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/iceye-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.iceye.com/
- group: other
  title: ''
  type: SARData
  url: https://www.iceye.com/sar-data
- group: other
  title: ''
  type: SARDataAPI
  url: https://www.iceye.com/sar-data/api
- group: other
  title: ''
  type: Tasking
  url: https://www.iceye.com/sar-data/tasking
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iceye.com/
- group: docs
  title: ''
  type: APIDocumentation
  url: https://docs.iceye.com/constellation/api/1.0/
- group: other
  title: ''
  type: Platform
  url: https://platform.iceye.com/
- group: other
  title: ''
  type: ProductDocuments
  url: https://www.iceye.com/resources/product-documents
- group: other
  title: ''
  type: FloodInsights
  url: https://www.iceye.com/solutions/natural-catastrophe-insights/flood-insights
- group: other
  title: ''
  type: WildfireInsights
  url: https://www.iceye.com/solutions/natural-catastrophe-insights/wildfire-insights
- group: other
  title: ''
  type: HurricaneInsights
  url: https://www.iceye.com/solutions/natural-catastrophe-insights/hurricane-insights
- group: other
  title: ''
  type: MissionSystems
  url: https://www.iceye.com/government-and-defense/mission-systems
- group: company
  title: ''
  type: Newsroom
  url: https://www.iceye.com/newsroom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iceye-ltd/
- group: other
  title: ''
  type: X
  url: https://x.com/ICEYEfi
- group: company
  title: ''
  type: Blog
  url: https://www.iceye.com/blog/rss.xml
created: '2026-05-23'
description: ICEYE operates the world's largest constellation of small Synthetic Aperture Radar (SAR) satellites, delivering all-weather day-and-night imagery down to 25 cm resolution across multiple modes. The ICEYE API Platform at api.iceye.com exposes a Catalog API over an archive of 60,000+ SAR scenes and a Tasking API that lets customers schedule the constellation up to 14 days in advance without a feasibility study or human-in-the-loop. A companion Company API exposes account context. Beyond raw imagery, ICEYE publishes natural catastrophe products - Flood Insights, Wildfire Insights, and Hurricane Insights - used by insurance, government, banking, and utilities customers, and ships Gen 4 ISR, ISR Cell, Connect, and Federate sovereign mission systems for defense and intelligence.
finops:
- name: Iceye Finops
  service_category: API
  slug: iceye-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iceye.png
layout: provider
modified: '2026-05-23'
name: ICEYE
nav: Providers
network: true
overview: 'ICEYE publishes 3 APIs on the [APIs.io](https://apis.io/) network: Catalog API, Company API, and Tasking API. Tagged areas include SAR, Satellite Imagery, Earth Observation, Tasking, and Catalog.


  ICEYE''s developer surface includes authentication, documentation, engineering blog, and 17 more developer resources.'
plans:
- name: Iceye Plans Pricing
  plan_count: 1
  slug: iceye-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 2
  name: Iceye Rate Limits
  slug: iceye-rate-limits
score:
  band: thin
  composite: 34.9
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 53.4
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iceye/refs/heads/main/screenshots/iceye-2026-06-20T183148.png
security:
- kind: authentication
  name: Iceye Authentication
  slug: iceye-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Iceye Domain Security
  slug: iceye-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Iceye Vulnerability Disclosure
  slug: iceye-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: iceye
tags:
- SAR
- Satellite Imagery
- Earth Observation
- Tasking
- Catalog
- Flood Monitoring
- Disaster Response
- Defense
- ISR
- Geospatial
- All-Weather
website: https://www.iceye.com/
---
