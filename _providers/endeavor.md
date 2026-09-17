---
access_model:
  confidence: medium
  label: Free · no signup
  onboarding: unknown
  pricing: free
  public: true
  source:
  - '{''url'': ''https://wmegrp.com/wp-json/wp/v2/posts?per_page=1'', ''status'': 200, ''note'': "Anonymous GET returned HTTP 200 with content on 2026-09-06 — the only API surface the company serves is its corporate site''s WordPress content API, which needs no key, no account and no plan. There is nothing to buy and nothing to sign up for, so this is free-and-open access to a CMS surface, NOT a commercial API product."}'
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: A Model Context Protocol server endpoint advertised in the wmegrp.com WordPress REST route index under the "mcp" namespace and served at /wp-json/mcp/mcp-adapter-default-server. The namespace index an
  name: WME Group MCP Server (WordPress MCP Adapter)
  slug: mcp
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Blocks API from Endeavor — 6 operation(s) for blocks.
  name: Endeavor Blocks API
  slug: endeavor-blocks-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Businesses API from Endeavor — 2 operation(s) for businesses.
  name: Endeavor Businesses API
  slug: endeavor-businesses-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The BusinessesCities API from Endeavor — 2 operation(s) for businessescities.
  name: Endeavor Businesses Cities API
  slug: endeavor-businessescities-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Categories API from Endeavor — 2 operation(s) for categories.
  name: Endeavor Categories API
  slug: endeavor-categories-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Comments API from Endeavor — 2 operation(s) for comments.
  name: Endeavor Comments API
  slug: endeavor-comments-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Icons API from Endeavor — 3 operation(s) for icons.
  name: Endeavor Icons API
  slug: endeavor-icons-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Media API from Endeavor — 6 operation(s) for media.
  name: Endeavor Media API
  slug: endeavor-media-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Menus API from Endeavor — 2 operation(s) for menus.
  name: Endeavor Menus API
  slug: endeavor-menus-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Navigation API from Endeavor — 6 operation(s) for navigation.
  name: Endeavor Navigation API
  slug: endeavor-navigation-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Pages API from Endeavor — 6 operation(s) for pages.
  name: Endeavor Pages API
  slug: endeavor-pages-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Plugins API from Endeavor — 2 operation(s) for plugins.
  name: Endeavor Plugins API
  slug: endeavor-plugins-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Posts API from Endeavor — 6 operation(s) for posts.
  name: Endeavor Posts API
  slug: endeavor-posts-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The RmContentEditor API from Endeavor — 4 operation(s) for rmcontenteditor.
  name: Endeavor Rm Content Editor API
  slug: endeavor-rmcontenteditor-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Root API from Endeavor — 1 operation(s) for root.
  name: Endeavor Root API
  slug: endeavor-root-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Search API from Endeavor — 1 operation(s) for search.
  name: Endeavor Search API
  slug: endeavor-search-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Settings API from Endeavor — 1 operation(s) for settings.
  name: Endeavor Settings API
  slug: endeavor-settings-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Sidebars API from Endeavor — 2 operation(s) for sidebars.
  name: Endeavor Sidebars API
  slug: endeavor-sidebars-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Statuses API from Endeavor — 2 operation(s) for statuses.
  name: Endeavor Statuses API
  slug: endeavor-statuses-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Tags API from Endeavor — 2 operation(s) for tags.
  name: Endeavor Tags API
  slug: endeavor-tags-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Taxonomies API from Endeavor — 2 operation(s) for taxonomies.
  name: Endeavor Taxonomies API
  slug: endeavor-taxonomies-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Templates API from Endeavor — 7 operation(s) for templates.
  name: Endeavor Templates API
  slug: endeavor-templates-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Themes API from Endeavor — 2 operation(s) for themes.
  name: Endeavor Themes API
  slug: endeavor-themes-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Types API from Endeavor — 2 operation(s) for types.
  name: Endeavor Types API
  slug: endeavor-types-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Users API from Endeavor — 6 operation(s) for users.
  name: Endeavor Users API
  slug: endeavor-users-api
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Widgets API from Endeavor — 2 operation(s) for widgets.
  name: Endeavor Widgets API
  slug: endeavor-widgets-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The block directory API from Endeavor — 1 operation(s) for block directory.
  name: Endeavor block directory API
  slug: endeavor-block-directory-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The block patterns API from Endeavor — 2 operation(s) for block patterns.
  name: Endeavor block patterns API
  slug: endeavor-block-patterns-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The block renderer API from Endeavor — 1 operation(s) for block renderer.
  name: Endeavor block renderer API
  slug: endeavor-block-renderer-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The Block Types API from Endeavor — 3 operation(s) for block types.
  name: Endeavor Block Types API
  slug: endeavor-block-types-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The font collections API from Endeavor — 2 operation(s) for font collections.
  name: Endeavor font collections API
  slug: endeavor-font-collections-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The font families API from Endeavor — 4 operation(s) for font families.
  name: Endeavor font families API
  slug: endeavor-font-families-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The global styles API from Endeavor — 5 operation(s) for global styles.
  name: Endeavor global styles API
  slug: endeavor-global-styles-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The Icon Collections API from Endeavor — 2 operation(s) for icon collections.
  name: Endeavor Icon Collections API
  slug: endeavor-icon-collections-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The Menu Items API from Endeavor — 4 operation(s) for menu items.
  name: Endeavor Menu Items API
  slug: endeavor-menu-items-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The menu locations API from Endeavor — 2 operation(s) for menu locations.
  name: Endeavor menu locations API
  slug: endeavor-menu-locations-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The pattern directory API from Endeavor — 1 operation(s) for pattern directory.
  name: Endeavor pattern directory API
  slug: endeavor-pattern-directory-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The template parts API from Endeavor — 7 operation(s) for template parts.
  name: Endeavor template parts API
  slug: endeavor-template-parts-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The View Config API from Endeavor — 1 operation(s) for view config.
  name: Endeavor View Config API
  slug: endeavor-view-config-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The widget types API from Endeavor — 4 operation(s) for widget types.
  name: Endeavor widget types API
  slug: endeavor-widget-types-api
