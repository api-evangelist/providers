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
api_count: 2
apis:
- description: 'Matrix is Hebbia''s flagship AI workspace for reasoning across unstructured enterprise documents at scale. It runs spreadsheet-style queries (rows and columns) over very large document sets to extract '
  name: Hebbia Matrix
  slug: hebbia-matrix
- description: Hebbia connects to enterprise content stores and financial data providers to make their contents searchable and reasoning-ready inside Matrix. Connectors include enterprise data systems (Snowflake, AW
  name: Hebbia Connectors
  slug: hebbia-connectors
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/hebbia-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hebbia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hebbia.com/
- group: company
  title: ''
  type: Blog
  url: https://www.hebbia.com/blog
- group: operate
  title: ''
  type: Community
  url: https://forum.hebbia.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hebbia/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hebbia.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hebbia.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.hebbia.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.hebbia.com/careers
created: '2026-05-23'
description: Hebbia provides institutional-grade AI for finance and high-stakes enterprise work, centered on its Matrix product that reasons across massive volumes of unstructured documents. The platform connects to enterprise data sources such as Snowflake, AWS S3, SharePoint, Box, Dropbox, and Egnyte, and financial data providers including FactSet, S&P Capital IQ, PitchBook, Guidepoint, and Thirdbridge. Hebbia is a sales-led enterprise product without a fully public developer portal; API and integration access is granted to customers through their account team.
finops:
- name: Hebbia Finops
  service_category: API
  slug: hebbia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hebbia.png
layout: provider
modified: '2026-05-23'
name: Hebbia
nav: Providers
network: true
overview: 'Hebbia publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Document AI, Due Diligence, Enterprise Search, and Financial-Services.


  Hebbia''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Hebbia Plans Pricing
  plan_count: 1
  slug: hebbia-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Hebbia Rate Limits
  slug: hebbia-rate-limits
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hebbia/refs/heads/main/screenshots/hebbia-2026-06-20T182608.png
security:
- kind: domain-security
  name: Hebbia Domain Security
  slug: hebbia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hebbia Trust Center
  slug: hebbia-trust-center
  summary_line: SOC 2, GDPR
slug: hebbia
tags:
- Artificial Intelligence
- Document AI
- Due Diligence
- Enterprise Search
- Financial-Services
- Generative AI
- Investment Research
- Knowledge
- Matrix
- RAG
- Research
- Unstructured Data
website: https://www.hebbia.com/
---
