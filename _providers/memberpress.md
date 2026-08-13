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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.3
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: REST API exposed by the MemberPress Developer Tools add-on on the site owner's own WordPress installation, under the WordPress REST namespace mp/v1. Covers members, memberships, transactions, subscrip
  name: MemberPress Developer Tools REST API
  slug: developer-tools-rest-api
- description: WordPress MCP server shipped by the MemberPress AI Foundation add-on. It exposes membership, subscription, transaction, coupon, access-rule and reporting tools — MemberPress states 41 tools on a stand
  name: MemberPress AI Foundation MCP Server
  slug: ai-foundation-mcp
artifact_total: 8
asyncapis:
- description: ''
  name: Memberpress Webhooks
  slug: memberpress-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/memberpress-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://memberpress.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://memberpress.com/addons/developer-tools/
- group: docs
  title: ''
  type: Documentation
  url: https://memberpress.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/caseproof/memberpress-rest-api-documentation#core-resources-and-endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://memberpress.com/docs/overview-of-using-the-developer-tools/
- group: operate
  title: ''
  type: Support
  url: https://memberpress.com/support/
- group: company
  title: ''
  type: Blog
  url: https://memberpress.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://memberpress.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/caseproof
- group: commercial
  title: ''
  type: Pricing
  url: https://memberpress.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://memberpress.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://memberpress.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://memberpress.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://memberpress.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://memberpress.com/changelog/
- group: build
  title: ''
  type: Postman
  url: postman/memberpress-api-postman-collection.json
- group: build
  title: ''
  type: Packages
  url: packages/memberpress-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/memberpress-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/memberpress-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/memberpress-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/memberpress-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/memberpress-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/memberpress-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/memberpress-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/memberpress-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/memberpress-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/memberpress-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/memberpress-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/memberpress-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/memberpress-changelog.yml
created: '2026-08-12'
description: MemberPress is a WordPress membership, course and subscription-commerce plugin built by Caseproof. It turns a self-hosted WordPress site into a paid membership business — content protection through Smart Rules, memberships and groups as products, coupons, transactions, recurring subscriptions across Stripe, PayPal, Square and Authorize.net, courses and quizzes, ClubSuite communities and CoachKit coaching. Its developer surface is the Developer Tools add-on, which exposes a REST API under the WordPress namespace /wp-json/mp/v1 on the site owner's own installation, plus a webhook subscription surface for fourteen membership and billing events. The AI Foundation add-on ships a WordPress MCP server that lets Claude, Cursor and VS Code read and act on membership data directly.
image: https://memberpress.com/wp-content/uploads/2022/10/mp-icon-RGB_Icon-01.jpg
layout: provider
mcp_servers:
- description: ''
  name: memberpress-mcp.yml
  slug: memberpress-mcpyml
modified: '2026-08-12'
name: MemberPress
nav: Providers
network: true
overview: 'MemberPress publishes 1 API on the [APIs.io](https://apis.io/) network: Developer Tools REST API. Tagged areas include Company, Membership, Subscriptions, WordPress, and Payments.


  The MemberPress catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MemberPress'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Memberpress Plans Pricing
  plan_count: 3
  slug: memberpress-plans-pricing
random_paper: 109
rate_limits:
- limit_count: 0
  name: Memberpress Rate Limits
  slug: memberpress-rate-limits
score:
  band: strong
  composite: 58.3
  facets:
    commercial_clarity: 76.3
    contract_quality: 67.9
    developer_ergonomics: 78.3
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 28.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: authentication
  name: Memberpress Authentication
  slug: memberpress-authentication
  summary_line: apiKey/wordpress-capability · 3 schemes
- kind: domain-security
  name: Memberpress Domain Security
  slug: memberpress-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: memberpress
tags:
- Company
- Membership
- Subscriptions
- WordPress
- Payments
- E-Commerce
- Courses
- Content Management
- Webhooks
- MCP
website: https://memberpress.com/
---
