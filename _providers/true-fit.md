---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 27
  human_in_the_loop: 2
  name: True Fit Agentic Access
  operation_count: 58
  slug: true-fit-agentic-access
  summary_line: 58 operations · 27 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: 'Two-endpoint data API that packages True Fit machine-learning assets for a retailer partner: a Metadata endpoint returning the descriptor of the current weekly 360 Member View file (client id, created'
  name: True Fit 360 Member View API
  slug: 360-member-view-api
- description: Provide session information for more advanced reporting.
  name: True Fit Analytics API
  slug: true-fit-analytics-api
- description: Endpoints to allow saving and logging in to a True Fit account.
  name: True Fit Auth API
  slug: true-fit-auth-api
- description: The bra sizes that are available to choose from for the bra size measurement on a Women's profile.
  name: True Fit Bra Sizes API
  slug: true-fit-bra-sizes-api
- description: The brands that are available to choose from when entering a reference closet item.
  name: True Fit Brands API
  slug: true-fit-brands-api
- description: An endpoint for tracking checkout events.
  name: True Fit Checkout API
  slug: true-fit-checkout-api
- description: Information about the profile's closet.
  name: True Fit Closet API
  slug: true-fit-closet-api
- description: Retrieve True Fit powered product recommendations for the shopper profile.
  name: True Fit Discovery Recommendation API
  slug: true-fit-discovery-recommendation-api
- description: Retrieve True Fit powered size recommendations for a profile.
  name: True Fit Fit Recommendation API
  slug: true-fit-fit-recommendation-api
- description: Establishing a True Fit user for one of your users.
  name: True Fit Identity API
  slug: true-fit-identity-api
- description: The available inseam lengths to choose from for the inseam measurement on a profile.
  name: True Fit Inseams API
  slug: true-fit-inseams-api
- description: Body measurements attached to a profile.
  name: True Fit Measurements API
  slug: true-fit-measurements-api
- description: Retrieve normalized sizes for the shopper profile.
  name: True Fit Normalized Sizes API
  slug: true-fit-normalized-sizes-api
- description: An endpoint for rating discovery recommendations.
  name: True Fit Product Ratings API
  slug: true-fit-product-ratings-api
- description: The products available at a store.
  name: True Fit Products API
  slug: true-fit-products-api
- description: Information about the person being shopped for.
  name: True Fit Profile API
  slug: true-fit-profile-api
- description: Creating and managing fit profiles belonging to a partner user.
  name: True Fit Profiles API
  slug: true-fit-profiles-api
- description: Size recommendations and general fit guidance for retailer products.
  name: True Fit Recommendations API
  slug: true-fit-recommendations-api
- description: The sizes that are available to choose from when entering a reference closet item.
  name: True Fit Sizes API
  slug: true-fit-sizes-api
- description: The available sleeve lengths to choose from for the sleeve length measurement on a profile.
  name: True Fit Sleeve Lengths API
  slug: true-fit-sleeve-lengths-api
- description: The style attributes available for particular ageGroup, gender, category and optional class combination.
  name: True Fit Style Attributes API
  slug: true-fit-style-attributes-api
- description: A token is used to identify requests from a device and associate the requests with a session. As the user interacts with True Fit, the token will update. The most recent token returned by True Fit sho
  name: True Fit Token API
  slug: true-fit-token-api
artifact_total: 48
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: True Fit - Consumer Analytics API
  slug: open-true-fit-analytics-api
- collection_type: open
  name: True Fit - Consumer Auth API
  slug: open-true-fit-auth-api
- collection_type: open
  name: True Fit - Consumer Bra Sizes API
  slug: open-true-fit-bra-sizes-api
- collection_type: open
  name: True Fit - Consumer Brands API
  slug: open-true-fit-brands-api
- collection_type: open
  name: True Fit - Consumer Checkout API
  slug: open-true-fit-checkout-api
- collection_type: open
  name: True Fit Closet API
  slug: open-true-fit-closet-api
- collection_type: open
  name: True Fit - Consumer Discovery Recommendation API
  slug: open-true-fit-discovery-recommendation-api
- collection_type: open
  name: True Fit - Consumer Fit Recommendation API
  slug: open-true-fit-fit-recommendation-api
- collection_type: open
  name: True Fit Partner Identity API
  slug: open-true-fit-identity-api
- collection_type: open
  name: True Fit - Consumer Inseams API
  slug: open-true-fit-inseams-api
- collection_type: open
  name: True Fit Partner Measurements API
  slug: open-true-fit-measurements-api
- collection_type: open
  name: True Fit - Consumer Normalized Sizes API
  slug: open-true-fit-normalized-sizes-api
- collection_type: open
  name: True Fit - Consumer Product Ratings API
  slug: open-true-fit-product-ratings-api
- collection_type: open
  name: True Fit - Consumer Products API
  slug: open-true-fit-products-api
- collection_type: open
  name: True Fit - Consumer Profile API
  slug: open-true-fit-profile-api
- collection_type: open
  name: True Fit Partner Profiles API
  slug: open-true-fit-profiles-api
- collection_type: open
  name: True Fit Partner Recommendations API
  slug: open-true-fit-recommendations-api
- collection_type: open
  name: True Fit - Consumer Sizes API
  slug: open-true-fit-sizes-api
- collection_type: open
  name: True Fit - Consumer Sleeve Lengths API
  slug: open-true-fit-sleeve-lengths-api
- collection_type: open
  name: True Fit - Consumer Style Attributes API
  slug: open-true-fit-style-attributes-api
- collection_type: open
  name: True Fit - Consumer Token API
  slug: open-true-fit-token-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/true-fit-consumer-api-overlay.yaml
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
- description: True Fit publicly markets a "Fit Intelligence Layer via MCP" as one of its activation paths, described in section 7 of its own technical specification. NO public MCP endpoint, tools/list manifest, reg
  name: True Fit MCP Server
  slug: true-fit-mcp-server
modified: '2026-08-05'
name: True Fit
nav: Providers
network: true
overview: 'True Fit publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Auth API, Bra Sizes API, and 18 more. Tagged areas include Company, Fit and Sizing, Apparel, Footwear, and Retail.


  True Fit''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 30 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 46.3
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 23.8
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/true-fit/refs/heads/main/screenshots/true-fit-2026-08-17T082444.png
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
- MCP
website: https://www.truefit.com/
---
