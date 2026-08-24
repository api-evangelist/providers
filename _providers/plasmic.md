---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Plasmic Agentic Access
  operation_count: 6
  slug: plasmic-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 11
apis:
- description: Browser-based visual builder where designers and developers compose pages, components, and design systems. Outputs are consumed downstream by the Loader, Codegen, and CMS APIs.
  name: Plasmic Studio
  slug: studio
- description: Runtime fetching API used by React, Next.js, and Gatsby integrations to pull Studio-published pages and components into a host app. Supports server-side rendering, incremental static regeneration, and
  name: Plasmic Loader (Headless API)
  slug: loader
- description: Generates React source code from a Plasmic project, synced into the host repository via the Plasmic CLI. Produces editable presentational components alongside skeleton wrappers for app code.
  name: Plasmic Codegen API
  slug: codegen
- description: Headless content API for structured data managed inside Plasmic. Supports reading and writing rows in models defined in Studio, used to power data bindings inside Plasmic pages or external apps.
  name: Plasmic CMS API
  slug: cms
- description: Command-line tool (plasmicapp/cli) for authenticating against Plasmic and syncing generated code into a repository. Commands include `plasmic auth`, `plasmic sync`, and `plasmic watch`.
  name: Plasmic CLI
  slug: cli
- description: React loader and components for embedding Plasmic-built pages inside React apps.
  name: Plasmic React Integration
  slug: react
- description: Next.js loader supporting both pages and app router. Used to render Plasmic-managed pages with SSR/SSG/ISR.
  name: Plasmic Next.js Integration
  slug: nextjs
- description: Gatsby plugin loader for embedding Plasmic-built pages inside Gatsby sites.
  name: Plasmic Gatsby Integration
  slug: gatsby
- description: Model Context Protocol server exposing Plasmic project context to AI agents and IDE assistants.
  name: Plasmic MCP Server
  slug: mcp
- description: Query and count items in a CMS model.
  name: Plasmic Items API
  slug: plasmic-items-api
- description: Create, update, publish, and delete CMS rows.
  name: Plasmic Rows API
  slug: plasmic-rows-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Plasmic CMS Items API
  slug: open-plasmic-items-api
- collection_type: open
  name: Plasmic CMS Items Rows API
  slug: open-plasmic-rows-api
- collection_type: open
  name: Plasmic CMS API
  slug: open-plasmic
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/plasmicapp/plasmic/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/plasmic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plasmic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plasmic-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.plasmic.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.plasmic.app/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/plasmicapp/plasmic
- group: operate
  title: ''
  type: Forums
  url: https://forum.plasmic.app/
- group: operate
  title: ''
  type: Slack
  url: https://plasmic.app/slack
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/plasmicapp
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/plasmicapp
- group: company
  title: ''
  type: Blog
  url: https://www.plasmic.app/blog/feed.xml
created: '2026-05-23'
description: Plasmic is a visual builder and headless CMS for front-end development. Designers and developers compose pages and components in Plasmic Studio, then ship them via either the Headless API (Loader) for runtime fetching or the Codegen pipeline for generated React/Next.js/Gatsby source. The platform also exposes a CMS for structured content, a CLI for code synchronization, and a REST API for programmatic access. Open source components live under the plasmicapp GitHub organization.
finops:
- name: Plasmic Finops
  service_category: API
  slug: plasmic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plasmic.png
layout: provider
modified: '2026-05-23'
name: Plasmic
nav: Providers
network: true
overview: 'Plasmic publishes 2 APIs on the [APIs.io](https://apis.io/) network: Items API and Rows API. Tagged areas include Visual Builder, Headless CMS, React, Next.js, and Gatsby.


  Plasmic''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Plasmic Plans Pricing
  plan_count: 1
  slug: plasmic-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Plasmic Rate Limits
  slug: plasmic-rate-limits
score:
  band: thin
  composite: 34.6
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plasmic/refs/heads/main/screenshots/plasmic-2026-06-20T191800.png
security:
- kind: authentication
  name: Plasmic Authentication
  slug: plasmic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Plasmic Domain Security
  slug: plasmic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: plasmic
tags:
- Visual Builder
- Headless CMS
- React
- Next.js
- Gatsby
- Low-Code
- Frontend
website: https://www.plasmic.app/
---
