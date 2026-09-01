---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Open Banking API in the Truist Developer Center covering personal and small-business accounts - account information, balances, and transaction data. Documented in a registration-gated sandbox that ret
  name: Truist Personal and Small Business Accounts API
  slug: truist-personal-and-small-business-accounts-api
- description: Consumer-permissioned data-sharing surface for Truist, delivered through the Truist Open Banking API Developer Portal and FDX-aligned, tokenized connections (including a Plaid data-access partnership)
  name: Truist Open Banking Data Access (FDX-aligned)
  slug: truist-open-banking-data-access
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truist-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.truist.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.truist.com/
- group: start
  title: ''
  type: Portal
  url: https://truist-1132.my.site.com/truist/s/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.truist.com/api/working-with-truist
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.truist.com/api/working-with-truist
- group: docs
  title: ''
  type: APIReference
  url: https://developer.truist.com/api/view-api
- group: start
  title: ''
  type: SignUp
  url: https://developer.truist.com/signup
- group: start
  title: ''
  type: Login
  url: https://developer.truist.com/ui/login/1000
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/truist
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truist.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truist.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.truist.com/support
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truist-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/truist-conformance.yml
created: '2026-07-23'
description: Truist Financial Corporation is a U.S. bank holding company headquartered in Charlotte, North Carolina, formed in December 2019 through the merger of BB&T and SunTrust Banks. Its principal subsidiary, Truist Bank, is a North Carolina state-chartered commercial bank and member of the Federal Reserve System, ranking among the largest U.S. commercial banks by assets and serving consumer, small-business, commercial, and wealth clients. On the API and open-finance side Truist runs a first-party Truist Developer Center at developer.truist.com that publishes registration-gated Open Banking APIs in a sandbox environment returning mock data (personal and small-business accounts, balances, transactions, and credit-transfer payments), and it operates a separate Truist Open Banking API Developer Portal for consumer-permissioned data sharing. Consumer data access is delivered largely through FDX-aligned, tokenized connections and aggregator partnerships (notably a Plaid data-access agreement)
  rather than an open first-party production API, and Truist states it monitors and complies with evolving CFPB Section 1033 personal-financial-data rules.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Truist
nav: Providers
network: true
overview: 'Truist publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Open Finance, and FDX.


  Truist''s developer surface includes developer portal, documentation, getting-started guide, API reference, signup flow, support, and 9 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 3
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 15.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 24.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Truist Domain Security
  slug: truist-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: truist
tags:
- Financial-Services
- Banking
- United States
- Open Finance
- FDX
- Payments
- Data Aggregation
website: https://www.truist.com
---
