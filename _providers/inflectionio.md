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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 57.1
  scored_at: '2026-11-06'
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
- description: Inflection's first-party remote MCP server — the agent-facing authoring surface for journeys, audiences, segments, emails, tokens and analytics, gated by OAuth 2.1 with PKCE.
  name: Inflection MCP
  slug: inflectionio-mcp
- baseURL: https://api.inflection.io/v1
  baseurl_source: declared
  description: Read journeys (campaigns), their schedule and their derived status.
  name: Inflection.io Journeys API
  slug: inflectionio-journeys-api
- baseURL: https://api.inflection.io/v1
  baseurl_source: declared
  description: Static and dynamic lists, and static-list members.
  name: Inflection.io Lists API
  slug: inflectionio-lists-api
- baseURL: https://api.inflection.io/v1
  baseurl_source: declared
  description: Read organizations (company accounts) and a contact's memberships.
  name: Inflection.io Organizations API
  slug: inflectionio-organizations-api
- baseURL: https://api.inflection.io/v1
  baseurl_source: declared
  description: Read product users -- the logins underneath a contact -- by id or email, and list them for a contact or an organization.
  name: Inflection.io Product Users API
  slug: inflectionio-product-users-api
- baseURL: https://api.inflection.io/v1
  baseurl_source: declared
  description: Send and engagement metrics for journeys and emails, with a journey rollup.
  name: Inflection.io Stats API
  slug: inflectionio-stats-api
artifact_total: 31
asyncapis:
- description: ''
  name: Inflectionio Webhooks
  slug: inflectionio-webhooks
collections:
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
- group: other
  href: https://artifacts.apis.io/inflectionio/capabilities/inflectionio-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/inflectionio-capability-edges.yml
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
  href: https://artifacts.apis.io/inflectionio/changelog/inflectionio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/inflectionio-changelog.yml
- group: docs
  href: https://artifacts.apis.io/inflectionio/openapi/_original/inflectionio-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/inflectionio-openapi-original.yml
- group: other
  href: https://artifacts.apis.io/inflectionio/overlays/inflectionio-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/inflectionio-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/inflectionio/authentication/inflectionio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/inflectionio-authentication.yml
- group: auth
  href: https://artifacts.apis.io/inflectionio/scopes/inflectionio-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/inflectionio-scopes.yml
- group: design
  href: https://artifacts.apis.io/inflectionio/conventions/inflectionio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/inflectionio-conventions.yml
- group: design
  href: https://artifacts.apis.io/inflectionio/errors/inflectionio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/inflectionio-problem-types.yml
- group: design
  href: https://artifacts.apis.io/inflectionio/data-model/inflectionio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/inflectionio-data-model.yml
- group: design
  href: https://artifacts.apis.io/inflectionio/lifecycle/inflectionio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/inflectionio-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/inflectionio/conformance/inflectionio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/inflectionio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.inflection.io/agents/mcp-trust-security
- group: auth
  href: https://artifacts.apis.io/inflectionio/security/inflectionio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/inflectionio-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.inflection.io/agents/mcp-trust-security
- group: auth
  href: https://artifacts.apis.io/inflectionio/security/inflectionio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/inflectionio-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/inflectionio/security/inflectionio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inflectionio-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/inflectionio/mcp/inflectionio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/inflectionio-mcp.yml
- group: build
  href: https://artifacts.apis.io/inflectionio/mcp/inflectionio-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/inflectionio-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/inflectionio/a2a/inflectionio-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/inflectionio-a2a.yml
- group: agent
  href: https://artifacts.apis.io/inflectionio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/inflectionio/well-known/inflectionio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/inflectionio-well-known.yml
- group: agent
  href: https://artifacts.apis.io/inflectionio/llms/inflectionio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/inflectionio-llms.txt
- group: agent
  href: https://artifacts.apis.io/inflectionio/agentic-access/inflectionio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/inflectionio-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/inflectionio/rate-limits/inflectionio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/inflectionio-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/inflectionio/plans/inflectionio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/inflectionio-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/inflectionio/asyncapi/inflectionio-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/inflectionio-webhooks.yml
