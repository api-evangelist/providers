---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-09-01'
api_count: 6
apis:
- description: Global Apex service classes for automating revenue recognition to ASC 606 and IFRS 15. RevenueContractService creates and updates revenue contracts, generates performance obligations, allocates revenu
  name: Certinia Revenue Management API
  slug: certinia-revenue-management-api
- description: 'Global Apex service classes for subscription and usage billing. BillingService, BillingDocumentsService, BillingSchedulesService, and ContractsService generate billing documents and schedules, manage '
  name: Certinia Billing Central API
  slug: certinia-billing-central-api
- description: Domain-oriented Apex service classes for Professional Services Automation - projects, resource requests and assignments, milestones, timecards, expenses, and billing events. Runs against PSA managed-p
  name: Certinia Professional Services Automation (PSA) API
  slug: certinia-psa-api
- description: Certinia Accounting Apex API (namespace prefix CODAAPI) for core financials - sales and purchase invoices, credit notes, journals, cash entries, and general-ledger transactions - against the Accountin
  name: Certinia Accounting (ERP) API
  slug: certinia-accounting-api
- description: Certinia Supply Chain Management Apex API (FFAAPI) for inventory, sales and purchase orders, and fulfillment against SCM managed-package objects. Invoked as Apex within a Salesforce org; endpoints mod
  name: Certinia Supply Chain Management (SCM) API
  slug: certinia-scm-api
- description: Certinia Services CPQ Apex API for configuring, pricing, and quoting services engagements and estimates that feed PSA projects. Invoked as Apex within a Salesforce org against Services CPQ managed-pac
  name: Certinia Services CPQ API
  slug: certinia-services-cpq-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/certinia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/certinia-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/certinia
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/certinia
- group: company
  title: ''
  type: Website
  url: https://www.certinia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.certinia.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/certinia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/certinia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/certinia-finops.yml
created: '2026-07-11'
description: Certinia (formerly FinancialForce) is a Salesforce-native ERP, Professional Services Automation (PSA), and revenue-management suite delivered as managed packages that run inside a customer's Salesforce org. Its programmatic surface is not a standalone public REST product; it is a set of global Apex service classes (and legacy SOAP APIs) - Revenue Management, Billing Central, PSA, Accounting/ERP, Supply Chain, and Services CPQ - invoked on the Salesforce platform against Certinia managed-package objects. Certinia automates revenue recognition to ASC 606 and IFRS 15, subscription billing, project and resource management, and accounting. Access is gated - it requires a provisioned Salesforce org with the relevant Certinia managed package installed and the appropriate permission set or profile assigned. The endpoints documented here are modeled from Certinia's public Apex API developer references; they are not called against a public, unauthenticated HTTP base URL.
finops:
- name: Certinia Finops
  service_category: ERP and Professional Services Automation
  slug: certinia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/certinia.png
layout: provider
modified: '2026-07-11'
name: Certinia
nav: Providers
network: true
overview: 'Certinia publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Revenue Recognition, ASC 606, ERP, Professional Services Automation, and PSA.


  Certinia''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Certinia Plans Pricing
  plan_count: 5
  slug: certinia-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Certinia Rate Limits
  slug: certinia-rate-limits
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 22.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/certinia/refs/heads/main/screenshots/certinia-2026-07-25T205017.png
security:
- kind: authentication
  name: Certinia Authentication
  slug: certinia-authentication
  summary_line: oauth2/session · 3 schemes
- kind: domain-security
  name: Certinia Domain Security
  slug: certinia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: certinia
tags:
- Revenue Recognition
- ASC 606
- ERP
- Professional Services Automation
- PSA
- Billing
- Accounting
- Salesforce
- FinancialForce
- Finance
website: https://www.certinia.com/
---
