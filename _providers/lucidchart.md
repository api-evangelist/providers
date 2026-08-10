---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Lucidchart Agentic Access
  operation_count: 5
  slug: lucidchart-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 9
apis:
- description: Programmatically create, search, read, copy, trash, and restore Lucid documents and folders. Manage collaborators and document permissions. Transfer content (import/export) and embed Lucid documents i
  name: Lucid REST API
  slug: lucid-rest-api
- description: Read structured document content (shapes, lines, pages) and import standard formats (Visio VSDX, Gliffy, draw.io, Mermaid, AWS architecture). Export to PNG, PDF, JPEG, SVG, and CSV.
  name: Lucid Document Content / Import-Export API
  slug: lucid-content-api
- description: Embed Lucid diagrams and whiteboards into external apps with read-only or interactive viewing, and listen to events such as page change and shape selection.
  name: Lucid Embed SDK & API
  slug: lucid-embed-api
- description: Build extensions that run inside Lucidchart, Lucidspark, and Lucidscale editors. Read and modify canvas content, import data, and ship custom shape libraries via the lucid-package CLI.
  name: Lucid Extension API
  slug: lucid-extension-api
- description: OAuth 2.0 authorization-code flow used by all Lucid REST API integrations to obtain user-scoped access tokens.
  name: Lucid OAuth 2.0 API
  slug: lucid-oauth-api
- description: SCIM 2.0 API for Enterprise customers. Provisions users and groups from Okta, Azure AD, OneLogin, and other IdPs across the Lucid Visual Collaboration Suite.
  name: Lucid SCIM API
  slug: lucid-scim-api
- description: Subscribe to events on documents and folders (create, update, trash, restore) and receive HTTP callbacks at your endpoint.
  name: Lucid Webhooks API
  slug: lucid-webhooks-api
- description: The Documents API from Lucidchart — 2 operation(s) for documents.
  name: Lucidchart Documents API
  slug: lucidchart-documents-api
- description: The Folders API from Lucidchart — 2 operation(s) for folders.
  name: Lucidchart Folders API
  slug: lucidchart-folders-api
artifact_total: 16
collections:
- collection_type: open
  name: Lucid REST API
  slug: open-lucidchart
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lucidchart-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lucidchart-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lucidchart-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/lucidchart
- group: company
  title: ''
  type: Website
  url: https://www.lucidchart.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lucid.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lucidchart.com/pages/pricing/lucidchart
- group: build
  title: ''
  type: GitHub
  url: https://github.com/lucidsoftware
- group: commercial
  title: ''
  type: Plans
  url: plans/lucidchart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lucidchart-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lucidchart-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.lucid.co/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://lucid.co/blog
created: '2026-05-08'
description: Lucidchart is a web-based intelligent diagramming application by Lucid Software, part of the Lucid Visual Collaboration Suite (Lucidchart, Lucidspark, Lucidscale). The Lucid Developer Platform exposes a REST API for documents/folders/collaborators/content, an Extension API for in-editor extensions, an Embed SDK for embedding diagrams in external apps, and a SCIM API for enterprise provisioning.
finops:
- name: Lucidchart Finops
  service_category: Productivity
  slug: lucidchart-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lucidchart.png
layout: provider
modified: '2026-05-08'
name: Lucidchart
nav: Providers
network: true
overview: 'Lucidchart publishes 2 APIs on the [APIs.io](https://apis.io/) network: Documents API and Folders API. Tagged areas include Productivity, Diagramming, Visualization, Visual Workspace, and SaaS.


  Lucidchart''s developer surface includes authentication, pricing, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Lucidchart Plans Pricing
  plan_count: 4
  slug: lucidchart-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Lucidchart Rate Limits
  slug: lucidchart-rate-limits
score:
  band: thin
  composite: 40.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lucidchart/refs/heads/main/screenshots/lucidchart-2026-06-20T184747.png
security:
- kind: authentication
  name: Lucidchart Authentication
  slug: lucidchart-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lucidchart Domain Security
  slug: lucidchart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lucidchart
tags:
- Productivity
- Diagramming
- Visualization
- Visual Workspace
- SaaS
website: https://www.lucidchart.com/
---
