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
api_count: 6
apis:
- description: Public and private REST API exposing CMA CGM, ANL, APL, CNC, and Containerships shipment events aligned with the DCSA Track & Trace v2.2.0 OpenAPI specification (`/operation/trackandtrace/v1`). Two op
  name: CMA CGM Track and Trace API
  slug: cma-cgm-track-and-trace-api
- description: Vessel schedule and routing API exposing point-to-point sailing solutions, port schedules, and vessel itineraries for the upcoming 12-week horizon across the CMA CGM, ANL, APL, CNC, and Containerships
  name: CMA CGM Schedules API
  slug: cma-cgm-schedules-api
- description: Spot quotation and US service contract API delivering ocean freight rates with all applicable surcharges (BAF, currency adjustment, security, origin/destination handling, peak season, etc.) directly i
  name: CMA CGM Quotation API
  slug: cma-cgm-quotation-api
- description: Booking request API allowing shippers, NVOCCs, and freight forwarders to submit, amend, and cancel ocean bookings against CMA CGM Group services directly from their TMS or ERP. The REST profile mirror
  name: CMA CGM Booking Request API
  slug: cma-cgm-booking-request-api
- description: Invoice API family exposing freight invoices and associated documents programmatically — including a "Copy Invoice PDF" operation that retrieves the original PDF artifact for a given invoice number. L
  name: CMA CGM Invoice API
  slug: cma-cgm-invoice-api
- description: CEVA Logistics — the CMA CGM Group contract logistics, freight forwarding, and ground transportation subsidiary — exposes a separate shipment tracking REST API through developer.cevalogistics.com. The
  name: CEVA Logistics Tracking API
  slug: ceva-logistics-tracking-api
artifact_total: 30
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cma-cgm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cma-cgm.com
- group: other
  title: ''
  type: Group
  url: https://www.cmacgm-group.com/en
- group: start
  title: ''
  type: Portal
  url: https://api-portal.cma-cgm.com/
- group: start
  title: ''
  type: Portal
  url: https://www.cma-cgm.com/my-cma-cgm
- group: start
  title: ''
  type: GettingStarted
  url: https://api-portal.cma-cgm.com/usage-guide
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://api-portal.cma-cgm.com/release-notes
- group: other
  title: ''
  type: EDICatalog
  url: https://cloud.customer.cmacgm-group.com/EDI_catalog_EN
- group: other
  title: ''
  type: EDISolutions
  url: https://www.cma-cgm.com/products-services/ecommerce/edi-api-channels
- group: operate
  title: ''
  type: Support
  url: https://mycustomerservice.cma-cgm.com/s/selfcare/article/API-Solution
- group: other
  title: ''
  type: Schedules
  url: https://www.cma-cgm.com/ebusiness/schedules
- group: other
  title: ''
  type: Documents
  url: https://www.cma-cgm.com/products-services/ecommerce/documents-bl
- group: other
  title: ''
  type: Finance
  url: https://www.cma-cgm.com/products-services/ecommerce/finance
- group: other
  title: ''
  type: SmartContainers
  url: https://www.cma-cgm.com/services/smart-containers
- group: other
  title: ''
  type: Sustainability
  url: https://www.cmacgm-group.com/en/sustainability-and-innovation
- group: other
  title: ''
  type: Innovation
  url: https://www.cmacgm-group.com/en/innovation/digital-startup%20support
- group: other
  title: ''
  type: ZEBOX
  url: https://www.ze-box.io/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cmacgm-group.com/en/news-media
- group: company
  title: ''
  type: Investors
  url: https://www.cmacgm-group.com/en/finance
- group: company
  title: ''
  type: Careers
  url: https://www.cma-cgm.com/about/careers
- group: other
  title: ''
  type: Subsidiary
  url: https://www.cevalogistics.com
- group: other
  title: ''
  type: Subsidiary
  url: https://www.apl.com
- group: other
  title: ''
  type: Subsidiary
  url: https://www.anl.com.au
- group: other
  title: ''
  type: Subsidiary
  url: https://www.cnc-line.com
- group: other
  title: ''
  type: Subsidiary
  url: https://www.containershipsgroup.com
- group: other
  title: ''
  type: Subsidiary
  url: https://www.cmacgm-aircargo.com
