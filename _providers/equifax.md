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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'The Equifax API platform provides programmatic access to Equifax''s consumer credit information, including credit reports, credit scores, identity verification, and fraud detection. APIs are organized '
  name: Equifax API
  slug: equifax
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/equifax-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Equifax-Public
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/equifax
- group: company
  title: ''
  type: Website
  url: https://www.equifax.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.equifax.com/
- group: company
  title: ''
  type: Blog
  url: https://www.equifax.com/newsroom/
created: '2025-02-24'
description: Equifax is a consumer credit reporting agency that collects and aggregates information on individuals' credit history, including borrowing and repayment habits. This information is used by lenders and creditors to assess creditworthiness and make decisions about extending credit. Equifax also offers identity theft protection, credit monitoring, and fraud detection services, plus analytics and consulting offerings to help businesses manage risk.
finops:
- name: Equifax Finops
  service_category: Credit Bureau / Identity Data
  slug: equifax-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/equifax.png
layout: provider
modified: '2026-04-28'
name: Equifax
nav: Providers
network: true
overview: 'Equifax publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Credit, Credit History, Credit Reporting, Identity, and Fraud Detection.


  Equifax''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Equifax Plans Pricing
  plan_count: 4
  slug: equifax-plans-pricing
press:
- date: '2026-05-25'
  title: Driving AI Innovation | Equifax
  url: https://www.equifax.com/about-equifax/ai/
- date: '2026-05-25'
  title: Explainability and Artificial Intelligence
  url: https://www.equifax.com/newsroom/all-news/-/story/explainability-and-artificial-intelligence/
- date: '2026-05-25'
  title: Equifax Secures 27 New Patents in the Second Half of 2025
  url: https://investor.equifax.com/news-events/press-releases/detail/1384/equifax-secures-27-new-patents-in-the-second-half-of-2025
- date: '2026-05-25'
  title: Newsroom
  url: https://www.equifax.com/newsroom/
- date: '2026-05-25'
  title: Equifax Releases 2025 Security Annual Report
  url: https://www.prnewswire.com/news-releases/equifax-releases-2025-security-annual-report-302716637.html
random_paper: 20
rate_limits:
- limit_count: 2
  name: Equifax Rate Limits
  slug: equifax-rate-limits
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/equifax/refs/heads/main/screenshots/equifax-2026-06-20T180803.png
security:
- kind: domain-security
  name: Equifax Domain Security
  slug: equifax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: equifax
tags:
- Credit
- Credit History
- Credit Reporting
- Identity
- Fraud Detection
- Fortune 1000
website: https://www.equifax.com/
---
