---
access_model:
  confidence: high
  label: Freemium · Self-serve signup · 14-day trial, no card
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
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
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.1
  scored_at: '2026-09-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Developerhub Agentic Access
  operation_count: 20
  slug: developerhub-agentic-access
  summary_line: 20 operations · 9 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: DeveloperHub provides a hosted platform for creating developer documentation including API references auto-generated from OpenAPI specs, user guides with a WYSIWYG editor, versioned documentation, ful
  name: DeveloperHub Documentation Platform
  slug: platform
- baseURL: https://api.developerhub.io/api/v1
  baseurl_source: declared
  description: Lists the documentation sections inside a version of a DeveloperHub project — 1 operation.
  name: DeveloperHub Documentation API
  slug: developerhub-documentation-api
- baseURL: https://api.developerhub.io/api/v1
  baseurl_source: declared
  description: Creates, reads, updates, publishes and deletes documentation pages, with Markdoc bodies staged as drafts until an explicit publish — 6 operations.
  name: DeveloperHub Pages API
  slug: developerhub-pages-api
- baseURL: https://api.developerhub.io/api/v1
  baseurl_source: declared
  description: Project-level operations — export, search, whole-project dump, audit log and users. Export and audit are enterprise-plan only — 5 operations.
  name: DeveloperHub Project API
  slug: developerhub-project-api
- baseURL: https://api.developerhub.io/api/v1
  baseurl_source: declared
  description: Grants, lists and revokes access for invited readers of a private documentation project, keyed on email address — 3 operations.
  name: DeveloperHub Reader Access API
  slug: developerhub-reader-access-api
- baseURL: https://api.developerhub.io/api/v1
  baseurl_source: declared
  description: Uploads, downloads and publishes the OpenAPI specification behind an API reference — the CI/CD surface, and the one replay-safe write in the API — 3 operations.
  name: DeveloperHub References API
  slug: developerhub-references-api
- baseURL: https://api.developerhub.io/api/v1
  baseurl_source: declared
  description: Lists, updates, clones and reports on documentation versions, including a broken-link check for the whole version — 5 operations.
  name: DeveloperHub Versions API
  slug: developerhub-versions-api
- baseURL: https://api.developerhub.io/api/v1
  baseurl_source: declared
  description: Creates and lists changelog posts from Markdoc content, with cursor pagination and named API-key permissions (changelog.edit, changelog.read) — 2 operations.
  name: DeveloperHub Changelog API
  slug: developerhub-changelog-api
- description: Two first-party remote MCP servers over Streamable HTTP. The reader server runs at the /mcp route of every customer docs site and exposes one read-only search tool anonymously; the editor server at ai
  name: DeveloperHub MCP Servers
  slug: developerhub-mcp
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DeveloperHub.io Documentation API
  slug: open-developerhub-documentation-api
- collection_type: open
  name: DeveloperHub.io Documentation Pages API
  slug: open-developerhub-pages-api
- collection_type: open
  name: DeveloperHub.io Documentation Project API
  slug: open-developerhub-project-api
- collection_type: open
  name: DeveloperHub.io Documentation Reader Access API
  slug: open-developerhub-reader-access-api
- collection_type: open
  name: DeveloperHub.io Documentation References API
  slug: open-developerhub-references-api
- collection_type: open
  name: DeveloperHub.io Documentation Versions API
  slug: open-developerhub-versions-api
- collection_type: open
  name: DeveloperHub.io API
  slug: open-developerhub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/developerhub-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/developerhub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/developerhub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/developerhub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/developerhub-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/developerhub-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/developerhub-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/developerhub-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/developerhub-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/developerhub-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/developerhub-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/developerhub-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/developerhub-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/developerhub-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/developerhub-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/developerhub-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/developerhub-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/developerhub-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/developerhub-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/developerhub-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/developerhub-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/developerhub-llms.txt
- group: operate
  title: ''
  type: StatusPage
  url: https://status.developerhub.io
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.developerhub.io/support-center/upcoming-features
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/developerhub-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/developer-hub
- group: company
  title: ''
  type: Website
  url: https://developerhub.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.developerhub.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developerhub.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.developerhub.io/api/ref
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developerhub.io/support-center/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://developerhub.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://developerhub.io/blog
- group: start
  title: ''
  type: Login
  url: https://app.developerhub.io
- group: start
  title: ''
  type: SignUp
  url: https://app.developerhub.io/signup
- group: operate
  title: ''
  type: Support
  url: https://docs.developerhub.io/support-center/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://talk.developerhub.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developerhub.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developerhub.io/terms
created: '2026-03-25'
description: 'DeveloperHub is a hosted developer documentation platform that enables teams to create beautiful API references, user guides, and knowledge bases. It features auto-generated API documentation from OpenAPI specifications, built-in versioning, full-text search, custom domains, and a WYSIWYG editor. DeveloperHub provides a complete developer portal solution with support for multiple documentation projects, custom branding, and SEO optimization. The platform is itself programmable: a published OpenAPI 3.2 contract covers 25 operations for pages, versions, documentation sections, API references, reader access, project export and changelog posts, and two first-party remote MCP servers expose the same surface to agents — a read-only reader server on every customer''s docs site and an OAuth-protected editor server.'
finops:
- name: Developerhub Finops
  service_category: API
  slug: developerhub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/developerhub.png
layout: provider
mcp_servers:
- description: ''
  name: DeveloperHub MCP Server
  slug: developerhub-mcp-server
modified: '2026-09-06'
name: DeveloperHub
nav: Providers
network: true
overview: 'DeveloperHub publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Documentation API, Pages API, Project API, and 4 more. Tagged areas include API Reference, Developer Portals, Documentation, Knowledge Base, and OpenAPI.


  DeveloperHub''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, pricing, and 33 more developer resources.'
plans:
- name: Developerhub Plans Pricing
  plan_count: 4
  slug: developerhub-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 25
  name: Developerhub Rate Limits
  slug: developerhub-rate-limits
scopes:
- name: Developerhub Scopes
  scope_count: 0
  slug: developerhub-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 20.9
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 59.4
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 34.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/developerhub/refs/heads/main/screenshots/developerhub-2026-06-20T175947.png
security:
- kind: authentication
  name: Developerhub Authentication
  slug: developerhub-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Developerhub Domain Security
  slug: developerhub-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Developerhub Vulnerability Disclosure
  slug: developerhub-vulnerability-disclosure
  summary_line: disclosure policy published
slug: developerhub
tags:
- API Reference
- Developer Portals
- Documentation
- Knowledge Base
- OpenAPI
- Docs as Code
- Model Context Protocol
- Agent Skills
website: https://developerhub.io
---
