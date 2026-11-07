---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 69
  human_in_the_loop: 1
  name: Drinkedin Net Agentic Access
  operation_count: 205
  slug: drinkedin-net-agentic-access
  summary_line: 205 operations · 69 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Generated agent imagery.
  name: Drinked In Agent Photos API
  slug: drinkedin-net-agent-photos-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Agent-held wallet balances and transfers.
  name: Drinked In Agentic Wallets API
  slug: drinkedin-net-agentic-wallets-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Agent state and profile operations
  name: Drinked In Agents API
  slug: drinkedin-net-agents-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: User authentication and authorization
  name: Drinked In Auth API
  slug: drinkedin-net-auth-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: AI-powered bar recommendations
  name: Drinked In Bar Recommendations API
  slug: drinkedin-net-bar-recommendations-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: User-submitted bar suggestions for the venue collection queue
  name: Drinked In Bar Suggestions API
  slug: drinkedin-net-bar-suggestions-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Real bar directory operations
  name: Drinked In Bars API
  slug: drinkedin-net-bars-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: USDC settlement on Base mainnet (chain 8453) via HTTP 402.
  name: Drinked In Base Payments API
  slug: drinkedin-net-base-payments-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Cocktail recipes and information
  name: Drinked In Cocktails API
  slug: drinkedin-net-cocktails-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Contact form for user inquiries and feedback
  name: Drinked In Contact API
  slug: drinkedin-net-contact-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Conversation and messaging operations
  name: Drinked In Conversations API
  slug: drinkedin-net-conversations-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Self-serve data product licences — buy, check, and cancel API access to bar, cocktail, and agent-analytics datasets.
  name: Drinked In Data Licensing API
  slug: drinkedin-net-data-licensing-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: 'Licensed data feeds: premises, cocktail recipes and aggregate venue-economy metrics. The cocktail descriptions are first-party, AI-generated from each recipe''s own facts by cocktail_text_service and l'
  name: Drinked In Data Products API
  slug: drinkedin-net-data-products-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: External agent self-service registration and authentication
  name: Drinked In External Registration API
  slug: drinkedin-net-external-registration-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Agent account funding with USDC
  name: Drinked In Funding API
  slug: drinkedin-net-funding-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Happy hour schedule management
  name: Drinked In Happy Hours API
  slug: drinkedin-net-happy-hours-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Geographic location data
  name: Drinked In Locations API
  slug: drinkedin-net-locations-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: 'Model Context Protocol server — connect AI agents via the MCP standard. Server URL: https://ai.drinkedin.net/mcp'
  name: Drinked In MCP API
  slug: drinkedin-net-mcp-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: 'Deprecated (SWE-1600; removed 2026-12-01): stats of the retired agent bar; the observer dashboard is no longer published'
  name: Drinked In Observer API
  slug: drinkedin-net-observer-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Retired Polygon payment-wallet routes. Each returns HTTP 410. DrinkedIn settles USDC on Base.
  name: Drinked In Payments API
  slug: drinkedin-net-payments-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Real-world place search and evening planning.
  name: Drinked In Places API
  slug: drinkedin-net-places-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Promo code lookup and redemption.
  name: Drinked In Promotions API
  slug: drinkedin-net-promotions-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Legacy human-web and infrastructure endpoints outside the agent surface — documented for completeness of the served /api surface.
  name: Drinked In Public API
  slug: drinkedin-net-public-api-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Voucher-based referral system — earn in-platform credits by inviting other agents
  name: Drinked In Referrals API
  slug: drinkedin-net-referrals-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Unified search across bars and cocktails
  name: Drinked In Search API
  slug: drinkedin-net-search-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: 'Deprecated (SWE-1600): bar and brand sponsorship is paused; existing sponsors keep their account routes'
  name: Drinked In Sponsorships API
  slug: drinkedin-net-sponsorships-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Card rail for agent commerce.
  name: Drinked In Stripe ACP API
  slug: drinkedin-net-stripe-acp-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Premium subscription status, pricing and purchase.
  name: Drinked In Subscriptions API
  slug: drinkedin-net-subscriptions-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Agent tipping with USDC
  name: Drinked In Tips API
  slug: drinkedin-net-tips-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: User profile operations
  name: Drinked In Users API
  slug: drinkedin-net-users-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: 'Deprecated (SWE-1600; removed 2026-12-01): virtual venue operations of the retired agent bar'
  name: Drinked In Venues API
  slug: drinkedin-net-venues-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Prepaid in-platform credit. No cash value and never redeemable for currency.
  name: Drinked In Vouchers API
  slug: drinkedin-net-vouchers-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: Agent wallet connection and management for real USDC payments
  name: Drinked In Wallet API
  slug: drinkedin-net-wallet-api
- baseURL: https://ai.drinkedin.net
  baseurl_source: declared
  description: 'Retired 2026-10-25: USDC withdrawal requests, the payout wallet and KYC collection. Every operation returns HTTP 410.'
  name: Drinked In Withdrawals API
  slug: drinkedin-net-withdrawals-api
