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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alternativeto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alternativeto.net/
- group: company
  title: ''
  type: About
  url: https://alternativeto.net/about/
- group: operate
  title: ''
  type: FAQ
  url: https://alternativeto.net/faq/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alternativeto.net/about/privacy/
- group: company
  title: ''
  type: News
  url: https://alternativeto.net/news/all/
- group: company
  title: ''
  type: Blog
  url: https://blog.alternativeto.net/
- group: start
  title: ''
  type: SignUp
  url: https://alternativeto.net/signup/
- group: other
  title: ''
  type: X
  url: https://x.com/alternativeto
- group: company
  title: ''
  type: Mastodon
  url: https://mastodon.social/@alternativeto
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alternativeto.net/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alternativeto-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alternativeto-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alternativeto-lifecycle.yml
created: '2024-01-01'
description: AlternativeTo is a crowdsourced software discovery platform that helps users find alternatives to software products based on user recommendations across desktop, mobile, and web applications. The platform does not currently offer a public API, but provides partner integration opportunities for software vendors.
features:
- description: Crowdsourced database of software alternatives with user voting, ratings, and comparisons across web, desktop, and mobile platforms.
  name: Software Alternative Discovery
- description: Filter alternatives by platform (Windows, Mac, Linux, Android, iPhone, Online) and license type (open source, free, commercial).
  name: Platform Filtering
- description: Community-driven reviews and rating system for software products with likes and alternative recommendations.
  name: User Reviews and Ratings
- description: Vendor-managed software listings with features, screenshots, and links for software discovery and comparison.
  name: Software Vendor Listings
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alternativeto.png
layout: provider
modified: '2026-06-20'
name: AlternativeTo
nav: Providers
network: true
overview: 'AlternativeTo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Alternatives, Reviews, Software Discovery, and Software Directory.


  AlternativeTo''s developer surface includes FAQ, product news, engineering blog, signup flow, and 10 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 12.0
  delta: -1.2
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 13.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alternativeto/refs/heads/main/screenshots/alternativeto-2026-07-25T195828.png
security:
- kind: domain-security
  name: Alternativeto Domain Security
  slug: alternativeto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alternativeto
tags:
- Alternatives
- Reviews
- Software Discovery
- Software Directory
use_cases:
- description: Find alternatives to discontinued, expensive, or unavailable software products based on crowdsourced community recommendations.
  name: Software Discovery
- description: Discover free and open source alternatives to commercial software products with platform filtering and license search.
  name: Open Source Alternatives
- description: Software vendors can list their products on AlternativeTo to reach users searching for alternatives to competing products.
  name: Vendor Software Listing
website: https://alternativeto.net/
---
