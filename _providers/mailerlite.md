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
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Mailerlite Agentic Access
  operation_count: 21
  slug: mailerlite-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 9
apis:
- description: 'The MailerLite Classic API serves legacy MailerLite Classic accounts. New integrations should target the current API at connect.mailerlite.com. Corrected 2026-08-13: the Classic documentation host is '
  name: MailerLite Classic API (Legacy)
  slug: mailerlite-classic-api
- description: The Automations API from MailerLite — 1 operation(s) for automations.
  name: MailerLite Automations API
  slug: mailerlite-automations-api
- description: The Campaigns API from MailerLite — 2 operation(s) for campaigns.
  name: MailerLite Campaigns API
  slug: mailerlite-campaigns-api
- description: The Fields API from MailerLite — 1 operation(s) for fields.
  name: MailerLite Fields API
  slug: mailerlite-fields-api
- description: The Forms API from MailerLite — 1 operation(s) for forms.
  name: MailerLite Forms API
  slug: mailerlite-forms-api
- description: The Groups API from MailerLite — 2 operation(s) for groups.
  name: MailerLite Groups API
  slug: mailerlite-groups-api
- description: The Segments API from MailerLite — 1 operation(s) for segments.
  name: MailerLite Segments API
  slug: mailerlite-segments-api
- description: The Subscribers API from MailerLite — 4 operation(s) for subscribers.
  name: MailerLite Subscribers API
  slug: mailerlite-subscribers-api
- description: The Webhooks API from MailerLite — 2 operation(s) for webhooks.
  name: MailerLite Webhooks API
  slug: mailerlite-webhooks-api
artifact_total: 32
asyncapis:
- description: AsyncAPI 2.6 description of MailerLite's outbound webhook surface. MailerLite delivers event notifications by issuing HTTP POST requests with a JSON body to a callback URL the customer registers throu
  name: MailerLite Webhooks
  slug: mailerlite-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MailerLite Automations API
  slug: open-mailerlite-automations-api
- collection_type: open
  name: MailerLite Automations Campaigns API
  slug: open-mailerlite-campaigns-api
- collection_type: open
  name: MailerLite Automations Fields API
  slug: open-mailerlite-fields-api
- collection_type: open
  name: MailerLite Automations Forms API
  slug: open-mailerlite-forms-api
- collection_type: open
  name: MailerLite Automations Groups API
  slug: open-mailerlite-groups-api
- collection_type: open
  name: MailerLite Automations Segments API
  slug: open-mailerlite-segments-api
- collection_type: open
  name: MailerLite Automations Subscribers API
  slug: open-mailerlite-subscribers-api
- collection_type: open
  name: MailerLite Automations Webhooks API
  slug: open-mailerlite-webhooks-api
- collection_type: open
  name: MailerLite API
  slug: open-mailerlite
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mailerlite-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mailerlite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mailerlite-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mailerlite-international
- group: company
  title: ''
  type: Website
  url: https://www.mailerlite.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.mailerlite.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailerlite
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mailerlite.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/mailerlite-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mailerlite-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mailerlite-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.mailerlite.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mailerlite-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mailerlite-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://github.com/mailerlite/mailerlite-skills
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mailerlite-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/mailerlite-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mailerlite-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/mailerlite-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mailerlite-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mailerlite-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mailerlite-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mailerlite-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mailerlite.com/
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/mailerlite-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: https://developers.mailerlite.com/api/webhooks
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mailerlite-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: https://www.mailerlite.com/robots.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mailerlite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.mailerlite.com/legal/responsible-disclosure-program
- group: auth
  title: ''
  type: TrustCenter
  url: security/mailerlite-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mailerlite.com/trust-page
- group: design
  title: ''
  type: Conformance
  url: conformance/mailerlite-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mailerlite-subscribers-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mailerlite-groups-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mailerlite-segments-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mailerlite-fields-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mailerlite-campaigns-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mailerlite-automations-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mailerlite-forms-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mailerlite-webhooks-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.mailerlite.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.mailerlite.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.mailerlite.com/api/subscribers
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.mailerlite.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.mailerlite.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.mailerlite.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.mailerlite.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.mailerlite.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mailerlite.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mailerlite.com/legal/privacy-policy
created: '2026-05-08'
description: MailerLite is an email marketing and automation platform used by creators, e-commerce sellers and small businesses to build lists, send campaigns and run behavioural automations. The current REST API at connect.mailerlite.com exposes subscribers, groups, segments, custom fields, campaigns, automations, forms, webhooks, batching, and a full e-commerce surface (shops, products, categories, customers, orders, carts) that drives abandoned-cart and post-purchase automations. Authentication is a bearer API key minted in the dashboard; responses are cursor-paginated and the API version can be pinned with an X-Version date header. Alongside the REST API, MailerLite ships six official SDKs, a first-party Go CLI with an interactive TUI, a published Agent Skill, and a hosted OAuth-protected MCP server at mcp.mailerlite.com exposing roughly 76 tools to AI assistants. A legacy Classic API v2 still serves older accounts.
finops:
- name: Mailerlite Finops
  service_category: Email Marketing
  slug: mailerlite-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mailerlite.png
layout: provider
mcp_servers:
- description: ''
  name: MailerLite MCP Server
  slug: mailerlite-mcp-server
- description: ''
  name: MCP Server Manifest
  slug: mcp-server-manifest
modified: '2026-08-13'
name: MailerLite
nav: Providers
network: true
overview: 'MailerLite publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Automations API, Campaigns API, Fields API, and 5 more. Tagged areas include Email Marketing, Automation, Newsletters, Subscribers, and Campaigns.


  The MailerLite catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  MailerLite''s developer surface includes authentication, developer portal, pricing, CLI, documentation, API reference, getting-started guide, and 45 more developer resources.'
plans:
- name: Mailerlite Plans Pricing
  plan_count: 4
  slug: mailerlite-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Mailerlite Rate Limits
  slug: mailerlite-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: MailerLite API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: mailerlite-asyncapi-spectral-rules
score:
  band: exemplar
  composite: 77.6
  delta: 10.6
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 41.7
    contract_quality: 62.3
    developer_ergonomics: 78.6
    discoverability: 92.6
    governance: 41.7
    operational_transparency: 57.9
  previous_composite: 67.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 59.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/mailerlite/refs/heads/main/screenshots/mailerlite-2026-06-20T184854.png
security:
- kind: authentication
  name: Mailerlite Authentication
  slug: mailerlite-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Mailerlite Domain Security
  slug: mailerlite-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Mailerlite Vulnerability Disclosure
  slug: mailerlite-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Mailerlite Trust Center
  slug: mailerlite-trust-center
  summary_line: ISO/IEC 27001:2022, PCI DSS, GDPR, EU-U.S. Data Privacy Framework, Swiss-U.S. Data Privacy Framework, UK Extension to the EU-U.S. Data Privacy Framework
skill_count: 1
skills:
- name: MailerLite
  slug: mailerlite
slug: mailerlite
tags:
- Email Marketing
- Automation
- Newsletters
- Subscribers
- Campaigns
- Webhooks
- E-commerce
- Segmentation
- Transactional Email
- MCP
website: https://www.mailerlite.com/
---
