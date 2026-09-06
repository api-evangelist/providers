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
  - sandbox
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.reachware.com
  baseurl_source: declared
  description: Card save / tokenization flows
  name: Reachware Inc. Cards API
  slug: reachware-inc-cards-api
- baseURL: https://api.reachware.com
  baseurl_source: declared
  description: Request payments, retrieve payment details, and refunds
  name: Reachware Inc. Payments API
  slug: reachware-inc-payments-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Reach Pay Cards API
  slug: open-reachware-inc-cards-api
- collection_type: open
  name: Reach Pay Cards Payments API
  slug: open-reachware-inc-payments-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/reachware-inc-reachpay-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/reachware-inc-reachpay-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reachware-inc-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reachware-inc-domain-security.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/reachware-inc-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reachware-inc-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reachware-inc-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reachware-inc-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/reachware-inc-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reachware-inc-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/reachware-inc-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reachware-inc-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.reachware.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reachware.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.reachware.com/reference/reach-pay-checkout.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.reachware.com/docs/getting-started.md
- group: operate
  title: ''
  type: Support
  url: mailto:support@reachware.com
- group: start
  title: ''
  type: Login
  url: https://app.reachware.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reachware.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reachware.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://reachware.com
created: '2026-07-17'
description: Reachware is an Integration Platform as a Service (iPaaS) that lets separate SaaS and business systems operate as one connected ecosystem, with 200+ prebuilt connectors to systems like NetSuite, QuickBooks, Microsoft Dynamics 365, Odoo, SAP, Oracle, Magento, Zid and Qoyod. Alongside the core platform it ships Reach Pay (a payment API for Saudi Arabia payment gateways), Reachware Fatoora (ZATCA e-invoicing), and extension modules for banking, HR, inventory, loyalty and property management. Reach Pay exposes a hosted-redirect REST API for requesting payments, retrieving payment details, refunds and card tokenization. Reachware reports 3,500+ active subscriptions, 300+ customers, 100M+ transactions, and is CMMI Level 3 certified. It was surfaced as a portfolio company of 500 Global and profiled by the API Evangelist enrichment pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reachware-inc.png
layout: provider
modified: '2026-07-20'
name: Reachware Inc.
nav: Providers
network: true
overview: 'Reachware Inc. publishes 2 APIs on the [APIs.io](https://apis.io/) network: Cards API and Payments API. Tagged areas include Company, Payments, iPaaS, Integration, and Fintech.


  Reachware Inc.''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, and 16 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 18.2
    contract_quality: 55.8
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - saudi-arabia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 40.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 53.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reachware-inc/refs/heads/main/screenshots/reachware-inc-2026-08-17T081449.png
security:
- kind: authentication
  name: Reachware Inc Authentication
  slug: reachware-inc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Reachware Inc Domain Security
  slug: reachware-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reachware-inc
tags:
- Company
- Payments
- iPaaS
- Integration
- Fintech
- Payment Gateway
- Tokenization
- Saudi Arabia
website: https://reachware.com
---
