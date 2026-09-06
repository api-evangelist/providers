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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'REST API for Cuenca''s banking-as-a-service platform in Mexico: SPEI / internal transfers, deposits, CLABE accounts, debit card issuing and card transactions, bill payments, balances, statements, webho'
  name: Cuenca API
  slug: cuenca-api
artifact_total: 4
asyncapis:
- description: ''
  name: Cuenca Webhooks
  slug: cuenca-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://cuenca.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cuenca-mx
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/cuenca-mx/cuenca-python
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/cuenca-mx/cuenca-python#readme
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/cuenca-mx/cuenca-python#authentication
- group: operate
  title: ''
  type: Support
  url: https://cuenca.com/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://cuenca.com/comisiones
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cuenca.com/contrato-adhesion
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cuenca.com/aviso-privacidad
- group: operate
  title: ''
  type: StatusPage
  url: https://cuenca.statuspage.io
- group: build
  title: ''
  type: Packages
  url: packages/cuenca-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cuenca-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cuenca-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cuenca-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cuenca-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cuenca-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/cuenca-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cuenca-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cuenca-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cuenca-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cuenca-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cuenca-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/cuenca-components.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cuenca-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cuenca-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cuenca-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cuenca-well-known.yml
created: '2026-07-17'
description: Cuenca is a Mexican fintech (challenger bank / neobank) founded in 2018 that offers a banking-as-a-service REST API for moving money in Mexico. The API at api.cuenca.com covers SPEI and internal transfers, deposits, CLABE account provisioning, debit card issuing (physical and virtual), card transactions, bill payments to service providers, balances, statements, commissions, and KYC / identity validation (CURP validation, identity verification, KYC checks). It authenticates with an API key plus secret (HTTP basic), optional short-lived JWTs, and login / session tokens, exposes a sandbox at sandbox.cuenca.com, signs transfers with an idempotency key, paginates with a cursor (next_page_uri), and pushes webhooks for transaction, card, deposit and user events. Official client libraries ship for Python (cuenca) and Java (CuencaJava), with open-source tooling for CLABE validation and CEP receipts under the cuenca-mx GitHub organization.
image: https://cuenca.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Cuenca
nav: Providers
network: true
overview: 'Cuenca publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Banking, and Neobank.


  The Cuenca catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cuenca''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, sandbox, and 21 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - mexico
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 40.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cuenca/refs/heads/main/screenshots/cuenca-2026-07-25T210910.png
security:
- kind: authentication
  name: Cuenca Authentication
  slug: cuenca-authentication
  summary_line: http-basic/jwt/session-token · 4 schemes
- kind: domain-security
  name: Cuenca Domain Security
  slug: cuenca-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cuenca
tags:
- Company
- Fintech
- Payments
- Banking
- Neobank
- SPEI
- Card Issuing
- Money Transfer
- Mexico
- KYC
website: https://cuenca.com
---
