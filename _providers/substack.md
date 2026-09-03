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
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: 'Narrowly scoped official API that returns public Substack profile data for a given LinkedIn handle. Access requires accepting the Developer API Terms of Use, applying via form, and generating a token '
  name: Substack Developer API
  slug: substack-developer-api
- description: 'Official remote Model Context Protocol server that connects a Substack publication to an MCP-capable AI assistant (Claude, ChatGPT, Cursor). Read-only: it serves publication dashboard metrics, subscri'
  name: Substack MCP Server
  slug: substack-mcp-server
- description: Per-publication public RSS feeds available at https://{publication}.substack.com/feed for syndication and read-only access to posts. RSS 2.0 with the content, dc, atom and itunes namespaces; no creden
  name: Substack RSS Feeds
  slug: substack-rss-feeds
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/substack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/substack-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://substack.com/vulnerability-disclosure
- group: agent
  title: ''
  type: MCPServer
  url: mcp/substack-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/substack-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/substack-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/substack-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/substack-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/substack-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/substack-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/substack-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.substack.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/substack-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/substack-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/substack-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/substack-packages.yml
- group: design
  title: ''
  type: Components
  url: components/substack-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/substack-llms.txt
- group: company
  title: ''
  type: Website
  url: https://substack.com/
- group: company
  title: ''
  type: About
  url: https://substack.com/about
- group: operate
  title: ''
  type: Help
  url: https://support.substack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.substack.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://support.substack.com/hc/en-us/articles/43904995414164-How-to-contact-Substack-Support
- group: company
  title: ''
  type: Blog
  url: https://on.substack.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://on.substack.com/feed
- group: commercial
  title: ''
  type: Pricing
  url: https://support.substack.com/hc/en-us/articles/360037607131-How-much-does-Substack-cost
- group: commercial
  title: ''
  type: Pricing
  url: https://substack.com/going-paid
- group: start
  title: ''
  type: SignUp
  url: https://substack.com/signup
- group: start
  title: ''
  type: Login
  url: https://substack.com/sign-in
- group: company
  title: ''
  type: Jobs
  url: https://substack.com/jobs
- group: operate
  title: ''
  type: Contact
  url: https://substack.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://substack.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://substack.com/privacy
- group: docs
  title: ''
  type: ContentGuidelines
  url: https://substack.com/content
- group: other
  title: ''
  type: Accessibility
  url: https://substack.com/accessibility
- group: other
  title: ''
  type: Sitemap
  url: https://substack.com/sitemap
- group: other
  title: ''
  type: BrandAssets
  url: https://substack.com/brand
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/substackinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/substack
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SubstackInc
created: '2026-05-08'
description: Substack is an independent newsletter and media platform that lets writers, podcasters, video creators, and other culture makers publish directly to readers and monetize through paid subscriptions. Founded in 2017 by Chris Best (CEO), Jairaj Sethi (CTO), and Hamish McKenzie (CWO) and headquartered in San Francisco with a New York City office, Substack provides built-in subscription billing, paid posts, podcasting, chat, video, Notes, and a cross-publication recommendations network. Creators keep 90 percent of subscription revenue (less credit card fees) and own their mailing lists and content. The platform reports more than five million paid subscriptions and tens of millions of weekly active readers. Substack does not offer a general-purpose public REST API for managing publications, posts, or subscribers. It does publish a narrowly scoped official Developer API (released April 2026) that allows token-authenticated lookup of public Substack profiles by LinkedIn handle, gated
  by an application and Terms-of-Use process. Substack also runs an official remote MCP server at https://mcp.substack.com/api/v1/mcp, documented August 2026, which gives an MCP-capable AI assistant read-only access to publication analytics under OAuth 2.1 with the mcp:read scope, gated to Admins of Bestseller publications. Read access to public content is otherwise available via per-publication RSS feeds, and the broader integration ecosystem relies on reverse-engineered, unofficial JSON endpoints used by the Substack web application. Substack publishes no OpenAPI, no AsyncAPI, no webhooks and no first-party SDK in any package registry.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/substack.png
layout: provider
mcp_servers:
- description: ''
  name: Substack
  slug: substack
modified: '2026-08-13'
name: Substack
nav: Providers
network: true
overview: 'Substack publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Newsletters, Publishing, Creator Economy, Subscription, and Email.


  Substack''s developer surface includes authentication, changelog, documentation, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Substack Plans Pricing
  plan_count: 2
  slug: substack-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Substack Rate Limits
  slug: substack-rate-limits
scopes:
- name: Substack Scopes
  scope_count: 8
  slug: substack-scopes
  summary_line: 8 scopes · authorizationCode/deviceCode/implicit
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 36.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/substack/refs/heads/main/screenshots/substack-2026-06-20T194631.png
security:
- kind: authentication
  name: Substack Authentication
  slug: substack-authentication
  summary_line: oauth2/openIdConnect/http · 4 schemes
- kind: domain-security
  name: Substack Domain Security
  slug: substack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Substack Vulnerability Disclosure
  slug: substack-vulnerability-disclosure
  summary_line: disclosure policy published
slug: substack
tags:
- Newsletters
- Publishing
- Creator Economy
- Subscription
- Email
- Podcasting
- Notes
- Media
- Independent Media
- Paid Content
- MCP
- Agents
- RSS
- Analytics
website: https://substack.com/
---
