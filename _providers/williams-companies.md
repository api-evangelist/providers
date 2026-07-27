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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/williams-companies-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.williams.com/feed/
- group: company
  title: ''
  type: Website
  url: https://www.williams.com
- group: start
  title: ''
  type: Portal
  url: https://www.williams.com/customers/
created: '2026-03-24'
description: The Williams Companies is an American Fortune 500 energy company focused on natural gas infrastructure, processing, and transportation. Williams owns and operates midstream energy assets including the Transco pipeline (the largest natural gas pipeline in the United States), gathering and processing systems, and storage facilities. Williams serves natural gas producers, local distribution companies, and large-volume end users. The company provides customer portal access for operational data and FERC-regulated electronic bulletin boards for capacity transactions, but does not offer public developer REST APIs.
features:
- description: The Transco pipeline is the largest natural gas pipeline system in the US, running from the Gulf Coast to New York City.
  name: Transco Pipeline
- description: Williams gathers and processes natural gas from producing basins in the Appalachian, Gulf Coast, and Rockies regions.
  name: Gathering and Processing
- description: Williams operates natural gas storage facilities providing seasonal and peak supply balancing for customers.
  name: Storage Facilities
- description: Customer portal providing access to operational data, nominations, and account management for gas shippers.
  name: Customer Data Portal
- description: FERC-mandated electronic bulletin boards for capacity release, scheduling, and tariff information on interstate pipelines.
  name: FERC Electronic Bulletin Board
- description: Open Access Technology International (OATI) platform integration for natural gas transportation nominations and scheduling.
  name: OATI Integration
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/williams-companies.png
integrations:
- description: Williams participates in OATI's webEBB electronic bulletin board platform for interstate pipeline capacity transactions.
  name: OATI webEBB
- description: Williams uses Infopost for FERC-mandated posting of operational data, tariff information, and capacity availability.
  name: Infopost
- description: Industry-standard EDI/electronic nominations system for natural gas transportation scheduling with Williams pipelines.
  name: NEXTT
layout: provider
modified: '2026-05-03'
name: Williams Companies
nav: Providers
network: true
overview: 'Williams Companies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Natural Gas, Energy Infrastructure, Midstream, Pipeline, and Fortune 500.


  Williams Companies'' developer surface includes engineering blog, developer portal, and 2 more developer resources.'
random_paper: 34
score:
  band: minimal
  composite: 8.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/williams-companies/refs/heads/main/screenshots/williams-companies-2026-06-20T201507.png
security:
- kind: domain-security
  name: Williams Companies Domain Security
  slug: williams-companies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: williams-companies
tags:
- Natural Gas
- Energy Infrastructure
- Midstream
- Pipeline
- Fortune 500
use_cases:
- description: End-to-end transportation of natural gas from producing regions to local distribution companies and end users.
  name: Natural Gas Transportation
- description: Shippers access Williams' FERC electronic bulletin boards to reserve, release, and manage interstate pipeline capacity.
  name: Capacity Management
- description: Natural gas liquids extraction and conditioning services for producers in Williams' gathering and processing footprint.
  name: Gas Processing
- description: Utilities use Williams' pipeline and storage assets to balance seasonal demand and ensure supply reliability.
  name: Supply Reliability
website: https://www.williams.com
---
