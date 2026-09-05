---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Racq Bank Agentic Access
  operation_count: 19
  slug: racq-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 1
apis:
- baseURL: https://cdrbank.racq.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: RACQ Bank Banking Account Balances API
  slug: racq-bank-banking-account-balances-api
- baseURL: https://cdrbank.racq.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: RACQ Bank Banking Account Direct Debits API
  slug: racq-bank-banking-account-direct-debits-api
- baseURL: https://cdrbank.racq.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: RACQ Bank Banking Account Scheduled Payments API
  slug: racq-bank-banking-account-scheduled-payments-api
- baseURL: https://cdrbank.racq.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: RACQ Bank Banking Account Transactions API
  slug: racq-bank-banking-account-transactions-api
- baseURL: https://cdrbank.racq.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account endpoints
  name: RACQ Bank Banking Accounts API
  slug: racq-bank-banking-accounts-api
- baseURL: https://cdrbank.racq.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Payee endpoints
  name: RACQ Bank Banking Payees API
  slug: racq-bank-banking-payees-api
- baseURL: https://cdrbank.racq.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Product endpoints
  name: RACQ Bank Banking Products API
  slug: racq-bank-banking-products-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-racq-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-racq-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-racq-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-racq-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-racq-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-racq-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-racq-bank-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/racq-bank-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/racq-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/racq-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/racq-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/racq-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/racq-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/racq-bank-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/racq-bank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/racq-bank-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/racq-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/racq-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/racq-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.racq.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.racq.com.au/banking/open-banking/api-access
- group: start
  title: ''
  type: GettingStarted
  url: https://www.racq.com.au/banking/open-banking/api-access
- group: start
  title: ''
  type: Portal
  url: https://www.racq.com.au/banking/open-banking
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/racq/
- group: operate
  title: ''
  type: Support
  url: https://www.racq.com.au/banking/support-and-faqs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.racq.com.au/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.racq.com.au/legal
created: '2026-07-20'
description: RACQ Bank is the retail banking division of RACQ (The Royal Automobile Club of Queensland), a member-owned mutual organisation and one of Queensland's largest clubs, long known for roadside assistance, insurance, and banking for its members. The bank is an Australian authorised deposit-taking institution (ADI) regulated by APRA, offering transaction and savings accounts, term deposits, home loans, personal loans, and credit cards. Its banking arm traces to QT Mutual Bank, which merged with RACQ in 2016. As an active data holder under Australia's Consumer Data Right (CDR / Open Banking), RACQ Bank exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the DSB Consumer Data Standards, alongside the accredited-data-recipient consumer-data-sharing channels mandated of every Australian bank.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/racq-bank.png
layout: provider
modified: '2026-07-21T13:00:00Z'
name: RACQ Bank
nav: Providers
network: true
overview: 'RACQ Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  RACQ Bank''s developer surface includes authentication, documentation, getting-started guide, developer portal, support, and 16 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 39.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/racq-bank/refs/heads/main/screenshots/racq-bank-2026-07-21T114746.png
security:
- kind: authentication
  name: Racq Bank Authentication
  slug: racq-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 0 schemes
- kind: domain-security
  name: Racq Bank Domain Security
  slug: racq-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: racq-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
- Mutual
website: https://www.racq.com.au/
---
