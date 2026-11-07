---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Connexis Cash Agentic Access
  operation_count: 10
  slug: connexis-cash-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 2
apis:
- description: A documented Strong Customer Authentication flow that BNP Paribas provides for Connexis Cash to satisfy PSD2 SCA requirements. TPPs integrate the SCA flow into their PSD2 journeys so that Connexis Cas
  name: Connexis Cash Strong Customer Authentication (SCA)
  slug: strong-authentication
- description: The Connexis Cash digital banking application itself. While not a public REST API, it is the user-facing platform that powers payment initiation, real-time tracking, reconciliation, account reporting,
  name: Connexis Cash Digital Banking Platform
  provenance: unpublished
  slug: digital-banking-platform
- baseURL: https://psd2.api.cib.bnpparibas.com/gb-account-information-psd2-stet
  baseurl_source: declared
  description: The Accounts API from Connexis Cash — 2 operation(s) for accounts.
  name: Connexis Cash Accounts API
  slug: connexis-cash-accounts-api
- baseURL: https://psd2.api.cib.bnpparibas.com/gb-account-information-psd2-stet
  baseurl_source: declared
  description: The Balances API from Connexis Cash — 1 operation(s) for balances.
  name: Connexis Cash Balances API
  slug: connexis-cash-balances-api
- baseURL: https://psd2.api.cib.bnpparibas.com/gb-account-information-psd2-stet
  baseurl_source: declared
  description: The Beneficiaries API from Connexis Cash — 1 operation(s) for beneficiaries.
  name: Connexis Cash Beneficiaries API
  slug: connexis-cash-beneficiaries-api
- baseURL: https://psd2.api.cib.bnpparibas.com/gb-account-information-psd2-stet
  baseurl_source: declared
  description: The Consents API from Connexis Cash — 1 operation(s) for consents.
  name: Connexis Cash Consents API
  slug: connexis-cash-consents-api
- baseURL: https://psd2.api.cib.bnpparibas.com/gb-account-information-psd2-stet
  baseurl_source: declared
  description: The Transactions API from Connexis Cash — 1 operation(s) for transactions.
  name: Connexis Cash Transactions API
  slug: connexis-cash-transactions-api
- baseURL: https://psd2.api.cib.bnpparibas.com/gb-account-information-psd2-stet
  baseurl_source: declared
  description: The AISP API from Connexis Cash — 4 operation(s) for aisp.
  name: Connexis Cash AISP API
  slug: connexis-cash-aisp-api
artifact_total: 26
collections:
- collection_type: open
  name: BNP Paribas Connexis Cash - STET PSD2 Account Information (AISP) Accounts API
  slug: open-connexis-cash-accounts-api
- collection_type: open
  name: BNP Paribas Connexis Cash - STET PSD2 Account Information (AISP) Accounts Balances API
  slug: open-connexis-cash-balances-api
- collection_type: open
  name: BNP Paribas Connexis Cash - STET PSD2 Account Information (AISP) Accounts Beneficiaries API
  slug: open-connexis-cash-beneficiaries-api
- collection_type: open
  name: BNP Paribas Connexis Cash - STET PSD2 Account Information (AISP) Accounts Consents API
  slug: open-connexis-cash-consents-api
- collection_type: open
  name: BNP Paribas Connexis Cash - STET PSD2 Account Information (AISP) Accounts Transactions API
  slug: open-connexis-cash-transactions-api
- collection_type: open
  name: BNP Paribas Connexis Cash - STET PSD2 Account Information (AISP)
  slug: open-connexis-cash
common:
- group: commercial
  href: https://artifacts.apis.io/connexis-cash/finops/connexis-cash-finops.yml
  title: ''
  type: FinOps
  url: finops/connexis-cash-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://cashmanagement.bnpparibas.com/rss.xml
- group: agent
  href: https://artifacts.apis.io/connexis-cash/agentic-access/connexis-cash-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/connexis-cash-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/connexis-cash/security/connexis-cash-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connexis-cash-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/connexis-cash/authentication/connexis-cash-authentication.yml
  title: ''
  type: Authentication
  url: authentication/connexis-cash-authentication.yml
- group: auth
  href: https://artifacts.apis.io/connexis-cash/scopes/connexis-cash-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/connexis-cash-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://cashmanagement.bnpparibas.com/solutions/digital-channels
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cib.bnpparibas.com/
- group: other
  title: ''
  type: Open Banking Tracker
  url: https://www.openbankingtracker.com/provider/connexis-cash
- group: other
  title: ''
  type: BNP Paribas CIB
  url: https://cib.bnpparibas/
- group: other
  title: ''
  type: Mobile App
  url: https://apps.apple.com/us/app/connexis-cash-mobile/id1053068521
- group: operate
  title: ''
  type: Support
  url: ''
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cib.bnpparibas.com/index.php/api-docs/account-information-psd2-stet-mock
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cib.bnpparibas.com/index.php/api-docs/account-information-psd2-stet-mock
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cib.bnpparibas.com/index.php/docs/get-started
- group: start
  title: ''
  type: SignUp
  url: https://developers.cib.bnpparibas.com/index.php/user/register
