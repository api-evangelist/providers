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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.9
  scored_at: '2026-09-21'
api_count: 5
apis:
- baseURL: https://api.channelseal.com/platform
  baseurl_source: declared
  description: Platform resources behind the ChannelSeal Interface Scorecard — services, service providers, channels (HTTP paths, Kafka topics, queues), applications, non-human identities (API keys, client IDs, serv
  name: ChannelSeal Platform API
  slug: platform-api
- baseURL: https://api.channelseal.com/platform
  baseurl_source: declared
  description: Discover and manage API registry entries — get, list, search, update and delete discovered or registered API specifications (OpenAPI, AsyncAPI, GraphQL, WSDL, gRPC and others) with their security sche
  name: ChannelSeal API Discovery Service API
  slug: api-discovery-service-api
- baseURL: https://api.channelseal.com/catalog
  baseurl_source: declared
  description: Import API specifications into the ChannelSeal platform (POST /v1/api-specifications/import with an ImportContext), plus Spring Boot Actuator health for the catalog service. OpenAPI 3.1.0, version 0.1
  name: ChannelSeal API Catalog API
  slug: api-catalog-api
- baseURL: https://api.channelseal.com/platform
  baseurl_source: declared
  description: Manage the data-classification vocabulary the scorecard scores against — sensitive info types (data type, format, pattern match, jurisdiction, risk), sensitive info groups (PII, Financial, Health) and
  name: ChannelSeal Data Classification API
  slug: data-classification-api
artifact_total: 9
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/authentication/channelseal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/channelseal-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/scopes/channelseal-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/channelseal-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.channelseal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.channelseal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.channelseal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.channelseal.com/api-reference
- group: auth
  title: ''
  type: Authentication
  url: https://docs.channelseal.com/api-reference#authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.channelseal.com/api-reference#rate-limiting
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.channelseal.com/api-reference#error-handling
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.channelseal.com/api-reference#changelog
- group: agent
  title: ''
  type: AgentSkill
  url: https://docs.channelseal.com/agent-skills
- group: start
  title: ''
  type: SignUp
  url: https://docs.channelseal.com/signup
- group: start
  title: ''
  type: Login
  url: https://docs.channelseal.com/signin
- group: operate
  title: ''
  type: Support
  url: mailto:support@channelseal.com
- group: company
  title: ''
  type: Blog
  url: https://www.channelseal.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.channelseal.com/blog/feed.xml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/channelseal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/channelseal
- group: commercial
  title: ''
  type: Privacy
  url: https://www.channelseal.com/privacy.html
- group: operate
  title: ''
  type: Contact
  url: mailto:hello@channelseal.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/security/channelseal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/channelseal-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/well-known/channelseal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/channelseal-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/conformance/channelseal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/channelseal-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/errors/channelseal-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/channelseal-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/lifecycle/channelseal-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/channelseal-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/conventions/channelseal-conventions.yml
  title: ''
  type: Conventions
  url: conventions/channelseal-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/rate-limits/channelseal-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/channelseal-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/plans/channelseal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/channelseal-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/changelog/channelseal-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/channelseal-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/sandbox/channelseal-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/channelseal-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/data-model/channelseal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/channelseal-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/llms/channelseal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/channelseal-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/skills/channelseal-import-and-inventory-apis.md
  title: ''
  type: AgentSkill
  url: skills/channelseal-import-and-inventory-apis.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/skills/channelseal-find-sensitive-data-flows.md
  title: ''
  type: AgentSkill
  url: skills/channelseal-find-sensitive-data-flows.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/skills/channelseal-triage-alerts.md
  title: ''
  type: AgentSkill
  url: skills/channelseal-triage-alerts.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/mcp/channelseal-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/channelseal-mcp.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.channelseal.com/privacy.html
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/overlays/channelseal-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/channelseal-platform-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/overlays/channelseal-api-discovery-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/channelseal-api-discovery-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/overlays/channelseal-catalog-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/channelseal-catalog-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/overlays/channelseal-data-classification-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/channelseal-data-classification-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/channelseal/refs/heads/main/overlays/channelseal-schemas-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/channelseal-schemas-overlay.yaml
created: '2026-09-20'
description: ChannelSeal scores, monitors, and protects the interfaces AI agents reach — APIs, MCP servers and other agents — with an Interface Scorecard per interface (agent usability, governance, risk, compliance, security), sensitive-data-flow identification from schemas and metadata without payload inspection, and inline runtime policy enforcement inside the customer's environment. Invite-only, founding-customer stage in 2026; publishes a Zudoku developer portal with OpenAPI 3.1 documents for its Platform, API Discovery, Data Classification and Catalog APIs, authenticated with OAuth 2.0 client credentials via an Auth0 tenant, plus eighteen provider-authored Agent Skills (resource and process) that drive the same APIs with curl, and an OpenTelemetry (OTLP) collector integration for feeding third-party API traffic metadata into the platform.
image: https://www.channelseal.com/images/channelseal_logo_transparent.png
layout: provider
modified: '2026-09-20'
name: ChannelSeal
nav: Providers
network: true
overview: 'ChannelSeal publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Platform API, API Discovery Service API, API Catalog API, and 1 more. Tagged areas include Company, API Security, AI Agents, MCP, and Data Classification.


  ChannelSeal''s developer surface includes authentication, documentation, API reference, changelog, signup flow, support, engineering blog, and 36 more developer resources.'
plans:
- name: Channelseal Plans Pricing
  plan_count: 3
  slug: channelseal-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Channelseal Rate Limits
  slug: channelseal-rate-limits
scopes:
- name: Channelseal Scopes
  scope_count: 5
  slug: channelseal-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 49.8
    developer_ergonomics: 59.5
    discoverability: 74.1
    operational_transparency: 52.6
  previous_composite: 51.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Channelseal Authentication
  slug: channelseal-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Channelseal Domain Security
  slug: channelseal-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: channelseal
tags:
- Company
- API Security
- AI Agents
- MCP
- Data Classification
- API Discovery
- Non-Human Identity
- Sensitive Data
- Observability
- OpenTelemetry
- Governance
website: https://www.channelseal.com/
---
