---
access_model:
  confidence: high
  label: Enterprise / contract-negotiated
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - docs
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 36
  human_in_the_loop: 0
  name: Green Screens Ai Agentic Access
  operation_count: 54
  slug: green-screens-ai-agentic-access
  summary_line: 54 operations · 36 acting
api_count: 2
apis:
- baseURL: https://api.greenscreens.ai/v3
  baseurl_source: declared
  description: Prediction service v3 — lane rate prediction, batch rates, network rates, long-term batch rates and prediction history. Spec version 3.8.0, 6 paths. The flagship service.
  name: Green Screens AI Prediction API
  slug: green-screens-ai-prediction-api
- baseURL: https://api.greenscreens.ai/v1
  baseurl_source: declared
  description: Authentication service. OAuth 2.0 client_credentials grant (RFC 6749) issuing a Keycloak JWT that is presented as an RFC 6750 bearer token on every other operation in the estate.
  name: Green Screens AI Auth API
  slug: green-screens-ai-auth-api
- baseURL: https://api.greenscreens.ai/v1
  baseurl_source: declared
  description: Analytics service v1 — lane top carriers and lane Triumph carriers, returned with SCAC, FMCSA MC and USDOT identifiers. The only paginated collection in the estate. Spec version 1.7.1, 2 paths.
  name: Green Screens AI Analytics API
  slug: green-screens-ai-analytics-api
- baseURL: https://api.greenscreens.ai/v1
  baseurl_source: declared
  description: Carrier bids service v1 — save, read, update and delete bids, search carriers, accept a bid, and send a bid request to an external carrier. Spec version 1.3.2, 7 paths. Contains the one irreversible w
  name: Green Screens AI Bids API
  slug: green-screens-ai-bids-api
- baseURL: https://api.greenscreens.ai/v1
  baseurl_source: declared
  description: Historical rate data and similar lanes analysis v1 — load history and recent rates. Spec version 1.0.0, 2 paths.
  name: Green Screens AI History API
  slug: green-screens-ai-history-api
- baseURL: https://api.greenscreens.ai/v1
  baseurl_source: declared
  description: Pricing service v1 — priority rules, combination rules and threshold rules (full CRUD each), 3PL pricing, and marketplace broker partners. Spec version 1.1.0, 8 paths. The largest service surface.
  name: Green Screens AI Pricing API
  slug: green-screens-ai-pricing-api
- baseURL: https://api.greenscreens.ai/v2
  baseurl_source: declared
  description: 'Quotes service v2 — list quotes, import and batch import. Spec version 2.0.0, 3 paths. NOT a superset of v1: the accept, reject, update, delete, shipper-search and lane-top-quotes operations live only'
  name: Green Screens AI Quotes API
  slug: green-screens-ai-quotes-api
- baseURL: https://api.greenscreens.ai/v2
  baseurl_source: declared
  description: TmsConnector service v2 — import loads, carriers and shippers, singly or in batches, from a broker transportation management system. Spec version 2.18.6, 6 paths. One-way ingestion with no published r
  name: Green Screens AI TMS API
  slug: green-screens-ai-tms-api
- baseURL: https://api.greenscreens.ai/v3
  baseurl_source: declared
  description: Market Intelligence service v1 View separately Try it in swagger
  name: Green Screens AI Market Intelligence API
  slug: green-screens-ai-market-intelligence-api
artifact_total: 30
collections:
- collection_type: open
  name: Triumph Intelligence Connect Analytics API
  slug: open-green-screens-ai-analytics-api
- collection_type: open
  name: Triumph Intelligence Connect Analytics Auth API
  slug: open-green-screens-ai-auth-api
- collection_type: open
  name: Triumph Intelligence Connect Analytics Bids API
  slug: open-green-screens-ai-bids-api
- collection_type: open
  name: Triumph Intelligence Connect Analytics History API
  slug: open-green-screens-ai-history-api
- collection_type: open
  name: Triumph Intelligence Connect Analytics MarketIntelligence API
  slug: open-green-screens-ai-marketintelligence-api
- collection_type: open
  name: Triumph Intelligence Connect Analytics Prediction API
  slug: open-green-screens-ai-prediction-api
- collection_type: open
  name: Triumph Intelligence Connect Analytics Pricing API
  slug: open-green-screens-ai-pricing-api
- collection_type: open
  name: Triumph Intelligence Connect Analytics Quotes API
  slug: open-green-screens-ai-quotes-api
- collection_type: open
  name: Triumph Intelligence Connect Analytics TMS API
  slug: open-green-screens-ai-tms-api
- collection_type: open
  name: Triumph Intelligence Connect
  slug: open-green-screens-ai
common:
- group: other
  href: https://artifacts.apis.io/green-screens-ai/capabilities/green-screens-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/green-screens-ai-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/green-screens-ai/finops/green-screens-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/green-screens-ai-finops.yml
- group: other
  href: https://artifacts.apis.io/green-screens-ai/overlays/green-screens-ai-marketintelligence-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/green-screens-ai-marketintelligence-overlay.yaml
- group: other
  href: https://artifacts.apis.io/green-screens-ai/overlays/green-screens-ai-prediction-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/green-screens-ai-prediction-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/green-screens-ai/overlays/green-screens-ai-quotes-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/green-screens-ai-quotes-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/green-screens-ai/overlays/green-screens-ai-datalake-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/green-screens-ai-datalake-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://triumph.io/solutions/rates/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://connect.greenscreens.ai/
