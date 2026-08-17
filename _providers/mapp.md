---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 63.1
  scored_at: '2026-08-17'
api_count: 4
apis:
- description: 'The Mapp Engage REST API (REST 2.0, incremental version v19) exchanges data between external systems and Mapp Engage: create and update contacts, manage group memberships and attributes, send single, '
  name: Mapp Engage API
  slug: engage
- description: The Mapp Intelligence Analytics API gives programmatic access to Mapp Intelligence (formerly Webtrekk) digital-analytics data and functions — submit analysis queries (pivot, comparison, time series, p
  name: Mapp Intelligence Analytics API
  slug: intelligence-analytics
- description: The Product Catalog Public API manages product and variant data inside Mapp Cloud catalogs — create, replace, partially update, upsert, bulk-load and delete variants, manage variant attributes, read c
  name: Mapp Product Catalog Public API
  slug: product-catalog
- description: 'The Mapp Fashion (formerly Dressipi) recommendation API returns curated fashion and retail recommendations: related and complementary items for a seed product, themed and facetted recommendations, top'
  name: Mapp Fashion API
  slug: fashion
artifact_total: 17
asyncapis:
- description: ''
  name: Mapp Data Streams
  slug: mapp-data-streams
collections:
- collection_type: open
  name: Mapp Engage public API
  slug: open-mapp-engage
- collection_type: open
  name: Mapp Fashion API
  slug: open-mapp-fashion
- collection_type: open
  name: Analytics API
  slug: open-mapp-intelligence-analytics
- collection_type: open
  name: Product Catalog - Public API
  slug: open-mapp-product-catalog
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/mapp-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/mapp-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mapp-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mapp-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mapp-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mapp-tool-crosswalk.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mapp-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mapp-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mapp-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.mapp.com/docs/news
- group: design
  title: ''
  type: Conventions
  url: conventions/mapp-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mapp-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mapp-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mapp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mapp-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Events
  url: asyncapi/mapp-data-streams.yml
- group: other
  title: ''
  type: StreamingEndpoint
  url: asyncapi/mapp-data-streams.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mapp-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mapp-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mapp-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mapp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mapp.com/docs/api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mapp.com/apidocs/engage-api-calls
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mapp.com/apidocs/getting-started-with-engage-api
- group: operate
  title: ''
  type: Support
  url: https://support.mapp.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://mapp.com/technical-support/
- group: company
  title: ''
  type: Blog
  url: https://mapp.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mapp-digital
- group: commercial
  title: ''
  type: Pricing
  url: https://mapp.com/mapp-marketing-cloud-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://mapp.com/request-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mapp.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mapp.com/privacy-mapp-cloud/
- group: auth
  title: ''
  type: TrustCenter
  url: https://mapp.com/trust/
- group: auth
  title: ''
  type: Compliance
  url: https://mapp.com/trust/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.webtrekk.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.mapp.com/docs/news
- group: build
  title: ''
  type: Postman
  url: https://docs.mapp.com/apidocs/postman
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mapp-llms.txt
created: '2026-08-12'
description: 'Mapp is a German-headquartered marketing technology vendor whose Mapp Marketing Cloud combines cross-channel campaign execution (Mapp Engage), digital analytics and customer intelligence (Mapp Intelligence, formerly Webtrekk), product catalog management, and AI fashion/retail recommendations (Mapp Fashion, formerly Dressipi). The platform is API-addressable across four public surfaces: the Mapp Engage REST API (REST 2.0 / v19, HTTP Basic auth, ~196 documented operations covering contacts, memberships, groups, messages, mobile push, segmentation, whiteboards, attributes, e-commerce events and audit logs), the Mapp Intelligence Analytics API (OAuth2 client-credentials on api.mapp.com/api/analytics), the Product Catalog Public API, and the Mapp Fashion recommendation API. Mapp publishes machine-readable OpenAPI fragments for every endpoint on docs.mapp.com, an llms.txt documentation index, published list pricing, and an ISO 27001/27017/27018/27701/22301 trust center.'
image: https://mapp.com/wp-content/uploads/2026/05/mapp-default-open-graph-image-square.png
layout: provider
mcp_servers:
- description: ''
  name: mapp-mcp.yml
  slug: mapp-mcpyml
modified: '2026-08-12'
name: Mapp Marketing Cloud
nav: Providers
network: true
overview: 'Mapp Marketing Cloud publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Mapp Engage API, Mapp Intelligence Analytics API, Mapp Product Catalog Public API, and 1 more. Tagged areas include Company, Marketing, Marketing Automation, Email, and Analytics.


  The Mapp Marketing Cloud catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mapp Marketing Cloud''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 33 more developer resources.'
plans:
- name: Mapp Plans Pricing
  plan_count: 3
  slug: mapp-plans-pricing
random_paper: 132
rate_limits:
- limit_count: 1
  name: Mapp Rate Limits
  slug: mapp-rate-limits
scopes:
- name: Mapp Scopes
  scope_count: 2
  slug: mapp-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: exemplar
  composite: 69.0
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 60.9
    developer_ergonomics: 78.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 65.8
  previous_composite: 69.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 65.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Mapp Authentication
  slug: mapp-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Mapp Domain Security
  slug: mapp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mapp Vulnerability Disclosure
  slug: mapp-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Mapp Trust Center
  slug: mapp-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018, ISO 27701, ISO 22301, GDPR, CCPA, NIS-2, DORA, Certified Sender Alliance
slug: mapp
tags:
- Company
- Marketing
- Marketing Automation
- Email
- Analytics
- Customer Data
- Personalization
- Push Notifications
- SMS
- E-Commerce
- Digital Analytics
- Recommendations
website: https://mapp.com/
---
