---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: Standard oEmbed endpoint that returns a rich embed payload (iframe HTML, thumbnail URL, author metadata) for any public CodePen Pen URL. Supports JSON and JSONP response formats and an optional height
  name: CodePen oEmbed API
  slug: oembed
- description: Client-side JavaScript API for rendering and lazy-loading embedded Pens on external web pages. Uses the global window.__CPEmbed() function with data-* attributes on a .codepen div to control height, t
  name: CodePen Embed API
  slug: embed
- description: HTTP POST endpoint that accepts JSON-encoded code and configuration and opens a new (unsaved) Pen in the CodePen editor pre-populated with that content. Supports HTML, CSS, and JS content fields, prep
  name: CodePen POST to Prefill API
  slug: post-to-prefill
- description: Declarative embed API that transforms existing code blocks on a web page into live, interactive CodePen sandboxes without requiring users to navigate away. Code is supplied via data-prefill JSON attri
  name: CodePen Prefill Embeds API
  slug: prefill-embeds
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codepen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://codepen.io
- group: docs
  title: ''
  type: Documentation
  url: https://blog.codepen.io/documentation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codepen
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/codepen
- group: company
  title: ''
  type: Blog
  url: https://blog.codepen.io
- group: commercial
  title: ''
  type: Pricing
  url: https://codepen.io/pricing
- group: other
  title: ''
  type: X
  url: https://twitter.com/CodePen
- group: commercial
  title: ''
  type: Plans
  url: plans/codepen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/codepen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/codepen-finops.yml
created: '2026-06-12'
description: CodePen is a social development environment for front-end designers and developers, offering a browser-based playground for writing and sharing HTML, CSS, and JavaScript. The platform allows users to create "Pens" (interactive code snippets) and share them publicly or privately. CodePen provides developer-facing APIs including an Embed API for displaying Pens on external sites, a POST to Prefill API for programmatically opening the Pen editor with pre-populated code, Prefill Embeds for transforming existing code blocks into interactive sandboxes, and an oEmbed endpoint for standard embed discovery. The platform is widely used by educators, tutorial authors, and documentation teams who need live, interactive code examples embedded in external pages.
finops:
- name: Codepen Finops
  service_category: Developer Tools
  slug: codepen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codepen.png
jsonld:
- class_count: 0
  name: Codepen Context
  property_count: 37
  slug: codepen-context
layout: provider
modified: '2026-06-12'
name: CodePen
nav: Providers
network: true
overview: 'CodePen publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, Front-End Development, Code Playground, Embeds, and Education.


  The CodePen catalog on APIs.io includes 1 JSON-LD context.


  CodePen''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Codepen Plans Pricing
  plan_count: 5
  slug: codepen-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Codepen Rate Limits
  slug: codepen-rate-limits
score:
  band: thin
  composite: 30.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 15.1
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 30.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codepen/refs/heads/main/screenshots/codepen-2026-06-20T174703.png
security:
- kind: domain-security
  name: Codepen Domain Security
  slug: codepen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: codepen
tags:
- Developer Tools
- Front-End Development
- Code Playground
- Embeds
- Education
website: https://codepen.io
---
