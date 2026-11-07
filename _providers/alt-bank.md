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
  - '{''url'': ''https://altbank.ai/en/'', ''status'': 301, ''note'': ''declared website redirects to https://www.novutech.com.br/ — a different registrable domain (altbank.ai -> novutech.com.br), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Real-time consumer credit underwriting / risk-assessment API. Partners POST an underwriting request for a credit-card applicant and receive a Guard Score, risk band and credit-limit decision. The call
  name: GUARD API
  slug: guard-api
- description: Credit-card module integration API (private, partner B2B) for issuing and managing alt.bank white-label credit cards.
  name: CC Integration API
  slug: cc-integration-api
- description: Identity verification / KYC SDK and API for onboarding and verifying applicants as part of the alt.bank credit and card flows.
  name: SDK KYC API
  slug: sdk-kyc-api
- baseURL: https://guard.altbank.ai
  baseurl_source: declared
  description: Credit underwriting and risk scoring for partner card issuance.
  name: Alt Bank Underwriting API
  slug: alt-bank-underwriting-api
artifact_total: 10
asyncapis:
- description: ''
  name: Alt Bank Guard Webhooks
  slug: alt-bank-guard-webhooks
collections:
- collection_type: open
  name: alt.bank GUARD Underwriting API
  slug: open-alt-bank-underwriting-api
common:
- group: other
  href: https://artifacts.apis.io/alt-bank/capabilities/alt-bank-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/alt-bank-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/alt-bank/security/alt-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alt-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altbank.ai/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.altbank.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developers.altbank.ai/docs/guard-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.altbank.ai/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.altbank.ai/docs/guard
- group: operate
  title: ''
  type: Support
  url: https://altbank.ai/en/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alt-bank
- group: auth
  href: https://artifacts.apis.io/alt-bank/authentication/alt-bank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alt-bank-authentication.yml
- group: design
  href: https://artifacts.apis.io/alt-bank/conventions/alt-bank-conventions.yml
  title: ''
  type: Conventions
  url: conventions/alt-bank-conventions.yml
- group: start
  href: https://artifacts.apis.io/alt-bank/sandbox/alt-bank-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/alt-bank-sandbox.yml
- group: design
  href: https://artifacts.apis.io/alt-bank/asyncapi/alt-bank-guard-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/alt-bank-guard-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/alt-bank/mcp/alt-bank-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/alt-bank-mcp.yml
- group: agent
  href: https://artifacts.apis.io/alt-bank/llms/alt-bank-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alt-bank-llms.txt
- group: agent
  href: https://artifacts.apis.io/alt-bank/well-known/alt-bank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alt-bank-well-known.yml
- group: agent
  href: https://artifacts.apis.io/alt-bank/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: alt.bank (Alt Bank) is a Brazilian fintech providing a fully integrated, turnkey credit-card and consumer-credit platform for partners who want to launch prepaid and postpaid cards without becoming a financial institution. Its flagship product, GUARD, is a machine-learning underwriting / credit-risk engine ("Brazil's most accurate credit model") that returns a Guard Score, risk band and credit-limit decision through a real-time partner API. The platform also bundles white-label credit cards (novücard), Visa BIN sponsorship, KYC, anti-fraud, dispute management and Pix/boleto payment processing. Partners integrate over a documented HTTPS API secured with a per-partner X-Partner-Auth token plus IP allow-listing, with a mirrored staging sandbox and asynchronous callback delivery of underwriting results. Backed by Anthemis, Union Square Ventures, Repeat Ventures and SquareOne Capital, alt.bank targets financial inclusion for underbanked consumers.
image: https://altbank.ai/wp-content/uploads/2020/08/cropped-alt.bank-logo-square-300x300.png
layout: provider
modified: '2026-08-08'
name: Alt Bank
nav: Providers
network: true
overview: 'Alt Bank publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Underwriting API, and 3 more. Tagged areas include Company, Fintech, Banking, Credit, and Underwriting.


  The Alt Bank catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Alt Bank''s developer surface includes documentation, getting-started guide, API reference, support, authentication, sandbox, and 11 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Alt Bank API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: alt-bank-rules
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 57.6
    developer_ergonomics: 18.5
    discoverability: 64.3
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 25.2
  provenance:
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
    score: 10.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/alt-bank/alt-bank-2026-07-25T195815.png
security:
- kind: authentication
  name: Alt Bank Authentication
  slug: alt-bank-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Alt Bank Domain Security
  slug: alt-bank-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: Submit a GUARD credit-card underwriting
  slug: alt-bank-submit-underwriting
slug: alt-bank
tags:
- Company
- Fintech
- Banking
- Credit
- Underwriting
- Credit Cards
- Payments
- KYC
- Risk Management
- Brazil
- Financial Inclusion
- Banking as a Service
website: https://altbank.ai/en/
---
