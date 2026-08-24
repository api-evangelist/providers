---
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.9
  scored_at: '2026-08-24'
api_count: 6
apis:
- description: AskNicely's remote Model Context Protocol server, exposing Ask NiceAI's tools — NPS summaries, survey responses, leaderboards and more — to external AI clients such as Claude. Served per tenant at htt
  name: AskNicely MCP Server (Ask NiceAI)
  slug: asknicely-mcp-server-ask-niceai
- description: Import, look up, deactivate and privacy-delete contacts.
  name: AskNicely Contacts API
  slug: asknicely-contacts-api
- description: Server-to-server negotiation of an in-app survey slug.
  name: AskNicely In-App Surveys API
  slug: asknicely-in-app-surveys-api
- description: Retrieve survey responses.
  name: AskNicely Responses API
  slug: asknicely-responses-api
- description: NPS, sent and historical survey statistics.
  name: AskNicely Statistics API
  slug: asknicely-statistics-api
- description: Trigger NPS/CSAT/5-Star surveys to contacts.
  name: AskNicely Surveys API
  slug: asknicely-surveys-api
artifact_total: 19
asyncapis:
- description: ''
  name: Asknicely Webhooks
  slug: asknicely-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AskNicely Contacts API
  slug: open-asknicely-contacts-api
- collection_type: open
  name: AskNicely In-App Survey In-App Surveys API
  slug: open-asknicely-in-app-surveys-api
- collection_type: open
  name: AskNicely Responses API
  slug: open-asknicely-responses-api
- collection_type: open
  name: AskNicely Statistics API
  slug: open-asknicely-statistics-api
- collection_type: open
  name: AskNicely Surveys API
  slug: open-asknicely-surveys-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/asknicely-openapi-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/asknicely-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.asknicely.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://demo.asknice.ly/help/apidocs
- group: docs
  title: ''
  type: Documentation
  url: https://demo.asknice.ly/help/apidocs
- group: docs
  title: ''
  type: APIReference
  url: https://demo.asknice.ly/help/apidocs
- group: start
  title: ''
  type: GettingStarted
  url: https://demo.asknice.ly/help/apidocs/auth
- group: operate
  title: ''
  type: Support
  url: https://asknicely.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.asknicely.com/resource-hub
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/asknicely
- group: commercial
  title: ''
  type: Pricing
  url: https://www.asknicely.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://start.asknice.ly/findlogin/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.asknicely.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.asknicely.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.asknicely.com/security
- group: operate
  title: ''
  type: StatusPage
  url: https://status.asknicely.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/asknicely-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/asknicely-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://demo.asknice.ly/help/apidocs/changelog
- group: auth
  title: ''
  type: Authentication
  url: authentication/asknicely-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/asknicely-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/asknicely-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/asknicely-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/asknicely-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/asknicely-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/asknicely-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/asknicely-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/asknicely-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/asknicely-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/asknicely-packages.yml
- group: design
  title: ''
  type: Components
  url: components/asknicely-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/asknicely-llms.txt
created: '2026-08-06'
description: AskNicely is a customer-experience (CX) platform for service businesses, built around Net Promoter Score, CSAT and 5-Star surveys delivered by email, SMS, web badge and in-app. It collects frontline feedback, routes it to managers and staff through leaderboards, coaching and case management, and syndicates positive responses to review sites through its Reputation/Review Manager. Founded in Auckland, New Zealand in 2014, AskNicely serves franchise, home-services, healthcare, fitness and professional-services operators. Its public REST API (`https://{domain}.asknice.ly/api/v1`) covers contact import, survey triggering, response and statistics retrieval, unsubscribe lists and GDPR erasure, authenticated with a single `X-apikey` header, and it ships a per-tenant remote MCP server for its Ask NiceAI assistant.
image: https://cdn.prod.website-files.com/5e55a51f5f18f823ee05f445/5ec34b022aca806dce613ba4_AN_logo_white.png
layout: provider
mcp_servers:
- description: AskNicely ships a first-party remote MCP server that exposes Ask NiceAI — its in-product AI assistant — to external MCP clients. It is served per tenant at https://{domain}.asknice.ly/mcp and is docum
  name: AskNicely MCP Server
  slug: asknicely-mcp-server
modified: '2026-08-06'
name: AskNicely
nav: Providers
network: true
overview: 'AskNicely publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, In-App Surveys API, Responses API, and 2 more. Tagged areas include Company, Customer Experience, NPS, Surveys, and Feedback.


  The AskNicely catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AskNicely''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 4
  name: Asknicely Rate Limits
  slug: asknicely-rate-limits
scopes:
- name: Asknicely Scopes
  scope_count: 1
  slug: asknicely-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 68.5
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 16.7
    contract_quality: 69.7
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 81.6
  previous_composite: 68.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 65.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/asknicely/refs/heads/main/screenshots/asknicely-2026-08-07T161800.png
security:
- kind: authentication
  name: Asknicely Authentication
  slug: asknicely-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Asknicely Domain Security
  slug: asknicely-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Asknicely Trust Center
  slug: asknicely-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR, CSA STAR (CAIQ), New Zealand Privacy Act
slug: asknicely
tags:
- Company
- Customer Experience
- NPS
- Surveys
- Feedback
- Reputation Management
- Software-as-a-Service
- Customer Success
- Reviews
- SMS
website: https://www.asknicely.com/
---
