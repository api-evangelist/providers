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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yrc-worldwide-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yrc-worldwide-inc
- group: company
  title: ''
  type: Website
  url: https://www.myyellow.com
- group: docs
  title: ''
  type: Documentation
  url: https://my.yrc.com
- group: docs
  title: ''
  type: Documentation
  url: https://my.hollandregional.com
- group: docs
  title: ''
  type: Documentation
  url: https://my.reddawayregional.com
- group: docs
  title: ''
  type: Documentation
  url: https://tools.newpenn.com
- group: docs
  title: ''
  type: Documentation
  url: https://myyellow.com/yellow-logistics/
- group: docs
  title: ''
  type: Documentation
  url: https://investors.myyellow.com
- group: operate
  title: ''
  type: FAQ
  url: https://myyellow.com/customer-faq/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://myyellow.com/privacy-policy/
- group: commercial
  title: ''
  type: Legal
  url: https://myyellow.com/notice-and-legal-disclaimer/
- group: commercial
  title: ''
  type: Legal
  url: https://dm.epiq11.com/case/yellowcorporation/info
- group: operate
  title: ''
  type: Support
  url: mailto:customer.care@myyellow.com
- group: operate
  title: ''
  type: StatusPage
  url: https://www.myyellow.com
- group: other
  title: ''
  type: ProfessionalServices
  url: https://www.rbauction.com
description: YRC Worldwide (rebranded as Yellow Corporation in 2021) was a holding company whose subsidiaries — YRC Freight, Holland, Reddaway, New Penn, and HNRY Logistics — provided less-than-truckload (LTL) freight transportation, brokerage, and logistics services across North America. The company ceased operations on July 30, 2023 and filed for Chapter 11 bankruptcy on August 6, 2023, ending nearly 100 years of operation. Bankruptcy asset sales redistributed terminals and equipment to Saia, XPO, Estes, and other carriers; no public developer APIs were ever published.
features:
- description: National and regional LTL freight transportation across the U.S., Canada, and Mexico.
  name: Less-Than-Truckload Shipping
- description: PRO number, bill of lading, PO number, booking number, and load number tracking via the customer portals.
  name: Shipment Tracking
- description: Online rate quote tools for obtaining freight pricing prior to shipment.
  name: Rate Quoting
- description: Web-based creation and management of bills of lading and shipping documents.
  name: Bill of Lading Management
- description: Cargo claim filing, overcharge claims, and claim status tracking.
  name: Claims Management
- description: Open invoice management, online payment, and payment history lookup by check or PRO.
  name: Invoicing and Online Payment
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yrc-worldwide.png
integrations:
- description: Standard freight EDI document exchange (e.g., 204, 210, 211, 214, 990) for shipper integration with TMS platforms.
  name: EDI
- description: Integration with shipper TMS platforms via EDI for tendering, status updates, and invoicing.
  name: Transportation Management Systems
layout: provider
modified: '2026-05-03'
name: YRC Worldwide
nav: Providers
network: true
overview: 'YRC Worldwide is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500.


  YRC Worldwide''s developer surface includes documentation, FAQ, legal docs, support, and 12 more developer resources.'
press:
- date: '2026-05-25'
  title: Augment Raises $85M Series A to Supercharge Augie ...
  url: https://www.businesswire.com/news/home/20250904472410/en/Augment-Raises-%2485M-Series-A-to-Supercharge-Augie-The-AI-Teammate-for-Logistics
- date: '2026-05-25'
  title: YRC to tap James Welch, long-time trucking executive, as ...
  url: https://www.dcvelocity.com/articles/25511-yrc-to-tap-james-welch-long-time-trucking-executive-as-new-ceo
- date: '2026-05-25'
  title: Yellow Corp trucking company shares plunge as ...
  url: https://www.21alivenews.com/2023/07/28/yellow-corp-trucking-company-shares-plunge-bankruptcy-looms/
- date: '2026-05-25'
  title: YRC Worldwide, Teamsters Set to Meet
  url: https://www.truckinginfo.com/news/yrc-worlwide-and-teamsters-set-to-meet
- date: '2026-05-25'
  title: Yellow is shutting down and headed for bankruptcy, the ...
  url: https://fox5sandiego.com/news/business/ap-business/ap-yellow-is-shutting-down-and-headed-for-bankruptcy-the-teamsters-union-says-heres-what-to-know/
random_paper: 47
score:
  band: minimal
  composite: 10.8
  delta: -1.5
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 12.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yrc-worldwide/refs/heads/main/screenshots/yrc-worldwide-2026-06-20T201750.png
security:
- kind: domain-security
  name: Yrc Worldwide Domain Security
  slug: yrc-worldwide-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yrc-worldwide
tags:
- Fortune 500
use_cases:
- description: Long-haul less-than-truckload movement between major U.S. metro areas via YRC Freight.
  name: National LTL Distribution
- description: Next-day and two-day regional LTL coverage through Holland (Midwest), Reddaway (West), and New Penn (Northeast).
  name: Regional LTL Service
- description: U.S.–Canada and U.S.–Mexico LTL service through YRC Freight's North American network.
  name: Cross-Border Freight
- description: Truckload brokerage and managed transportation through HNRY Logistics.
  name: Freight Brokerage
website: https://www.myyellow.com
---
