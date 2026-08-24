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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.9
  scored_at: '2026-08-24'
api_count: 11
apis:
- description: Category terms used to classify posts.
  name: Lish Categories API
  slug: lish-categories-api
- description: Comments left on Lish posts.
  name: Lish Comments API
  slug: lish-comments-api
- description: Media library items (images, attachments).
  name: Lish Media API
  slug: lish-media-api
- description: Static marketing pages on the Lish site.
  name: Lish Pages API
  slug: lish-pages-api
- description: Blog posts published on the Lish site.
  name: Lish Posts API
  slug: lish-posts-api
- description: Cross-resource search over site content.
  name: Lish Search API
  slug: lish-search-api
- description: Registered post statuses.
  name: Lish Statuses API
  slug: lish-statuses-api
- description: Tag terms used to classify posts.
  name: Lish Tags API
  slug: lish-tags-api
- description: Registered taxonomies.
  name: Lish Taxonomies API
  slug: lish-taxonomies-api
- description: Registered post types.
  name: Lish Types API
  slug: lish-types-api
- description: Post authors exposed by the site.
  name: Lish Users API
  slug: lish-users-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lish WordPress REST Categories API
  slug: open-lish-categories-api
- collection_type: open
  name: Lish WordPress REST Categories Comments API
  slug: open-lish-comments-api
- collection_type: open
  name: Lish WordPress REST Categories Media API
  slug: open-lish-media-api
- collection_type: open
  name: Lish WordPress REST Categories Pages API
  slug: open-lish-pages-api
- collection_type: open
  name: Lish WordPress REST Categories Posts API
  slug: open-lish-posts-api
- collection_type: open
  name: Lish WordPress REST Categories Search API
  slug: open-lish-search-api
- collection_type: open
  name: Lish WordPress REST Categories Statuses API
  slug: open-lish-statuses-api
- collection_type: open
  name: Lish WordPress REST Categories Tags API
  slug: open-lish-tags-api
- collection_type: open
  name: Lish WordPress REST Categories Taxonomies API
  slug: open-lish-taxonomies-api
- collection_type: open
  name: Lish WordPress REST Categories Types API
  slug: open-lish-types-api
- collection_type: open
  name: Lish WordPress REST Categories Users API
  slug: open-lish-users-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lish-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lish-wordpress-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lish-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lish-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lish-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lish-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lish-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lish-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lish-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lish-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.lishfood.com
- group: company
  title: ''
  type: Blog
  url: https://www.lishfood.com/blog
- group: company
  title: ''
  type: About
  url: https://www.lishfood.com/pages/about
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.lishfood.com/pages/faq
- group: operate
  title: ''
  type: Support
  url: https://www.lishfood.com/pages/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.lishfood.com/pages/get-started
- group: start
  title: ''
  type: Login
  url: https://www.lishfood.com/account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lishfood.com/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lishfood.com/pages/privacy
created: '2026-07-17'
description: 'Lish is a corporate catering and workplace food service company serving Seattle and the Bellevue/Eastside area of Washington, including Redmond and Kirkland. It connects employers with a curated roster of local partner chefs and runs the whole workplace meal program — menu curation, ordering, delivery and setup — across four service lines: subscription catering, PopUp restaurants that employees buy from directly, on-demand one-off catering, and occasion catering for breakfast, lunch, box lunches, happy hours, meetings and events. The company reports more than 3,000,000 meals served, 100+ curated menus from dozens of partner chefs, an average meal rating of 4.6 stars, and 97.8% of orders delivered on time within a 20-minute window, with dietary accommodation (gluten-free, vegetarian, vegan, dairy-free) as a stated focus. Lish describes an admin dashboard, budget tracking, GPS delivery tracking, Google Calendar and Outlook menu visibility and Slack feedback notifications, but
  these are end-user product integrations — Lish operates no developer program and publishes no product API. The only public, self-describing HTTP API is the WordPress REST API behind its marketing site, profiled here.'
image: https://www.lishfood.com/wp-content/uploads/2024/05/Lish-Hero-Lish_part_two_finals080jpghalf.jpg
layout: provider
mcp_servers:
- description: ''
  name: Lish MCP Server
  slug: lish-mcp-server
modified: '2026-07-19'
name: Lish
nav: Providers
network: true
overview: 'Lish publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Comments API, Media API, and 8 more. Tagged areas include Company, Catering, Food and Beverage, Food Delivery, and Workplace.


  Lish''s developer surface includes authentication, engineering blog, support, signup flow, and 16 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 24.7
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 14.2
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 24.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lish/refs/heads/main/screenshots/lish-2026-07-25T225325.png
security:
- kind: authentication
  name: Lish Authentication
  slug: lish-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lish Domain Security
  slug: lish-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lish
tags:
- Company
- Catering
- Food and Beverage
- Food Delivery
- Workplace
- Corporate Services
- Content
website: https://www.lishfood.com
---