- group: start
  title: ''
  type: Login
  url: https://developers.cib.bnpparibas.com/index.php/user/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.cib.bnpparibas.com/index.php/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cib.bnpparibas.com/about/privacy-policy_a-38-60.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bnpparibas
- group: docs
  href: https://artifacts.apis.io/connexis-cash/openapi/_original/connexis-cash-account-information-psd2-stet-mock-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/connexis-cash-account-information-psd2-stet-mock-openapi.yml
- group: other
  href: https://artifacts.apis.io/connexis-cash/overlays/connexis-cash-account-information-psd2-stet-mock-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/connexis-cash-account-information-psd2-stet-mock-overlay.yaml
- group: design
  href: https://artifacts.apis.io/connexis-cash/conventions/connexis-cash-conventions.yml
  title: ''
  type: Conventions
  url: conventions/connexis-cash-conventions.yml
- group: design
  href: https://artifacts.apis.io/connexis-cash/errors/connexis-cash-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/connexis-cash-problem-types.yml
- group: design
  href: https://artifacts.apis.io/connexis-cash/lifecycle/connexis-cash-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/connexis-cash-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/connexis-cash/conformance/connexis-cash-conformance.yml
  title: ''
  type: Conformance
  url: conformance/connexis-cash-conformance.yml
- group: auth
  href: https://artifacts.apis.io/connexis-cash/conformance/connexis-cash-conformance.yml
  title: ''
  type: Compliance
  url: conformance/connexis-cash-conformance.yml
- group: design
  href: https://artifacts.apis.io/connexis-cash/data-model/connexis-cash-data-model.yml
  title: ''
  type: DataModel
  url: data-model/connexis-cash-data-model.yml
- group: start
  href: https://artifacts.apis.io/connexis-cash/sandbox/connexis-cash-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/connexis-cash-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/connexis-cash/plans/connexis-cash-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/connexis-cash-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/connexis-cash/rate-limits/connexis-cash-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/connexis-cash-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/connexis-cash/llms/connexis-cash-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/connexis-cash-llms.txt
- group: agent
  href: https://artifacts.apis.io/connexis-cash/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/connexis-cash/mcp/connexis-cash-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/connexis-cash-mcp.yml
created: '2024-01-01'
description: Connexis Cash is BNP Paribas's corporate digital banking and cash management platform. It gives multinational corporates a unified online channel for payment initiation, real-time payment tracking, account reporting, reconciliation, and liquidity management across BNP Paribas's global network. Connexis Cash also exposes PSD2-compliant Open Banking APIs through the BNP Paribas CIB developer portal so that third-party providers (TPPs) can retrieve account information and initiate payments on behalf of Connexis Cash users, as well as a Strong Customer Authentication (SCA) flow.
finops:
- has_sources: true
  method: derived
  name: Connexis Cash Finops
  primary_unit: ''
  service_category: ''
  slug: connexis-cash-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/connexis-cash.png
layout: provider
modified: '2026-10-06'
name: Connexis Cash
nav: Providers
network: true
overview: 'Connexis Cash publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Accounts API, Balances API, and Beneficiaries API. Tagged areas include Account Information, BNP Paribas, Cash Management, Corporate Banking, and Digital Banking.


  The Connexis Cash catalog on APIs.io includes 1 Spectral governance ruleset.


  Connexis Cash''s developer surface includes authentication, support, documentation, API reference, getting-started guide, signup flow, sandbox, and 26 more developer resources.'
plans:
- name: Connexis Cash Plans Pricing
  plan_count: 0
  slug: connexis-cash-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Connexis Cash Rate Limits
  slug: connexis-cash-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Connexis Cash API Rules
  rule_count: 56
  severity_counts:
    error: 49
    hint: 0
    info: 3
    warn: 4
  slug: connexis-cash-rules
scopes:
- name: Connexis Cash Scopes
  scope_count: 3
  slug: connexis-cash-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    contract_governance: 31.8
    contract_quality: 48.1
    developer_ergonomics: 60.1
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/connexis-cash/connexis-cash-2026-06-20T174906.png
security:
- kind: authentication
  name: Connexis Cash Authentication
  slug: connexis-cash-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Connexis Cash Domain Security
  slug: connexis-cash-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: connexis-cash-account-discovery
  slug: connexis-cash-account-discovery
- name: connexis-cash-balance-reporting
  slug: connexis-cash-balance-reporting
- name: connexis-cash-transaction-retrieval
  slug: connexis-cash-transaction-retrieval
- name: connexis-cash-trusted-beneficiaries
  slug: connexis-cash-trusted-beneficiaries
slug: connexis-cash
tags:
- Account Information
- BNP Paribas
- Cash Management
- Corporate Banking
- Digital Banking
- Liquidity Management
- Open Banking
- Payments
- PSD2
- STET
- Strong Customer Authentication
website: https://cashmanagement.bnpparibas.com/solutions/digital-channels
---
