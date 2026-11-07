---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Fairing Agentic Access
  operation_count: 3
  slug: fairing-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://app.fairing.co/api
  baseurl_source: declared
  description: The Questions API from Fairing — 1 operation(s) for questions.
  name: Fairing Questions API
  slug: fairing-questions-api
- baseURL: https://app.fairing.co/api
  baseurl_source: declared
  description: The Responses API from Fairing — 1 operation(s) for responses.
  name: Fairing Responses API
  slug: fairing-responses-api
- baseURL: https://app.fairing.co/api
  baseurl_source: declared
  description: The Sources API from Fairing — 1 operation(s) for sources.
  name: Fairing Sources API
  slug: fairing-sources-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/fairing/agentic-access/fairing-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fairing-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/fairing/plans/fairing-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fairing-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fairing/rules/fairing-rules.yml
  title: ''
  type: Spectral
  url: rules/fairing-rules.yml
- group: agent
  href: https://artifacts.apis.io/fairing/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/fairing/changelog/fairing-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fairing-changelog.yml
- group: design
  href: https://artifacts.apis.io/fairing/errors/fairing-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fairing-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fairing/conformance/fairing-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fairing-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fairing/llms/fairing-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fairing-llms.txt
- group: agent
  href: https://artifacts.apis.io/fairing/mcp/fairing-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fairing-mcp.yml
- group: agent
  href: https://artifacts.apis.io/fairing/well-known/fairing-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fairing-well-known.yml
- group: other
  href: https://artifacts.apis.io/fairing/hosts/fairing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fairing-hosts.yml
- group: other
  href: https://artifacts.apis.io/fairing/vendors/fairing-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fairing-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.fairing.co/
- group: start
  title: ''
  type: Login
  url: https://app.fairing.co/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.fairing.co/docs/release-notes
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fairing.co/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fairing.co/docs/sdk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fairing.co/
- group: auth
  href: https://artifacts.apis.io/fairing/security/fairing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fairing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fairing.co
- group: company
  title: ''
  type: Blog
  url: https://fairing.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://fairing.co/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fairing.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fairing.co/privacy
created: '2026-10-29'
description: Fairing is a post‑purchase attribution platform used by over 3,500 ecommerce brands to understand how customers discovered them, why they bought, and what almost stopped a purchase, by asking brief surveys immediately after checkout. The service provides actionable insights into marketing channels, including AI‑driven attribution, and integrates with Shopify, WooCommerce, Salesforce Commerce Cloud, Recharge and headless stores via a Web SDK. Trusted by thousands of brands, Fairing helps marketers allocate spend more effectively and improve ROI.
image: https://framerusercontent.com/images/YUAqUYpgssxmlILYVvvvc8JaoIA.webp
layout: provider
mcp_servers:
- description: Remote MCP server at docs.fairing.co.
  name: Fairing MCP Server
  slug: fairing-mcp-yml
modified: '2026-10-29'
name: Fairing
nav: Providers
network: true
overview: 'Fairing publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Questions API, Responses API, and Sources API. Tagged areas include Post-Purchase, Surveys, Marketing, Attribution, and E-Commerce.


  The Fairing catalog on APIs.io includes 1 Spectral governance ruleset.


  Fairing''s developer surface includes changelog, support, API reference, getting-started guide, documentation, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Fairing Plans Pricing
  plan_count: 9
  slug: fairing-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Fairing Rate Limits
  slug: fairing-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Fairing API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: fairing-rules
scopes:
- name: Fairing Scopes
  scope_count: 0
  slug: fairing-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 53.1
    developer_ergonomics: 24.3
    discoverability: 75.0
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fairing/fairing-2026-11-03T131810.png
security:
- kind: authentication
  name: Fairing Authentication
  slug: fairing-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Fairing Domain Security
  slug: fairing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: post-sources
  slug: post-sources
- name: retrieve-questions
  slug: retrieve-questions
- name: retrieve-responses
  slug: retrieve-responses
slug: fairing
tags:
- Post-Purchase
- Surveys
- Marketing
- Attribution
- E-Commerce
website: https://fairing.co
---
