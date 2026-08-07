---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: 'The current Cordial REST API. 106 operations across 24 resource groups: contacts, contact activities, orders, products, supplements, account lists, contact attributes, batch messages, automation templ'
  name: Cordial API v2
  slug: cordial-api-v2
- description: The legacy Cordial REST API, still published and documented alongside v2. 83 operations across 50 paths covering the same contact, event, order, product, supplement, list, message and job surface at a
  name: Cordial API v1
  slug: cordial-api-v1
- description: 'Cordial''s hosted Model Context Protocol server, which gives any MCP client secure read access to a Cordial account: audiences, messages, analytics, content, orchestrations, sculpt blocks and templates'
  name: Cordial MCP Server
  slug: cordial-mcp
artifact_total: 11
asyncapis:
- description: ''
  name: Cordial Webhooks
  slug: cordial-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://cordial.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cordial.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.cordial.com/hc/en-us/categories/12092749097741-Developer-resources
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cordial.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://support.cordial.com/hc/en-us/articles/360001897772-Get-started-for-developers
- group: operate
  title: ''
  type: Support
  url: https://support.cordial.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.cordial.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://cordial.com/resource-library/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CordialExperience
- group: start
  title: ''
  type: SignUp
  url: https://cordial.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://admin.cordial.io/#login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cordial.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.cordial.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cordial.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.cordial.com/hc/en-us/sections/115000944092-Monthly-release-notes
- group: auth
  title: ''
  type: Compliance
  url: https://cordial.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/cordial-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cordial-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cordial-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cordial-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/cordial-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cordial-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cordial-cli.yml
- group: design
  title: ''
  type: Components
  url: components/cordial-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cordial-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cordial-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cordial-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cordial-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/cordial-error-keys.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cordial-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cordial-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cordial-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cordial-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cordial-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cordial-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cordial-sandbox.yml
created: '2026-08-04'
description: 'Cordial is a cross-channel marketing and customer data platform headquartered in San Diego, California, used by consumer brands to unify customer data and orchestrate personalized messaging across email, SMS/MMS, RCS, mobile app (push, in-app, mobile inbox), website, and any external channel reachable over REST. The platform combines a native customer data platform built on a document database, real-time journey orchestration, identity resolution, and the Cordial Edge AI suite of brand-specific predictive models. Cordial is API-first: a documented Swagger 2.0 REST API at api.cordial.io exposes 106 operations across 24 resource groups covering contacts, contact activities, orders, products, supplements, lists, attributes, batch messages, automation templates, orchestrations, data jobs, imports/exports, alerts, and analytics. Alongside REST it publishes a hosted Model Context Protocol server with 56 read tools over 17 domains, a first-party npm CLI, mobile SDKs for iOS, Android,
  React Native and Expo, an embedded JavaScript listener, configurable outbound webhooks, and an open-source cookbook of packaged Claude Agent Skills.'
image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-site/companies/cordial.jpg
layout: provider
mcp_servers:
- description: ''
  name: cordial-mcp.yml
  slug: cordial-mcpyml
modified: '2026-08-04'
name: Cordial
nav: Providers
network: true
overview: 'Cordial publishes 2 APIs on the [APIs.io](https://apis.io/) network: API v2 and API v1. Tagged areas include Company, Marketing, Marketing Automation, Messaging, and Email.


  The Cordial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cordial''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 30 more developer resources.'
random_paper: 56
rate_limits:
- limit_count: 1
  name: Cordial Rate Limits
  slug: cordial-rate-limits
scopes:
- name: Cordial Scopes
  scope_count: 2
  slug: cordial-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 59.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 56.2
    developer_ergonomics: 78.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 65.8
  previous_composite: 59.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 65.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Cordial Authentication
  slug: cordial-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cordial Domain Security
  slug: cordial-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cordial Vulnerability Disclosure
  slug: cordial-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Cordial Trust Center
  slug: cordial-trust-center
  summary_line: SOC 2 Type II
slug: cordial
tags:
- Company
- Marketing
- Marketing Automation
- Messaging
- Email
- SMS
- Push Notifications
- Customer Data Platform
- Personalization
- Customer Engagement
- Artificial Intelligence
- Retail
- E-Commerce
website: https://cordial.com/
---
