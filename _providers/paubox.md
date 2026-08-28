---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.3
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: HIPAA compliant transactional email API. Send a single message, send bulk messages (batches of 50 or fewer recommended), retrieve a message receipt with delivery, open and click tracking, and manage H
  name: Paubox Email API
  slug: paubox-email-api
- description: HIPAA compliant email marketing API. Create, fetch, update, send, schedule, test and bulk-delete campaign mailings; run drip campaigns; manage subscribers, subscriptions and subscription lists includi
  name: Paubox Marketing API
  slug: paubox-marketing-api
- description: HIPAA compliant online form API. Public respondent-facing endpoints retrieve a form definition (HTML, JSON schema, CSS) and submit a response with no authentication — the form UUID is the access contr
  name: Paubox Forms API
  slug: paubox-forms-api
- description: Hosted Model Context Protocol server exposing 30 Paubox tools across email, forms and email marketing to MCP-compatible AI clients. Reachable over streamable HTTP at https://mcp.paubox.com/mcp with OA
  name: Paubox MCP Server
  slug: paubox-mcp-server
artifact_total: 12
asyncapis:
- description: ''
  name: Paubox Email Webhooks
  slug: paubox-email-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.paubox.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.paubox.com/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paubox.com/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://docs.paubox.com/email-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.paubox.com/email-api/quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.paubox.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://github.com/Paubox/community/discussions
- group: company
  title: ''
  type: Blog
  url: https://www.paubox.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Paubox
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paubox.com/pricing/paubox-email-api
- group: start
  title: ''
  type: SignUp
  url: https://www.paubox.com/pricing/paubox-email-api
- group: start
  title: ''
  type: Login
  url: https://next.paubox.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paubox.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paubox.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paubox.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.paubox.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/paubox-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paubox-llms.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/paubox-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/paubox-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/paubox-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paubox-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/paubox-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paubox-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paubox-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paubox-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paubox-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paubox-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paubox-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/paubox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paubox-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paubox-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/paubox-email-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/paubox-well-known.yml
created: '2026-08-26'
description: Paubox is a HIPAA compliant, HITRUST certified email infrastructure company serving healthcare organizations in the United States. Its products encrypt outbound email without recipient portals, passwords, or plugins, and work alongside Google Workspace and Microsoft 365. The developer surface is three REST APIs on api.paubox.com — the Paubox Email API for transactional email (send, bulk send, message receipt, Handlebars dynamic templates, templated messages) with an SMTP relay alternative at smtp.paubox.com:587; the Paubox Marketing API for HIPAA compliant campaign mailings, drip campaigns, subscribers, subscription lists, tracking links and campaign analytics; and the Paubox Forms API for building, hosting and processing secure patient intake forms with public respondent endpoints and scoped management endpoints. Paubox publishes OpenAPI 3.0 definitions for all three, official SDKs for ten languages, a Node-based CLI, delivery webhooks, an llms.txt, an A2A agent card, a published
  Agent Skill, and a hosted MCP server at mcp.paubox.com exposing 30 tools across email, forms and marketing.
image: https://www.paubox.com/hubfs/Logos/Paubox_Primary_color.svg
layout: provider
mcp_servers:
- description: 'Paubox ships a first-party Model Context Protocol server exposing 30 tools across the Email API, Forms API and Marketing API. It is offered over two transports: a hosted streamable-HTTP endpoint at ht'
  name: Paubox MCP Server
  slug: paubox-mcp-server
modified: '2026-08-26'
name: Paubox
nav: Providers
network: true
overview: 'Paubox publishes 3 APIs on the [APIs.io](https://apis.io/) network: Email API, Marketing API, and Forms API. Tagged areas include Email, HIPAA, Healthcare, Compliance, and Transactional Email.


  The Paubox catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paubox''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Paubox Plans Pricing
  plan_count: 6
  slug: paubox-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Paubox Rate Limits
  slug: paubox-rate-limits
score:
  band: exemplar
  composite: 74.8
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 30.3
    contract_quality: 65.9
    developer_ergonomics: 78.6
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 57.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 43.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Paubox Authentication
  slug: paubox-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Paubox Domain Security
  slug: paubox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Paubox Vulnerability Disclosure
  slug: paubox-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Paubox Trust Center
  slug: paubox-trust-center
  summary_line: paubox_own, inherited_from_infrastructure
slug: paubox
tags:
- Email
- HIPAA
- Healthcare
- Compliance
- Transactional Email
- Email Marketing
- Forms
- Security
- Encryption
- Messaging
website: https://www.paubox.com/
---
