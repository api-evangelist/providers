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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 36
  human_in_the_loop: 2
  name: Cardlytics Agentic Access
  operation_count: 86
  slug: cardlytics-agentic-access
  summary_line: 86 operations · 36 acting · 2 human-in-the-loop
api_count: 6
apis:
- description: The AdGroups API from Cardlytics — 8 operation(s) for adgroups.
  name: Cardlytics Ad Groups API
  slug: cardlytics-adgroups-api
- description: The Ads API from Cardlytics — 10 operation(s) for ads.
  name: Cardlytics Ads API
  slug: cardlytics-ads-api
- description: The ads-controller API from Cardlytics — 1 operation(s) for ads-controller.
  name: Cardlytics Ads Controller API
  slug: cardlytics-ads-controller-api
- description: The AudienceReach API from Cardlytics — 1 operation(s) for audiencereach.
  name: Cardlytics Audience Reach API
  slug: cardlytics-audiencereach-api
- description: The Audiences API from Cardlytics — 6 operation(s) for audiences.
  name: Cardlytics Audiences API
  slug: cardlytics-audiences-api
- description: The AuditLogs API from Cardlytics — 1 operation(s) for auditlogs.
  name: Cardlytics Audit Logs API
  slug: cardlytics-auditlogs-api
- description: The Authentication API from Cardlytics — 1 operation(s) for authentication.
  name: Cardlytics Authentication API
  slug: cardlytics-authentication-api
- description: The Campaigns API from Cardlytics — 14 operation(s) for campaigns.
  name: Cardlytics Campaigns API
  slug: cardlytics-campaigns-api
- description: The customer-controller API from Cardlytics — 3 operation(s) for customer-controller.
  name: Cardlytics Customer Controller API
  slug: cardlytics-customer-controller-api
- description: The Geo API from Cardlytics — 6 operation(s) for geo.
  name: Cardlytics Geo API
  slug: cardlytics-geo-api
- description: The Merchants API from Cardlytics — 1 operation(s) for merchants.
  name: Cardlytics Merchants API
  slug: cardlytics-merchants-api
- description: The Offers API from Cardlytics — 1 operation(s) for offers.
  name: Cardlytics Offers API
  slug: cardlytics-offers-api
- description: The PricingModels API from Cardlytics — 3 operation(s) for pricingmodels.
  name: Cardlytics Pricing Models API
  slug: cardlytics-pricingmodels-api
- description: The PurchaseCategories API from Cardlytics — 2 operation(s) for purchasecategories.
  name: Cardlytics Purchase Categories API
  slug: cardlytics-purchasecategories-api
- description: The Redemptions API from Cardlytics — 1 operation(s) for redemptions.
  name: Cardlytics Redemptions API
  slug: cardlytics-redemptions-api
- description: The Reports API from Cardlytics — 1 operation(s) for reports.
  name: Cardlytics Reports API
  slug: cardlytics-reports-api
- description: The Rewards API from Cardlytics — 6 operation(s) for rewards.
  name: Cardlytics Rewards API
  slug: cardlytics-rewards-api
- description: The session-controller API from Cardlytics — 1 operation(s) for session-controller.
  name: Cardlytics Session Controller API
  slug: cardlytics-session-controller-api
artifact_total: 29
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cardlytics-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cardlytics-partner-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cardlytics-campaign-build-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cardlytics-publisher-api-overlay.yaml
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
overview: 'Cardlytics publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Ad Groups API, Ads API, Ads Controller API, and 15 more. Tagged areas include Company, Advertising, Commerce Media, Card-Linked Offers, and Purchase Intelligence.


  The Cardlytics catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cardlytics'' developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, engineering blog, and 31 more developer resources.'
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
  composite: 54.6
  coverage:
    artifact_dirs: 25
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 54.8
    developer_ergonomics: 54.2
    discoverability: 92.6
    governance: 4.5
    operational_transparency: 47.4
  previous_composite: 54.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: sox
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
