---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.6
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: REST API for retrieving public company org charts, prospecting positions/people, and monitoring credit usage. Metered in credits; authenticated with an X-Api-Key header.
  name: The Org API
  slug: the-org-api
artifact_total: 8
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/security/theorg-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/theorg-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://theorg.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.theorg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.theorg.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.theorg.com/api/endpoints/company-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.theorg.com/api/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.theorg.com/api/change-log
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/changelog/theorg-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/theorg-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/mcp/theorg-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/theorg-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/mcp/theorg-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/theorg-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/authentication/theorg-authentication.yml
  title: ''
  type: Authentication
  url: authentication/theorg-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/scopes/theorg-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/theorg-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/conventions/theorg-conventions.yml
  title: ''
  type: Conventions
  url: conventions/theorg-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/errors/theorg-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/theorg-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/lifecycle/theorg-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/theorg-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/data-model/theorg-data-model.yml
  title: ''
  type: DataModel
  url: data-model/theorg-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/components/theorg-components.yml
  title: ''
  type: Components
  url: components/theorg-components.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/rate-limits/theorg-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/theorg-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/conformance/theorg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/theorg-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/llms/theorg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/theorg-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/security/theorg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/theorg-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/well-known/theorg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/theorg-well-known.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/plans/theorg-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/theorg-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://theorg.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.theorg.com/en/
- group: company
  title: ''
  type: Blog
  url: https://blog.theorg.com/
- group: start
  title: ''
  type: SignUp
  url: https://theorg.com/signup
- group: start
  title: ''
  type: Login
  url: https://theorg.com/subscription
- group: commercial
  title: ''
  type: TermsOfService
  url: https://theorg.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://theorg.com/privacy
created: '2026-07-17'
description: 'The Org operates the world''s largest network of public organizational charts, mapping companies, their teams, and reporting hierarchies. Its developer platform exposes a metered REST API and an official MCP server for retrieving a company''s public org chart by domain or LinkedIn URL, prospecting positions and people with rich filters, resolving a person''s manager, and monitoring credit usage. Authentication is via an account-scoped X-Api-Key header over HTTPS, usage is metered in monthly credits, and the same key powers a remote Model Context Protocol endpoint exposing thirteen tools for agent-native access — company and person lookup, job search, reporting-line traversal, work-email resolution, and lead-list management. The MCP surface is materially wider than the REST API: eight of the thirteen tools have no REST equivalent, and list creation is the only write operation The Org exposes anywhere. Originally added to the API Evangelist network as a portfolio company of Balderton
  Capital.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/theorg.png
layout: provider
mcp_servers:
- description: ''
  name: The Org MCP Server
  slug: the-org-mcp-server
modified: '2026-08-14'
name: The Org
nav: Providers
network: true
overview: 'The Org publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Organizational Charts, People Data, Sales Intelligence, and Prospecting.


  The Org''s developer surface includes documentation, API reference, getting-started guide, changelog, authentication, pricing, support, and 24 more developer resources.'
plans:
- name: Theorg Plans Pricing
  plan_count: 4
  slug: theorg-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Theorg Rate Limits
  slug: theorg-rate-limits
scopes:
- name: Theorg Scopes
  scope_count: 1
  slug: theorg-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 68.5
    operational_transparency: 36.8
  previous_composite: 42.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/screenshots/theorg-2026-08-17T082341.png
security:
- kind: authentication
  name: Theorg Authentication
  slug: theorg-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Theorg Domain Security
  slug: theorg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Theorg Trust Center
  slug: theorg-trust-center
  summary_line: trust center published
slug: theorg
tags:
- Company
- Organizational Charts
- People Data
- Sales Intelligence
- Prospecting
- Org Chart
- B2B Data
- MCP
- Contact Data
- Lead Generation
- Job
- Agents
website: https://theorg.com/
---
