---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: Chord's hosted Model Context Protocol server — a remote, OAuth-protected, read-only window into a customer's Chord data warehouse. Fourteen documented tools cover schema search, saved views, prior que
  name: Chord MCP
  slug: chord-mcp
- description: The HTTP ingest surface of the Chord customer data platform. Backend systems POST track and identify events to /api/track and /api/identify, authenticated with a per-source write key (X-Write-Key head
  name: Chord CDP Ingest API
  slug: chord-cdp-ingest-api
- description: Read API for activated audiences. Once the Dynamic Audiences API destination is enabled on an account, a sync mirrors a custom audience into the API and a server-side GET on /audiences returns that us
  name: Chord Audiences API
  slug: chord-audiences-api
artifact_total: 10
asyncapis:
- description: ''
  name: Chord Commerce Events
  slug: chord-commerce-events
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/chordcommerce/chord-copilot/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chord-commerce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chordcommerce.com
- group: other
  title: ''
  type: Platform
  url: https://www.chordcommerce.com/platform
- group: other
  title: ''
  type: AI
  url: https://www.chordcommerce.com/platform/agents
- group: other
  title: ''
  type: CDP
  url: https://www.chordcommerce.com/platform/data-foundation
- group: other
  title: ''
  type: ContextLayer
  url: https://www.chordcommerce.com/platform/context-layer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chord.co
- group: docs
  title: ''
  type: OMSDocumentation
  url: https://docs.chord.co/oms
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chord.co/sdk-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chord.co/analytics-developer-docs
- group: other
  title: ''
  type: EventTracking
  url: https://docs.chord.co/chord-event-tracking
- group: other
  title: ''
  type: DataPlatform
  url: https://docs.chord.co/chord-data-platform
- group: other
  title: ''
  type: Copilot
  url: https://docs.chord.co/chord-copilot-chat
- group: build
  title: ''
  type: AnthropicIntegration
  url: https://docs.chord.co/chord-ai-models-powered-by-anthropic
- group: agent
  title: ''
  type: MCPServer
  url: mcp/chord-commerce-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chord-commerce-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/chord-commerce-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/chord-commerce-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chord-commerce-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/chord-commerce-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chord-commerce-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chord-commerce-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/chord-commerce-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chord-commerce-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chord-commerce-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chord.co
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/chord-commerce-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://chord.launchnotes.io
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/chord-commerce-events.yml
- group: design
  title: ''
  type: Components
  url: components/chord-commerce-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/chord-commerce-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/chord-commerce-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chord-commerce-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.chordcommerce.com/resources/insights
- group: other
  title: ''
  type: CaseStudies
  url: https://www.chordcommerce.com/resources/case-studies
- group: company
  title: ''
  type: About
  url: https://www.chordcommerce.com/about
- group: operate
  title: ''
  type: Support
  url: https://www.chordcommerce.com/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chordcommerce.com/request-a-demo
- group: start
  title: ''
  type: Demo
  url: https://www.chordcommerce.com/request-a-demo
- group: start
  title: ''
  type: Login
  url: https://hub.chord.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chordcommerce.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chordcommerce.com/legal/privacy-policy
- group: auth
  title: ''
  type: SecurityMeasures
  url: https://www.chordcommerce.com/legal/security-measures
- group: other
  title: ''
  type: DataProcessingAddendum
  url: https://www.chordcommerce.com/legal/data-processing-addendum
- group: other
  title: ''
  type: Subprocessors
  url: https://www.chordcommerce.com/legal/subprocessors
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chordcommerce
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chordcommerce
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/arfa
created: '2026-05-25'
description: 'Chord is a New York / Santa Barbara-based commerce data and AI platform founded in 2021 by Bryan Mahoney (CEO) and Henry Davis (President & Chairman), both former Glossier executives. Chord began as a headless commerce backbone built on top of Solidus — the open-source Spree Commerce fork written in Ruby on Rails — and has since evolved into an AI-native commerce data platform with three layers: a Data Foundation that unifies sources such as Shopify, ad platforms, and CDPs; a Context Stack that grounds AI in store-specific business context; and a set of Agents that take action across the commerce stack. Its current product surface includes Chord OMS (a Solidus-based order management system covering orders, products, promotions, subscriptions, affiliates, gift cards, returns, shipping, tax, and digital products documented at chord.stoplight.io), Chord CDP (customer data platform with identity resolution, RFM scoring, customer lifetime revenue, and destination activations), Chord
  Event Tracking (client- and server-side eventing with Shopify Web Pixel integration and consent management via OneTrust and Shopify Customer Privacy API), Chord Data Platform (analytics, predictive modeling, attribution, recommendations, Fivetran ingestion, GA4 compatibility), and Chord AI / Copilot Chat, powered by Anthropic Claude (Opus 4.5 for SQL generation, Haiku 4.5 for response generation and classification) with charts, monitors, context modeling, and natural-language data querying. Chord''s GitHub org (github.com/chordcommerce) maintains a fleet of Solidus extensions (solidus_stripe, solidus_braintree, solidus_paypal_braintree, solidus_subscriptions, solidus_virtual_gift_card, solidus_importer, solidus_avatax_certified), a consent-manager TypeScript library, a Jitsu fork for event ingestion, and example repos for eventing and analytics. Notable customers include Sonos, Blue Bottle Coffee, Rodan + Fields, MrBeast, and Ritual. Funding has come from M13 Ventures, Equal Ventures,
  Act One Ventures, Chingona Ventures, and CEAS Investments, with an $18M Series A reported by TechCrunch in 2021. The commercial model is sales-led with custom enterprise pricing gated behind a demo request.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chord-commerce.png
layout: provider
mcp_servers:
- description: 'Chord''s hosted MCP server. Gives an MCP client a read-only window into the customer''s Chord data warehouse: schema search, saved views, prior question/SQL pairs, org SQL conventions, table preview, re'
  name: Chord MCP Server
  slug: chord-mcp-server
modified: '2026-08-13'
name: Chord
nav: Providers
network: true
overview: 'Chord publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Commerce, Composable Commerce, Headless Commerce, Order Management, and OMS.


  The Chord catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Chord''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, release notes, engineering blog, and 43 more developer resources.'
plans:
- name: Chord Commerce Plans Pricing
  plan_count: 0
  slug: chord-commerce-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Chord Commerce Rate Limits
  slug: chord-commerce-rate-limits
scopes:
- name: Chord Commerce Scopes
  scope_count: 0
  slug: chord-commerce-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 61.9
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 46.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chord-commerce/refs/heads/main/screenshots/chord-commerce-2026-06-20T174322.png
security:
- kind: authentication
  name: Chord Commerce Authentication
  slug: chord-commerce-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Chord Commerce Domain Security
  slug: chord-commerce-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chord-commerce
tags:
- Commerce
- Composable Commerce
- Headless Commerce
- Order Management
- OMS
- Customer Data Platform
- CDP
- Event Tracking
- Commerce Analytics
- Customer Lifetime Value
- AI Agents
- Commerce Copilot
- Solidus
- Spree
- Ruby on Rails
- Shopify
- Direct to Consumer
website: https://www.chordcommerce.com
---
