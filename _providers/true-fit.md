---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 27
  human_in_the_loop: 2
  name: True Fit Agentic Access
  operation_count: 58
  slug: true-fit-agentic-access
  summary_line: 58 operations · 27 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: Server-to-server REST API for managing True Fit profiles on behalf of your own users and requesting size recommendations for retailer products. Covers identity sync, profiles, body measurements, close
  name: True Fit Partner API
  slug: partner-api
- description: 'Browser/device-facing REST API used to build a custom True Fit integration: session tokens, shopper profiles and recipient profiles, closet items, brands, sizes, bra sizes, inseams, sleeve lengths, st'
  name: True Fit Consumer API
  slug: consumer-api
- description: 'Two-endpoint data API that packages True Fit machine-learning assets for a retailer partner: a Metadata endpoint returning the descriptor of the current weekly 360 Member View file (client id, created'
  name: True Fit 360 Member View API
  slug: 360-member-view-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/true-fit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/true-fit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/true-fit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.truefit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://techdocs.truefitcorp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://techdocs.truefitcorp.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://techdocs.truefitcorp.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://techdocs.truefitcorp.com/docs/product-detail-page-integration
- group: operate
  title: ''
  type: Support
  url: https://www.truefit.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.truefit.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truefit.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truefit.com/privacy-policy-and-choices
- group: other
  title: ''
  type: Marketplace
  url: https://apps.shopify.com/truefit
- group: docs
  title: ''
  type: TechnicalSpecification
  url: https://www.truefit.com/fit-intelligence-spec
- group: auth
  title: ''
  type: Compliance
  url: https://www.truefit.com/gdpr-faq
- group: auth
  title: ''
  type: PrivacyDisclosures
  url: https://www.truefit.com/us-state-privacy-disclosures
- group: operate
  title: ''
  type: StatusPage
  url: https://status.truefit.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://techdocs.truefitcorp.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/true-fit-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/true-fit-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/true-fit-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/true-fit-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/true-fit-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/true-fit-error-codes.yml
- group: build
  title: ''
  type: Packages
  url: packages/true-fit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/true-fit-packages.yml
- group: other
  title: ''
  type: CDN
  url: https://cdn.truefitcorp.com/fitrec/global/js/tf-integration.js
- group: design
  title: ''
  type: Components
  url: components/true-fit-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/true-fit-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/true-fit-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/true-fit-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/true-fit-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/true-fit-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/true-fit-techdocs-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: well-known/true-fit-robots.txt
created: '2026-08-05'
description: True Fit Corporation is an AI-powered fit and sizing intelligence platform for apparel and footwear ecommerce. Its Fashion Genome dataset is built on roughly two decades of real purchase-and-return outcomes across 100M+ registered shoppers, 60M unique products and 91K+ brands, and powers size recommendations, fit confidence scores, cross-brand size calibration and shopper fit profiles. True Fit ships as a product-detail-page JavaScript widget, a Shopify app, native iOS/Android/React Native SDKs, a documented Partner REST API and Consumer REST API, a 360 Member View data API, and a Fit Intelligence Layer exposed to AI agents over the Model Context Protocol.
image: https://cdn.prod.website-files.com/64ee50f98275d03e3242bdef/69d410679088692a9df73243_256px%20webclip.png
layout: provider
mcp_servers:
- description: ''
  name: true-fit-mcp.yml
  slug: true-fit-mcpyml
modified: '2026-08-05'
name: True Fit
nav: Providers
network: true
overview: 'True Fit publishes 2 APIs on the [APIs.io](https://apis.io/) network: Partner API and Consumer API. Tagged areas include Company, Fit and Sizing, Apparel, Footwear, and Retail.


  True Fit''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 29 more developer resources.'
random_paper: 25
score:
  band: developing
  composite: 46.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.0
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: True Fit Authentication
  slug: true-fit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: True Fit Domain Security
  slug: true-fit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: true-fit
tags:
- Company
- Fit and Sizing
- Apparel
- Footwear
- Retail
- E-Commerce
- Recommendations
- Personalization
- Artificial Intelligence
- Agentic Commerce
- Model Context Protocol
website: https://www.truefit.com/
---
