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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: RESTful API for uploading and analyzing financial documents for fraud detection and data extraction. Supports bank statements, pay stubs, tax forms, invoices, and identity documents. Provides fraud si
  name: Inscribe Document Fraud Detection API
  slug: document-fraud-detection-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/inscribe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inscribe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.inscribe.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inscribe.ai/reference/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InscribeAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inscribeai/
- group: other
  title: ''
  type: X
  url: https://twitter.com/inscribeai
- group: company
  title: ''
  type: Blog
  url: https://www.inscribe.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.inscribe.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/inscribe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inscribe-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/inscribe-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/inscribe-context.jsonld
created: '2026-06-12'
description: Inscribe is an AI-powered document fraud detection platform founded in 2017, serving banks, credit unions, fintechs, and lending institutions. The platform uses agentic AI trained by fraud experts to detect forged, manipulated, and AI-generated documents including bank statements, pay stubs, tax forms, invoices, and identity documents. Inscribe's REST API provides programmatic access to fraud detection, document verification, credit insights, and transaction enrichment workflows at scale. Financial institutions integrate the API to automate underwriting, onboarding, KYC/KYB, and bank account verification decisions, with results delivered via webhook or polling. The platform processes millions of applications annually and serves notable customers including Bluevine, Ramp, Plaid, and BHG Financial.
finops:
- name: Inscribe Finops
  service_category: ''
  slug: inscribe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inscribe.png
jsonld:
- class_count: 9
  name: Inscribe Context
  property_count: 16
  slug: inscribe-context
layout: provider
modified: '2026-06-12'
name: Inscribe
nav: Providers
network: true
overview: 'Inscribe publishes 1 API on the [APIs.io](https://apis.io/) network: Document Fraud Detection API. Tagged areas include Fraud Detection, Document Verification, Financial-Services, KYC, and KYB.


  The Inscribe catalog on APIs.io includes 1 JSON-LD context.


  Inscribe''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Inscribe Plans Pricing
  plan_count: 0
  slug: inscribe-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Inscribe Rate Limits
  slug: inscribe-rate-limits
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 41.3
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 23.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/screenshots/inscribe-2026-06-20T183404.png
security:
- kind: domain-security
  name: Inscribe Domain Security
  slug: inscribe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Inscribe Vulnerability Disclosure
  slug: inscribe-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: inscribe
tags:
- Fraud Detection
- Document Verification
- Financial-Services
- KYC
- KYB
- Bank Statements
- Paystubs
- Identity Verification
- Risk Management
- Fintech
- Artificial Intelligence
- Machine-Learning
website: https://www.inscribe.ai/
---
