---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'A live, OAuth-protected Model Context Protocol server that involve.me serves from its own infrastructure and advertises through RFC 9728 protected-resource metadata on www.involve.me. SCOPE: it expose'
  name: involve.me Website Content MCP Server
  slug: involveme-website-content-mcp-server
artifact_total: 10
asyncapis:
- description: ''
  name: Involve Me Webhooks
  slug: involve-me-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/involve-me-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/involve-me-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/involve-me-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/involve-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.involve.me/
- group: docs
  title: ''
  type: Documentation
  url: https://help.involve.me/en/
- group: operate
  title: ''
  type: Support
  url: https://www.involve.me/contact
- group: company
  title: ''
  type: Blog
  url: https://www.involve.me/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.involve.me/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.involve.me/register
- group: start
  title: ''
  type: Login
  url: https://app.involve.me/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.involve.me/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.involve.me/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stereosense
- group: operate
  title: ''
  type: StatusPage
  url: https://status.involve.me/
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://www.involve.me/data-processing
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/involve-me-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/involve-me-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/involve-me-security.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/involve-me-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/involve-me-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/involve-me-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/involve-me-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/involve-me-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/involve-me-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/involve-me-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/involve-me-plans-pricing.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/involve-me-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/involve-me-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/involve-me-data-model.yml
created: '2026-08-12'
description: 'involve.me is an AI quiz, form and funnel builder with built-in email automation and a lightweight CRM, operated by stereosense GmbH and used by marketing teams to capture, qualify and follow up on leads. Customers build quizzes, assessments, calculators, product finders, landing pages, surveys and payment pages in a no-code editor, publish them as a hosted page or an embedded widget, and route submissions into 55+ native CRM and email destinations. Its programmable surface is deliberately narrow: there is no public REST API and no OpenAPI, and the only machine-addressable paths are an outbound webhook that fires when a participant completes a funnel (Scale plan and above), a copy-paste JavaScript embed loader, Zapier and Make connectors, and an OAuth-protected Model Context Protocol server that exposes the marketing website''s Statamic CMS rather than the product itself.'
image: https://www.involve.me/favicons/favicon-32x32.png
layout: provider
mcp_servers:
- description: ''
  name: involve-me-mcp.yml
  slug: involve-me-mcpyml
modified: '2026-08-12'
name: involve.me
nav: Providers
network: true
overview: 'involve.me publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Lead Generation, Forms, and Surveys.


  The involve.me catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  involve.me''s developer surface includes documentation, support, engineering blog, pricing, signup flow, authentication, and 24 more developer resources.'
plans:
- name: Involve Me Plans Pricing
  plan_count: 5
  slug: involve-me-plans-pricing
random_paper: 132
rate_limits:
- limit_count: 0
  name: Involve Me Rate Limits
  slug: involve-me-rate-limits
scopes:
- name: Involve Me Scopes
  scope_count: 21
  slug: involve-me-scopes
  summary_line: 21 scopes
score:
  band: developing
  composite: 52.5
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 51.6
    developer_ergonomics: 34.8
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 52.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Involve Me Authentication
  slug: involve-me-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Involve Me Domain Security
  slug: involve-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Involve Me Vulnerability Disclosure
  slug: involve-me-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Involve Me Trust Center
  slug: involve-me-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: involve-me
tags:
- Company
- Marketing
- Lead Generation
- Forms
- Surveys
- Quizzes
- No-Code
- Email Marketing
- CRM
- Webhooks
- Model Context Protocol
- Austria
website: https://www.involve.me/
---
