---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 2
  name: Wealth Reader Agentic Access
  operation_count: 20
  slug: wealth-reader-agentic-access
  summary_line: 20 operations · 12 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.wealthreader.com/
  baseurl_source: declared
  description: Optional endpoints not required for standard integrations. Use only if explicitly instructed by Wealth Reader.
  name: Wealth Reader Advanced API
  slug: wealth-reader-advanced-api
- baseURL: https://api.wealthreader.com/
  baseurl_source: declared
  description: 'Real-time card expense synchronization from the Open Sync mobile app: per-customer employee pre-registration, signed webhooks (card_transaction.created / card_enrollment.confirmed), and REST query / b'
  name: Wealth Reader Cards (real time) API
  slug: wealth-reader-cards-real-time-api
- baseURL: https://api.wealthreader.com/
  baseurl_source: declared
  description: Core API required for standard integrations
  name: Wealth Reader Core API
  slug: wealth-reader-core-api
artifact_total: 29
asyncapis:
- description: ''
  name: Wealth Reader Webhooks
  slug: wealth-reader-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/wealth-reader/agentic-access/wealth-reader-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wealth-reader-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/wealth-reader/rules/wealth-reader-rules.yml
  title: ''
  type: Spectral
  url: rules/wealth-reader-rules.yml
- group: design
  href: https://artifacts.apis.io/wealth-reader/json-ld/wealth-reader-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wealth-reader-context.jsonld
- group: design
  href: https://artifacts.apis.io/wealth-reader/vocabulary/wealth-reader-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wealth-reader-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/wealth-reader/lifecycle/wealth-reader-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/wealth-reader-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/wealth-reader/hosts/wealth-reader-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wealth-reader-hosts.yml
- group: other
  href: https://artifacts.apis.io/wealth-reader/vendors/wealth-reader-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wealth-reader-vendors.yml
- group: build
  href: https://artifacts.apis.io/wealth-reader/packages/wealth-reader-packages.yml
  title: ''
  type: SDKs
  url: packages/wealth-reader-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.wealthreader.com/en/about-wealth-reader/press/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.wealthreader.com/feed/
- group: company
  title: ''
  type: Website
  url: https://www.wealthreader.com/
- group: auth
  href: https://artifacts.apis.io/wealth-reader/security/wealth-reader-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wealth-reader-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.wealthreader.com/docs/
- group: start
  title: ''
  type: SignUp
  url: https://www.wealthreader.com/en/pricing/
- group: company
  title: ''
  type: Blog
  url: https://blog.wealthreader.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wealthreader.com/es/politica-privacidad/
- group: docs
  href: https://artifacts.apis.io/wealth-reader/openapi/_original/wealth-reader-api-for-ai.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/wealth-reader-api-for-ai.yaml
- group: docs
  href: https://artifacts.apis.io/wealth-reader/openapi/_original/wealth-reader-api.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/wealth-reader-api.yaml
- group: other
  href: https://artifacts.apis.io/wealth-reader/overlays/wealth-reader-api-for-ai-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wealth-reader-api-for-ai-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.wealthreader.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.wealthreader.com/api-reference/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.wealthreader.com/docs/en/introduction/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Wealth-Reader
- group: operate
  title: ''
  type: Support
  url: https://help.wealthreader.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wealthreader.com/en/pricing/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/wealtreader/wealth-reader-api-definition/overview
- group: agent
  href: https://artifacts.apis.io/wealth-reader/llms/wealth-reader-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wealth-reader-llms.txt
- group: auth
  href: https://artifacts.apis.io/wealth-reader/authentication/wealth-reader-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wealth-reader-authentication.yml
- group: design
  href: https://artifacts.apis.io/wealth-reader/conventions/wealth-reader-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wealth-reader-conventions.yml
- group: design
  href: https://artifacts.apis.io/wealth-reader/conventions/wealth-reader-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/wealth-reader-conventions.yml
- group: design
  href: https://artifacts.apis.io/wealth-reader/errors/wealth-reader-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wealth-reader-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: https://api.wealthreader.com/error-codes/
- group: operate
  href: https://artifacts.apis.io/wealth-reader/rate-limits/wealth-reader-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wealth-reader-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/wealth-reader/plans/wealth-reader-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wealth-reader-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/wealth-reader/lifecycle/wealth-reader-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wealth-reader-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/wealth-reader/conformance/wealth-reader-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wealth-reader-conformance.yml
- group: auth
  href: https://artifacts.apis.io/wealth-reader/conformance/wealth-reader-conformance.yml
  title: ''
  type: Compliance
  url: conformance/wealth-reader-conformance.yml
- group: auth
  href: https://artifacts.apis.io/wealth-reader/security/wealth-reader-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/wealth-reader-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/wealth-reader/security/wealth-reader-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/wealth-reader-vulnerability-disclosure.yml
- group: start
  href: https://artifacts.apis.io/wealth-reader/sandbox/wealth-reader-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/wealth-reader-sandbox.yml
