---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'The public content API NeueHouse serves from its own host at https://www.neuehouse.com/wp-json/. NeueHouse runs on WordPress and the WordPress REST API is exposed and answering anonymously; the route '
  name: NeueHouse Content API
  slug: neuehouse-content-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.neuehouse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wordpress.org/rest-api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.neuehouse.com/wp-json/
- group: operate
  title: ''
  type: Support
  url: https://www.neuehouse.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://www.neuehouse.com/membership/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neuehouse.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neuehouse.com/privacy-policy/
- group: commercial
  title: ''
  type: Plans
  url: plans/neuehouse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/neuehouse-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/neuehouse-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/neuehouse-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/neuehouse-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/neuehouse-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/neuehouse-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/neuehouse-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neuehouse-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/neuehouse-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/neuehouse-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neuehouse-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/neuehouse-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/neuehouse-content-api-overlay.yaml
- group: design
  title: ''
  type: HouseRules
  url: https://www.neuehouse.com/house-rules/
- group: commercial
  title: ''
  type: MembershipAgreement
  url: https://www.neuehouse.com/membership-agreement/
- group: other
  title: ''
  type: Accessibility
  url: https://www.neuehouse.com/accessibility/
- group: other
  title: ''
  type: Events
  url: https://luma.com/neuehouse
- group: other
  title: ''
  type: RSS
  url: https://www.neuehouse.com/feed/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/neuehouse_stock/
created: '2026-08-26'
description: 'NeueHouse is a private work and cultural home for creatives — a members-only workspace, screening room, podcast studio and events club founded in New York in 2011. It is a hospitality brand rather than a software company and it runs no developer program, publishes no API documentation and issues no API credentials. It does, however, serve a live, anonymous, machine-readable content API from its own host: the site runs on WordPress and its WordPress REST API is exposed at https://www.neuehouse.com/wp-json/, where the route index declares 313 routes across 16 namespaces. Alongside the WordPress defaults the deployment registers four NeueHouse-specific content types that read anonymously — event (467 records of cultural programming), press (66), location (3 houses) and neuejournal (empty) — making the events and press archives genuinely useful to an outside consumer. NeueHouse ceased operations in September 2025 and filed Chapter 7; Convene Hospitality Group acquired the brand,
  intellectual property and the Madison Square flagship out of bankruptcy and relaunched the brand in January 2026. The Los Angeles houses were not acquired and are not reopening, although their records are still served by the content API.'
image: https://neuehouse.com/wp-content/uploads/2023/05/NeueHouse-Social-Logo.png
layout: provider
mcp_servers:
- description: ''
  name: NeueHouse MCP Server
  slug: neuehouse-mcp-server
modified: '2026-08-26'
name: NeueHouse
nav: Providers
network: true
overview: 'NeueHouse publishes 1 API on the [APIs.io](https://apis.io/) network: Content API. Tagged areas include Hospitality, Coworking, Events, Content, and WordPress.


  NeueHouse''s developer surface includes documentation, API reference, support, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Neuehouse Plans Pricing
  plan_count: 0
  slug: neuehouse-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Neuehouse Rate Limits
  slug: neuehouse-rate-limits
score:
  band: thin
  composite: 37.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 57.2
    developer_ergonomics: 35.1
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Neuehouse Authentication
  slug: neuehouse-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Neuehouse Domain Security
  slug: neuehouse-domain-security
  summary_line: TLSv1.3 · DMARC
slug: neuehouse
tags:
- Hospitality
- Coworking
- Events
- Content
- WordPress
- Membership
- Real Estate
- Media
- Workspace
website: https://www.neuehouse.com/
---
