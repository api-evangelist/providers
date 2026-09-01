---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Regions Financial Agentic Access
  operation_count: 8
  slug: regions-financial-agentic-access
  summary_line: 8 operations · 2 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Consumer and business account balances and details
  name: regions-financial Account Information API
  slug: regions-financial-account-information-api
- description: Customer consent management for data sharing
  name: regions-financial Consent API
  slug: regions-financial-consent-api
- description: Customer profile and identity
  name: regions-financial Customer API
  slug: regions-financial-customer-api
- description: Payment initiation and status
  name: regions-financial Payments API
  slug: regions-financial-payments-api
- description: Account transaction history
  name: regions-financial Transactions API
  slug: regions-financial-transactions-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Regions Open Banking Account Information API
  slug: open-regions-financial-account-information-api
- collection_type: open
  name: Regions Open Banking Account Information Consent API
  slug: open-regions-financial-consent-api
- collection_type: open
  name: Regions Open Banking Account Information Customer API
  slug: open-regions-financial-customer-api
- collection_type: open
  name: Regions Open Banking Account Information Payments API
  slug: open-regions-financial-payments-api
- collection_type: open
  name: Regions Open Banking Account Information Transactions API
  slug: open-regions-financial-transactions-api
- collection_type: open
  name: Regions Open Banking API
  slug: open-regions-open-banking
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/regions-financial-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/regions-financial-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/regions-financial-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/regions-financial-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/regions-financial-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.regions.com
- group: company
  title: ''
  type: Website
  url: https://www.regions.com/personal-banking
- group: company
  title: ''
  type: Website
  url: https://www.regions.com/commercial-banking
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/regions-financial-corporation
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/regions-financial/refs/heads/main/openapi/regions-open-banking-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/regions-financial/refs/heads/main/vocabulary/regions-financial-vocabulary.yml
description: Regions Financial Corporation is a member of the S&P 500 Index and one of the nation's largest full-service providers of consumer and commercial banking, wealth management, and mortgage products and services. Regions Bank is implementing open banking capabilities through a partnership with Axway's Amplify Open Banking solution, building APIs aligned to the Financial Data Exchange (FDX) standard to enable secure financial data sharing with fintech partners and third-party platforms. Regions joined FDX in 2021 and is targeting compliance with CFPB open banking rules by April 2027.
examples:
- key_count: 2
  name: Regions List Accounts Example
  slug: regions-list-accounts-example
- key_count: 2
  name: Regions List Transactions Example
  slug: regions-list-transactions-example
finops:
- name: Regions Financial Finops
  service_category: Banking
  slug: regions-financial-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/regions-financial.png
json_schemas:
- name: Account
  property_count: 8
  slug: regions-account
- name: Transaction
  property_count: 12
  slug: regions-transaction
json_structures:
- name: Regions Account Structure
  property_count: 0
  slug: regions-account-structure
- name: Regions Transaction Structure
  property_count: 0
  slug: regions-transaction-structure
jsonld:
- class_count: 32
  name: Regions Financial Context
  property_count: 2
  slug: regions-financial-context
layout: provider
modified: '2026-05-19'
name: Regions Financial Corporation
nav: Providers
network: true
overview: 'Regions Financial Corporation publishes 5 APIs on the [APIs.io](https://apis.io/) network, including regions-financial Account Information API, regions-financial Consent API, regions-financial Customer API, and 2 more. Tagged areas include Banking, Financial-Services, Open Banking, FDX, and Consumer Banking.


  The Regions Financial Corporation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Regions Financial Corporation''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Regions Financial Plans Pricing
  plan_count: 1
  slug: regions-financial-plans-pricing
press:
- date: '2026-05-25'
  title: Regions Says AI Lifts Productivity 20% as Loan Growth Cools
  url: https://www.pymnts.com/earnings/2026/regions-says-ai-lifts-productivity-20percent-loan-growth-cools/
- date: '2026-05-25'
  title: Regions Bank Taps IBM's AI to Power Next Generation ...
  url: https://www.prnewswire.com/news-releases/regions-bank-taps-ibms-ai-to-power-next-generation-customer-service-300837762.html
- date: '2026-05-25'
  title: Regions Bank and CRE FinTech Blooma Collaborate to ...
  url: https://ir.regions.com/news-events/press-releases/news-details/2023/Regions-Bank-and-CRE-FinTech-Blooma-Collaborate-to-Modernize-Lending-Workflow-02-15-2023/default.aspx
- date: '2026-05-25'
  title: 'Generative Artificial Intelligence: The Next Disruptive ...'
  url: https://www.regions.com/-/media/pdfs/wealth-management/Generative-Artificial-Intelligence-6923V5.pdf?revision=3dff6e95-3e98-4aeb-b8be-0e7c3d4790d5
- date: '2026-05-25'
  title: Regions AI tool helps steer cross-selling
  url: https://www.americanbanker.com/news/regions-ai-tool-helps-steer-cross-selling
random_paper: 15
rate_limits:
- limit_count: 1
  name: Regions Financial Rate Limits
  slug: regions-financial-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Regions Financial Corporation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: regions-financial-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Regions Financial Corporation API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: regions-financial-rules
scopes:
- name: Regions Financial Scopes
  scope_count: 4
  slug: regions-financial-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 56.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 57.8
    developer_ergonomics: 11.9
    discoverability: 63.0
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 48.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Regions Financial Authentication
  slug: regions-financial-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Regions Financial Domain Security
  slug: regions-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: regions-financial
tags:
- Banking
- Financial-Services
- Open Banking
- FDX
- Consumer Banking
- Wealth Management
- Fortune 500
website: https://www.regions.com
---