- group: start
  title: ''
  type: Portal
  url: https://connect.greenscreens.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://connect.greenscreens.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://connect.greenscreens.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://intelligencehelp.triumph.io/en/collections/8387516-partners-and-integrations
- group: auth
  href: https://artifacts.apis.io/green-screens-ai/authentication/green-screens-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/green-screens-ai-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://triumph.io/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://intelligencehelp.triumph.io/en/
- group: company
  title: ''
  type: Blog
  url: https://triumph.io/blog/broker/
- group: start
  title: ''
  type: Login
  url: https://intelligence.triumph.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://triumph.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://triumph.io/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/greenscreensai
- group: operate
  title: ''
  type: StatusPage
  url: https://triumph.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://intelligencehelp.triumph.io/en/articles/8520083-what-s-new
- group: operate
  href: https://artifacts.apis.io/green-screens-ai/changelog/green-screens-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/green-screens-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/green-screens-ai/lifecycle/green-screens-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/green-screens-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/green-screens-ai/conventions/green-screens-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/green-screens-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/green-screens-ai/errors/green-screens-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/green-screens-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/green-screens-ai/data-model/green-screens-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/green-screens-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/green-screens-ai/conformance/green-screens-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/green-screens-ai-conformance.yml
- group: start
  href: https://artifacts.apis.io/green-screens-ai/sandbox/green-screens-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/green-screens-ai-sandbox.yml
- group: build
  href: https://artifacts.apis.io/green-screens-ai/packages/green-screens-ai-packages.yml
  title: ''
  type: Packages
  url: packages/green-screens-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/green-screens-ai/packages/green-screens-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/green-screens-ai-packages.yml
- group: design
  href: https://artifacts.apis.io/green-screens-ai/components/green-screens-ai-components.yml
  title: ''
  type: Components
  url: components/green-screens-ai-components.yml
- group: commercial
  href: https://artifacts.apis.io/green-screens-ai/plans/green-screens-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/green-screens-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/green-screens-ai/rate-limits/green-screens-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/green-screens-ai-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/green-screens-ai/llms/green-screens-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/green-screens-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/green-screens-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/green-screens-ai/mcp/green-screens-ai-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/green-screens-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/green-screens-ai/agentic-access/green-screens-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/green-screens-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/green-screens-ai/security/green-screens-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/green-screens-ai-domain-security.yml
created: '2024-07-02'
description: 'Green Screens AI — now sold as Triumph Intelligence following its acquisition by Triumph Financial — publishes predictive freight rate, capacity and pricing intelligence APIs for truckload brokers and shippers across the United States and Canada. The estate spans eleven versioned services behind one OAuth2 client-credentials gateway: lane rate prediction (spot, network and long-term batch), market intelligence and negotiation advice, carrier and lane analytics keyed on SCAC, MC and USDOT identifiers, historical rates, pricing rules, quotes, a carrier bid cycle, and a TMS connector for importing loads, carriers and shippers. Twelve first-party OpenAPI 3.0.2 documents, 36 paths and 47 operations are published openly at connect.greenscreens.ai; the callable production host is api.greenscreens.ai. A CDN-distributed browser widget bundle and a Chrome extension are the only client libraries.'
finops:
- has_sources: true
  method: derived
  name: Green Screens Ai Finops
  primary_unit: ''
  service_category: ''
  slug: green-screens-ai-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/green-screens-ai.png
layout: provider
modified: '2026-09-12'
name: Green Screens AI
nav: Providers
network: true
overview: 'Green Screens AI publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Prediction API, Auth API, Analytics API, and 6 more. Tagged areas include Artificial Intelligence, Freight, Logistics, Machine Learning, and Pricing.


  The Green Screens AI catalog on APIs.io includes 1 Spectral governance ruleset.


  Green Screens AI''s developer surface includes developer portal, documentation, API reference, getting-started guide, authentication, support, engineering blog, and 32 more developer resources.'
plans:
- name: Green Screens Ai Plans Pricing
  plan_count: 0
  slug: green-screens-ai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Green Screens Ai Rate Limits
  slug: green-screens-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Green Screens AI API Rules
  rule_count: 65
  severity_counts:
    error: 55
    hint: 0
    info: 2
    warn: 8
  slug: green-screens-ai-rules
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 51.2
    developer_ergonomics: 73.2
    discoverability: 66.1
    operational_transparency: 31.6
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 11.1
      derived: 0
      marker_coverage: 88.9
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/green-screens-ai/green-screens-ai-2026-06-20T182355.png
security:
- kind: authentication
  name: Green Screens Ai Authentication
  slug: green-screens-ai-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Green Screens Ai Domain Security
  slug: green-screens-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: green-screens-ai-price-an-rfp-batch
  slug: green-screens-ai-price-an-rfp-batch
- name: green-screens-ai-quote-a-lane
  slug: green-screens-ai-quote-a-lane
- name: green-screens-ai-source-capacity-and-bid
  slug: green-screens-ai-source-capacity-and-bid
- name: green-screens-ai-sync-tms-and-quotes
  slug: green-screens-ai-sync-tms-and-quotes
slug: green-screens-ai
tags:
- Artificial Intelligence
- Freight
- Logistics
- Machine Learning
- Pricing
- Transportation
website: https://triumph.io/solutions/rates/
---
