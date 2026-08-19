---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The only public, unauthenticated, machine-readable API surface AiDASH exposes. It is the standard Atlassian Statuspage Status API v2 served from the AiDASH status page, returning JSON for overall stat
  name: AiDASH Status API
  slug: status
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/aidash-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aidash-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aidash-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aidash-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://aidash.statuspage.io/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aidash-llms.txt
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/aidash-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.aidash.com/
- group: company
  title: ''
  type: About
  url: https://www.aidash.com/about/
- group: other
  title: ''
  type: Platform
  url: https://www.aidash.com/platform/
- group: start
  title: ''
  type: SignUp
  url: https://www.aidash.com/get-a-demo-all/
- group: operate
  title: ''
  type: Support
  url: https://www.aidash.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.aidash.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.aidash.com/feed/
- group: company
  title: ''
  type: News
  url: https://www.aidash.com/news/
- group: other
  title: ''
  type: Resources
  url: https://www.aidash.com/resources/
- group: other
  title: ''
  type: Customers
  url: https://www.aidash.com/customers/
- group: company
  title: ''
  type: Careers
  url: https://www.aidash.com/careers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aidash
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aidash.com/policy/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aidash.com/policy/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.aidash.com/security-compliance-and-responsible-ai/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aidash
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/aidashinc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCdU1Xuncxsn0YXY-YigOoJg
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/aidash
- group: other
  title: ''
  type: StockMarket
  url: https://forgeglobal.com/aidash_stock/
created: '2026-08-02'
description: AiDASH is an AI-first vertical SaaS company that uses satellite imagery and machine learning to run operations, maintenance, and climate-resilience programs for industries with geographically distributed assets — primarily electric and gas utilities, water companies, and landowners. Founded in 2019 by Abhishek Vinod Singh, Rahul Saxena, and Nitin Das and headquartered in San Jose, California with offices in the Washington D.C. metro area and Bengaluru, the company fuses high-resolution multispectral and SAR imagery from commercial satellite constellations with proprietary AI models. Its product line spans the Intelligent Vegetation Management System (IVMS), the Climate Risk Intelligence System (CRIS), the Asset Inspection and Monitoring System (AIMS), Wildfire Mitigation Planning Services (WMPS) and the IRIS wildfire planning platform, and a Biodiversity Net Gain management system (BNGAI). AiDASH markets REST APIs and industry-standard connectors for integrating its intelligence
  into existing utility systems, but publishes no public developer portal, API reference, or machine-readable contract — the API surface is customer-gated behind commercial engagement. In June 2026 Schneider Electric agreed to acquire approximately 90% of AiDASH at an implied enterprise value of USD 350 million, pending regulatory close.
image: https://www.aidash.com/wp-content/uploads/2024/10/AiDash_Logo-orange.png
layout: provider
modified: '2026-08-02'
name: AiDASH
nav: Providers
network: true
overview: 'AiDASH publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Satellite, Artificial Intelligence, Geospatial, and Utilities.


  AiDASH''s developer surface includes signup flow, support, engineering blog, product news, YouTube channel, and 22 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 25.5
  delta: 1.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 24.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 32.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aidash/refs/heads/main/screenshots/aidash-2026-08-07T161053.png
security:
- kind: domain-security
  name: Aidash Domain Security
  slug: aidash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aidash Trust Center
  slug: aidash-trust-center
  summary_line: SOC 2, SOC 3, CSA STAR Level 1
slug: aidash
tags:
- Company
- Satellite
- Artificial Intelligence
- Geospatial
- Utilities
- Energy
- Vegetation Management
- Wildfire
- Climate Risk
- Asset Management
- Remote Sensing
- Vertical SaaS
website: https://www.aidash.com/
---
