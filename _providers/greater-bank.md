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
  name: Greater Bank Agentic Access
  operation_count: 19
  slug: greater-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 1
apis:
- baseURL: https://public.cdr.greater.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: Greater Bank Banking Account Balances API
  slug: greater-bank-banking-account-balances-api
- baseURL: https://public.cdr.greater.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: Greater Bank Banking Account Direct Debits API
  slug: greater-bank-banking-account-direct-debits-api
- baseURL: https://public.cdr.greater.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: Greater Bank Banking Account Scheduled Payments API
  slug: greater-bank-banking-account-scheduled-payments-api
- baseURL: https://public.cdr.greater.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: Greater Bank Banking Account Transactions API
  slug: greater-bank-banking-account-transactions-api
- baseURL: https://public.cdr.greater.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account endpoints
  name: Greater Bank Banking Accounts API
  slug: greater-bank-banking-accounts-api
- baseURL: https://public.cdr.greater.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Payee endpoints
  name: Greater Bank Banking Payees API
  slug: greater-bank-banking-payees-api
- baseURL: https://public.cdr.greater.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Product endpoints
  name: Greater Bank Banking Products API
  slug: greater-bank-banking-products-api
arazzos:
- description: List Greater Bank's public CDR Product Reference Data (PRD) offerings, then retrieve the full detail for one product. Runs unauthenticated against the live public CDS host (no consumer consent / ADR h
  name: Greater Bank product lookup
  slug: greater-bank-product-lookup
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-greater-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-greater-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-greater-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-greater-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-greater-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-greater-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-greater-bank-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/greater-bank-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/greater-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/greater-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/greater-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/greater-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/greater-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/greater-bank-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://public.cdr.greater.com.au/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: Conformance
  url: conformance/greater-bank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/greater-bank-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/greater-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/greater-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/greater-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/greater-bank-product-lookup.yml
- group: company
  title: ''
  type: Website
  url: https://www.greater.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.greater.com.au/openbanking
- group: start
  title: ''
  type: GettingStarted
  url: https://www.greater.com.au/openbanking
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.greater.com.au/privacy-policy
- group: other
  title: ''
  type: CDRPolicy
  url: https://www.greater.com.au/globalassets/open-banking/cdr-policy/cdr-policy.pdf
- group: operate
  title: ''
  type: Support
  url: https://www.greater.com.au/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.greater.com.au/termsandconditions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/greater-bank
created: '2026-07-20'
description: Greater Bank is a customer-owned Australian retail bank headquartered in Newcastle, New South Wales, offering everyday transaction and savings accounts, term deposits, home loans, personal loans, and credit cards to personal and business customers. In March 2023 Greater Bank merged with Newcastle Permanent to form Newcastle Greater Mutual Group (NGM Group), one of Australia's largest customer-owned mutual banking organisations, while continuing to trade under the Greater Bank brand. As an Authorised Deposit-taking Institution (ADI) it is a designated data holder under Australia's Consumer Data Right (CDR / Open Banking) and exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body (DSB) Consumer Data Standards. Consumer-data sharing beyond PRD runs on the accredited CDR data-recipient (ADR) model with OAuth2/OpenID Connect FAPI-profile security.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/greater-bank.png
layout: provider
modified: '2026-07-22'
name: Greater Bank
nav: Providers
network: true
overview: 'Greater Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Greater Bank''s developer surface includes authentication, documentation, getting-started guide, API reference, support, and 20 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 36.3
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
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 36.3
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
    score: 31.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/greater-bank/refs/heads/main/screenshots/greater-bank-2026-07-21T130910.png
security:
- kind: authentication
  name: Greater Bank Authentication
  slug: greater-bank-authentication
  summary_line: none/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Greater Bank Domain Security
  slug: greater-bank-domain-security
  summary_line: TLSv1.3 · DMARC
slug: greater-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Mutual
- Product Reference Data
website: https://www.greater.com.au/
---
