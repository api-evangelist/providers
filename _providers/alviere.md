---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 53
  human_in_the_loop: 0
  name: Alviere Agentic Access
  operation_count: 75
  slug: alviere-agentic-access
  summary_line: 75 operations · 53 acting
api_count: 1
apis:
- baseURL: https://api.snd.alviere.com
  baseurl_source: declared
  description: 'This section details the ledger which contains the funding information for the account. ### Ledger and Balances There are three types of funding buckets managed by the Alviere ledger: | Bucket | Descr'
  name: ALVIERE Account Wallet API
  slug: alviere-account-wallet-api
- baseURL: https://api.snd.alviere.com
  baseurl_source: declared
  description: This section outlines the integration with Alviere to create and manage your customers and users, and to perform KYC and Identity Verification on them.<br/> A user account is a representation of a cus
  name: ALVIERE Accounts API
  slug: alviere-accounts-api
- baseURL: https://api.snd.alviere.com
  baseurl_source: declared
  description: 'Alviere uses the openid authentication standard. This section details what is required for authentication and access to the Alviere endpoints. ### Get API Credentials In order to connect to the API, y'
  name: ALVIERE Authentication API
  slug: alviere-authentication-api
- baseURL: https://api.snd.alviere.com
  baseurl_source: declared
  description: This section describes how to execute payment ACH transactions, such as ACH Debits and ACH Credits. ACH is processed in Alviere based on the NACHA processing windows. Alviere posts transactions Monday
  name: ALVIERE Bank Processing API
  slug: alviere-bank-processing-api
- baseURL: https://api.snd.alviere.com
  baseurl_source: declared
  description: 'This section describes how to issue and manage cards with the Alviere platform. To issue cards, you''ll need to have a Cardholder Program with Alviere. ### Card Types The Alviere platform supports the '
  name: ALVIERE Card Issuance API
  slug: alviere-card-issuance-api
- baseURL: https://api.snd.alviere.com
  baseurl_source: declared
  description: This section describes how to execute payment processing transactions, such as authorizations and cancellations of existing transactions.
  name: ALVIERE Card Processing API
  slug: alviere-card-processing-api
- baseURL: https://api.snd.alviere.com
  baseurl_source: declared
  description: Use Alviere cross-border payments API to transfer funds with integrated risk management, configurable fees and high availability.
  name: ALVIERE Remittances API
  slug: alviere-remittances-api
- baseURL: https://api.snd.alviere.com
  baseurl_source: declared
  description: Use the Reporting API to get all transactions processed by Alviere and to check the statuses of transactions, such as their settlement status. Below are the statuses that will be returned from the API
  name: ALVIERE Reporting API
  slug: alviere-reporting-api
- baseURL: https://api.snd.alviere.com
  baseurl_source: declared
  description: 'This section outlines the endpoints related to our tokenization service.<br/> ### Card Tokenization Process When a card is added to our system through our tokenization service, we perform multiple tes'
  name: ALVIERE Tokenization API
  slug: alviere-tokenization-api
- baseURL: https://api.snd.alviere.com
  baseurl_source: declared
  description: Use Alviere integrated Treasury Management API to fund and/or move funds across all you internal accounts.
  name: ALVIERE Treasury Management API
  slug: alviere-treasury-management-api
artifact_total: 14
common:
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.alviere.com/
- group: agent
  href: https://artifacts.apis.io/alviere/agentic-access/alviere-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/alviere-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/alviere/rules/alviere-rules.yml
  title: ''
  type: Spectral
  url: rules/alviere-rules.yml
- group: design
  href: https://artifacts.apis.io/alviere/vocabulary/alviere-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alviere-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/alviere/changelog/alviere-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/alviere-changelog.yml
- group: auth
  href: https://artifacts.apis.io/alviere/authentication/alviere-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alviere-authentication.yml
- group: design
  href: https://artifacts.apis.io/alviere/errors/alviere-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alviere-problem-types.yml
- group: design
  href: https://artifacts.apis.io/alviere/conformance/alviere-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alviere-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alviere/llms/alviere-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alviere-llms.txt
- group: agent
  href: https://artifacts.apis.io/alviere/well-known/alviere-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alviere-well-known.yml
- group: other
  href: https://artifacts.apis.io/alviere/hosts/alviere-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alviere-hosts.yml
- group: other
  href: https://artifacts.apis.io/alviere/vendors/alviere-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alviere-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.alviere.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alviere.com/privacy-policies
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.alviere.com/release-notes
- group: docs
  title: ''
  type: APIReference
  url: https://developer.alviere.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Alviere
- group: auth
  href: https://artifacts.apis.io/alviere/security/alviere-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alviere-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alviere.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.alviere.com
- group: company
  title: ''
  type: Newsroom
  url: https://alviere.com/press
- group: operate
  title: ''
  type: Contact
  url: https://alviere.com/get-started
created: '2026-10-19'
description: Alviere provides a full‑stack embedded finance platform that enables businesses to integrate banking, payments, and credit services directly into their products. The company offers APIs for account creation, transaction processing, compliance, and reporting, targeting fintechs and enterprises seeking seamless financial infrastructure.
image: https://alviere.com/imgs/og-default.jpg
layout: provider
modified: '2026-10-19'
name: ALVIERE
nav: Providers
network: true
overview: 'ALVIERE publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Wallet API, Accounts API, Authentication API, and 7 more. Tagged areas include Company, Fintech, Embedded Finance, and Banking.


  The ALVIERE catalog on APIs.io includes 1 Spectral governance ruleset.


  ALVIERE''s developer surface includes documentation, changelog, authentication, support, API reference, engineering blog, and 16 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: ALVIERE API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: alviere-rules
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 48.4
    developer_ergonomics: 35.7
    discoverability: 58.9
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 16.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alviere Authentication
  slug: alviere-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Alviere Domain Security
  slug: alviere-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alviere
tags:
- Company
- Fintech
- Embedded Finance
- Banking
website: https://alviere.com/
---
