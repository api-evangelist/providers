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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sears-hometown-and-outlet-stores-inc-
coverage:
  checked: '2026-08-28'
  detail: Sears Hometown and Outlet Stores was liquidated under Chapter 7 in February 2023 and its corporate domain shos.com is now a parked HostGator page — it presents a wildcard *.hostgator.com TLS certificate, redirects the root to /404.html, and answers HTTP 406 on every path — while developer.shos.com and api.shos.com no longer resolve at all.
  evidence:
  - note: TLS name mismatch (*.hostgator.com); with verification disabled the root redirects to https://www.shos.com/404.html — a parked-domain soft-404, not a company site.
    status: 200
    url: https://www.shos.com/
  - status: 406
    url: https://www.shos.com/.well-known/security.txt
  - status: 406
    url: https://www.shos.com/robots.txt
  - note: DNS does not resolve (NXDOMAIN).
    status: 0
    url: https://developer.shos.com/
  - note: DNS does not resolve (NXDOMAIN).
    status: 0
    url: https://api.shos.com/
  - note: NXDOMAIN — previously carried in this file as the company Website; a slug-shaped guess that has never resolved. Removed as a dead pointer.
    status: 0
    url: https://www.sears-hometown-and-outlet-stores.com/
  - note: Redirects to https://www.sears.com/ — the former Sears Outlet brand domain is now controlled by Transformco, a different company, so it is not recorded here as this provider's website.
    status: 200
    url: https://www.searsoutlet.com/
  - note: Verified live — the only surviving pointer for this company.
    status: 200
    url: https://www.linkedin.com/company/sears-hometown-and-outlet-stores-inc-
  reason: defunct
  state: none
created: '2026-03-24'
description: 'Sears Hometown and Outlet Stores, Inc. (NASDAQ: SHOS) was a national retailer of home appliances, lawn and garden equipment, tools and hardware, spun off from Sears Holdings in October 2012 and operating two segments: Sears Hometown and Hardware, a largely franchised network of smaller-format stores in rural and suburban markets, and Sears Outlet, which sold new, one-of-a-kind, out-of-carton, discontinued, obsolete, used, reconditioned, overstocked and scratch-and-dent merchandise. The company was acquired by Transform Holdco (Transformco) and ESL Investments in October 2019, at which point the Sears Outlet business was sold on to Franchise Group and rebranded American Freight. Sears Hometown filed for Chapter 11 in December 2022 and converted to a Chapter 7 liquidation in February 2023. The company is defunct: it never operated a public developer program, and its corporate domain shos.com is now a parked registrar page serving a wildcard *.hostgator.com certificate and a 404,
  so there is no API surface, documentation, or /.well-known/ document left to profile.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sears-hometown-and-outlet-stores.png
layout: provider
modified: '2026-08-28'
name: Sears Hometown and Outlet Stores
nav: Providers
network: true
overview: Sears Hometown and Outlet Stores is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Specialty Retail, Home Appliances, Tools and Hardware, and Lawn and Garden.
press:
- date: '2026-05-25'
  title: Advertising Paper.docx - In 1910 S. Duncan Black & Alonzo...
  url: https://www.coursehero.com/file/59959320/Advertising-Paperdocx/
- date: '2026-05-25'
  title: Sears looks to boost Kenmore and Craftsman brands with new hire
  url: https://www.reuters.com/article/business/sears-looks-to-boost-kenmore-and-craftsman-brands-with-new-hire-idUSKCN0QU054/
- date: '2026-05-25'
  title: Securities Enforcement and Litigation Update
  url: https://www.sullcrom.com/SullivanCromwell/_Assets/PDFs/Memos/Securities-Enforcement-Litigation-Update-2025.pdf
- date: '2026-05-25'
  title: Newly Proposed Amendments to the Delaware General ...
  url: https://www.stblaw.com/about-us/publications/view/2025/02/19/newly-proposed-amendments-to-the-delaware-general-corporation-law
- date: '2026-05-25'
  title: Stanley Black & Decker Completes Purchase Of Craftsman ...
  url: https://www.prnewswire.com/news-releases/stanley-black--decker-completes-purchase-of-craftsman-brand-from-sears-holdings-300420760.html
random_paper: 17
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
slug: sears-hometown-and-outlet-stores
tags:
- Retail
- Specialty Retail
- Home Appliances
- Tools and Hardware
- Lawn and Garden
- Franchise Retail
- Defunct Company
---