- group: other
  title: ''
  type: Standards
  url: https://dcsa.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cma-cgm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cma-cgm
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cmacgm
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/cmacgmtv
created: '2026-05-25'
description: CMA CGM is a Marseille-headquartered French container shipping, logistics, and port operator and the third-largest ocean carrier in the world. Founded in 1978 by Jacques Saadé and led today by Chairman & CEO Rodolphe Saadé, the CMA CGM Group operates a fleet of 593 vessels with 4.5 million TEU of capacity calling 420 ports across 160 countries on 257 maritime services. The group includes maritime brands ANL, APL, CNC Line, Containerships, Comanav, and Mercosul Line; terminal operator CMA Terminals and Terminal Link; the CEVA Logistics contract logistics and freight forwarding business (acquired 2019); CMA CGM Air Cargo; Brittany Ferries and La Méridionale passenger ferries; and the CMA Média portfolio (La Provence, La Tribune, BFM-RMC, Brut). Through api-portal.cma-cgm.com the group exposes a DCSA-aligned REST API surface — Track and Trace v1 (DCSA v2.2.0), Schedules, Booking Request, Quotation, and Invoice — plus a parallel EDI catalog (EDIFACT IFTSAI, IFTMBF, IFTSTA, INVOIC)
  and group-level digital initiatives including ZEBOX (startup accelerator), Traxens-based IoT smart containers, and a strategic AI partnership with Mistral.
features:
- DCSA Track & Trace v2.2.0 REST API (Public API Key + Private OAuth2 tiers)
- Vessel and port-to-port Schedules API covering CMA CGM, ANL, APL, CNC, Containerships
- Quotation API for spot rates and US service contracts with full surcharge breakdown
- Booking Request API mirroring EDIFACT IFTMBF for programmatic ocean bookings
- Invoice API family including Copy Invoice PDF retrieval
- Parallel EDI catalog with IFTSAI (schedules), IFTMBF (booking), IFTSTA (tracking), INVOIC (billing)
- Self-service API portal at api-portal.cma-cgm.com with subscription, live consumption monitoring, FAQ
- Founding member of the Digital Container Shipping Association (DCSA) — APIs align with DCSA standards
- CEVA Logistics Tracking API (developer.cevalogistics.com) for contract-logistics and forwarding flows
- Traxens-based smart container telemetry (shock, temperature, humidity, door-open) accessible by API
- Founded 1978 in Marseille by Jacques Saadé; led by Chairman & CEO Rodolphe Saadé
- 3rd-largest container carrier worldwide; fleet of 593 vessels and 4.5M TEU capacity
- Operates 257 maritime services calling 420 ports across 160 countries
- 160,000 employees globally across maritime, terminals, logistics, air cargo, and media
- Group revenue $55.48B and net income $5.71B in FY2024; Q1 2026 revenue $13.23B
- Subsidiaries: ANL, APL, CNC Line, Containerships, Comanav, Mercosul Line, CEVA Logistics, CMA CGM Air Cargo, CMA Terminals, Terminal Link, La Méridionale
- Strategic stake in Brittany Ferries; UK intermodal Freightliner acquired in 2026
- CMA Média portfolio includes La Provence, Corse-Matin, La Tribune, BFM-RMC, Brut
- Member of the Ocean Alliance shipping consortium alongside COSCO and Evergreen
- $10B United Ports JV with Stonepeak (2025) for accelerated US port investment
- Decarbonization strategy investing in LNG, biogas, and methanol-powered vessels
- €100M strategic AI partnership with Mistral for customer service and logistics innovation
- ZEBOX international startup accelerator (founded by Rodolphe Saadé, 6 global hubs, 15+ corporate partners)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cma-cgm.png
layout: provider
modified: '2026-05-25'
name: CMA CGM
nav: Providers
network: true
overview: 'CMA CGM publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, Container Shipping, Maritime, Logistics, and Freight.


  CMA CGM''s developer surface includes developer portal, getting-started guide, release notes, support, YouTube channel, and 26 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 14.0
  delta: -2.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cma-cgm/refs/heads/main/screenshots/cma-cgm-2026-06-20T174627.png
security:
- kind: domain-security
  name: Cma Cgm Domain Security
  slug: cma-cgm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cma-cgm
tags:
- Shipping
- Container Shipping
- Maritime
- Logistics
- Freight
- Supply Chain
- Ports
- Terminals
- Track and Trace
- DCSA
- EDI
- Air Cargo
- Intermodal
- Ocean Freight
- Smart Containers
website: https://www.cma-cgm.com
---
