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
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: TJX Companies requires EDI compliance for all resale vendors, supporting purchase orders (850), purchase order acknowledgements (855), advanced shipping notices (856), invoices (810), motor carrier lo
  name: TJX EDI Integration
  slug: tjx-edi
- description: The TJX SupplierOne portal enables diverse supplier registration, certification tracking, and quarterly Tier II program reporting. Suppliers can complete vendor applications, provide business document
  name: TJX SupplierOne Diversity Portal
  slug: tjx-supplierone
artifact_total: 25
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tjx-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tjx
- group: company
  title: ''
  type: Website
  url: https://www.tjx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tjx.com/mytjx/supplier/supplier.html
- group: start
  title: ''
  type: Portal
  url: https://www.mytjx.com/mytjx/supplier.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TJX
- group: other
  title: ''
  type: Suppliers
  url: https://diweb.dicentral.com/tjx/SignUp/GetStarted.aspx
created: '2024-11-27'
description: The TJX Companies, Inc. is an American multinational off-price department store corporation headquartered in Framingham, Massachusetts, ranked No. 80 on the 2024 Fortune 500 list. Operating over 4,800 stores across nine countries and three continents under brands including T.J. Maxx, Marshalls, HomeGoods, Sierra, HomeSense (US), and Winners, HomeSense, Marshalls (Canada), TJX provides supplier and vendor integration through EDI and web-based portal platforms. Supplier connectivity is handled via Oracle iSupplier, SupplierOne, and the DiCentral ASN Vendor Portal, supporting purchase orders, advanced shipping notices, invoicing, and payment tracking.
features:
- description: Web-based supplier self-service for invoice tracking, payment status, deduction management, and purchase order visibility.
  name: Oracle iSupplier Portal
- description: Electronic Data Interchange compliance for purchase orders (850), ASNs (856), invoices (810), and related transactions for resale suppliers.
  name: EDI Vendor Integration
- description: DiCentral-powered portal for creating and submitting advance shipping notices and managing compliance.
  name: ASN Vendor Portal
- description: Supplier diversity portal for diverse supplier registration, certification, and Tier II reporting.
  name: SupplierOne Diversity Registration
- description: Digital invoice submission via Transcepta integration, reducing paperwork and expediting payment cycles.
  name: Transcepta Electronic Invoicing
- description: Vendor integration covering all TJX banners including T.J. Maxx, Marshalls, HomeGoods, Sierra, HomeSense, Winners, and TK Maxx.
  name: Multi-Brand Vendor Support
finops:
- name: Tjx Finops
  service_category: Retail
  slug: tjx-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tjx.png
integrations:
- description: EDI integration and compliance platform for TJX vendor connectivity.
  name: SPS Commerce
- description: ASN Vendor Portal and EDI integration provider powering TJX's vendor shipping notice system.
  name: DiCentral
- description: EDI integration platform supporting TJX vendor compliance requirements.
  name: Zenbridge
- description: Order management and EDI integration connector for TJX Companies.
  name: Pipe17
- description: Electronic invoicing platform for TJX supplier invoice submission.
  name: Transcepta
- description: Oracle-based supplier portal for invoice management and purchase order tracking.
  name: Oracle iSupplier
- description: EDI integration solution for TJX trading partner compliance.
  name: Cleo
layout: provider
modified: '2026-07-25'
name: TJX Companies
nav: Providers
network: true
overview: 'TJX Companies publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Off-Price, Fortune 100, Supply Chain, and EDI.


  TJX Companies'' developer surface includes documentation, developer portal, and 5 more developer resources.'
plans:
- name: Tjx Plans Pricing
  plan_count: 1
  slug: tjx-plans-pricing
press:
- date: '2026-05-25'
  title: 'TJX Companies'' AI Strategy: Analysis of Dominance in Retail'
  url: https://www.klover.ai/tjx-companies-ai-strategy-analysis-of-dominance-in-retail/
- date: '2026-05-25'
  title: 'TJX Companies: Low-Tech Retailer Thrives Amid AI Bubble'
  url: https://www.linkedin.com/posts/redafarran_this-best-in-class-retailer-could-be-a-great-activity-7419666311129116672-gR0c
- date: '2026-05-25'
  title: Form 10-K for TJX Companies INC DE filed 04/02/2025
  url: https://investor.tjx.com/static-files/d01e59d1-c20c-494c-8d7b-6bd41a4db1a2
- date: '2026-05-25'
  title: TJX Companies Archives
  url: https://www.intelligize.com/tag/tjx-companies/
- date: '2026-05-25'
  title: Retailers Embracing AI
  url: https://logisticsti.com/insights/f/retailers-embracing-ai
random_paper: 6
rate_limits:
- limit_count: 1
  name: Tjx Rate Limits
  slug: tjx-rate-limits
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tjx/refs/heads/main/screenshots/tjx-2026-06-20T195419.png
security:
- kind: domain-security
  name: Tjx Domain Security
  slug: tjx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tjx
tags:
- Retail
- Off-Price
- Fortune 100
- Supply Chain
- EDI
use_cases:
- description: Suppliers electronically submit invoices through iSupplier or Transcepta and track payment status in real time.
  name: Supplier Invoice Submission
- description: Suppliers receive and acknowledge purchase orders from TJX banners via EDI 850/855 transactions.
  name: Purchase Order Management
- description: Vendors create and submit ASNs (EDI 856) to notify TJX distribution centers of incoming shipments.
  name: Advance Shipping Notice
- description: Suppliers manage and dispute payment deductions through the Oracle iSupplier portal.
  name: Deduction Dispute Automation
- description: Diverse suppliers register, maintain certifications, and submit quarterly Tier II reports through SupplierOne.
  name: Supplier Diversity Reporting
- description: New vendors establish EDI connectivity via approved service providers and complete TJX's testing requirements.
  name: EDI Compliance Onboarding
website: https://www.tjx.com/
---
