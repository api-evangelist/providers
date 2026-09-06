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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
    well_known_catalog: true
  schema_version: 0.2
  score: 11.9
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: AmerisourceBergen (now Cencora) is one of the largest global pharmaceutical distributors, serving pharmaceutical manufacturers, healthcare providers, and patients worldwide. The company does not curre
  name: AmerisourceBergen Website
  slug: website
- description: Cencora operates an SAP API Business Hub Enterprise developer portal at api.cencora.com — DNS resolves to ab-cloud-foundry-prd.apibhubenterprise.cfapps.us21.hana.ondemand.com, and every request, on ev
  name: Cencora API Developer Portal
  slug: developer-portal
artifact_total: 26
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amerisourcebergen-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amerisourcebergen-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/amerisourcebergen-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/amerisourcebergen-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amerisourcebergen-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amerisourcebergen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cencora.com/responsible-disclosure
- group: start
  title: ''
  type: Portal
  url: https://api.cencora.com
- group: company
  title: ''
  type: Website
  url: https://www.cencora.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cencora.com/global-privacy-statement-overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cencora.com/global-terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.cencora.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cencoraglobal/
- group: other
  title: ''
  type: X
  url: https://x.com/CencoraGlobal
coverage:
  checked: '2026-09-02'
  detail: Cencora runs a real SAP API Business Hub Enterprise developer portal at api.cencora.com, but every path on that host — including /openapi.json, /.well-known/* and a control path that cannot exist — returns the same 858-byte HTML shim redirecting to SAP XSUAA OAuth (client_id sb-dev-portal-xsuaa!b33), so no catalogue, reference or contract is readable without portal credentials Cencora publishes no way to request.
  evidence:
  - status: 200
    url: https://api.cencora.com/
  - status: 200
    url: https://api.cencora.com/openapi.json
  - status: 403
    url: https://developer.cencora.com/
  - status: 200
    url: https://www.cencora.com/llms.txt
  reason: partner-login
  state: gated
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
modified: '2026-09-02'
name: AmerisourceBergen
nav: Providers
network: true
overview: 'AmerisourceBergen publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmaceutical Distribution, Healthcare, Drug Distribution, Manufacturer Solutions, and Provider Solutions.


  AmerisourceBergen''s developer surface includes authentication, developer portal, support, and 11 more developer resources.'
plans:
- name: Amerisourcebergen Plans Pricing
  plan_count: 0
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
random_paper: 4
rate_limits:
- limit_count: 0
  name: Amerisourcebergen Rate Limits
  slug: amerisourcebergen-rate-limits
scopes:
- name: Amerisourcebergen Scopes
  scope_count: 6
  slug: amerisourcebergen-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 21.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 60.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/amerisourcebergen/refs/heads/main/screenshots/amerisourcebergen-2026-06-20T171929.png
security:
- kind: authentication
  name: Amerisourcebergen Authentication
  slug: amerisourcebergen-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Amerisourcebergen Domain Security
  slug: amerisourcebergen-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amerisourcebergen Vulnerability Disclosure
  slug: amerisourcebergen-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
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
