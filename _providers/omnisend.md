---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.2
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Omnisend Agentic Access
  operation_count: 60
  slug: omnisend-agentic-access
  summary_line: 60 operations · 38 acting
api_count: 15
apis:
- description: The Analytics API from Omnisend — 2 operation(s) for analytics. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Analytics API
  slug: omnisend-analytics-api
- description: The Batches API from Omnisend — 4 operation(s) for batches. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Batches API
  slug: omnisend-batches-api
- description: The Brands API from Omnisend — 2 operation(s) for brands. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Brands API
  slug: omnisend-brands-api
- description: The Campaigns API from Omnisend — 14 operation(s) for campaigns. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Campaigns API
  slug: omnisend-campaigns-api
- description: The Contacts API from Omnisend — 7 operation(s) for contacts. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Contacts API
  slug: omnisend-contacts-api
- description: The EmailContent API from Omnisend — 3 operation(s) for emailcontent. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend EmailContent API
  slug: omnisend-emailcontent-api
- description: The EmailTemplates API from Omnisend — 7 operation(s) for emailtemplates. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend EmailTemplates API
  slug: omnisend-emailtemplates-api
- description: The EmailUniversalLayouts API from Omnisend — 5 operation(s) for emailuniversallayouts. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend EmailUniversalLayouts API
  slug: omnisend-emailuniversallayouts-api
- description: The Events API from Omnisend — 1 operation(s) for events. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Events API
  slug: omnisend-events-api
- description: The Images API from Omnisend — 5 operation(s) for images. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Images API
  slug: omnisend-images-api
- description: The ProductCategories API from Omnisend — 5 operation(s) for productcategories. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend ProductCategories API
  slug: omnisend-productcategories-api
- description: The Products API from Omnisend — 5 operation(s) for products. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Products API
  slug: omnisend-products-api
- description: The Segments API from Omnisend — 6 operation(s) for segments. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Segments API
  slug: omnisend-segments-api
- description: The Automations API from Omnisend — 13 operation(s) for creating, enabling, copying and restructuring event-triggered automation workflows, including the sendWebhook action block that is Omnisend's on
  name: Omnisend Automations API
  slug: omnisend-automations-api
- description: The Event Metadata API from Omnisend — 3 operation(s) for declaring, merging and querying brand-custom event schemas. The only Omnisend operations that carry an operationId.
  name: Omnisend Event Metadata API
  slug: omnisend-event-metadata-api
arazzos:
- description: Copy an existing campaign, read the copy to confirm, then queue it for sending.
  name: Omnisend Copy and Send Campaign
  slug: omnisend-copy-and-send-campaign-workflow
- description: Create a campaign, read it back to confirm, then queue it for sending.
  name: Omnisend Create and Send Campaign
  slug: omnisend-create-and-send-campaign-workflow
- description: Create a product category, then read it back by id to confirm it was stored.
  name: Omnisend Create and Verify Product Category
  slug: omnisend-create-and-verify-category-workflow
- description: Create or update a contact, then read it back by id to confirm the write.
  name: Omnisend Create and Verify Contact
  slug: omnisend-create-and-verify-contact-workflow
- description: Create a product, then read it back by id to confirm it was stored.
  name: Omnisend Create and Verify Product
  slug: omnisend-create-and-verify-product-workflow
- description: Create a segment, read it back to confirm, then pull its membership statistics.
  name: Omnisend Create Segment and Read Statistics
  slug: omnisend-create-segment-and-stats-workflow
- description: Read a product by id, then replace it with an updated representation.
  name: Omnisend Refresh Product Catalog Entry
  slug: omnisend-replace-product-workflow
- description: Create or update a subscriber, then send a subscribed event to trigger the welcome automation.
  name: Omnisend Subscribe and Trigger Welcome
  slug: omnisend-subscribe-and-welcome-workflow
- description: Create or update a contact, then apply tags to it for segmentation.
  name: Omnisend Create and Tag Contact
  slug: omnisend-tag-contact-workflow
- description: Create or update the shopper contact, then send an added-to-cart customer event for them.
  name: Omnisend Track Added-to-Cart Event
  slug: omnisend-track-cart-event-workflow
- description: Create or update the buyer contact, then send a placed-order customer event for them.
  name: Omnisend Track Placed Order Event
  slug: omnisend-track-order-event-workflow
- description: Read a product category by id, then patch it with new values.
  name: Omnisend Update Product Category
  slug: omnisend-update-category-workflow
- description: Look up a contact by id and update it if it exists, otherwise create or update it by email.
  name: Omnisend Upsert a Contact
  slug: omnisend-upsert-contact-workflow
artifact_total: 78
asyncapis:
- description: ''
  name: Omnisend Webhooks
  slug: omnisend-webhooks
