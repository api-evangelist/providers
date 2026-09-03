---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Citizens Financial Agentic Access
  operation_count: 4
  slug: citizens-financial-agentic-access
  summary_line: 4 operations
api_count: 2
apis:
- description: The Citizens Pay API enables merchants and partners to integrate Citizens Pay point-of-sale financing into their applications and checkout experiences. Citizens Pay provides consumer financing solutio
  name: Citizens Pay API
  slug: citizens-pay-api
- baseURL: https://api.citizensbank.com
  baseurl_source: declared
  description: Retrieve account information
  name: Citizens Financial Accounts API
  slug: citizens-financial-accounts-api
- baseURL: https://api.citizensbank.com
  baseurl_source: declared
  description: Search and retrieve ATM location data
  name: Citizens Financial ATM Locations API
  slug: citizens-financial-atm-locations-api
- baseURL: https://api.citizensbank.com
  baseurl_source: declared
  description: Retrieve transaction history
  name: Citizens Financial Transactions API
  slug: citizens-financial-transactions-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Citizens Bank Accounts API
  slug: open-citizens-bank-accounts-api
- collection_type: open
  name: Citizens Bank ATM Locator API
  slug: open-citizens-bank-atm-locator-api
- collection_type: open
  name: Citizens Bank Accounts API
  slug: open-citizens-financial-accounts-api
- collection_type: open
  name: Citizens Bank Accounts ATM Locations API
  slug: open-citizens-financial-atm-locations-api
- collection_type: open
  name: Citizens Bank Accounts Transactions API
  slug: open-citizens-financial-transactions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/citizens-financial-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/citizens-financial-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/citizens-financial-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/citizens-financial-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/citizens-financial-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rbs-citizens-financial-group
- group: company
  title: ''
  type: Website
  url: https://www.citizensbank.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.citizensbank.com/
- group: start
  title: ''
  type: Sandbox
  url: https://sandboxdeveloper.citizensbank.com/api
- group: operate
  title: ''
  type: Support
  url: https://developer.citizensbank.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.citizensbank.com/privacy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/citizens-financial-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/citizens-financial-rules.yml
created: '2026-03-21'
description: Citizens Financial Group is one of the oldest and largest financial institutions in the United States, providing retail and commercial banking products and services to individuals, small businesses, middle-market companies, and large corporations. Citizens exposes its programmable surface through the Citizens developer portal at developer.citizensbank.com, with REST APIs for deposit account and transaction data, ATM location services, and point-of-sale consumer financing through Citizens Pay. Authentication is OAuth 2.0 and the portal provides both sandbox and production environments.
finops:
- name: Citizens Financial Finops
  service_category: Banking
  slug: citizens-financial-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/citizens-financial.png
jsonld:
- class_count: 14
  name: Citizens Financial Context
  property_count: 0
  slug: citizens-financial-context
layout: provider
modified: '2026-05-19'
name: Citizens Financial
nav: Providers
network: true
overview: 'Citizens Financial publishes 3 APIs on the [APIs.io](https://apis.io/) network: Accounts API, ATM Locations API, and Transactions API. Tagged areas include Account, ATMs, Banking, Open Banking, and Payments.


  The Citizens Financial catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Citizens Financial''s developer surface includes authentication, developer portal, sandbox, support, and 9 more developer resources.'
plans:
- name: Citizens Financial Plans Pricing
  plan_count: 2
  slug: citizens-financial-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Citizens Financial Rate Limits
  slug: citizens-financial-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Citizens Financial API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: citizens-financial-rules
scopes:
- name: Citizens Financial Scopes
  scope_count: 2
  slug: citizens-financial-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 13
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 45.5
    contract_quality: 62.6
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 45.5
    operational_transparency: 5.3
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 43.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/citizens-financial/refs/heads/main/screenshots/citizens-financial-2026-06-20T174412.png
security:
- kind: authentication
  name: Citizens Financial Authentication
  slug: citizens-financial-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Citizens Financial Domain Security
  slug: citizens-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: citizens-financial
tags:
- Account
- ATMs
- Banking
- Open Banking
- Payments
- Point-of-Sale
- Transaction
website: https://www.citizensbank.com/
---
