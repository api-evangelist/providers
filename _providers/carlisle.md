---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Carlisle Construction Materials and Carlisle's other operating segments exchange purchase orders, acknowledgments, advance ship notices, and invoices with distributors, retailers, and large contractor
  name: Carlisle EDI Trading Partner Integration
  slug: edi-trading-partner
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carlisle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carlisle.com/
- group: other
  title: ''
  type: Businesses
  url: https://www.carlisle.com/our-businesses/default.aspx
- group: other
  title: ''
  type: Construction Materials
  url: https://www.carlisleconstructionmaterials.com/
- group: other
  title: ''
  type: SynTec Systems
  url: https://www.carlislesyntec.com/
- group: company
  title: ''
  type: Investor Relations
  url: https://ir.carlisle.com/
- group: company
  title: ''
  type: Careers
  url: https://careers.carlisle.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.carlisle.com/contact-us/default.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carlisle.com/privacy-policy/default.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carlisle.com/terms-of-use/default.aspx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carlisle-companies-incorporated/
- group: other
  title: ''
  type: ProductPage
  url: https://customersuccesslogin.com
created: '2026-03-23'
description: 'Carlisle Companies Incorporated (NYSE: CSL) is a global diversified manufacturer of highly engineered building envelope products and solutions, serving commercial and residential construction, insulation, roofing, waterproofing, and specialty markets. Carlisle''s primary operating segment is Carlisle Construction Materials (CCM), which includes brands such as Carlisle SynTec Systems, Hunter Panels, Henry Company, MB Technology, and WIP Industrial. Carlisle does not publish a public developer API; distributors and direct contractors transact through the Carlisle Customer Success Portal, and commercial trading partners integrate with Carlisle using standard X12 EDI transactions (850, 855, 856, 810) over AS2/SFTP.'
finops:
- name: Carlisle Finops
  service_category: API
  slug: carlisle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carlisle.png
layout: provider
modified: '2026-07-25'
name: Carlisle Companies
nav: Providers
network: true
overview: Carlisle Companies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Building Envelope, Building Products, Construction, Contractor Portal, and Distributors.
plans:
- name: Carlisle Plans Pricing
  plan_count: 3
  slug: carlisle-plans-pricing
press:
- date: '2026-05-25'
  title: Pennsylvania Data Center Partners and PowerHouse ...
  url: https://www.americanrepartners.com/news/pennsylvania-data-center-partners-and-powerhouse-data-centers-launch-joint-venture-to-build-next-gen-1-35-gw-hyperscale-data-center-campus-in-carlisle-pennsylvania
- date: '2026-05-25'
  title: Nvidia and Microsoft Back AI for Genomic Data | Mike Carlisle ...
  url: https://www.linkedin.com/posts/carlislemike_ai-artificialintelligence-intelligence-activity-7416615564543983616-RM2I
- date: '2026-05-25'
  title: Our Stories
  url: https://www.carlisle.com/our-stories/our-stories-archive/our-stories/2025/Carlisle-Companies-is-helping-bridge-the-gap-between-energy-capacity-and-growing-energy-demand-in-the-U-S-/default.aspx
- date: '2026-05-25'
  title: Artificial Intelligence Task Force (AITF) 90 Day Update
  url: https://www.dhs.gov/sites/default/files/2024-05/24_02_14_sec_signed_ai_task_force_memo_508.pdf.pdf
- date: '2026-05-25'
  title: Ducker Carlisle Adds Data and AI Services to Help Clients ...
  url: https://www.prnewswire.com/news-releases/ducker-carlisle-adds-data-and-ai-services-to-help-clients-accelerate-growth-302309287.html
random_paper: 7
rate_limits:
- limit_count: 5
  name: Carlisle Rate Limits
  slug: carlisle-rate-limits
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 10.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carlisle/refs/heads/main/screenshots/carlisle-2026-07-25T204623.png
security:
- kind: domain-security
  name: Carlisle Domain Security
  slug: carlisle-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: carlisle
tags:
- Building Envelope
- Building Products
- Construction
- Contractor Portal
- Distributors
- EDI
- Insulation
- Manufacturing
- Roofing
- Waterproofing
- Fortune 1000
website: https://www.carlisle.com/
---