collections:
- collection_type: postman
  name: Omnisend REST API
  slug: postman-omnisend
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Analytics API
  slug: open-omnisend-analytics-api
- collection_type: open
  name: Automations API
  slug: open-omnisend-automations-api
- collection_type: open
  name: Batches API
  slug: open-omnisend-batches-api
- collection_type: open
  name: Brands API
  slug: open-omnisend-brands-api
- collection_type: open
  name: Campaigns API
  slug: open-omnisend-campaigns-api
- collection_type: open
  name: Contacts API
  slug: open-omnisend-contacts-api
- collection_type: open
  name: Email Content API
  slug: open-omnisend-emailcontent-api
- collection_type: open
  name: Email Templates API
  slug: open-omnisend-emailtemplates-api
- collection_type: open
  name: Email Universal Layouts API
  slug: open-omnisend-emailuniversallayouts-api
- collection_type: open
  name: Event Metadata API
  slug: open-omnisend-event-metadata-api
- collection_type: open
  name: Events API
  slug: open-omnisend-events-api
- collection_type: open
  name: Images API
  slug: open-omnisend-images-api
- collection_type: open
  name: Product Categories API
  slug: open-omnisend-productcategories-api
- collection_type: open
  name: Products API
  slug: open-omnisend-products-api
- collection_type: open
  name: Segments API
  slug: open-omnisend-segments-api
- collection_type: open
  name: Omnisend REST API
  slug: open-omnisend
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/omnisend-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/omnisend-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/omnisend-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/omnisend-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/omnisend-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/omnisend/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/omnisend-copy-and-send-campaign-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/omnisend-create-and-send-campaign-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/omnisend-create-and-verify-category-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/omnisend-create-and-verify-contact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/omnisend-create-and-verify-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/omnisend-create-segment-and-stats-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/omnisend-replace-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/omnisend-subscribe-and-welcome-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/omnisend-tag-contact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/omnisend-track-cart-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/omnisend-track-order-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/omnisend-update-category-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/omnisend-upsert-contact-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.omnisend.com
- group: start
  title: ''
  type: Portal
  url: https://www.omnisend.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.omnisend.com
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.omnisend.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.omnisend.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://api-docs.omnisend.com/reference/authentication
- group: auth
  title: ''
  type: OAuth
  url: https://api-docs.omnisend.com/reference/oauth
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.omnisend.com/changelog/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://api-docs.omnisend.com/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://www.omnisend.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/omnisend-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/omnisend-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/omnisend-finops.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.omnisend.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.omnisend.com/login
- group: operate
  title: ''
  type: Support
  url: https://support.omnisend.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.omnisend.com/en/articles/1061798-omnisend-api-documentation
- group: operate
  title: ''
  type: ContactSupport
  url: https://www.omnisend.com/contact-us/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.omnisend.com
- group: company
  title: ''
  type: Blog
  url: https://www.omnisend.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/omnisend
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/omnisend
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.omnisend.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.omnisend.com/terms
- group: build
  title: ''
  type: SDKs
  url: https://github.com/omnisend/php-sdk
- group: build
  title: ''
  type: Plugin
  url: https://github.com/omnisend/wp-omnisend
- group: build
  title: ''
  type: Plugin
  url: https://github.com/omnisend/magento2-plugin
- group: build
  title: ''
  type: Plugin
  url: https://www.omnisend.com/integrations/woocommerce
- group: build
  title: ''
  type: Plugin
  url: https://www.omnisend.com/integrations/shopify
- group: build
  title: ''
  type: Plugin
  url: https://www.omnisend.com/integrations/bigcommerce
- group: other
  title: ''
  type: AppMarket
  url: https://www.omnisend.com/app-market
- group: build
  title: ''
  type: Packages
  url: packages/omnisend-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/omnisend-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/omnisend-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/omnisend-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/omnisend-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/omnisend-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/omnisend-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/omnisend-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/omnisend-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/omnisend-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: security/omnisend-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/omnisend-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/omnisend-changelog.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://www.omnisend.com/changelog/#roadmap
