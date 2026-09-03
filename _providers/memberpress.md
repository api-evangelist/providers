---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.1
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: WordPress MCP server shipped by the MemberPress AI Foundation add-on. It exposes membership, subscription, transaction, coupon, access-rule and reporting tools — MemberPress states 41 tools on a stand
  name: MemberPress AI Foundation MCP Server
  slug: ai-foundation-mcp
- baseURL: https://{site}/wp-json/mp/v1
  baseurl_source: declared
  description: Verify the API key and inspect permissions.
  name: MemberPress Authentication API
  slug: memberpress-authentication-api
- baseURL: https://{site}/wp-json/mp/v1
  baseurl_source: declared
  description: Discount codes applied at checkout.
  name: MemberPress Coupons API
  slug: memberpress-coupons-api
- baseURL: https://{site}/wp-json/mp/v1
  baseurl_source: declared
  description: The MemberPress event log.
  name: MemberPress Events API
  slug: memberpress-events-api
- baseURL: https://{site}/wp-json/mp/v1
  baseurl_source: declared
  description: Groups of memberships, used for pricing pages and upgrade paths.
  name: MemberPress Groups API
  slug: memberpress-groups-api
- baseURL: https://{site}/wp-json/mp/v1
  baseurl_source: declared
  description: Members are the WordPress users MemberPress tracks.
  name: MemberPress Members API
  slug: memberpress-members-api
- baseURL: https://{site}/wp-json/mp/v1
  baseurl_source: declared
  description: Memberships are the products members buy.
  name: MemberPress Memberships API
  slug: memberpress-memberships-api
- baseURL: https://{site}/wp-json/mp/v1
  baseurl_source: declared
  description: Scheduled member emails triggered by events.
  name: MemberPress Reminders API
  slug: memberpress-reminders-api
- baseURL: https://{site}/wp-json/mp/v1
  baseurl_source: declared
  description: Smart Rules that protect content and drip access.
  name: MemberPress Rules API
  slug: memberpress-rules-api
- baseURL: https://{site}/wp-json/mp/v1
  baseurl_source: declared
  description: Recurring billing agreements.
  name: MemberPress Subscriptions API
  slug: memberpress-subscriptions-api
- baseURL: https://{site}/wp-json/mp/v1
  baseurl_source: declared
  description: One-time and recurring payment records.
  name: MemberPress Transactions API
  slug: memberpress-transactions-api
- baseURL: https://{site}/wp-json/mp/v1
  baseurl_source: declared
  description: Subscribe callback URLs to MemberPress events.
  name: MemberPress Webhooks API
  slug: memberpress-webhooks-api
artifact_total: 19
asyncapis:
- description: ''
  name: Memberpress Webhooks
  slug: memberpress-webhooks
collections:
- collection_type: open
  name: MemberPress Developer Tools REST API
  slug: open-memberpress-developer-tools
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/memberpress-developer-tools-overlay.yaml
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
  name: MemberPress AI Foundation
  slug: memberpress-ai-foundation
modified: '2026-08-12'
name: MemberPress
nav: Providers
network: true
overview: 'MemberPress publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Coupons API, Events API, and 8 more. Tagged areas include Company, Membership, Subscription, WordPress, and Payments.


  The MemberPress catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MemberPress'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Memberpress Plans Pricing
  plan_count: 3
  slug: memberpress-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Memberpress Rate Limits
  slug: memberpress-rate-limits
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 22
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 25.0
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 48.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/memberpress/refs/heads/main/screenshots/memberpress-2026-08-17T081042.png
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
- Subscription
- WordPress
- Payments
- E-Commerce
- Courses
- Content Management
- Webhook
- MCP
website: https://memberpress.com/
---
