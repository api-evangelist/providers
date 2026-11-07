---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mettle Agentic Access
  operation_count: 12
  slug: mettle-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- description: OBIE Read/Write Account & Transaction Information (AIS) API for Mettle business current accounts, exposing accounts, balances, transactions, and related resources to FCA-authorised third parties. FAPI
  name: Mettle Account and Transaction API
  slug: mettle-account-transaction-api
- description: OBIE Read/Write Payment Initiation Services (PIS) API for Mettle, allowing FCA-authorised third parties to initiate domestic and other payments from a customer's Mettle account with their consent. FAP
  name: Mettle Payment Initiation API
  slug: mettle-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds (CBPII) API for Mettle, letting card-based payment instrument issuers confirm whether funds are available on a customer's Mettle account. FAPI-secured with OAuth2
  name: Mettle Confirmation of Funds API
  slug: mettle-confirmation-of-funds-api
- baseURL: https://api.openbanking.prd-mettle.co.uk/open-banking/v2.3
  baseurl_source: declared
  description: Endpoint for getting ATM data
  name: Mettle ATM API
  slug: mettle-atm-api
- baseURL: https://api.openbanking.prd-mettle.co.uk/open-banking/v2.3
  baseurl_source: declared
  description: Endpoint for getting Business Current Account data
  name: Mettle BCA API
  slug: mettle-bca-api
- baseURL: https://api.openbanking.prd-mettle.co.uk/open-banking/v2.3
  baseurl_source: declared
  description: Endpoint for getting Branch data
  name: Mettle Branch API
  slug: mettle-branch-api
- baseURL: https://api.openbanking.prd-mettle.co.uk/open-banking/v2.3
  baseurl_source: declared
  description: Endpoint for getting Commercial Credit Card data
  name: Mettle CCC API
  slug: mettle-ccc-api
- baseURL: https://api.openbanking.prd-mettle.co.uk/open-banking/v2.3
  baseurl_source: declared
  description: Endpoint for getting Personal Current Account data
  name: Mettle PCA API
  slug: mettle-pca-api
- baseURL: https://api.openbanking.prd-mettle.co.uk/open-banking/v2.3
  baseurl_source: declared
  description: Endpoint for getting Unsecured SME Loan data
  name: Mettle SME API
  slug: mettle-sme-api
artifact_total: 16
collections:
- collection_type: open
  name: Open Data API
  slug: open-mettle-open-data-api
common:
- group: design
  href: https://artifacts.apis.io/mettle/rules/mettle-rules.yml
  title: ''
  type: Spectral
  url: rules/mettle-rules.yml
- group: design
  href: https://artifacts.apis.io/mettle/vocabulary/mettle-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mettle-vocabulary.yml
- group: start
  href: https://artifacts.apis.io/mettle/sandbox/mettle-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mettle-sandbox.yml
- group: other
  href: https://artifacts.apis.io/mettle/hosts/mettle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mettle-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.mettle.co.uk/blog/register-as-a-sole-trader-customer/
- group: other
  href: https://artifacts.apis.io/mettle/capabilities/mettle-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mettle-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/mettle/agentic-access/mettle-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mettle-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mettle/security/mettle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mettle-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/mettle/authentication/mettle-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mettle-authentication.yml
- group: auth
  href: https://artifacts.apis.io/mettle/scopes/mettle-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mettle-scopes.yml
- group: design
  href: https://artifacts.apis.io/mettle/conformance/mettle-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mettle-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bankofapis.com/products/natwest-group-open-banking
- group: design
  href: https://artifacts.apis.io/mettle/conventions/mettle-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mettle-conventions.yml
- group: design
  href: https://artifacts.apis.io/mettle/conventions/mettle-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/mettle-conventions.yml
- group: design
  href: https://artifacts.apis.io/mettle/errors/mettle-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mettle-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mettle/lifecycle/mettle-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mettle-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.bankofapis.com/products/natwest-group-open-banking
- group: design
  href: https://artifacts.apis.io/mettle/data-model/mettle-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mettle-data-model.yml
- group: agent
  href: https://artifacts.apis.io/mettle/well-known/mettle-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mettle-well-known.yml
- group: agent
  href: https://artifacts.apis.io/mettle/mcp/mettle-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mettle-mcp.yml
- group: other
  href: https://artifacts.apis.io/mettle/overlays/mettle-open-data-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mettle-open-data-api-overlay.yaml
- group: start
  title: ''
  type: Sandbox
  url: https://developer.sandbox.natwest.com/
- group: agent
  href: https://artifacts.apis.io/mettle/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.mettle.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bankofapis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bankofapis.com/products/natwest-group-open-banking/products-and-locations/documentation/mettle
- group: operate
  title: ''
  type: StatusPage
  url: https://www.bankofapis.com/performance/service-interruptions
- group: company
  title: ''
  type: Blog
  url: https://www.mettle.co.uk/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/join-mettle
- group: operate
  title: ''
  type: Support
  url: https://www.mettle.co.uk/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mettle.co.uk/docs/terms-and-conditions/1.5.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mettle.co.uk/privacy-notice/
created: '2026-07-23'
description: Mettle is a digital-only business bank account brand for UK sole traders, freelancers, and small limited companies, wholly owned by NatWest Group and originally built with Capco. It has no physical branches and is run on separate technology from the core NatWest bank, offering an app-based current account with a UK sort code and account number, invoicing, bookkeeping, tax tools, and a free FreeAgent accounting integration. As a NatWest Group brand, Mettle participates in UK Open Banking through NatWest Group's "Bank of APIs" developer platform, publishing PSD2 / OBIE-conformant APIs - a public, unsecured Open Data (Product) API describing its business current accounts, plus the FAPI-secured Read/Write family (Account & Transaction Information, Payment Initiation, and Confirmation of Funds). Read/Write access runs against a live production gateway (api.openbanking.prd-mettle.co.uk) secured with OAuth2/OIDC, mutual-TLS client authentication, and PSD2 strong customer authentication
  using OBIE/eIDAS certificates, onboarded via the Bank of APIs portal. Mettle is delivered under NatWest Group's FCA-authorised banking group and is a challenger/digital proposition rather than one of the CMA9 mandated brands.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Mettle
nav: Providers
network: true
overview: 'Mettle publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including ATM API, BCA API, Branch API, and 6 more. Tagged areas include Financial Services, Banking, Business Banking, Open Banking, and PSD2.


  The Mettle catalog on APIs.io includes 1 Spectral governance ruleset.


  Mettle''s developer surface includes sandbox, signup flow, authentication, documentation, engineering blog, support, and 26 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Mettle API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: mettle-rules
scopes:
- name: Mettle Scopes
  scope_count: 4
  slug: mettle-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 57.1
    contract_governance: 35.6
    contract_quality: 35.5
    developer_ergonomics: 20.8
    discoverability: 73.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: eidas
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 44.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/mettle/mettle-2026-08-07T172804.png
security:
- kind: authentication
  name: Mettle Authentication
  slug: mettle-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Mettle Domain Security
  slug: mettle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Discover Mettle published products and locations
  slug: mettle-open-data-discovery
slug: mettle
tags:
- Financial Services
- Banking
- Business Banking
- Open Banking
- PSD2
- OBIE
- FAPI
- United Kingdom
- Payments
- Account Information
- Challenger Bank
- Fintech
website: https://www.mettle.co.uk/
---
