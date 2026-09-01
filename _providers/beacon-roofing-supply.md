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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Beacon PRO+ API provides roofing contractors and integration partners with programmatic access to Beacon's product catalog, real-time inventory and pricing, order management, delivery tracking, ac
  name: Beacon PRO+ API
  slug: beacon-pro-plus
artifact_total: 19
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beacon-roofing-supply-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beacon-building-products
- group: company
  title: ''
  type: Website
  url: https://www.becn.com/
- group: start
  title: ''
  type: Portal
  url: https://www.beaconproplus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://beaconproplus.com/swagger/all_api/
- group: operate
  title: ''
  type: Support
  url: https://www.becn.com/contact-us
created: '2026-03-23'
description: Beacon Roofing Supply (BECN) is one of the largest distributors of residential and non-residential roofing materials and complementary building products in North America. Beacon operates the Beacon PRO+ digital platform providing roofing contractors with real-time inventory, pricing, online ordering, delivery tracking, and account management. Beacon PRO+ offers a REST API and Swagger-documented integration layer for contractor management software, ERP systems, and roofing business applications. Beacon was acquired by QXO in 2025.
features:
- description: Access live product inventory levels and pricing across Beacon locations for accurate contractor quoting.
  name: Real-Time Inventory and Pricing
- description: Place, manage, and track roofing material orders programmatically through the Beacon PRO+ API.
  name: Online Ordering
- description: Real-time delivery status updates and tracking for all Beacon material orders.
  name: Delivery Tracking
- description: Manage contractor account details, billing, and payment information through the API.
  name: Account Management
- description: Receive storm event notifications to proactively reach out to customers in affected areas.
  name: Storm Tracking Alerts
- description: Track manufacturer rebate programs and earned rebates through the API.
  name: Rebate Tracking
finops:
- name: Beacon Roofing Supply Finops
  service_category: Construction Distribution / E-Commerce APIs
  slug: beacon-roofing-supply-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beacon-roofing-supply.png
integrations:
- description: Roofing contractor management software with native Beacon PRO+ integration for material ordering.
  name: AccuLynx
- description: Contractor CRM and project management platform with Beacon PRO+ material order integration.
  name: JobNimbus
- description: Roofing manufacturer partnership enabling GAF product ordering through Beacon PRO+ e-commerce.
  name: GAF
- description: EDI integration service enabling electronic purchase orders, ASNs, and invoices with Beacon Roofing Supply.
  name: TrueCommerce EDI
layout: provider
modified: '2026-04-19'
name: Beacon Roofing Supply
nav: Providers
network: true
overview: 'Beacon Roofing Supply publishes 1 API on the [APIs.io](https://apis.io/) network: Beacon PRO+ API. Tagged areas include Construction, Distribution, Roofing, Building Materials, and E-Commerce.


  Beacon Roofing Supply''s developer surface includes developer portal, documentation, support, and 3 more developer resources.'
plans:
- name: Beacon Roofing Supply Plans Pricing
  plan_count: 1
  slug: beacon-roofing-supply-plans-pricing
press:
- date: '2026-05-25'
  title: QXO completes the acquisition of Beacon Roofing Supply ...
  url: https://news.mergerlinks.com/daily-review/qxo-completes-the-acquisition-of-beacon-roofing-supply-for-$-11bn
- date: '2026-05-25'
  title: BEACON ROOFING SUPPLY, INC. QUEEN MERGERCO, INC ...
  url: https://d18rn0p25nwr6d.cloudfront.net/CIK-0001124941/30855609-2f78-44b5-a21b-d4113cd5aee5.pdf
- date: '2026-05-25'
  title: 'In case you missed it: From private label roofing products ...'
  url: https://www.facebook.com/RoofingContractor/posts/in-case-you-missed-it-from-private-label-roofing-products-%EF%B8%8F-to-ai-powered-logist/1405757331590241/
- date: '2026-05-25'
  title: How QXO is Using AI to Streamline Distribution
  url: https://www.roofingcontractor.com/articles/101320-how-qxo-is-using-ai-to-streamline-distribution
- date: '2026-05-25'
  title: QXO launches $11 billion tender offer for Beacon Roofing ...
  url: https://www.investing.com/news/company-news/qxo-launches-11-billion-tender-offer-for-beacon-roofing-supply-93CH-3831708
random_paper: 5
rate_limits:
- limit_count: 1
  name: Beacon Roofing Supply Rate Limits
  slug: beacon-roofing-supply-rate-limits
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 20.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/screenshots/beacon-roofing-supply-2026-06-20T173105.png
security:
- kind: domain-security
  name: Beacon Roofing Supply Domain Security
  slug: beacon-roofing-supply-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beacon-roofing-supply
tags:
- Construction
- Distribution
- Roofing
- Building Materials
- E-Commerce
- Fortune 1000
use_cases:
- description: Integrate Beacon PRO+ with AccuLynx, JobNimbus, or other contractor management platforms to enable in-app material ordering.
  name: Contractor Management Software Integration
- description: Connect enterprise ERP systems with Beacon ordering and inventory for automated procurement workflows.
  name: ERP Integration
- description: Build custom ordering interfaces for roofing contractors that pull live Beacon pricing and inventory.
  name: Custom Ordering Portals
- description: Integrate Beacon delivery tracking into construction project management and scheduling tools.
  name: Delivery Logistics
website: https://www.becn.com/
---
