---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The C.H. Robinson Carrier API enables carriers to find, offer, book, and auto-create loads directly from their own TMS, send visibility updates, upload documents for faster invoicing, and check paymen
  name: C.H. Robinson Carrier API
  slug: carrier-api
- description: The Navisphere Shipper API integrates C.H. Robinson's global transportation management system into a shipper's TMS or ERP. Capabilities include real-time rate quoting, load tendering, shipment trackin
  name: C.H. Robinson Navisphere Shipper API
  slug: shipper-navisphere-api
artifact_total: 50
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ch-robinson-worldwide-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ch-robinson
- group: company
  title: ''
  type: Website
  url: https://www.chrobinson.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.chrobinson.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.chrobinson.com/en-us/technology/connectivity-integrations/
- group: other
  title: ''
  type: Technology
  url: https://www.chrobinson.com/en-us/technology/
- group: other
  title: ''
  type: Navisphere
  url: https://www.chrobinson.com/en-us/technology/shipper-technology/navisphere/
- group: start
  title: ''
  type: CarrierPortal
  url: https://www.chrobinson.com/en-us/carriers/api-connectivity/
- group: company
  title: ''
  type: About
  url: https://www.chrobinson.com/en-us/about-us/
- group: company
  title: ''
  type: Careers
  url: https://jobs.chrobinson.com/
- group: company
  title: ''
  type: News
  url: https://www.chrobinson.com/en-us/newsroom/
- group: company
  title: ''
  type: Investors
  url: https://investor.chrobinson.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chrobinson.com/en-us/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chrobinson.com/en-us/privacy-notice/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/c.h.-robinson/
- group: other
  title: ''
  type: X
  url: https://x.com/CHRobinsonInc
- group: other
  title: ''
  type: Services
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.chrobinson.com/llms.txt
created: '2025-01-01'
description: C.H. Robinson is one of the world's largest third-party logistics (3PL) providers, offering global freight transportation, supply chain management, customs brokerage, and sourcing of fresh produce. Its Navisphere transportation management system provides end-to-end supply chain planning, purchase order management, execution, freight payment, and business intelligence. C.H. Robinson exposes APIs that allow shippers and carriers to integrate quoting, booking, tracking, documents, and payment workflows directly into their own TMS or ERP platforms.
features:
- name: Rate Quoting
- name: Load Booking
- name: Load Tendering
- name: Shipment Tracking
- name: Real-Time Visibility
- name: Document Exchange
- name: Payment Status
- name: Freight Audit
- name: Freight Payment
- name: Business Intelligence
- name: EDI
- name: XML
- name: API Connectivity
- name: Carrier Onboarding
- name: Load Matching
- name: Capacity Search
- name: Automated Booking
- name: Tracking Webhooks
- name: Proof of Delivery
- name: Invoice Upload
finops:
- name: Ch Robinson Worldwide Finops
  service_category: Logistics / Freight
  slug: ch-robinson-worldwide-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ch-robinson-worldwide.png
integrations:
- name: Navisphere
- name: Axele
- name: Beyond Trucks
- name: SmartHop
- name: Geotab
- name: SOS Trucking
- name: SAP
- name: Oracle
- name: NetSuite
- name: Microsoft Dynamics
- name: Manhattan Associates
- name: Blue Yonder
- name: MercuryGate
- name: Kuebix
layout: provider
modified: '2026-04-23'
name: C.H. Robinson
nav: Providers
network: true
overview: 'C.H. Robinson publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Freight, Logistics, Shipping, Supply Chain, and Transportation.


  C.H. Robinson''s developer surface includes documentation, product news, and 15 more developer resources.'
plans:
- name: Ch Robinson Worldwide Plans Pricing
  plan_count: 2
  slug: ch-robinson-worldwide-plans-pricing
press:
- date: '2026-05-25'
  title: More than 100 trillion data points fuel ...
  url: https://www.chrobinson.com/en-us/about-us/newsroom/press-releases/2026/100-trillion-data-points-fuel-chrobinson-agentic-supply-chains/
- date: '2026-05-25'
  title: C.H. Robinson Worldwide, Inc. - Search Results
  url: https://investor.chrobinson.com/Search-Results/default.aspx?SearchTerm=&PageNumber=4
- date: '2026-05-25'
  title: Artificial Intelligence
  url: https://www.chrobinson.com/en-us/about-us/newsroom/tags/artificial-intelligence/
- date: '2026-05-25'
  title: C.H. Robinson Launches AI Agents to Combat ...
  url: https://investor.chrobinson.com/News-and-Events/Press-Releases/press-release-details/2026/C-H--Robinson-Launches-AI-Agents-to-Combat-Industrywide-Problem-of-Missed-LTL-Pickups/default.aspx
- date: '2026-05-25'
  title: In-House Tech and AI Agents Expand Impact
  url: https://www.chrobinson.com/en-us/about-us/newsroom/news/2026/lean-ai-growing-shipper-impact/
random_paper: 64
rate_limits:
- limit_count: 2
  name: Ch Robinson Worldwide Rate Limits
  slug: ch-robinson-worldwide-rate-limits
score:
  band: emerging
  composite: 23.7
  delta: -2.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 26.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/screenshots/ch-robinson-worldwide-2026-06-20T174153.png
security:
- kind: domain-security
  name: Ch Robinson Worldwide Domain Security
  slug: ch-robinson-worldwide-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ch-robinson-worldwide
tags:
- Freight
- Logistics
- Shipping
- Supply Chain
- Transportation
- Transportation Management
- Fortune 500
use_cases:
- name: TMS Integration
- name: Carrier Load Booking
- name: Shipper Rate Shopping
- name: Multi-Modal Transportation
- name: Customs Brokerage
- name: Global Forwarding
- name: Produce Sourcing
- name: Managed Transportation
- name: Supply Chain Consulting
- name: Fresh Produce Logistics
website: https://www.chrobinson.com
---
