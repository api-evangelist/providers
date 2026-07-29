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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Zeplin Agentic Access
  operation_count: 123
  slug: zeplin-agentic-access
  summary_line: 123 operations · 46 acting
api_count: 16
apis:
- description: The Authorization API from Zeplin — 2 operation(s) for authorization.
  name: Zeplin Authorization API
  slug: zeplin-authorization-api
- description: The Colors API from Zeplin — 4 operation(s) for colors.
  name: Zeplin Colors API
  slug: zeplin-colors-api
- description: The Components API from Zeplin — 10 operation(s) for components.
  name: Zeplin Components API
  slug: zeplin-components-api
- description: The Connected Components API from Zeplin — 2 operation(s) for connected components.
  name: Zeplin Connected Components API
  slug: zeplin-connected-components-api
- description: The Design Tokens API from Zeplin — 2 operation(s) for design tokens.
  name: Zeplin Design Tokens API
  slug: zeplin-design-tokens-api
- description: The Flows API from Zeplin — 7 operation(s) for flows.
  name: Zeplin Flows API
  slug: zeplin-flows-api
- description: The Notifications API from Zeplin — 2 operation(s) for notifications.
  name: Zeplin Notifications API
  slug: zeplin-notifications-api
- description: The Organizations API from Zeplin — 11 operation(s) for organizations.
  name: Zeplin Organizations API
  slug: zeplin-organizations-api
- description: The Projects API from Zeplin — 5 operation(s) for projects.
  name: Zeplin Projects API
  slug: zeplin-projects-api
- description: The Screens API from Zeplin — 17 operation(s) for screens.
  name: Zeplin Screens API
  slug: zeplin-screens-api
- description: The Spacing API from Zeplin — 6 operation(s) for spacing.
  name: Zeplin Spacing API
  slug: zeplin-spacing-api
- description: The Styleguides API from Zeplin — 6 operation(s) for styleguides.
  name: Zeplin Styleguides API
  slug: zeplin-styleguides-api
- description: The TextStyles API from Zeplin — 4 operation(s) for textstyles.
  name: Zeplin TextStyles API
  slug: zeplin-textstyles-api
- description: The Users API from Zeplin — 3 operation(s) for users.
  name: Zeplin Users API
  slug: zeplin-users-api
- description: The Variable Collections API from Zeplin — 2 operation(s) for variable collections.
  name: Zeplin Variable Collections API
  slug: zeplin-variable-collections-api
- description: The Webhooks API from Zeplin — 8 operation(s) for webhooks.
  name: Zeplin Webhooks API
  slug: zeplin-webhooks-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zeplin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zeplin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zeplin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zeplin-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://zeplin.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zeplin.dev
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zeplin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zeplin-io
- group: company
  title: ''
  type: Blog
  url: https://blog.zeplin.io
- group: commercial
  title: ''
  type: Pricing
  url: https://zeplin.io/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zeplin.io
- group: other
  title: ''
  type: X
  url: https://twitter.com/zeplinproject
- group: commercial
  title: ''
  type: Plans
  url: plans/zeplin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zeplin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zeplin-finops.yml
created: '2026-06-12'
description: Zeplin is a design-to-development handoff platform that bridges the gap between designers and developers by providing a structured workspace for accessing design specs, assets, style guides, components, and annotations. The Zeplin REST API enables programmatic access to all resources within Zeplin including projects, screens, components, layers, assets, and notes exported from Figma, Sketch, and Adobe XD. Developers can build custom integrations using read and write operations on design data, receive real-time updates via webhooks, and automate design-to-code workflows. The API uses OAuth 2.0 with PKCE support and personal access tokens for authentication, with an official JavaScript SDK and OpenAPI specification available.
finops:
- name: Zeplin Finops
  service_category: ''
  slug: zeplin-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Zeplin design handoff and collaboration platform. Zeplin bridges designers and developers by providing structured access to design specs, as
  name: Zeplin GraphQL Schema
  slug: zeplin-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zeplin.png
json_schemas:
- name: Zeplin API Schemas
  property_count: 0
  slug: zeplin-schemas
jsonld:
- class_count: 118
  name: Zeplin Context
  property_count: 5
  slug: zeplin-context
layout: provider
modified: '2026-06-12'
name: Zeplin
nav: Providers
network: true
overview: 'Zeplin publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Colors API, Components API, and 13 more. Tagged areas include Design, Design Handoff, Developer Tools, Figma, and Sketch.


  The Zeplin catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zeplin''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Zeplin Plans Pricing
  plan_count: 4
  slug: zeplin-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Zeplin Rate Limits
  slug: zeplin-rate-limits
rules:
- name: Zeplin API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: zeplin-jsonschema-spectral-rules
scopes:
- name: Zeplin Scopes
  scope_count: 0
  slug: zeplin-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.7
  delta: -3.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zeplin/refs/heads/main/screenshots/zeplin-2026-06-20T201824.png
security:
- kind: authentication
  name: Zeplin Authentication
  slug: zeplin-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Zeplin Domain Security
  slug: zeplin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zeplin
tags:
- Design
- Design Handoff
- Developer Tools
- Figma
- Sketch
- Adobe XD
- Style Guides
- Components
- Assets
- Webhooks
website: https://zeplin.io
---