- baseURL: https://wmegrp.com/wp-json/mcp/mcp-adapter-default-server
  baseurl_source: declared
  description: The Wp Pattern Category API from Endeavor — 2 operation(s) for wp pattern category.
  name: Endeavor Wp Pattern Category API
  slug: endeavor-wp-pattern-category-api
artifact_total: 46
common:
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Endeavor
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/endeavor/
- group: other
  title: ''
  type: Subsidiary
  url: https://www.wmeagency.com/
- group: other
  title: ''
  type: Subsidiary
  url: https://imglicensing.com/
- group: other
  title: ''
  type: Subsidiary
  url: https://www.pantheonmedia.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/endeavor/refs/heads/main/authentication/endeavor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/endeavor-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/endeavor/refs/heads/main/security/endeavor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/endeavor-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/endeavor/refs/heads/main/conventions/endeavor-conventions.yml
  title: ''
  type: Conventions
  url: conventions/endeavor-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/endeavor/refs/heads/main/conformance/endeavor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/endeavor-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/endeavor/refs/heads/main/lifecycle/endeavor-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/endeavor-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/endeavor/refs/heads/main/plans/endeavor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/endeavor-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/endeavor/refs/heads/main/llms/endeavor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/endeavor-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/endeavor/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wmegrp.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wmegrp.com/terms-of-use/
- group: company
  title: ''
  type: Careers
  url: https://wmeimg.wd1.myworkdayjobs.com/WMEGRP
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/endeavor-co
- group: company
  title: ''
  type: Website
  url: https://wmegrp.com/
- group: other
  title: ''
  type: Successor
  url: https://wmegrp.com/
- group: other
  title: ''
  type: Spinoff
  url: https://www.tkogrp.com/
created: '2026-03-21'
description: Endeavor was a global sports and entertainment company representing talent and owning and operating events, with subsidiaries including WME, IMG, and UFC. Following the 2024 take-private transaction by Silver Lake and the separation of TKO Group Holdings (UFC and WWE), the remaining talent, media, marketing, and licensing businesses were rebranded as WME Group. This repository tracks Endeavor as a corporate entity. It publishes no developer program, no API documentation and no OpenAPI; the only machine-readable surfaces on its own hosts are the wmegrp.com WordPress content API, which is anonymously readable, and a live but authentication-gated WordPress MCP Adapter endpoint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/endeavor.png
layout: provider
mcp_servers:
- description: ''
  name: Endeavor MCP Server
  slug: endeavor-mcp-server
modified: '2026-09-06'
name: Endeavor
nav: Providers
network: true
overview: 'Endeavor publishes 40 APIs on the [APIs.io](https://apis.io/) network, including Blocks API, Businesses API, Businesses Cities API, and 37 more. Tagged areas include Sports, Entertainment, Talent, Media, and Licensing.


  Endeavor''s developer surface includes authentication and 19 more developer resources.'
plans:
- name: Endeavor Plans Pricing
  plan_count: 0
  slug: endeavor-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Endeavor Rate Limits
  slug: endeavor-rate-limits
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 17.5
    developer_ergonomics: 13.7
    discoverability: 68.5
    operational_transparency: 0.0
  previous_composite: 18.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 40
      marker_coverage: 100.0
      total: 40
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/endeavor/refs/heads/main/screenshots/endeavor-2026-06-20T180654.png
security:
- kind: authentication
  name: Endeavor Authentication
  slug: endeavor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Endeavor Domain Security
  slug: endeavor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: endeavor
tags:
- Sports
- Entertainment
- Talent
- Media
- Licensing
- Marketing
website: https://wmegrp.com/
---
