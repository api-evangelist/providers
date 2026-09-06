---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://developer.cashflo.io
  baseurl_source: declared
  description: The Ingest API from CashFlo — 3 operation(s) for ingest.
  name: CashFlo Ingest API
  slug: cashflo-ingest-api
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cashflo Data Ingestion API Documentation Ingest API
  slug: open-cashflo-ingest-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/cashflo-ingest-grns.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cashflo-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cashflo-data-ingestion-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cashflo.io
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cashflo.io
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cashflo.io
- group: auth
  title: ''
  type: Authentication
  url: authentication/cashflo-authentication.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cashflo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cashflo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cashflo-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cashflo-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cashflo-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cashflo.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cashflo
- group: company
  title: ''
  type: Blog
  url: https://www.cashflo.io/magazine
- group: start
  title: ''
  type: Login
  url: https://app.cashflo.io/#/account/login
- group: operate
  title: ''
  type: Support
  url: https://www.cashflo.io/talk-to-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cashflo.io/tnc/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cashflo.io/tnc/privacy-policy
created: '2026-07-17'
description: CashFlo is an India-based fintech platform that automates enterprise finance operations across accounts payable, payments, GST compliance, vendor management, and supply-chain financing. Its modules cover invoice OCR and n-way matching, approval workflows, multi-bank payments and reconciliation, GST filing / e-invoicing / e-way bills, vendor onboarding and KYC, and dynamic cash discounting for working-capital optimization. CashFlo connects to major ERPs (SAP ECC/S4 HANA/Business One, Oracle NetSuite/Fusion/EBS, Microsoft Dynamics 365/NAV/Business Central) and exposes a JWT-secured Data Ingestion API for pushing purchase orders and goods-receipt notes into the platform. Backed by General Catalyst.
image: https://cdn.prod.website-files.com/649d312d8aeae2926e7af2fe/674acdb7d5b408c0e8e9cf34_Homepage.webp
layout: provider
modified: '2026-07-18'
name: CashFlo
nav: Providers
network: true
overview: 'CashFlo publishes 1 API on the [APIs.io](https://apis.io/) network: Ingest API. Tagged areas include Company, Fintech, Accounts Payable, Payments, and Working Capital.


  CashFlo''s developer surface includes documentation, API reference, authentication, engineering blog, support, and 14 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 54.2
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 40.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cashflo/refs/heads/main/screenshots/cashflo-2026-07-25T204721.png
security:
- kind: authentication
  name: Cashflo Authentication
  slug: cashflo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cashflo Domain Security
  slug: cashflo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cashflo
tags:
- Company
- Fintech
- Accounts Payable
- Payments
- Working Capital
- Supply Chain Finance
- ERP Integration
- Compliance
- India
website: https://developer.cashflo.io
---
