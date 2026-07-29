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
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Instapage Agentic Access
  operation_count: 25
  slug: instapage-agentic-access
  summary_line: 25 operations · 14 acting
api_count: 2
apis:
- description: REST API for managing landing pages, leads, accounts, workspaces, and team members in Instapage. Authentication uses a Personal API Token generated from the Instapage dashboard, with a default rate li
  name: Instapage Public API
  slug: public-api
- description: The Workspaces API from Instapage — 13 operation(s) for workspaces.
  name: Instapage Workspaces API
  slug: instapage-workspaces-api
artifact_total: 7
collections:
- collection_type: open
  name: Instapage API
  slug: open-instapage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/instapage-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/instapage-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instapage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instapage-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Instapage
- group: company
  title: ''
  type: Website
  url: https://instapage.com
- group: docs
  title: ''
  type: Documentation
  url: https://devdocs.instapage.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://instapage.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.instapage.com/signup
- group: company
  title: ''
  type: Blog
  url: https://instapage.com/blog
- group: operate
  title: ''
  type: Help Center
  url: https://help.instapage.com
- group: other
  title: ''
  type: API Overview
  url: https://instapage.com/api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/instapage
created: '2026-05-11'
description: Instapage is a landing page and post-click optimization platform that lets marketers build, personalize, A/B test, and analyze landing pages used in paid advertising and conversion campaigns. The platform includes a drag and drop builder, AdMap for ad-to-page connection, heatmaps, experiments, and AI-powered content generation, and integrates with major ad platforms, CRMs, and marketing automation tools. Instapage's REST API provides programmatic access to landing pages, leads, accounts, and team members using a Personal API Token for authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instapage.png
layout: provider
modified: '2026-05-11'
name: Instapage
nav: Providers
network: true
overview: 'Instapage publishes 1 API on the [APIs.io](https://apis.io/) network: Workspaces API. Tagged areas include Landing Pages, Conversion Optimization, Marketing, A/B Testing, and Post-Click Optimization.


  Instapage''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 65
score:
  band: thin
  composite: 29.8
  delta: -1.9
  facets:
    commercial_clarity: 18.4
    contract_quality: 53.4
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instapage/refs/heads/main/screenshots/instapage-2026-06-20T183418.png
security:
- kind: authentication
  name: Instapage Authentication
  slug: instapage-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Instapage Domain Security
  slug: instapage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Instapage Trust Center
  slug: instapage-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: instapage
tags:
- Landing Pages
- Conversion Optimization
- Marketing
- A/B Testing
- Post-Click Optimization
- Lead Generation
website: https://instapage.com
---
