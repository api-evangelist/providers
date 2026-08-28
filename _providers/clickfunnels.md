---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 224
  human_in_the_loop: 4
  name: Clickfunnels Agentic Access
  operation_count: 418
  slug: clickfunnels-agentic-access
  summary_line: 418 operations · 224 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: 'The ClickFunnels 2.0 REST API — 418 operations across 230 paths and 102 resource tags, covering the whole platform: teams, users, workspaces, sites, funnels, pages, blogs, communities, courses, contac'
  name: ClickFunnels API
  slug: clickfunnels-api
artifact_total: 12
asyncapis:
- description: ''
  name: Clickfunnels Webhooks
  slug: clickfunnels-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ClickFunnels API
  slug: open-clickfunnels-api
- collection_type: open
  name: ClickFunnels 2.0 API
  slug: open-clickfunnels
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/clickfunnels-api-openapi-original.json
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clickfunnels-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clickfunnels-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/clickfunnels-api-catalog.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/clickfunnels-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/clickfunnels-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clickfunnels-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clickfunnels-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/clickfunnels-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clickfunnels-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.myclickfunnels.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/clickfunnels-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clickfunnels-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/clickfunnels-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/clickfunnels-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/clickfunnels-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/clickfunnels-cli.yml
- group: design
  title: ''
  type: Components
  url: components/clickfunnels-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/clickfunnels-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clickfunnels-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clickfunnels-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/clickfunnels-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clickfunnels-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clickfunnels-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.myclickfunnels.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.myclickfunnels.com/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://developers.myclickfunnels.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.myclickfunnels.com/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.myclickfunnels.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.myclickfunnels.com
- group: company
  title: ''
  type: Blog
  url: https://www.clickfunnels.com/blog/feed
- group: company
  title: ''
  type: Website
  url: https://www.clickfunnels.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clickfunnels.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://signup.clickfunnels.com
- group: start
  title: ''
  type: Login
  url: https://accounts.myclickfunnels.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clickfunnels.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clickfunnels.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clickfunnels
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clickfunnels2
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/clickfunnels/cli
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clickfunnels
- group: other
  title: ''
  type: Classic API
  url: https://apidocs.clickfunnels.com/
created: '2026-05-11'
description: 'ClickFunnels is a sales funnel and online business platform that lets entrepreneurs build landing pages, sales funnels, checkout flows, courses, membership sites, communities, blogs and email marketing campaigns without code. The ClickFunnels 2.0 REST API is a 418-operation OpenAPI 3.1 contract covering teams, workspaces, funnels, pages, blogs, products, discounts, orders, invoices, transactions, subscriptions, contacts, courses, communities, forms, workflows, email and analytics, authenticated with a team-scoped Bearer token or with workspace-scoped OAuth 2.0. It is discoverable the correct way: an RFC 9727 api-catalog links the spec, RFC 8414 metadata publishes the OAuth scopes, and sixteen Markdown Agent Skills are served from /.well-known/ for agents driving the API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clickfunnels.png
layout: provider
modified: '2026-08-13'
name: ClickFunnels
nav: Providers
network: true
overview: 'ClickFunnels publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Funnels, Landing Pages, E-Commerce, Marketing, and Checkout.


  The ClickFunnels catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ClickFunnels'' developer surface includes authentication, changelog, CLI, sandbox, documentation, API reference, getting-started guide, and 36 more developer resources.'
plans:
- name: Clickfunnels Plans Pricing
  plan_count: 4
  slug: clickfunnels-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Clickfunnels Rate Limits
  slug: clickfunnels-rate-limits
scopes:
- name: Clickfunnels Scopes
  scope_count: 5
  slug: clickfunnels-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: strong
  composite: 64.3
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 30.3
    contract_quality: 66.7
    developer_ergonomics: 66.7
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 34.2
  previous_composite: 64.3
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clickfunnels/refs/heads/main/screenshots/clickfunnels-2026-06-20T174514.png
security:
- kind: authentication
  name: Clickfunnels Authentication
  slug: clickfunnels-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Clickfunnels Domain Security
  slug: clickfunnels-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clickfunnels Vulnerability Disclosure
  slug: clickfunnels-vulnerability-disclosure
  summary_line: Hackerone
slug: clickfunnels
tags:
- Sales Funnels
- Landing Pages
- E-Commerce
- Marketing
- Checkout
- CRM
- Email Marketing
- Online Courses
- Webhook
- Website Builder
- Subscription
- Marketing Automation
- Agent Skills
website: https://www.clickfunnels.com
---
