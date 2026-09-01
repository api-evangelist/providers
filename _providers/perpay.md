---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: Internal REST API that powers checkout on the Perpay Marketplace. Handles product ordering, spending-limit enforcement, and installment plan creation for approved consumers. Access is limited to Perpa
  name: Perpay Marketplace Checkout API
  slug: perpay-marketplace-checkout-api
- description: REST integration layer built on Pinwheel's payroll connectivity API. Supports direct-deposit switching, income and employment verification, and real-time confirmation of paycheck routing updates for 1
  name: Perpay Payroll Direct-Deposit API
  slug: perpay-payroll-direct-deposit-api
- description: Internal API that submits on-time payment history and spending-limit data to Experian, TransUnion, and Equifax for credit-building purposes. Governed by FCRA requirements.
  name: Perpay Credit Reporting API
  slug: perpay-credit-reporting-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/perpay-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.perpay.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.perpay.com/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Perpay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/perpay
- group: commercial
  title: ''
  type: TermsOfService
  url: https://perpay.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://perpay.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/perpay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/perpay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/perpay-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.perpay.com/
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/perpay-context.jsonld
created: '2026-06-13'
description: Perpay is a buy-now-pay-later and credit-building platform that lets consumers shop and pay via automatic payroll deductions. Its internal REST platform supports marketplace checkout, installment plan creation, payroll direct-deposit switching (via Pinwheel), identity and income verification, and credit-bureau reporting to Experian, TransUnion, and Equifax. Perpay operates a closed marketplace — third-party merchant checkout integration is not publicly available; API access is reserved for Perpay's own products and vetted partners.
finops:
- name: Perpay Finops
  service_category: Fintech
  slug: perpay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/perpay.png
jsonld:
- class_count: 0
  name: Perpay Context
  property_count: 7
  slug: perpay-context
layout: provider
modified: '2026-06-13'
name: Perpay
nav: Providers
network: true
overview: 'Perpay publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, BNPL, Buy Now Pay Later, Credit Building, and Payroll Deduction.


  The Perpay catalog on APIs.io includes 1 JSON-LD context.


  Perpay''s developer surface includes GitHub presence, engineering blog, and 12 more developer resources.'
plans:
- name: Perpay Plans Pricing
  plan_count: 1
  slug: perpay-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Perpay Rate Limits
  slug: perpay-rate-limits
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 28.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 37.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/perpay/refs/heads/main/screenshots/perpay-2026-06-20T191609.png
security:
- kind: domain-security
  name: Perpay Domain Security
  slug: perpay-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Perpay Trust Center
  slug: perpay-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: perpay
tags:
- Fintech
- BNPL
- Buy Now Pay Later
- Credit Building
- Payroll Deduction
- Payments
- Consumer Finance
website: https://www.perpay.com
---