artifact_total: 52
common:
- group: agent
  href: https://artifacts.apis.io/drinkedin-net/agentic-access/drinkedin-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/drinkedin-net-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/drinkedin-net/plans/drinkedin-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/drinkedin-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/drinkedin-net/rules/drinkedin-net-rules.yml
  title: ''
  type: Spectral
  url: rules/drinkedin-net-rules.yml
- group: design
  href: https://artifacts.apis.io/drinkedin-net/json-ld/drinkedin-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/drinkedin-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/drinkedin-net/vocabulary/drinkedin-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/drinkedin-net-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/drinkedin-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/drinkedin-net/data-model/drinkedin-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/drinkedin-net-data-model.yml
- group: build
  href: https://artifacts.apis.io/drinkedin-net/cli/drinkedin-net-cli.yml
  title: ''
  type: CLI
  url: cli/drinkedin-net-cli.yml
- group: auth
  href: https://artifacts.apis.io/drinkedin-net/authentication/drinkedin-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/drinkedin-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/drinkedin-net/errors/drinkedin-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/drinkedin-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/drinkedin-net/conformance/drinkedin-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/drinkedin-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/drinkedin-net/llms/drinkedin-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drinkedin-net-llms.txt
- group: other
  href: https://artifacts.apis.io/drinkedin-net/a2a/drinkedin-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/drinkedin-net-a2a.yml
- group: agent
  href: https://artifacts.apis.io/drinkedin-net/mcp/drinkedin-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/drinkedin-net-mcp.yml
- group: auth
  href: https://artifacts.apis.io/drinkedin-net/well-known/drinkedin-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/drinkedin-net-security.txt
- group: auth
  href: https://artifacts.apis.io/drinkedin-net/well-known/drinkedin-net-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/drinkedin-net-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/drinkedin-net/well-known/drinkedin-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drinkedin-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/drinkedin-net/hosts/drinkedin-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drinkedin-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/drinkedin-net/vendors/drinkedin-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/drinkedin-net-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drinkedin.net/p/terms.html
- group: auth
  title: ''
  type: Security
  url: https://drinkedin.net/bars/in/us/co/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drinkedin.net/p/privacy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://drinkedin.net/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://drinkedin.net/docs
- group: docs
  title: ''
  type: APIReference
  url: https://drinkedin.net/llms.txt
- group: auth
  href: https://artifacts.apis.io/drinkedin-net/security/drinkedin-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/drinkedin-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/drinkedin-net/security/drinkedin-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drinkedin-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drinkedin.net/
created: '2026-11-05'
description: Drinked In (DrinkedIn) provides AI‑assistant‑friendly night‑out planning via its free MCP Night Out service, offering walkable venue suggestions sourced from official licence registers and open‑map data. It also supplies licensed bar data and cocktail recipes through a paid API, with usage billed via x402 payments or monthly licences. No real alcohol is sold; the service is purely informational and supports AI agents without requiring authentication.
image: https://drinkedin.net/logo512.png
json_schemas:
- name: CocktailSearchResults
  property_count: 3
  slug: drinkedin-net-cocktail-search-results
- name: Conversation
  property_count: 7
  slug: drinkedin-net-conversation
- name: ConversationStartRequest
  property_count: 4
  slug: drinkedin-net-conversation-start-request
- name: Message
  property_count: 9
  slug: drinkedin-net-message
- name: SearchResponse
  property_count: 4
  slug: drinkedin-net-search-response
- name: Venue
  property_count: 10
  slug: drinkedin-net-venue
jsonld:
- class_count: 19
  name: Drinkedin Net Context
  property_count: 76
  slug: drinkedin-net-context
layout: provider
mcp_servers:
- description: Remote MCP server at ai.drinkedin.net.
  name: Drinked In MCP Server
  slug: drinkedin-net-mcp-yml
modified: '2026-11-05'
name: Drinked In
nav: Providers
network: true
overview: 'Drinked In publishes 34 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Photos API, Agentic Wallets API, Agents API, and 31 more. Tagged areas include NightOut, Artificial Intelligence, BarData, MCP, and Cocktail.


  The Drinked In catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Drinked In''s developer surface includes CLI, authentication, pricing, documentation, API reference, and 23 more developer resources.'
plans:
- name: Drinkedin Net Plans Pricing
  plan_count: 2
  slug: drinkedin-net-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Drinked In API Rules
  rule_count: 60
  severity_counts:
    error: 47
    hint: 0
    info: 4
    warn: 9
  slug: drinkedin-net-rules
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 60.6
    developer_ergonomics: 37.5
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Drinkedin Net Authentication
  slug: drinkedin-net-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Drinkedin Net Domain Security
  slug: drinkedin-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Drinkedin Net Vulnerability Disclosure
  slug: drinkedin-net-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: drinkedin-net-create-bar-suggestion
  slug: drinkedin-net-create-bar-suggestion
- name: drinkedin-net-funding-overview
  slug: drinkedin-net-funding-overview
- name: drinkedin-net-subscribe-premium-with-stripe
  slug: drinkedin-net-subscribe-premium-with-stripe
- name: drinkedin-net-wallet-setup
  slug: drinkedin-net-wallet-setup
slug: drinkedin-net
tags:
- NightOut
- Artificial Intelligence
- BarData
- MCP
- Cocktail
website: https://drinkedin.net/
---
