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
  - rate-limits
  - security
  trial: false
  try_now: true
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
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: Hosted Model Context Protocol server exposing 30 Paubox tools across email, forms and email marketing to MCP-compatible AI clients. Reachable over streamable HTTP at https://mcp.paubox.com/mcp with OA
  name: Paubox MCP Server
  slug: paubox-mcp-server
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Campaign analytics and reporting operations
  name: Paubox Analytics API
  slug: paubox-analytics-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Campaign mailing management and sending operations
  name: Paubox Campaign Mailings API
  slug: paubox-campaign-mailings-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Drip campaign management and automation operations
  name: Paubox Drip Campaigns API
  slug: paubox-drip-campaigns-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Manage and use dynamic Handlebars templates for email content
  name: Paubox Dynamic Templates API
  slug: paubox-dynamic-templates-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Create, list, update, copy, and archive forms (requires API key)
  name: Paubox Form management API
  slug: paubox-form-management-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Retrieve form definitions and accept submissions
  name: Paubox Forms API
  slug: paubox-forms-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Send individual or bulk transactional email
  name: Paubox Messages API
  slug: paubox-messages-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: List and export form submissions (requires API key)
  name: Paubox Submissions API
  slug: paubox-submissions-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Subscriber management operations
  name: Paubox Subscribers API
  slug: paubox-subscribers-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Subscription list management operations
  name: Paubox Subscription Lists API
  slug: paubox-subscription-lists-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Subscriber opt-in and opt-out operations
  name: Paubox Subscriptions API
  slug: paubox-subscriptions-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Tracking link analytics and data operations
  name: Paubox Tracking Links API
  slug: paubox-tracking-links-api
artifact_total: 21
asyncapis:
- description: ''
  name: Paubox Email Webhooks
  slug: paubox-email-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/paubox-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/paubox-email-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/paubox-marketing-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/paubox-forms-api-overlay.yaml
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
overview: 'Paubox publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Campaign Mailings API, Drip Campaigns API, and 9 more. Tagged areas include Email, HIPAA, Healthcare, Compliance, and Transactional Email.


  The Paubox catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paubox''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
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
  composite: 72.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 65.7
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 72.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    - jurisdiction: US
      standard: hitech
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 43.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/screenshots/paubox-2026-09-02T150917.png
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
