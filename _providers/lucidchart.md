---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://www.lucidchart.com/'', ''status'': 301, ''note'': ''declared website redirects to https://lucid.co/lucidchart — a different registrable domain (lucidchart.com -> lucid.co), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Lucidchart Agentic Access
  operation_count: 5
  slug: lucidchart-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
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
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Endpoints that deal with org groups or teams (dependent on which bearer token is used).
  name: Lucidchart Groups API
  slug: lucidchart-groups-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Endpoints that deal with lucid resource schemas.
  name: Lucidchart Schemas API
  slug: lucidchart-schemas-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Retrieve the SCIM service provider configuration, describing supported operations, authentication schemes, and bulk/filter capabilities.
  name: Lucidchart Service Provider Config API
  slug: lucidchart-service-provider-config-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Endpoints that deal with users.
  name: Lucidchart Users API
  slug: lucidchart-users-api
artifact_total: 22
collections:
- collection_type: open
  name: Lucid REST Documents API
  slug: open-lucidchart-documents-api
- collection_type: open
  name: Lucid REST Documents Folders API
  slug: open-lucidchart-folders-api
- collection_type: open
  name: Lucid REST API
  slug: open-lucidchart
common:
- group: other
  href: https://artifacts.apis.io/lucidchart/capabilities/lucidchart-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lucidchart-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/lucidchart/agentic-access/lucidchart-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lucidchart-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/lucidchart/security/lucidchart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lucidchart-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/lucidchart/authentication/lucidchart-authentication.yml
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
  href: https://artifacts.apis.io/lucidchart/plans/lucidchart-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lucidchart-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lucidchart/rate-limits/lucidchart-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lucidchart-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lucidchart/finops/lucidchart-finops.yml
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
- has_sources: true
  method: generated
  name: Lucidchart Finops
  primary_unit: ''
  service_category: Productivity
  slug: lucidchart-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lucidchart.png
layout: provider
mcp_servers:
- description: Remote MCP server at developer.lucid.co over HTTP; 6 tools listed.
  name: Lucidchart MCP Server
  slug: lucidchart
modified: '2026-05-08'
name: Lucidchart
nav: Providers
network: true
overview: 'Lucidchart publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Groups API, Schemas API, Service Provider Config API, and 8 more. Tagged areas include Productivity, Diagramming, Visualization, Visual Workspace, and Software-as-a-Service.


  The Lucidchart catalog on APIs.io includes 1 Spectral governance ruleset.


  Lucidchart''s developer surface includes authentication, pricing, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Lucidchart Plans Pricing
  plan_count: 4
  slug: lucidchart-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Lucidchart Rate Limits
  slug: lucidchart-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Lucidchart API Rules
  rule_count: 61
  severity_counts:
    error: 56
    hint: 0
    info: 3
    warn: 2
  slug: lucidchart-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 18.4
    contract_governance: 13.6
    contract_quality: 56.1
    developer_ergonomics: 47.6
    discoverability: 75.0
    operational_transparency: 13.2
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 57.1
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/lucidchart/lucidchart-2026-06-20T184747.png
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
- Software-as-a-Service
website: https://www.lucidchart.com/
---
