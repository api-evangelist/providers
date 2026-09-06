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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wsfs-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wsfsbank.com/
- group: start
  title: ''
  type: Portal
  url: https://www.wsfsbank.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.wsfsbank.com/about/newsroom
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.wsfsbank.com
- group: operate
  title: ''
  type: Contact
  url: https://www.wsfsbank.com/about/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wsfsbank.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wsfsbank.com/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wsfs-bank/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/WSFSBank
- group: other
  title: ''
  type: Subsidiaries
  url: ''
- group: other
  title: ''
  type: Scale
  url: ''
- group: other
  title: ''
  type: ProductPage
  url: https://www.wsfsbank.com/cash-connect
- group: other
  title: ''
  type: ProductPage
  url: https://www.bmt.com
- group: other
  title: ''
  type: ProductPage
  url: https://www.wsfsbank.com/institutional-services
created: '2026-05-23'
description: WSFS Financial Corporation is a multibillion-dollar financial services company headquartered in Wilmington, Delaware. Its primary subsidiary WSFS Bank has operated since 1832, making it one of the oldest banks in the United States. As of March 31, 2026 the company reported $22.1 billion in assets and $97.6 billion in assets under management and administration across 114 offices in six states. Business lines include personal banking, small business and commercial banking, treasury management, WSFS Mortgage, WSFS Wealth Management, Bryn Mawr Trust (acquired 2022), WSFS Institutional Services, and the Cash Connect ATM-as-a-service business that provides cash logistics and vault cash to independent ATM operators. WSFS does not publish a public developer portal, OpenAPI specifications, or SDKs; all APIs are bilateral treasury / cash management integrations delivered through Enhanced Business Online Banking, ACH/wire file feeds, and the Cash Connect partner portal.
features:
- description: Commercial online banking platform bundled with premier accounts, providing ACH, wire, positive pay, and reporting.
  name: Enhanced Business Online Banking Plus
- description: Remote deposit capture for businesses to deposit checks via scanner or mobile.
  name: Xpress Deposit
- description: Cash management hardware paired with provisional credit for retail deposits.
  name: Smart Safe Solutions
- description: Web portal for independent ATM operators to order cash and manage vault cash deployments.
  name: Cash Connect Partner Portal
- description: Personal and small business online and mobile banking with secure account access.
  name: Online and Mobile Banking
- description: Access to 80+ banking offices and one of the largest ATM networks in the Mid-Atlantic region.
  name: ATM Network Access
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wsfs-financial.png
integrations:
- description: Bilateral file-based ACH and wire origination integrations for commercial customers, typically via Enhanced Business Online Banking.
  name: ACH and Wire File Integration
- description: Partner integration for ATM operators with vault cash logistics; no public API documented.
  name: Cash Connect Partner Integration
- description: Card acceptance integrations through merchant services partners.
  name: Merchant Services Integration
layout: provider
modified: '2026-07-25'
name: WSFS Financial
nav: Providers
network: true
overview: 'WSFS Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Wealth Management, Trust Services, Cash Logistics, and Commercial Banking.


  WSFS Financial''s developer surface includes developer portal, engineering blog, YouTube channel, and 10 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wsfs-financial/refs/heads/main/screenshots/wsfs-financial-2026-06-20T201636.png
security:
- kind: domain-security
  name: Wsfs Financial Domain Security
  slug: wsfs-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wsfs-financial
tags:
- Banking
- Wealth Management
- Trust Services
- Cash Logistics
- Commercial Banking
use_cases:
- description: Consumer checking, savings, mortgages, debit cards, and home equity for customers in DE, PA, NJ, FL, NV, and VA.
  name: Regional Personal Banking
- description: Business checking, SBA lending, Express Loans, equipment finance, and merchant services for small business customers.
  name: Small Business Banking
- description: Commercial real estate financing, working capital, treasury management, and capital markets for middle-market businesses.
  name: Commercial Banking and Treasury
- description: Financial planning, investment management, trust and estate services through Bryn Mawr Trust.
  name: Wealth and Trust Services
- description: Vault cash supply, replenishment, and management for independent ATM operators via Cash Connect.
  name: ATM Cash Logistics
- description: SPV management, corporate trust, and global capital markets administration.
  name: Corporate Trust and Institutional Services
website: https://www.wsfsbank.com/
---
