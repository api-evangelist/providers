---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations related to user's note history.
  name: HackMD History API
  slug: hackmd-history-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations to retrieve user profile information.
  name: HackMD Profile API
  slug: hackmd-profile-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations related to folders within a team.
  name: HackMD Team Folders API
  slug: hackmd-team-folders-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations related to notes within a team.
  name: HackMD Team Notes API
  slug: hackmd-team-notes-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations related to user teams.
  name: HackMD Teams API
  slug: hackmd-teams-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations for listing and restoring trashed notes.
  name: HackMD Trash API
  slug: hackmd-trash-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations related to a user's personal folders.
  name: HackMD User Folders API
  slug: hackmd-user-folders-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations related to a user's personal notes.
  name: HackMD User Notes API
  slug: hackmd-user-notes-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations for reading and resolving note comments.
  name: HackMD Comments API
  slug: hackmd-comments-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations for managing webhooks in a team workspace.
  name: HackMD Team Webhooks API
  slug: hackmd-team-webhooks-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations for listing, retrieving, comparing, creating, and updating note versions.
  name: HackMD Versions API
  slug: hackmd-versions-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations for managing webhooks in a personal workspace.
  name: HackMD Webhooks API
  slug: hackmd-webhooks-api
artifact_total: 30
collections:
- collection_type: open
  name: HackMD Open History API
  slug: open-hackmd-history-api
- collection_type: open
  name: HackMD Open History Profile API
  slug: open-hackmd-profile-api
- collection_type: open
  name: HackMD Open History Team Folders API
  slug: open-hackmd-team-folders-api
- collection_type: open
  name: HackMD Open History Team Notes API
  slug: open-hackmd-team-notes-api
- collection_type: open
  name: HackMD Open History Teams API
  slug: open-hackmd-teams-api
- collection_type: open
  name: HackMD Open History Trash API
  slug: open-hackmd-trash-api
- collection_type: open
  name: HackMD Open History User Folders API
  slug: open-hackmd-user-folders-api
- collection_type: open
  name: HackMD Open History User Notes API
  slug: open-hackmd-user-notes-api
common:
- group: other
  href: https://artifacts.apis.io/hackmd/capabilities/hackmd-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hackmd-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/hackmd/plans/hackmd-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hackmd-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://hackmd.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hackmd.io/@docs/developer-portal
- group: docs
  title: ''
  type: Documentation
  url: https://hackmd.io/@docs/developer-portal
- group: docs
  title: ''
  type: APIReference
  url: https://api.hackmd.io/v1/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://hackmd.io/@docs/how-to-issue-an-api-token
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hackmdio
- group: company
  title: ''
  type: Blog
  url: https://hackmd.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://hackmd.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://hackmd.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hackmd.io/s/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hackmd.io/s/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hackmd.io/
- group: operate
  href: https://artifacts.apis.io/hackmd/changelog/hackmd-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hackmd-changelog.yml
- group: auth
  href: https://artifacts.apis.io/hackmd/authentication/hackmd-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hackmd-authentication.yml
- group: docs
  href: https://artifacts.apis.io/hackmd/openapi/_original/hackmd-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/hackmd-openapi-original.json
- group: other
  href: https://artifacts.apis.io/hackmd/overlays/hackmd-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hackmd-openapi-overlay.yaml
- group: build
  href: https://artifacts.apis.io/hackmd/packages/hackmd-packages.yml
  title: ''
  type: Packages
  url: packages/hackmd-packages.yml
- group: build
  href: https://artifacts.apis.io/hackmd/packages/hackmd-packages.yml
  title: ''
  type: SDKs
  url: packages/hackmd-packages.yml
- group: build
  href: https://artifacts.apis.io/hackmd/cli/hackmd-cli.yml
  title: ''
  type: CLI
  url: cli/hackmd-cli.yml
- group: agent
  href: https://artifacts.apis.io/hackmd/mcp/hackmd-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/hackmd-mcp.yml
- group: agent
  href: https://artifacts.apis.io/hackmd/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/hackmd/llms/hackmd-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hackmd-llms.txt
- group: agent
  href: https://artifacts.apis.io/hackmd/well-known/hackmd-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hackmd-well-known.yml
- group: other
  href: https://artifacts.apis.io/hackmd/well-known/hackmd-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/hackmd-api-catalog.json
- group: design
  href: https://artifacts.apis.io/hackmd/conventions/hackmd-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hackmd-conventions.yml
- group: design
  href: https://artifacts.apis.io/hackmd/errors/hackmd-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hackmd-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/hackmd/rate-limits/hackmd-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hackmd-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/hackmd/lifecycle/hackmd-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hackmd-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hackmd/data-model/hackmd-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hackmd-data-model.yml
- group: design
  href: https://artifacts.apis.io/hackmd/conformance/hackmd-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hackmd-conformance.yml
- group: auth
  href: https://artifacts.apis.io/hackmd/security/hackmd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hackmd-domain-security.yml
created: '2026-07-17'
description: HackMD is a real-time collaborative Markdown editor and knowledge base for individuals and teams. Multiple people can co-edit a Markdown document live, organize notes into folders and team workspaces, and publish them as web pages, slide decks or books. HackMD exposes a v1 REST API at api.hackmd.io that lets developers programmatically create, read, update and delete personal and team notes, manage folders and folder ordering, upload image attachments, restore notes from trash, and read the current user profile and view history. The API authenticates with a personal access token sent as an HTTP bearer credential, is described by a published OpenAPI 3.0 specification and Swagger UI, ships an official Node.js/TypeScript client (@hackmd/api) and command-line interface, and advertises its full developer surface through an RFC 9727 api-catalog. HackMD is a Techstars-backed company.
finops:
- has_sources: true
  method: derived
  name: Hackmd Finops
  primary_unit: team
  service_category: ''
  slug: hackmd-finops
  template: false
image: https://hackmd.io/favicon.png
layout: provider
modified: '2026-07-19'
name: HackMD
nav: Providers
network: true
overview: 'HackMD publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including History API, Profile API, Team Folders API, and 9 more. Tagged areas include Company, Markdown, Collaboration, Documentation, and Note Taking.


  The HackMD catalog on APIs.io includes 1 Spectral governance ruleset.


  HackMD''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 26 more developer resources.'
plans:
- name: Hackmd Plans Pricing
  plan_count: 3
  slug: hackmd-plans-pricing
- name: Hackmd Price Estimates
  plan_count: 0
  slug: hackmd-price-estimates
random_paper: 16
rate_limits:
- limit_count: 2
  name: Hackmd Rate Limits
  slug: hackmd-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: HackMD API Rules
  rule_count: 66
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 8
  slug: hackmd-rules
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 31
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 53.5
    developer_ergonomics: 68.5
    discoverability: 73.2
    operational_transparency: 55.3
  previous_composite: 60.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 57.1
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hackmd/hackmd-2026-07-25T220526.png
security:
- kind: authentication
  name: Hackmd Authentication
  slug: hackmd-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hackmd Domain Security
  slug: hackmd-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Create and publish a HackMD note
  slug: hackmd-create-and-publish-note
- name: Manage HackMD team notes
  slug: hackmd-manage-team-notes
- name: Organize HackMD notes with folders
  slug: hackmd-organize-with-folders
slug: hackmd
tags:
- Company
- Markdown
- Collaboration
- Documentation
- Note Taking
- Knowledge Base
- Productivity
- Content
website: https://hackmd.io/
---
