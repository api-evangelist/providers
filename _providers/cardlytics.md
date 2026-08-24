---
access_model:
  confidence: high
  label: Enterprise, partner-gated
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://platform.cardlytics.com/advertisers/docs/api-get-started
  - https://docs.cardlytics.com/ads/v2/integrations/sandbox-quickstart-guide.html
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 36
  human_in_the_loop: 2
  name: Cardlytics Agentic Access
  operation_count: 86
  slug: cardlytics-agentic-access
  summary_line: 86 operations · 36 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: The advertiser-partner integration surface. Partners upsert and delete merchants and offers keyed on their own external identifiers, pull aggregate merchant/offer performance metrics (impressions, pur
  name: Cardlytics Partner API
  slug: cardlytics-partner-api
- description: The Ads Manager campaign object model — Campaigns, AdGroups, Ads, Audiences, AudienceReach, Rewards, PricingModels, RedeemingMerchants, Geo, PurchaseCategories, AuditLogs and per-entity validation rul
  name: Cardlytics Campaign Build API
  slug: cardlytics-campaign-build-api
- description: The bank-side rewards platform API. A publisher opens an institution- or customer-scoped session, retrieves ranked targeted card-linked offers for a customer, and reads that customer's profile, reward
  name: Cardlytics Publisher API v2
  slug: cardlytics-publisher-api-v2
artifact_total: 14
asyncapis:
- description: ''
  name: Cardlytics Publisher Webhooks
  slug: cardlytics-publisher-webhooks
collections:
- collection_type: open
  name: Campaign Build API
  slug: open-cardlytics-campaign-build-api
- collection_type: open
  name: partner-api
  slug: open-cardlytics-partner-api
- collection_type: open
  name: OpenAPI definition
  slug: open-cardlytics-publisher-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cardlytics-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cardlytics-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cardlytics-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cardlytics-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cardlytics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cardlytics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cardlytics-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.cardlytics.com/sdk/unified-sdk-releases.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cardlytics-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cardlytics-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cardlytics-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cardlytics-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/cardlytics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cardlytics-packages.yml
- group: design
  title: ''
  type: Components
  url: components/cardlytics-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cardlytics-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cardlytics-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cardlytics-publisher-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cardlytics-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cardlytics-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://platform.cardlytics.com/.well-known/api-catalog
- group: company
  title: ''
  type: Website
  url: https://www.cardlytics.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.cardlytics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.cardlytics.com/
- group: docs
  title: ''
  type: APIReference
  url: https://platform.cardlytics.com/advertisers/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.cardlytics.com/advertisers/docs/api-get-started
- group: start
  title: ''
  type: Login
  url: https://platform.cardlytics.com/
- group: company
  title: ''
  type: Blog
  url: https://www.cardlytics.com/research-and-insights/browse-all-articles
- group: operate
  title: ''
  type: Support
  url: https://www.cardlytics.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cardlytics.com/master-advertiser-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cardlytics.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.cardlytics.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.cardlytics.com/trust-center
created: '2026-07-17'
description: 'Cardlytics is a commerce media platform that uses first-party purchase data from its financial-institution partners to help advertisers reach consumers inside banking apps with card-linked offers and measurable, closed-loop attribution. Advertisers plan, launch, and measure card-linked campaigns through Ads Manager and advertiser APIs, while banks and neobanks (publishers) embed Merchant Offers and the Cardlytics Rewards Platform into their digital channels via publisher APIs and SDKs. The company also operates the Dosh card-linked network and the Bridg offline purchase-intelligence business, giving advertisers person-level measurement across online and in-store spend. Cardlytics publishes three OpenAPI 3.0.1 definitions through its ReadMe developer hub — a Partner API for advertiser merchant and offer ingestion, reporting and a daily redemption feed; a Campaign Build API covering the Ads Manager campaign object model; and a Publisher API v2 for the bank-side rewards experience
  — alongside iOS, Android and web SDKs. Nothing is self-service: every credential is issued by an account manager under a partner agreement, and the API hosts answer 403 to anonymous callers. Cardlytics is a public company (NASDAQ: CDLX) and its platform is an enterprise, partnership-based product rather than a self-service developer API.'
image: https://cdn.prod.website-files.com/647efc90c29ecb765fcd4f1a/6481aadd2b75cd4512df022a_cardlytics_open_graph_01.png
layout: provider
modified: '2026-08-12'
name: Cardlytics
nav: Providers
network: true
overview: 'Cardlytics publishes 3 APIs on the [APIs.io](https://apis.io/) network: Partner API, Campaign Build API, and Publisher API v2. Tagged areas include Company, Advertising, Commerce Media, Card-Linked Offers, and Purchase Intelligence.


  The Cardlytics catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cardlytics'' developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, engineering blog, and 27 more developer resources.'
plans:
- name: Cardlytics Plans Pricing
  plan_count: 0
  slug: cardlytics-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Cardlytics Rate Limits
  slug: cardlytics-rate-limits
scopes:
- name: Cardlytics Scopes
  scope_count: 4
  slug: cardlytics-scopes
  summary_line: 4 scopes · clientCredentials/authorizationCode/custom
score:
  band: strong
  composite: 55.9
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 16.7
    contract_quality: 54.2
    developer_ergonomics: 54.2
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 47.4
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 0.0
      total: 3
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cardlytics/refs/heads/main/screenshots/cardlytics-2026-07-25T204515.png
security:
- kind: authentication
  name: Cardlytics Authentication
  slug: cardlytics-authentication
  summary_line: oauth2/mutualTLS/http/custom-session-token · 6 schemes
- kind: domain-security
  name: Cardlytics Domain Security
  slug: cardlytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cardlytics Trust Center
  slug: cardlytics-trust-center
  summary_line: SOC 1, SOC 2, SOX
slug: cardlytics
tags:
- Company
- Advertising
- Commerce Media
- Card-Linked Offers
- Purchase Intelligence
- Financial-Services
- Loyalty and Rewards
- Marketing
- Banking
- Retail Media
- Attribution
- Offers
website: https://www.cardlytics.com/
---