- group: design
  title: ''
  type: Components
  url: components/omnisend-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/omnisend-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/omnisend-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.omnisend.com
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-analytics-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-automations-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-batches-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-brands-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-campaigns-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-contacts-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-emailcontent-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-emailtemplates-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-emailuniversallayouts-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-event-metadata-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-events-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-images-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-productcategories-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-products-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/omnisend-segments-api-overlay.yaml
created: '2026-05-11'
description: Omnisend is a Lithuanian-headquartered email and SMS marketing automation platform purpose-built for ecommerce, with first-class integrations into Shopify, BigCommerce, WooCommerce, Magento, Wix, Square Online, and other storefronts. The platform unifies automation workflows, campaign builders, segmentation, popups and forms, web push, product recommendations, A/B testing, and reporting to drive customer engagement and revenue. The REST API at version 2026-03-15 is served from https://api.omnisend.com/api and covers contacts, events and custom event metadata, products, product categories, segments, campaigns, automations, batches, email templates, email content, universal layouts, images, brands and analytics — 82 published operations across 15 OpenAPI 3.0.0 documents. Authentication is an API key on the Authorization header (Omnisend-API-Key {key}) or OAuth 2.0 authorization code with PKCE and 26 resource scopes; every request must also carry an Omnisend-Version header, and
  a retired version returns 410. Omnisend additionally operates two first-party hosted MCP servers at mcp.omnisend.com and is listed in Claude's Connector Directory.
features:
- Email marketing automation with prebuilt ecommerce workflows (welcome, cart abandonment, browse abandonment, order confirmation, post-purchase, win-back)
- SMS marketing with global coverage and TCPA / GDPR compliant opt-in management
- Web push notifications across desktop and mobile browsers
- Drag-and-drop campaign builder with dynamic content blocks, product recommender, and conditional logic
- Audience segmentation with behavioral, lifecycle, predictive, and custom-event criteria
- Forms, popups, and signup boxes with Wheel-of-Fortune gamified opt-ins
- A/B testing on subject lines, content, and send time
- Advanced analytics and reporting with revenue attribution per campaign and workflow
- Native integrations with Shopify, BigCommerce, WooCommerce, Wix, Square Online, Magento, and PrestaShop
- REST API with X-API-KEY and OAuth 2.0 authentication, resource-scoped permissions, and cursor-based pagination
- Batch API for bulk contact, product, and event imports (up to 100 actions per batch)
- Email Templates, Email Content, and Email Universal Layouts APIs for programmatic template management
- Customer events tracking (predefined and custom) for automation triggers
- Brands API for managing brand identity across templates
- Analytics Reports and Statistics APIs for aggregated marketing performance data
- Postman public workspace and llms.txt feed for AI-agent friendly discovery
- 24/7 live support across all paid plans
- Free plan for up to 250 contacts and 500 emails/month
finops:
- name: Omnisend Finops
  service_category: Marketing and Commerce
  slug: omnisend-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/omnisend.png
json_schemas:
- name: Omnisend Contact
  property_count: 17
  slug: omnisend-contact
- name: Omnisend Customer Event
  property_count: 8
  slug: omnisend-event
jsonld:
- class_count: 0
  name: Omnisend Context
  property_count: 7
  slug: omnisend-context
layout: provider
mcp_servers:
- description: Omnisend ships two first-party hosted, remote MCP servers — the original at https://mcp.omnisend.com/mcp (4 tools) and a v2 at https://mcp.omnisend.com/v2/mcp (7 tools). Both are HTTPS endpoints an MC
  name: Omnisend MCP Server
  slug: omnisend-mcp-server
modified: '2026-08-13'
name: Omnisend
nav: Providers
network: true
overview: 'Omnisend publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Batches API, Brands API, and 12 more. Tagged areas include Email Marketing, Marketing Automation, E-Commerce, SMS Marketing, and Customer Engagement.


  The Omnisend catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Omnisend''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, changelog, pricing, and 77 more developer resources.'
plans:
- name: Omnisend Plans Pricing
  plan_count: 4
  slug: omnisend-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 7
  name: Omnisend Rate Limits
  slug: omnisend-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Omnisend API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: omnisend-jsonschema-spectral-rules
scopes:
- name: Omnisend Scopes
  scope_count: 20
  slug: omnisend-scopes
  summary_line: 20 scopes · clientCredentials
score:
  band: exemplar
  composite: 70.3
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 40.2
    contract_quality: 74.5
    developer_ergonomics: 47.0
    discoverability: 92.6
    governance: 40.2
    operational_transparency: 97.4
  previous_composite: 70.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 80.0
      derived: 0
      marker_coverage: 100.0
      total: 15
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/screenshots/omnisend-2026-06-20T190706.png
security:
- kind: authentication
  name: Omnisend Authentication
  slug: omnisend-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Omnisend Domain Security
  slug: omnisend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Omnisend Vulnerability Disclosure
  slug: omnisend-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: omnisend
tags:
- Email Marketing
- Marketing Automation
- E-Commerce
- SMS Marketing
- Customer Engagement
- Segmentation
- Campaigns
- Forms
- Popups
- Web Push
- Automation Workflows
- Analytics
- MCP
- Agent Ready
- Transactional Messaging
website: https://www.omnisend.com
---
