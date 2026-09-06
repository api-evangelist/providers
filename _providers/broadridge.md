---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    delegated_identity: false
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
  score: 26.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Broadridge Agentic Access
  operation_count: 6
  slug: broadridge-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: The Broadridge Galaxia Fund Data API enables access to and distribution of global fund data for regulatory reporting and investor communications. APIs provide fund data dissemination for UCITS, PRIIPS
  name: Broadridge Fund Data Distribution (Galaxia) API
  slug: broadridge-fund-data-api
- description: The Broadridge Investor Communications API provides access to proxy distribution, shareholder vote management, and corporate action communications. APIs support electronic proxy delivery, vote tabulat
  name: Broadridge Investor Communications API
  slug: broadridge-investor-communications-api
- description: The Broadridge Post-Trade Processing API provides access to trade settlement, reconciliation, and regulatory reporting functions. APIs and SFTP interfaces enable post-trade processing automation, fail
  name: Broadridge Post-Trade Processing API
  slug: broadridge-post-trade-api
- baseURL: https://api.broadridge.example.com
  baseurl_source: declared
  description: Account information and balances
  name: broadridge Accounts API
  slug: broadridge-accounts-api
- baseURL: https://api.broadridge.example.com
  baseurl_source: declared
  description: Portfolio performance data
  name: broadridge Performance API
  slug: broadridge-performance-api
- baseURL: https://api.broadridge.example.com
  baseurl_source: declared
  description: Portfolio positions and holdings
  name: broadridge Positions API
  slug: broadridge-positions-api
- baseURL: https://api.broadridge.example.com
  baseurl_source: declared
  description: Account transactions and activity
  name: broadridge Transactions API
  slug: broadridge-transactions-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Broadridge Wealth Management Accounts API
  slug: open-broadridge-accounts-api
- collection_type: open
  name: Broadridge Wealth Management Accounts Performance API
  slug: open-broadridge-performance-api
- collection_type: open
  name: Broadridge Wealth Management Accounts Positions API
  slug: open-broadridge-positions-api
- collection_type: open
  name: Broadridge Wealth Management Accounts Transactions API
  slug: open-broadridge-transactions-api
- collection_type: open
  name: Broadridge Wealth Management API
  slug: open-broadridge-wealth
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/broadridge-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/broadridge-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/broadridge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/broadridge-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/broadridge-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/broadridge-financial-solutions
- group: company
  title: ''
  type: Website
  url: https://www.broadridge.com
- group: start
  title: ''
  type: Portal
  url: https://www.broadridge.com/client-access/
- group: operate
  title: ''
  type: Support
  url: https://www.broadridge.com/resource/developer-api-contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.broadridge.com/legal/privacy-statement-english
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.broadridge.com/legal/terms-of-use
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/wealthapiconnector/Broadridge-Wealth-API-Docs
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/broadridge/refs/heads/main/openapi/broadridge-wealth-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/broadridge/refs/heads/main/json-schema/broadridge-position-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/broadridge/refs/heads/main/json-schema/broadridge-transaction-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/broadridge/refs/heads/main/json-ld/broadridge-context.jsonld
description: Best-in-class API components meet expert support to create the ideal wealth management operations environment. Optimize productivity, client experiences, and more.
finops:
- name: Broadridge Finops
  service_category: Financial Services Technology
  slug: broadridge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/broadridge.png
json_schemas:
- name: Broadridge Position
  property_count: 14
  slug: broadridge-position
- name: Broadridge Transaction
  property_count: 15
  slug: broadridge-transaction
jsonld:
- class_count: 0
  name: Broadridge Context
  property_count: 4
  slug: broadridge-context
layout: provider
modified: '2026-05-19'
name: Broadridge
nav: Providers
network: true
overview: 'Broadridge publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Performance API, Positions API, and 1 more. Tagged areas include Fortune 1000.


  The Broadridge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Broadridge''s developer surface includes authentication, developer portal, support, documentation, and 12 more developer resources.'
plans:
- name: Broadridge Plans Pricing
  plan_count: 1
  slug: broadridge-plans-pricing
press:
- date: '2026-05-25'
  title: Broadridge Transforming Financial Literacy in Ireland ...
  url: https://www.broadridge.com/press-release/2026/broadridge-to-transform-financial-literacy-in-ireland
- date: '2026-05-25'
  title: The Broadridge Newsroom
  url: https://www.broadridge.com/news-room
- date: '2026-05-25'
  title: Broadridge Deploys Agentic AI at Institutional Scale Across ...
  url: https://www.prnewswire.com/news-releases/broadridge-deploys-agentic-ai-at-institutional-scale-across-capital-markets-and-wealth-operations-302767688.html
- date: '2026-05-25'
  title: Press Hub
  url: https://www.broadridge.com/press-hub
- date: '2026-05-25'
  title: Governor Hochul Announces $78 Million Investment by ...
  url: https://esd.ny.gov/esd-media-center/press-releases/governor-hochul-announces-78-million-investment-broadridge
random_paper: 14
rate_limits:
- limit_count: 3
  name: Broadridge Rate Limits
  slug: broadridge-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Broadridge API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: broadridge-jsonschema-spectral-rules
scopes:
- name: Broadridge Scopes
  scope_count: 3
  slug: broadridge-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 43.3
    catalog_earned_first_party: 0.0
    catalog_gap: 71.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 9.8
    contract_quality: 55.6
    developer_ergonomics: 54.8
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/broadridge/refs/heads/main/screenshots/broadridge-2026-06-20T173715.png
security:
- kind: authentication
  name: Broadridge Authentication
  slug: broadridge-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Broadridge Domain Security
  slug: broadridge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: broadridge
tags:
- Fortune 1000
website: https://www.broadridge.com
---
