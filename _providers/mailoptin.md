---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The WordPress REST API served by mailoptin.io, plus the Model Context Protocol server exposed through the WordPress MCP Adapter at the mcp namespace. The REST root is a public, self-describing route i
  name: MailOptin Site REST API and MCP Server
  slug: mailoptin-site
artifact_total: 8
asyncapis:
- description: ''
  name: Mailoptin Webhooks
  slug: mailoptin-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://mailoptin.io/
- group: docs
  title: ''
  type: Documentation
  url: https://mailoptin.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://mailoptin.io/section/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://mailoptin.io/support/
- group: company
  title: ''
  type: Blog
  url: https://mailoptin.io/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://mailoptin.io/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailoptin
- group: commercial
  title: ''
  type: Pricing
  url: https://mailoptin.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://my.mailoptin.io/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mailoptin.io/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mailoptin.io/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mailoptin-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mailoptin-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mailoptin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mailoptin-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/mailoptin-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mailoptin-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mailoptin-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mailoptin-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mailoptin-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mailoptin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mailoptin-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mailoptin-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mailoptin-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mailoptin-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mailoptin-domain-security.yml
created: '2026-08-12'
description: 'MailOptin is a WordPress lead-generation and email-automation plugin that converts website visitors into subscribers with popups, slide-ins, notification bars and inline optin forms, then sends one-off newsletters and event-triggered automated emails. It connects WordPress to more than sixty email marketing platforms, CRMs, form plugins, e-commerce and membership systems — Mailchimp, ActiveCampaign, HubSpot, AWeber, Klaviyo, Brevo, Salesforce, WooCommerce and others — and can post optin submissions to an arbitrary endpoint through a generic webhook connection. MailOptin is self-hosted software rather than a hosted service: it publishes no product API, no OpenAPI and no client SDK, and all functionality runs inside the customer''s own WordPress installation. Its own website, mailoptin.io, runs WordPress and does serve a public self-describing REST API together with an OAuth-protected Model Context Protocol server.'
image: https://mailoptin.io/wp-content/uploads/2014/05/mailoptin-plugin-banner.png
layout: provider
mcp_servers:
- description: 'mailoptin.io runs a live Model Context Protocol server, exposed through the WordPress MCP Adapter as the `mcp` namespace of the site''s REST API. It was discovered from the RFC 9728 protected-resource '
  name: MailOptin Site MCP Server
  slug: mailoptin-site-mcp-server
modified: '2026-08-12'
name: MailOptin
nav: Providers
network: true
overview: 'MailOptin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email Marketing, Marketing Automation, Lead Generation, and WordPress.


  The MailOptin catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MailOptin''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 19 more developer resources.'
plans:
- name: Mailoptin Plans Pricing
  plan_count: 5
  slug: mailoptin-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Mailoptin Rate Limits
  slug: mailoptin-rate-limits
scopes:
- name: Mailoptin Scopes
  scope_count: 0
  slug: mailoptin-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.5
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 46.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mailoptin/refs/heads/main/screenshots/mailoptin-2026-08-17T124048.png
security:
- kind: authentication
  name: Mailoptin Authentication
  slug: mailoptin-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Mailoptin Domain Security
  slug: mailoptin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mailoptin
tags:
- Company
- Email Marketing
- Marketing Automation
- Lead Generation
- WordPress
- Newsletters
- Webhook
- MCP
- Plugins
website: https://mailoptin.io/
---
