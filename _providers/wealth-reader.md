---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.7
  scored_at: '2026-09-16'
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
artifact_total: 10
asyncapis:
- description: ''
  name: Wealth Reader Webhooks
  slug: wealth-reader-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.wealthreader.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/security/wealth-reader-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/openapi/_original/wealth-reader-api-for-ai.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/wealth-reader-api-for-ai.yaml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/openapi/_original/wealth-reader-api.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/wealth-reader-api.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/overlays/wealth-reader-api-for-ai-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/llms/wealth-reader-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wealth-reader-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/authentication/wealth-reader-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wealth-reader-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/conventions/wealth-reader-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wealth-reader-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/conventions/wealth-reader-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/wealth-reader-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/errors/wealth-reader-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wealth-reader-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: https://api.wealthreader.com/error-codes/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/rate-limits/wealth-reader-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wealth-reader-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/plans/wealth-reader-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wealth-reader-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/lifecycle/wealth-reader-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wealth-reader-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/changelog/wealth-reader-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/wealth-reader-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/conformance/wealth-reader-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wealth-reader-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/conformance/wealth-reader-conformance.yml
  title: ''
  type: Compliance
  url: conformance/wealth-reader-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/security/wealth-reader-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/wealth-reader-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/security/wealth-reader-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/wealth-reader-vulnerability-disclosure.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/sandbox/wealth-reader-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/wealth-reader-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/components/wealth-reader-components.yml
  title: ''
  type: Components
  url: components/wealth-reader-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/data-model/wealth-reader-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wealth-reader-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/packages/wealth-reader-packages.yml
  title: ''
  type: Packages
  url: packages/wealth-reader-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/cli/wealth-reader-cli.yml
  title: ''
  type: CLI
  url: cli/wealth-reader-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/mcp/wealth-reader-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wealth-reader-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/mcp/wealth-reader-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/wealth-reader-tool-crosswalk.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/asyncapi/wealth-reader-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/wealth-reader-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wealth-reader/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-24'
description: 'Read-only bank aggregation API: accounts, transactions, cards, loans, deposits and investment portfolios from banks, brokers and asset managers in 61 countries, over both the PSD2 regulatory channel and a non-PSD2 channel that returns wealth data the regulatory APIs do not expose.'
image: https://www.wealthreader.com/i/wealthreader.svg
layout: provider
mcp_servers:
- description: ''
  name: ALL WR Toolkit MCP server
  slug: all-wr-toolkit-mcp-server
modified: '2026-09-16'
name: Wealth Reader
nav: Providers
network: true
overview: 'Wealth Reader publishes 3 APIs on the [APIs.io](https://apis.io/) network: Advanced API, Cards (real time) API, and Core API. Tagged areas include Bank Aggregation, Open Banking, PSD2, Financial Data, and Account Aggregation.


  The Wealth Reader catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wealth Reader''s developer surface includes documentation, signup flow, engineering blog, API reference, getting-started guide, support, pricing, and 32 more developer resources.'
plans:
- name: Wealth Reader Plans Pricing
  plan_count: 4
  slug: wealth-reader-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Wealth Reader Rate Limits
  slug: wealth-reader-rate-limits
score:
  band: strong
  composite: 64.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.5
  facets:
    access_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 62.0
    developer_ergonomics: 75.6
    discoverability: 75.9
    operational_transparency: 57.9
  previous_composite: 61.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
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
    score: 50.6
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
website: https://www.wealthreader.com/
---
