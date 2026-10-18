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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
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
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hebbia/refs/heads/main/plans/hebbia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hebbia-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hebbia/refs/heads/main/rate-limits/hebbia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hebbia-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hebbia/refs/heads/main/finops/hebbia-finops.yml
  title: ''
  type: FinOps
  url: finops/hebbia-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hebbia/refs/heads/main/security/hebbia-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hebbia-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hebbia/refs/heads/main/security/hebbia-domain-security.yml
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
- has_sources: false
  method: generated
  name: Hebbia Finops
  primary_unit: ''
  service_category: API
  slug: hebbia-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hebbia.png
layout: provider
modified: '2026-05-23'
name: Hebbia
nav: Providers
network: true
overview: 'Hebbia is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Document AI, Due Diligence, Enterprise Search, and Financial Services.


  Hebbia''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Hebbia Plans Pricing
  plan_count: 1
  slug: hebbia-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Hebbia Rate Limits
  slug: hebbia-rate-limits
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 19.8
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 13.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- Financial Services
- Generative AI
- Investment Research
- Knowledge
- Matrix
- RAG
- Research
- Unstructured Data
website: https://www.hebbia.com/
---
