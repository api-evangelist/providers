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
api_count: 1
apis:
- description: AmerisourceBergen (now Cencora) is one of the largest global pharmaceutical distributors, serving pharmaceutical manufacturers, healthcare providers, and patients worldwide. The company does not curre
  name: AmerisourceBergen Website
  slug: website
artifact_total: 22
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amerisourcebergen-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.amerisourcebergen.com
- group: company
  title: ''
  type: Website
  url: https://www.cencora.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amerisourcebergen.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amerisourcebergen.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.amerisourcebergen.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amerisourcebergen
- group: other
  title: ''
  type: X
  url: https://twitter.com/AmerisourceBrg
created: '2024-01-01'
description: AmerisourceBergen (now Cencora) fosters a positive impact on healthcare around the world by advancing the development and delivery of pharmaceuticals and healthcare products. The company provides pharmaceutical distribution, manufacturer solutions, provider solutions, and animal health solutions across 50+ countries through 1,300+ facilities.
features:
- description: U.S. and global distribution network supplying pharmaceutical products from manufacturers to healthcare providers including pharmacies, hospitals, and physician practices.
  name: Pharmaceutical Distribution
- description: End-to-end support for pharmaceutical manufacturers from drug research and clinical development through commercialization, patient access, and specialty logistics.
  name: Manufacturer Solutions
- description: Solutions for healthcare providers including pharmacies, hospitals, health systems, long-term care facilities, and specialty physician practices to optimize operations and patient care.
  name: Provider Solutions
- description: Distribution and solutions for veterinary and livestock pharmaceutical products through the MWI Animal Health business.
  name: Animal Health Solutions
- description: Programs addressing barriers to medication access and improving speed-to-therapy through pharmaceutical patient support services.
  name: Patient Access and Adherence
- description: Global distribution with specialized packaging, temperature-controlled storage, and customs expertise for specialty and rare disease therapies.
  name: Specialty Logistics and Warehousing
- description: Commercialization capabilities connecting manufacturers to health systems and patients for advanced cell and gene therapy products.
  name: Cell and Gene Therapy Access
- description: Education and support programs for accessing and building confidence in biosimilar therapies across the healthcare ecosystem.
  name: Biosimilar Support
finops:
- name: Amerisourcebergen Finops
  service_category: Pharmaceutical Distribution
  slug: amerisourcebergen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amerisourcebergen.png
integrations:
- description: Independent pharmacy network providing purchasing programs, business solutions, and marketing support to community pharmacies.
  name: Good Neighbor Pharmacy Network
- description: Animal health distribution subsidiary providing veterinary products and solutions to veterinary practices and livestock operations.
  name: MWI Animal Health
- description: Consulting and market access affiliate providing healthcare analytics, reimbursement support, and market access strategies for manufacturers.
  name: Xcenda
layout: provider
modified: '2026-04-19'
name: AmerisourceBergen
nav: Providers
network: true
overview: 'AmerisourceBergen publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmaceutical Distribution, Healthcare, Drug Distribution, Manufacturer Solutions, and Provider Solutions.


  AmerisourceBergen''s developer surface includes developer portal, support, and 6 more developer resources.'
plans:
- name: Amerisourcebergen Plans Pricing
  plan_count: 1
  slug: amerisourcebergen-plans-pricing
press:
- date: '2026-05-25'
  title: Accenture and Salesforce Collaborate to Help Life ...
  url: https://newsroom.accenture.com/news/2023/accenture-and-salesforce-collaborate-to-help-life-sciences-companies-create-differentiation-with-data-and-ai
- date: '2026-05-25'
  title: WhizAI Closes New Round with Investment from Shanda ...
  url: https://www.businesswire.com/news/home/20221025005018/en/WhizAI-Closes-New-Round-with-Investment-from-Shanda-Group-and-AmerisourceBergen-Bringing-Total-Capital-Raised-to-%2421-Million
- date: '2026-05-25'
  title: AmerisourceBergen & TrakCel Launch Cell Therapy Tool
  url: https://www.cencora.com/newsroom/amerisourcebergen-and-trakcel-launch-integrated-platform-to-support-cgts
- date: '2026-05-25'
  title: AmerisourceBergen Reports Fiscal 2019 Second Quarter ...
  url: https://investor.amerisourcebergen.com/news/news-details/2019/AmerisourceBergen-Reports-Fiscal-2019-Second-Quarter-Results/default.aspx
- date: '2026-05-25'
  title: Artificial Intelligence at Cencora
  url: https://emerj.com/artificial-intelligence-at-cencora/
random_paper: 28
rate_limits:
- limit_count: 1
  name: Amerisourcebergen Rate Limits
  slug: amerisourcebergen-rate-limits
score:
  band: emerging
  composite: 21.5
  delta: -4.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amerisourcebergen/refs/heads/main/screenshots/amerisourcebergen-2026-06-20T171929.png
security:
- kind: domain-security
  name: Amerisourcebergen Domain Security
  slug: amerisourcebergen-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: amerisourcebergen
tags:
- Pharmaceutical Distribution
- Healthcare
- Drug Distribution
- Manufacturer Solutions
- Provider Solutions
- Animal Health
- Life Sciences
- Fortune 100
use_cases:
- description: Support pharmaceutical manufacturers in launching new drugs to market with distribution, patient support, and market access services.
  name: Drug Commercialization
- description: Enable independent, retail, and specialty pharmacies to efficiently source products and optimize business performance.
  name: Pharmacy Operations
- description: Supply hospitals and health systems with pharmaceutical products, specialty drugs, and biosimilars reliably and efficiently.
  name: Hospital and Health System Supply
- description: Specialized distribution and patient support programs for rare and orphan disease therapies requiring complex handling.
  name: Rare Disease and Orphan Drug Distribution
- description: Manage international pharmaceutical supply chains with local presence in 50+ countries and expertise in regulatory compliance.
  name: Global Pharmaceutical Logistics
- description: Streamline drug development processes and minimize risk by providing clinical trial supply chain and distribution support.
  name: Clinical Trial Supply
website: https://www.cencora.com
---
