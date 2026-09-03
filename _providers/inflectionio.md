---
access_model:
  confidence: high
  label: Annual contract, MMC-metered, published price ladder
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Inflectionio Agentic Access
  operation_count: 20
  slug: inflectionio-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.inflection.io/v1
  baseurl_source: declared
  description: The Contact Activity API from Inflection.io — 4 operation(s) for contact activity.
  name: Inflection.io Contact Activity API
  slug: inflectionio-contact-activity-api
- baseURL: https://api.inflection.io/v1
  baseurl_source: declared
  description: The Contacts API from Inflection.io — 6 operation(s) for contacts.
  name: Inflection.io Contacts API
  slug: inflectionio-contacts-api
- baseURL: https://api.inflection.io/v1
  baseurl_source: declared
  description: The Emails API from Inflection.io — 2 operation(s) for creating and reading HTML emails.
  name: Inflection.io Emails API
  slug: inflectionio-emails-api
- baseURL: https://api.inflection.io/v1
  baseurl_source: declared
  description: The Email Versions API from Inflection.io — 1 operation for pushing a per-contact personalized version of a Personalized Email Asset.
  name: Inflection.io Email Versions API
  slug: inflectionio-email-versions-api
- baseURL: https://api.inflection.io/v1
  baseurl_source: declared
  description: The Lists and Members API from Inflection.io — 7 operation(s) for lists and members.
  name: Inflection.io Lists and Members API
  slug: inflectionio-lists-and-members-api
- description: Inflection's first-party remote MCP server — the agent-facing authoring surface for journeys, audiences, segments, emails, tokens and analytics, gated by OAuth 2.1 with PKCE.
  name: Inflection MCP
  slug: inflectionio-mcp
artifact_total: 20
asyncapis:
- description: ''
  name: Inflectionio Webhooks
  slug: inflectionio-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Inflection Developer Contact Activity API
  slug: open-inflectionio-contact-activity-api
- collection_type: open
  name: Inflection Developer Contact Activity Contacts API
  slug: open-inflectionio-contacts-api
- collection_type: open
  name: Inflection Developer Contact Activity Lists and Members API
  slug: open-inflectionio-lists-and-members-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.inflection.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.inflection.io/api-reference/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inflection.io/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.inflection.io/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.inflection.io/api-reference/quickstart
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.inflection.io
- group: operate
  title: ''
  type: Support
  url: https://docs.inflection.io
- group: company
  title: ''
  type: Blog
  url: https://www.inflection.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.inflection.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.inflection.io/login/start
- group: start
  title: ''
  type: Login
  url: https://app.inflection.io/login/start
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.inflection.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.inflection.io/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inflectionio
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.inflection.io/whats-new/july-2026
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/inflectionio-changelog.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/inflectionio-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/inflectionio-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inflectionio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/inflectionio-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/inflectionio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/inflectionio-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/inflectionio-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/inflectionio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/inflectionio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.inflection.io/agents/mcp-trust-security
- group: auth
  title: ''
  type: TrustCenter
  url: security/inflectionio-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.inflection.io/agents/mcp-trust-security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/inflectionio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inflectionio-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/inflectionio-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/inflectionio-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/inflectionio-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/inflectionio-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inflectionio-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/inflectionio-agentic-access.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inflectionio-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/inflectionio-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/inflectionio-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/inflectionio-packages.yml
- group: design
  title: ''
  type: Components
  url: components/inflectionio-components.yml
created: '2026-07-17'
description: 'Inflection.io is a B2B marketing automation platform positioned as a modern, AI-native replacement for legacy tools like Marketo. It unifies target accounts, product users, customers, and leads with product-usage, sales, and behavioral signals so marketing teams can build audiences, draft campaigns, map customer journeys, score accounts, and report to the CMO — executing in minutes rather than weeks. The Inflection Developer API is a JSON-over-HTTPS REST API (OpenAPI 3.1, base https://api.inflection.io/v1) for reading and writing the people in a workspace: their profiles, product and marketing activity, static lists, emails, and per-contact personalized email versions, authenticated with scoped Personal Access Tokens or an OAuth 2.1 connected app. Alongside it Inflection runs a first-party remote MCP server at mcp.inflection.io — OAuth 2.1 with PKCE, its own trust and security page — that exposes the authoring surface the REST API does not: journeys, audiences, segments, tokens
  and analytics, driven by specialist agents. Surfaced as a version-one-ventures portfolio company and enriched from the provider''s public developer, agent, and trust surfaces.'
image: https://www.inflection.io/img/asset/YXNzZXRzL29nLWltYWdlLmpwZw/og-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: Inflection MCP
  slug: inflection-mcp
modified: '2026-08-13'
name: Inflection.io
nav: Providers
network: true
overview: 'Inflection.io publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Contact Activity API, Contacts API, Emails API, and 2 more. Tagged areas include Company, Software-as-a-Service, Marketing, Marketing Automation, and Email Marketing.


  The Inflection.io catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Inflection.io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 35 more developer resources.'
plans:
- name: Inflectionio Plans Pricing
  plan_count: 1
  slug: inflectionio-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Inflectionio Rate Limits
  slug: inflectionio-rate-limits
scopes:
- name: Inflectionio Scopes
  scope_count: 3
  slug: inflectionio-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 25
    catalog_gap: 62.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 63.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inflectionio/refs/heads/main/screenshots/inflectionio-2026-07-25T222410.png
security:
- kind: authentication
  name: Inflectionio Authentication
  slug: inflectionio-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Inflectionio Domain Security
  slug: inflectionio-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Inflectionio Vulnerability Disclosure
  slug: inflectionio-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Inflectionio Trust Center
  slug: inflectionio-trust-center
  summary_line: SOC 2, GDPR, CCPA, Penetration test
slug: inflectionio
tags:
- Company
- Software-as-a-Service
- Marketing
- Marketing Automation
- Email Marketing
- Customer Data
- B2B
- Contacts
- MCP
- Agents
- Artificial Intelligence
- Customer Journeys
- Webhook
website: https://www.inflection.io
---
