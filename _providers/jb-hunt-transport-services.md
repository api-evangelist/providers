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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Jb Hunt Transport Services Agentic Access
  operation_count: 8
  slug: jb-hunt-transport-services-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 5
apis:
- description: Upload and retrieve shipment documents.
  name: J.B. Hunt Transport Services Documents API
  slug: jb-hunt-transport-services-documents-api
- description: Create, search, and manage transportation orders.
  name: J.B. Hunt Transport Services Orders API
  slug: jb-hunt-transport-services-orders-api
- description: Request shipping quotes and rates.
  name: J.B. Hunt Transport Services Quotes API
  slug: jb-hunt-transport-services-quotes-api
- description: Manage pickup and delivery appointments.
  name: J.B. Hunt Transport Services Scheduling API
  slug: jb-hunt-transport-services-scheduling-api
- description: Near real-time freight shipment tracking.
  name: J.B. Hunt Transport Services Tracking API
  slug: jb-hunt-transport-services-tracking-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: J.B. Hunt 360 Connect API
  slug: open-jb-hunt-360-connect-api
- collection_type: open
  name: J.B. Hunt 360 Connect Documents API
  slug: open-jb-hunt-transport-services-documents-api
- collection_type: open
  name: J.B. Hunt 360 Connect Documents Orders API
  slug: open-jb-hunt-transport-services-orders-api
- collection_type: open
  name: J.B. Hunt 360 Connect Documents Quotes API
  slug: open-jb-hunt-transport-services-quotes-api
- collection_type: open
  name: J.B. Hunt 360 Connect Documents Scheduling API
  slug: open-jb-hunt-transport-services-scheduling-api
- collection_type: open
  name: J.B. Hunt 360 Connect Documents Tracking API
  slug: open-jb-hunt-transport-services-tracking-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jb-hunt-transport-services-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jb-hunt-transport-services-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jb-hunt-transport-services-inc
- group: start
  title: ''
  type: Portal
  url: https://apiportal.jbhunt.com/docs/services
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.jbhunt.com/connect-360
- group: company
  title: ''
  type: Website
  url: https://www.jbhunt.com/
- group: other
  title: ''
  type: Connectivity
  url: https://www.jbhunt.com/technology/connectivity
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.jbhunt.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.jbhunt.com/our-company/newsroom
created: '2025-03-01'
description: J.B. Hunt Transport Services, Inc. is one of the largest transportation and logistics companies in North America, providing trucking, intermodal, and contract services. J.B. Hunt offers the J.B. Hunt 360 Connect API portal for shippers and partners to programmatically access quotes, order management, shipment tracking, document management, and scheduling for full-truckload (FTL) and less-than-truckload (LTL) operations.
finops:
- name: Jb Hunt Transport Services Finops
  service_category: Logistics / Transportation
  slug: jb-hunt-transport-services-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jb-hunt-transport-services.png
layout: provider
modified: '2026-05-19'
name: J.B. Hunt Transport Services
nav: Providers
network: true
overview: 'J.B. Hunt Transport Services publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Orders API, Quotes API, and 2 more. Tagged areas include Freight, Intermodal, Logistics, Shipping, and Supply Chain.


  J.B. Hunt Transport Services'' developer surface includes developer portal, engineering blog, and 7 more developer resources.'
plans:
- name: Jb Hunt Transport Services Plans Pricing
  plan_count: 1
  slug: jb-hunt-transport-services-plans-pricing
press:
- date: '2026-05-25'
  title: Google and JBHT Announce Strategic Alliance
  url: https://www.jbhunt.com/content/dam/jbhunt/jbh/pr/press-releases/Google%20and%20JBHT%20Announce%20Strategic%20Alliance.pdf
- date: '2026-05-25'
  title: J.B. Hunt Transport Services Inc. Case Study
  url: https://cloud.google.com/customers/jb-hunt
- date: '2026-05-25'
  title: Press Releases
  url: https://www.googlecloudpresscorner.com/press-releases?l=10&o=700
- date: '2026-05-25'
  title: Google and J.B. Hunt Announce Strategic Alliance to ...
  url: https://www.prnewswire.com/news-releases/google-and-jb-hunt-announce-strategic-alliance-to-accelerate-innovation-in-transportation-and-logistics-301230485.html
- date: '2026-05-25'
  title: J.B. Hunt Teams up with Google for Next-Generation ...
  url: https://www.truckinginfo.com/news/j-b-hunt-teams-up-with-google-for-next-generation-supply-chain-technology
random_paper: 13
rate_limits:
- limit_count: 1
  name: Jb Hunt Transport Services Rate Limits
  slug: jb-hunt-transport-services-rate-limits
score:
  band: emerging
  composite: 24.7
  delta: -3.3
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 53.8
    developer_ergonomics: 2.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jb-hunt-transport-services/refs/heads/main/screenshots/jb-hunt-transport-services-2026-06-20T183810.png
security:
- kind: domain-security
  name: Jb Hunt Transport Services Domain Security
  slug: jb-hunt-transport-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jb-hunt-transport-services
tags:
- Freight
- Intermodal
- Logistics
- Shipping
- Supply Chain
- Transportation
- Trucking
- Fortune 500
website: https://www.jbhunt.com/
---