- group: build
  href: https://artifacts.apis.io/inflectionio/packages/inflectionio-packages.yml
  title: ''
  type: Packages
  url: packages/inflectionio-packages.yml
- group: design
  href: https://artifacts.apis.io/inflectionio/components/inflectionio-components.yml
  title: ''
  type: Components
  url: components/inflectionio-components.yml
- group: operate
  title: ''
  type: Contact
  url: mailto:support@inflection.io
created: '2026-07-17'
description: 'Inflection.io is a B2B marketing automation platform positioned as a modern, AI-native replacement for legacy tools like Marketo. It unifies target accounts, product users, customers, and leads with product-usage, sales, and behavioral signals so marketing teams can build audiences, draft campaigns, map customer journeys, score accounts, and report to the CMO — executing in minutes rather than weeks. The Inflection Developer API is a JSON-over-HTTPS REST API (OpenAPI 3.1, base https://api.inflection.io/v1) for reading and writing the people in a workspace: their profiles, product and marketing activity, static lists, emails, and per-contact personalized email versions, authenticated with scoped Personal Access Tokens or an OAuth 2.1 connected app. Alongside it Inflection runs a first-party remote MCP server at mcp.inflection.io — OAuth 2.1 with PKCE, its own trust and security page — that exposes the authoring surface the REST API does not: journeys, audiences, segments, tokens
  and analytics, driven by specialist agents. Surfaced as a version-one-ventures portfolio company and enriched from the provider''s public developer, agent, and trust surfaces.'
finops:
- has_sources: true
  method: derived
  name: Inflectionio Finops
  primary_unit: monthly marketed contacts (mmcs)
  service_category: ''
  slug: inflectionio-finops
  template: false
image: https://www.inflection.io/img/asset/YXNzZXRzL29nLWltYWdlLmpwZw/og-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.inflection.io over HTTP requiring OAuth; 17 tools listed.
  name: Inflection MCP
  slug: inflection-mcp
modified: '2026-08-13'
name: Inflection.io
nav: Providers
network: true
overview: 'Inflection.io publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Contact Activity API, Contacts API, Emails API, and 7 more. Tagged areas include Company, Software-as-a-Service, Marketing, Marketing Automation, and Email Marketing.


  The Inflection.io catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Inflection.io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Inflectionio Plans Pricing
  plan_count: 2
  slug: inflectionio-plans-pricing
- name: Inflectionio Price Estimates
  plan_count: 0
  slug: inflectionio-price-estimates
random_paper: 11
rate_limits:
- limit_count: 2
  name: Inflectionio Rate Limits
  slug: inflectionio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Inflection.io API Rules
  rule_count: 61
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 7
  slug: inflectionio-rules
scopes:
- name: Inflectionio Scopes
  scope_count: 3
  slug: inflectionio-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: exemplar
  composite: 67.8
  coverage:
    artifact_dirs: 33
    catalog_earned: 60.5
    catalog_earned_first_party: 16.0
    catalog_gap: 54.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 76.3
    contract_governance: 31.8
    contract_quality: 61.8
    developer_ergonomics: 64.3
    discoverability: 73.2
    operational_transparency: 57.9
  previous_composite: 66.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 60.0
      total: 15
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/inflectionio/inflectionio-2026-07-25T222410.png
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
skill_count: 5
skills:
- name: Batch upsert contacts
  slug: inflectionio-batch-upsert-contacts
- name: Build and populate a static list
  slug: inflectionio-build-static-list
- name: Send a per-contact personalized email version
  slug: inflectionio-personalized-email-version
- name: Inflection
  slug: inflectionio-provider-published-skill
- name: Sync a contact into Inflection
  slug: inflectionio-sync-contact
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
- Customer Journey
- Webhook
- A2A
website: https://www.inflection.io
---