- group: design
  href: https://artifacts.apis.io/wealth-reader/components/wealth-reader-components.yml
  title: ''
  type: Components
  url: components/wealth-reader-components.yml
- group: design
  href: https://artifacts.apis.io/wealth-reader/data-model/wealth-reader-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wealth-reader-data-model.yml
- group: build
  href: https://artifacts.apis.io/wealth-reader/packages/wealth-reader-packages.yml
  title: ''
  type: Packages
  url: packages/wealth-reader-packages.yml
- group: build
  href: https://artifacts.apis.io/wealth-reader/cli/wealth-reader-cli.yml
  title: ''
  type: CLI
  url: cli/wealth-reader-cli.yml
- group: agent
  href: https://artifacts.apis.io/wealth-reader/mcp/wealth-reader-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wealth-reader-mcp.yml
- group: build
  href: https://artifacts.apis.io/wealth-reader/mcp/wealth-reader-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/wealth-reader-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/wealth-reader/asyncapi/wealth-reader-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/wealth-reader-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/wealth-reader/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-24'
description: 'Read-only bank aggregation API: accounts, transactions, cards, loans, deposits and investment portfolios from banks, brokers and asset managers in 61 countries, over both the PSD2 regulatory channel and a non-PSD2 channel that returns wealth data the regulatory APIs do not expose.'
finops:
- has_sources: true
  method: derived
  name: Wealth Reader Finops
  primary_unit: products read
  service_category: ''
  slug: wealth-reader-finops
  template: false
image: https://www.wealthreader.com/i/wealthreader.svg
json_schemas:
- name: batch-connection
  property_count: 15
  slug: wealth-reader-batch-connection
- name: cards-enrollment-response
  property_count: 2
  slug: wealth-reader-cards-enrollment-response
- name: cards-transaction
  property_count: 15
  slug: wealth-reader-cards-transaction
- name: category-types
  property_count: 0
  slug: wealth-reader-category-types
- name: check-user-response
  property_count: 4
  slug: wealth-reader-check-user-response
- name: entities
  property_count: 6
  slug: wealth-reader-entities
- name: entity-data
  property_count: 3
  slug: wealth-reader-entity-data
- name: register-user-request
  property_count: 4
  slug: wealth-reader-register-user-request
- name: statistics
  property_count: 5
  slug: wealth-reader-statistics
- name: warning-error-codes
  property_count: 0
  slug: wealth-reader-warning-error-codes
jsonld:
- class_count: 27
  name: Wealth Reader Context
  property_count: 104
  slug: wealth-reader-context
layout: provider
mcp_servers:
- description: Local (stdio) MCP server requiring an API key; 11 tools listed.
  name: ALL WR Toolkit MCP server
  slug: all-wr-toolkit-mcp-server
modified: '2026-10-06'
name: Wealth Reader
nav: Providers
network: true
overview: 'Wealth Reader publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Advanced API, Cards (real time) API, and Core API. Tagged areas include Bank Aggregation, Open Banking, PSD2, Financial Data, and Account Aggregation.


  The Wealth Reader catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Wealth Reader''s developer surface includes documentation, signup flow, engineering blog, API reference, getting-started guide, support, pricing, and 41 more developer resources.'
plans:
- name: Wealth Reader Plans Pricing
  plan_count: 6
  slug: wealth-reader-plans-pricing
- name: Wealth Reader Price Estimates
  plan_count: 0
  slug: wealth-reader-price-estimates
random_paper: 21
rate_limits:
- limit_count: 2
  name: Wealth Reader Rate Limits
  slug: wealth-reader-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Wealth Reader API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: wealth-reader-rules
score:
  band: exemplar
  composite: 70.7
  coverage:
    artifact_dirs: 35
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 81.6
    contract_governance: 35.6
    contract_quality: 75.4
    developer_ergonomics: 82.7
    discoverability: 72.5
    operational_transparency: 50.0
  previous_composite: 69.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/wealth-reader/wealth-reader-2026-10-11T194550.png
security:
- kind: authentication
  name: Wealth Reader Authentication
  slug: wealth-reader-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Wealth Reader Domain Security
  slug: wealth-reader-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Wealth Reader Vulnerability Disclosure
  slug: wealth-reader-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 4
skills:
- name: wealth-reader-manage-tokens
  slug: wealth-reader-manage-tokens
- name: wealth-reader-onboard-widget-integration
  slug: wealth-reader-onboard-widget-integration
- name: wealth-reader-read-financial-assets
  slug: wealth-reader-read-financial-assets
- name: wealth-reader-realtime-card-transactions
  slug: wealth-reader-realtime-card-transactions
slug: wealth-reader
tags:
- Bank Aggregation
- Open Banking
- PSD2
- Financial Data
- Account Aggregation
- Investment Portfolios
- Wealth Management
- Banking
- Fintech
- Data Aggregation
website: https://www.wealthreader.com/
---
