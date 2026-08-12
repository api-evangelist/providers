---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Goodyear Tire And Rubber Agentic Access
  operation_count: 7
  slug: goodyear-tire-and-rubber-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 8
apis:
- description: The Goodyear Truck Tire Catalog API provides access to Goodyear's commercial truck tire catalog data.
  name: Goodyear Truck Tire Catalog API
  slug: catalog-api
- description: The Goodyear Work Order API enables management of service work orders for commercial truck tire services.
  name: Goodyear Work Order API
  slug: work-order-api
- description: The Goodyear Service Ticket API provides management of service tickets for commercial truck tire services.
  name: Goodyear Service Ticket API
  slug: service-ticket-api
- description: The Catalog API from Goodyear Tire & Rubber — 1 operation(s) for catalog.
  name: Goodyear Tire & Rubber Catalog API
  slug: goodyear-tire-and-rubber-catalog-api
- description: The Friction API from Goodyear Tire & Rubber — 1 operation(s) for friction.
  name: Goodyear Tire & Rubber Friction API
  slug: goodyear-tire-and-rubber-friction-api
- description: The Service Tickets API from Goodyear Tire & Rubber — 1 operation(s) for service tickets.
  name: Goodyear Tire & Rubber Service Tickets API
  slug: goodyear-tire-and-rubber-service-tickets-api
- description: The Tires API from Goodyear Tire & Rubber — 1 operation(s) for tires.
  name: Goodyear Tire & Rubber Tires API
  slug: goodyear-tire-and-rubber-tires-api
- description: The Work Orders API from Goodyear Tire & Rubber — 1 operation(s) for work orders.
  name: Goodyear Tire & Rubber Work Orders API
  slug: goodyear-tire-and-rubber-work-orders-api
artifact_total: 16
collections:
- collection_type: open
  name: Goodyear API Management Portal (GaaS)
  slug: open-gaas-portal
- collection_type: open
  name: Goodyear SightLine API
  slug: open-sightline-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/goodyear-tire-and-rubber-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goodyear-tire-and-rubber-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goodyear
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/goodyear
- group: company
  title: ''
  type: Website
  url: https://www.goodyear.com
- group: start
  title: ''
  type: Portal
  url: https://developer.goodyearsightline.com/
- group: start
  title: ''
  type: Portal
  url: https://gaas-portal.goodyear.com/
- group: company
  title: ''
  type: Blog
  url: https://news.goodyear.com/news?pagetemplate=rss
created: '2026-03-21'
description: The Goodyear Tire & Rubber Company is a global tire manufacturer that provides developer APIs for intelligent tire data, fleet management, and commercial truck tire services. Goodyear's SightLine technology and GaaS API platform enable programmatic access to tire telematics, catalogs, work orders, and service tickets.
finops:
- name: Goodyear Tire And Rubber Finops
  service_category: Connected Vehicles / Tire Telematics
  slug: goodyear-tire-and-rubber-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goodyear-tire-and-rubber.png
json_structures:
- name: Goodyear Tire And Rubber Structure
  property_count: 0
  slug: goodyear-tire-and-rubber-structure
layout: provider
modified: '2026-05-19'
name: Goodyear Tire & Rubber
nav: Providers
network: true
overview: 'Goodyear Tire & Rubber publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Friction API, Service Tickets API, and 2 more. Tagged areas include Connected Vehicles, Fleet Management, IoT, Telematics, and Tires.


  Goodyear Tire & Rubber''s developer surface includes developer portal, engineering blog, and 6 more developer resources.'
plans:
- name: Goodyear Tire And Rubber Plans Pricing
  plan_count: 1
  slug: goodyear-tire-and-rubber-plans-pricing
press:
- date: '2026-05-25'
  title: Goodyear And SafeAI Announce Tire Intelligence For ...
  url: https://news.goodyear.com/goodyear_and_safeai_
- date: '2026-05-25'
  title: PlusAI and Goodyear Collaborate to Enhance the Safety ...
  url: https://www.prnewswire.com/news-releases/plusai-and-goodyear-collaborate-to-enhance-the-safety-and-efficiency-features-of-autonomous-trucks-302522676.html
- date: '2026-05-25'
  title: Goodyear And Plus Collaborate On Autonomous Trucks
  url: https://news.goodyear.com/goodyear-and-plus-collaborate-on-autonomous-trucks
- date: '2026-05-25'
  title: PlusAI and Goodyear Collaborate to Enhance the Safety and ...
  url: https://plus.ai/news-and-insights/plusai-and-goodyear-collaborate-to-enhance-the-safety-and-efficiency-features-of-autonomous-trucks
- date: '2026-05-25'
  title: Goodyear
  url: https://www.ces.tech/success-stories/goodyear/
random_paper: 58
rate_limits:
- limit_count: 1
  name: Goodyear Tire And Rubber Rate Limits
  slug: goodyear-tire-and-rubber-rate-limits
score:
  band: thin
  composite: 28.0
  delta: -5.7
  facets:
    commercial_clarity: 13.2
    contract_quality: 57.5
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/goodyear-tire-and-rubber/refs/heads/main/screenshots/goodyear-tire-and-rubber-2026-06-20T181956.png
security:
- kind: domain-security
  name: Goodyear Tire And Rubber Domain Security
  slug: goodyear-tire-and-rubber-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goodyear-tire-and-rubber
tags:
- Connected Vehicles
- Fleet Management
- IoT
- Telematics
- Tires
website: https://www.goodyear.com
---
