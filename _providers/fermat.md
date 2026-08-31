---
access_model:
  confidence: high
  label: Customer only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.fermatcommerce.com/pricing (301 to root)
  - https://help.fermatcommerce.com/en/articles/14431099-fermat-mcp-connect-your-commerce-data-to-ai-tools
  - https://help.fermatcommerce.com/en/articles/14280269-fermat-pixel-v2-installation-guide-direct-script-google-tag-manager
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: Remote Model Context Protocol server exposing 64 read-only tools over FERMAT commerce data — product catalog, funnel analytics, ad performance, destination insights, experiments, session and behaviora
  name: FERMAT Platform MCP Server
  slug: fermat-platform-mcp-server
- description: First-party browser ES module (claire.mjs) a brand embeds to emit commerce telemetry to FERMAT. Exposes a window.fermat command queue with init, track and status methods, and six documented events — p
  name: FERMAT Pixel v2
  slug: fermat-pixel-v2
artifact_total: 8
asyncapis:
- description: 'Browser-to-FERMAT commerce telemetry. A brand installs the FERMAT Pixel v2 and calls window.fermat({ method: "track", eventName, properties }) for each of the six documented commerce events. Events ar'
  name: FERMAT Pixel v2 Event Ingest
  slug: fermat-pixel-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.fermatcommerce.com/
- group: company
  title: ''
  type: About
  url: https://www.fermatcommerce.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.fermatcommerce.com/resources
- group: company
  title: ''
  type: Newsroom
  url: https://www.fermatcommerce.com/newsroom
- group: operate
  title: ''
  type: Support
  url: https://help.fermatcommerce.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.fermatcommerce.com/en/
- group: start
  title: ''
  type: Login
  url: https://app.fermatcommerce.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fermatcommerce.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fermatcommerce.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.fermatcommerce.com/en/articles/11588666-what-s-new-at-fermat-product-features-and-updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fermat-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.fermatcommerce.com/subprocessor-list
- group: design
  title: ''
  type: Conformance
  url: conformance/fermat-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fermat-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.fermatcommerce.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.fermatcommerce.com/mcp/fermat-mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://help.fermatcommerce.com/en/articles/14431099-fermat-mcp-connect-your-commerce-data-to-ai-tools
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fermat-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fermat-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fermat-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fermat-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fermat-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fermat-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fermat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fermat-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/fermat-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fermat-packages.yml
- group: design
  title: ''
  type: Components
  url: components/fermat-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fermat-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/fermat-pixel-asyncapi.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fermat-llms.txt
created: '2026-07-17'
description: FERMÀT is an AI-native commerce platform that consolidates the shopper analytics, personalization, and experimentation stack into a single agentic system for direct-to-consumer and enterprise brands. It runs a closed loop — detect shopper behavior, recommend revenue-optimizing actions, generate adaptive storefront experiences and product pages, then feed performance signals back into detection — replacing tools like FullStory, Amplitude, Algolia, and Optimizely. FERMÀT integrates with ecommerce platforms including Shopify Plus, Salesforce Commerce Cloud, Adobe Commerce, and Oracle ATG via batch and streaming data syncs, and serves brands such as Glossier, GNC, Backcountry, AWAY, Travelpro, and TONAL. Surfaced as a portfolio company of Bain Capital Ventures, Greylock, and QED Investors.
image: https://www.fermatcommerce.com/assets/marketing/brand/open-graph.png
layout: provider
mcp_servers:
- description: ''
  name: Fermat Platform (External)
  slug: fermat-platform-external
modified: '2026-08-13'
name: Fermat
nav: Providers
network: true
overview: 'Fermat publishes 1 API on the [APIs.io](https://apis.io/) network: Pixel v2. Tagged areas include Company, Commerce, E-Commerce, Personalization, and Analytics.


  The Fermat catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fermat''s developer surface includes engineering blog, support, changelog, documentation, API reference, getting-started guide, authentication, and 25 more developer resources.'
plans:
- name: Fermat Plans Pricing
  plan_count: 0
  slug: fermat-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Fermat Rate Limits
  slug: fermat-rate-limits
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 42.6
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 40.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fermat/refs/heads/main/screenshots/fermat-2026-07-25T214339.png
security:
- kind: authentication
  name: Fermat Authentication
  slug: fermat-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Fermat Domain Security
  slug: fermat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fermat
tags:
- Company
- Commerce
- E-Commerce
- Personalization
- Analytics
- Conversion Rate Optimization
- Artificial Intelligence
- Merchandising
- MCP
- Agentic Commerce
- Session Replay
- Experimentation
- Attribution
website: https://www.fermatcommerce.com/
---
