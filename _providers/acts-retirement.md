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
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acts-retirement-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.actsretirement.org
- group: start
  title: ''
  type: Portal
  url: https://www.actsretirement.org
- group: company
  title: ''
  type: About
  url: https://www.actsretirement.org/about-acts/
- group: other
  title: ''
  type: Communities
  url: https://www.actsretirement.org/communities/
- group: company
  title: ''
  type: News
  url: https://www.actsretirement.org/latest-retirement-news/
- group: other
  title: ''
  type: HealthServices
  url: https://actshealthservices.org
- group: company
  title: ''
  type: Careers
  url: https://careers-actslife.icims.com/jobs/search
- group: operate
  title: ''
  type: Contact
  url: https://www.actsretirement.org/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.actsretirement.org/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acts-retirement-life-communities
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/ActsRetirement
- group: company
  title: ''
  type: Blog
  url: https://www.actsretirement.org/latest-retirement-news/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/ActsRetirementLife
- group: build
  title: ''
  type: GitHub
  url: https://github.com/api-evangelist/acts-retirement
- group: operate
  title: ''
  type: Contact
  url: ''
created: '2026-05-23'
description: Acts Retirement-Life Communities is a not-for-profit operator of continuing care retirement communities (CCRCs) headquartered in West Point, Pennsylvania. Founded in 1972, Acts operates 28 senior living campuses across nine Mid-Atlantic and Southeastern U.S. states (Alabama, Delaware, Florida, Georgia, Maryland, New Jersey, North Carolina, Pennsylvania, South Carolina) and serves approximately 10,000 residents. Its core service lines are independent living for adults 55+, assisted living, memory care, skilled nursing, short-term rehabilitation, and on-campus health services delivered under the Acts Life Care contract model. Acts publishes no public developer APIs, no OpenAPI specifications, no SDKs, and no developer portal — its digital surface consists of a marketing website, a community directory, an iCIMS-hosted careers portal at careers-actslife.icims.com, and a separate health-services marketing site at actshealthservices.org. This repository documents the organization
  and its likely senior-living IT vendor stack for ecosystem mapping purposes; it does not document a developer API surface because none is published.
features:
- description: Maintenance-free apartment, cottage, and villa residences for active adults 55+ across 28 campuses, with dining, fitness, social programming, and lifelong learning amenities included.
  name: Independent Living
- description: On-campus personal care residences providing assistance with activities of daily living (bathing, dressing, medication management) for residents who can no longer live fully independently.
  name: Assisted Living
- description: Specialized residential neighborhoods for residents living with Alzheimer's disease and other forms of dementia, with secured environments and dementia-trained staff.
  name: Memory Care
- description: On-site licensed skilled nursing facilities providing 24-hour professional nursing for residents requiring complex medical care or long-term custodial care.
  name: Skilled Nursing Care
- description: Inpatient and outpatient rehabilitation services including physical, occupational, and speech therapy following hospitalization, surgery, or illness.
  name: Short-Term Rehabilitation
- description: A continuing-care contract that combines independent-living residency with prepaid access to on-campus assisted living, memory care, and skilled nursing at the same monthly fee structure, providing long-term care cost certainty.
  name: Acts Life Care Contract
- description: A charitable program funded by the Acts Legacy Foundation that provides financial assistance to residents who outlive their personal resources, ensuring no resident is asked to leave for inability to pay.
  name: Acts Benevolence
- description: Primary-care medical clinics, nurse practitioner programs, and hospice services delivered on each Acts campus under the Acts Health Services brand.
  name: On-Campus Health Services
image: https://www.actsretirement.org/favicon.ico
integrations:
- description: The Acts careers portal is hosted on iCIMS at careers-actslife.icims.com, indicating iCIMS Talent Cloud as the applicant tracking system and recruiting marketing platform.
  name: iCIMS Talent Cloud (Careers)
- description: As a multi-site skilled nursing and assisted living operator, Acts almost certainly runs an LTC/PAC-focused electronic health record such as PointClickCare, MatrixCare, or Netsmart MyUnity, but the specific vendor is not publicly disclosed on the Acts website.
  name: Likely Clinical EHR (Vendor Not Publicly Disclosed)
- description: With ~10,000 residents across 28 campuses, Acts operates a large workforce that requires a multi-site HRIS, payroll, and workforce management platform (commonly Workday, UKG Pro/Ready, Paycom, or Oracle HCM in this market segment); the specific vendor is not publicly disclosed.
  name: Likely HRIS/Payroll (Vendor Not Publicly Disclosed)
- description: Multi-entity nonprofit CCRC operators typically run Workday Financials, Sage Intacct, Oracle NetSuite, or MRI/Yardi for resident billing and general ledger; the specific vendor is not publicly disclosed.
  name: Likely ERP/Financials (Vendor Not Publicly Disclosed)
layout: provider
modified: '2026-05-23'
name: Acts Retirement-Life Communities
nav: Providers
network: true
overview: 'Acts Retirement-Life Communities is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Senior Living, Retirement Communities, Continuing Care Retirement Community, Healthcare, and Skilled Nursing.


  Acts Retirement-Life Communities'' developer surface includes developer portal, product news, engineering blog, YouTube channel, GitHub presence, and 10 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.2
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acts-retirement/refs/heads/main/screenshots/acts-retirement-2026-06-20T164330.png
security:
- kind: domain-security
  name: Acts Retirement Domain Security
  slug: acts-retirement-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acts-retirement
solutions:
- description: The Acts Life Care contract addresses the senior-living industry's biggest financial risk — open-ended long-term-care costs — by bundling all future care levels into a single predictable monthly fee structure backed by Acts Benevolence.
  name: Lifetime Care Cost Certainty
- description: With 28 campuses across nine Eastern and Southeastern states, residents and their families can relocate within the Acts network while preserving their Life Care contract benefits and care history.
  name: Geographic Continuity Of Care
- description: As a not-for-profit organization rooted in a Christian ministry heritage, Acts reinvests operating margin into resident services, benevolent care, and capital improvements rather than distributing profits to investors.
  name: Faith-Based Nonprofit Operating Model
tags:
- Senior Living
- Retirement Communities
- Continuing Care Retirement Community
- Healthcare
- Skilled Nursing
- Assisted Living
- Memory Care
- Independent Living
- Non-Profit
- Long-Term Care
use_cases:
- description: Older adults and their families evaluating CCRC options across the Mid-Atlantic and Southeast U.S. can browse all 28 Acts campuses by state, compare pricing tiers, and request information packets through the public marketing site.
  name: Retirement Community Selection
- description: Prospective residents can sign an Acts Life Care contract at any of the 28 communities, locking in lifetime access to the full care continuum (independent through skilled nursing) at predictable monthly fees.
  name: Acts Life Care Contract Purchase
- description: Job seekers across nursing, dining, hospitality, facilities, and administrative roles can search and apply to openings at any Acts campus through the iCIMS-powered careers portal at careers-actslife.icims.com.
  name: Employment Search And Application
- description: Donors can contribute to the Acts Legacy Foundation to support benevolent care for residents who exhaust their personal financial resources during their tenure.
  name: Charitable Giving
- description: Healthcare technology vendors, food-service suppliers, construction contractors, and professional service firms can identify Acts procurement contacts through the public contact and corporate compliance pages.
  name: Vendor And Partner Inquiry
website: https://www.actsretirement.org
---
