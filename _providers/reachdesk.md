---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: The Reachdesk REST API enables programmatic triggering of gift campaigns and sending of physical gifts, branded merchandise, and digital rewards. Authenticated via API tokens generated in the Reachdes
  name: Reachdesk API
  slug: reachdesk-api
- description: Reachdesk operates a first-party remote Model Context Protocol server at https://app.reachdesk.com/mcp, on the same host as its REST API. It is a hosted HTTP endpoint an MCP client POSTs to directly —
  name: Reachdesk MCP Server
  slug: reachdesk-mcp
artifact_total: 13
asyncapis:
- description: ''
  name: Reachdesk Webhooks
  slug: reachdesk-webhooks
collections:
- collection_type: open
  name: Reachdesk API
  slug: open-reachdesk-api
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/reachdesk-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reachdesk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reachdesk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.reachdesk.com/hc/en-gb/categories/4404901379473-Integrations-API
- group: operate
  title: ''
  type: Support
  url: https://support.reachdesk.com/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://www.reachdesk.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reachdesk.com/pricing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reachdesk
- group: other
  title: ''
  type: X
  url: https://x.com/ReachdeskHQ
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/reachdesk
- group: commercial
  title: ''
  type: Plans
  url: plans/reachdesk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reachdesk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reachdesk-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://reachdesk.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://reachdesk.readme.io/reference/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://support.reachdesk.com/hc/en-gb/articles/29669486204305-Send-gifts-with-the-Reachdesk-Trigger-Campaign-API
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reachdesk.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reachdesk.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.reachdesk.com/users/sign_in
- group: agent
  title: ''
  type: WellKnown
  url: well-known/reachdesk-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reachdesk-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/reachdesk-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/reachdesk-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reachdesk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reachdesk-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reachdesk-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reachdesk-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/reachdesk-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reachdesk-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/reachdesk-trust-center.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/reachdesk-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/reachdesk-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reachdesk-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/reachdesk-api-overlay.yaml
created: '2026-06-13'
description: Reachdesk is a global B2B corporate gifting and direct mail platform that enables sales, marketing, and customer success teams to send physical gifts, branded merchandise, and digital rewards at scale. The Reachdesk REST API allows programmatic triggering of gift campaigns, integration with CRM and marketing automation tools, and management of sending workflows across 180+ countries. API tokens are generated via the platform settings and used to authenticate requests for campaign triggering and gift delivery operations.
finops:
- name: Reachdesk Finops
  service_category: ''
  slug: reachdesk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reachdesk.png
jsonld:
- class_count: 10
  name: Reachdesk Context
  property_count: 24
  slug: reachdesk-context
layout: provider
mcp_servers:
- description: 'Reachdesk operates a first-party remote MCP server on its own API host. It is a hosted HTTP endpoint an MCP client POSTs to directly — there is no npx/stdio package to install. Access is OAuth 2.1: th'
  name: Reachdesk MCP Server
  slug: reachdesk-mcp-server
modified: '2026-08-13'
name: Reachdesk
nav: Providers
network: true
overview: 'Reachdesk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Corporate Gifting, Direct Mail, Swag, B2B, and Sales Enablement.


  The Reachdesk catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Reachdesk''s developer surface includes authentication, documentation, support, engineering blog, pricing, API reference, getting-started guide, and 28 more developer resources.'
plans:
- name: Reachdesk Plans Pricing
  plan_count: 3
  slug: reachdesk-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Reachdesk Rate Limits
  slug: reachdesk-rate-limits
scopes:
- name: Reachdesk Scopes
  scope_count: 0
  slug: reachdesk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.6
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 16.7
    contract_quality: 72.0
    developer_ergonomics: 50.6
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 28.9
  previous_composite: 58.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reachdesk/refs/heads/main/screenshots/reachdesk-2026-06-20T192631.png
security:
- kind: authentication
  name: Reachdesk Authentication
  slug: reachdesk-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Reachdesk Domain Security
  slug: reachdesk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Reachdesk Trust Center
  slug: reachdesk-trust-center
  summary_line: verified, claimed, note
slug: reachdesk
tags:
- Corporate Gifting
- Direct Mail
- Swag
- B2B
- Sales Enablement
- Customer Success
- Marketing Automation
- Gifting Platform
- Rewards
- MCP
- AI Agents
- OpenAPI
website: https://www.reachdesk.com/
---
