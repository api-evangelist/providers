---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: Symetra's Benefits Administration API enables HR platforms, benefits administrators, and technology partners to integrate with Symetra's group benefits products. The API supports automated data exchan
  name: Symetra Benefits Administration API
  slug: symetra-benefits-api
- description: API for accessing Symetra annuity product information, rates, and illustrations. Supports fixed deferred annuities, fixed indexed annuities, registered index-linked annuities (RILA), and income annuit
  name: Symetra Annuities API
  slug: symetra-annuities-api
- description: API supporting Symetra's life insurance products including term life, SwiftTerm (instant-issue life insurance), and permanent life insurance. Enables financial advisors and distribution partners to ac
  name: Symetra Life Insurance API
  slug: symetra-life-insurance-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/symetra-financial-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/symetra-financial-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/symetra
- group: company
  title: ''
  type: Website
  url: https://www.symetra.com
- group: start
  title: ''
  type: Login
  url: https://accounts.symetra.com/ui/login
- group: operate
  title: ''
  type: Contact
  url: https://www.symetra.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.symetra.com/privacy-policy/
- group: operate
  title: ''
  type: Help Center
  url: https://www.symetra.com/help-center/
- group: company
  title: ''
  type: Blog
  url: https://www.symetra.com/benefits-blog-posts/
- group: other
  title: ''
  type: Technology Solutions
  url: https://www.symetra.com/learn/articles-for-employers/technology-solutions/
- group: other
  title: ''
  type: For Employers
  url: https://www.symetra.com/for-employers/
- group: other
  title: ''
  type: For Brokers
  url: https://www.symetra.com/for-brokers/
created: '2026-05-03'
description: Symetra Financial Corporation is a diversified financial services company headquartered in Bellevue, Washington, providing employee benefits, annuities, and life insurance products to individuals, families, and businesses through independent advisors and financial institutions. A subsidiary of Sumitomo Life Insurance Company since 2016, Symetra offers medical stop-loss insurance, group life and disability income protection, supplemental health coverage, fixed and indexed annuities, registered index-linked annuities, income annuities, term life, and permanent life insurance. The company offers API and EDI-based data integrations for benefits administrators and HR platforms.
finops:
- name: Symetra Financial Finops
  service_category: Insurance / Financial Services
  slug: symetra-financial-finops
image: https://www.symetra.com/favicon.ico
jsonld:
- class_count: 3
  name: Symetra Financial Context
  property_count: 37
  slug: symetra-financial-context
layout: provider
modified: '2026-05-03'
name: Symetra Financial
nav: Providers
network: true
overview: 'Symetra Financial publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Annuities, Benefits, Employee Benefits, Financial-Services, and Insurance.


  The Symetra Financial catalog on APIs.io includes 1 JSON-LD context.


  Symetra Financial''s developer surface includes engineering blog and 11 more developer resources.'
plans:
- name: Symetra Financial Plans Pricing
  plan_count: 1
  slug: symetra-financial-plans-pricing
press:
- date: '2026-05-25'
  title: Symetra Introduces New Supplemental Health Claims ...
  url: https://www.nayya.com/blog/Symetra-And-Nayya-Claims
- date: '2026-05-25'
  title: 'Research Update: Symetra Financial Corp. ''BBB'' Rating ...'
  url: https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/13057843
- date: '2026-05-25'
  title: Symetra Names Jeff Sealey Vice President, Stop Loss ...
  url: https://natlawreview.com/press-releases/symetra-names-jeff-sealey-vice-president-stop-loss-captives
- date: '2026-05-25'
  title: Premera and Symetra Collaborate to Offer Added Benefits ...
  url: https://www.prnewswire.com/news-releases/premera-and-symetra-collaborate-to-offer-added-benefits-and-value-for-employers-and-members-275174940.html
- date: '2026-05-25'
  title: Sumitomo Life to Acquire Symetra for $3.76 Billion - Best's News
  url: https://news.ambest.com/newscontent.aspx?refnum=185237&altsrc=114&SrvId=156
random_paper: 8
rate_limits:
- limit_count: 1
  name: Symetra Financial Rate Limits
  slug: symetra-financial-rate-limits
score:
  band: emerging
  composite: 22.2
  delta: 1.9
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 20.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Symetra Financial Domain Security
  slug: symetra-financial-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Symetra Financial Trust Center
  slug: symetra-financial-trust-center
  summary_line: ISO 27001
slug: symetra-financial
tags:
- Annuities
- Benefits
- Employee Benefits
- Financial-Services
- Insurance
- Life Insurance
- Stop Loss
- Fortune 1000
website: https://www.symetra.com
---
