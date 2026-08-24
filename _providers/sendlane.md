---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.7
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: REST API for managing contacts, lists, campaigns, automations, custom fields, sender profiles, tags, and custom integration events for e-commerce email and SMS marketing.
  name: Sendlane API
  slug: sendlane-api
artifact_total: 10
asyncapis:
- description: ''
  name: Sendlane Webhooks
  slug: sendlane-webhooks
collections:
- collection_type: open
  name: Api Reference
  slug: open-sendlane
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/sendlane-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendlane-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sendlane.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sendlane.stoplight.io/docs/api-documentation/c53add3c8b16f-overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sendlane
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendlane/
- group: company
  title: ''
  type: Blog
  url: https://www.sendlane.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sendlane.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sendlane.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/sendlane
- group: commercial
  title: ''
  type: Plans
  url: plans/sendlane-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sendlane-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sendlane-finops.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sendlane-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sendlane-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sendlane-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sendlane-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sendlane-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sendlane-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sendlane-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/sendlane-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sendlane-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/sendlane-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sendlane-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sendlane-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/sendlane-context.jsonld
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sendlane.stoplight.io/docs/api-documentation/c53add3c8b16f-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sendlane.com/articles/3807111349-sendlane-custom-integration-setup-api-v2
- group: operate
  title: ''
  type: Support
  url: https://www.sendlane.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.sendlane.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sendlane
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/sendlane/sendlane-s-public-workspace
- group: start
  title: ''
  type: SignUp
  url: https://auth.sendlane.com/register
- group: start
  title: ''
  type: Login
  url: https://auth.sendlane.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sendlane.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sendlane.com/privacy
created: '2026-06-13'
description: Email and SMS marketing platform built for e-commerce brands, unifying email, SMS, reviews and forms in one account. The Sendlane v2 REST API manages contacts, lists, segments, tags, custom fields, sender profiles, suppression lists and email and SMS consent, returns campaign and SMS performance and revenue reporting, and ingests e-commerce behaviour events such as product views, cart abandonment and orders placed to drive automations and revenue attribution.
finops:
- name: Sendlane Finops
  service_category: ''
  slug: sendlane-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sendlane.png
jsonld:
- class_count: 4
  name: Sendlane Context
  property_count: 14
  slug: sendlane-context
layout: provider
mcp_servers:
- description: Sendlane ships no Model Context Protocol server. This is a CANDIDATE tool list derived from the 82 operations in the published OpenAPI, showing what an MCP server over the Sendlane v2 API would expose
  name: Sendlane MCP Server (candidate)
  slug: sendlane-mcp-server-candidate
modified: '2026-08-13'
name: Sendlane
nav: Providers
network: true
overview: 'Sendlane publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email Marketing, SMS Marketing, E-Commerce, Marketing Automation, and Contacts.


  The Sendlane catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Sendlane''s developer surface includes authentication, documentation, engineering blog, pricing, sandbox, changelog, getting-started guide, and 30 more developer resources.'
plans:
- name: Sendlane Plans Pricing
  plan_count: 4
  slug: sendlane-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Sendlane Rate Limits
  slug: sendlane-rate-limits
score:
  band: strong
  composite: 65.1
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 16.7
    contract_quality: 70.8
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 63.2
  previous_composite: 65.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendlane/refs/heads/main/screenshots/sendlane-2026-06-20T193659.png
security:
- kind: authentication
  name: Sendlane Authentication
  slug: sendlane-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Sendlane Domain Security
  slug: sendlane-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sendlane
tags:
- Email Marketing
- SMS Marketing
- E-Commerce
- Marketing Automation
- Contacts
- Campaigns
- Segmentation
- Consent Management
- Suppression
- Event Tracking
- Revenue Attribution
website: https://www.sendlane.com/
---
