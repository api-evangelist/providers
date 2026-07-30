---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Slite Agentic Access
  operation_count: 25
  slug: slite-agentic-access
  summary_line: 25 operations · 10 acting
api_count: 7
apis:
- description: The Ask API from Slite — 2 operation(s) for ask.
  name: Slite Ask API
  slug: slite-ask-api
- description: The Groups API from Slite — 2 operation(s) for groups.
  name: Slite Groups API
  slug: slite-groups-api
- description: The Knowledge Management API from Slite — 4 operation(s) for knowledge management.
  name: Slite Knowledge Management API
  slug: slite-knowledge-management-api
- description: The Me API from Slite — 1 operation(s) for me.
  name: Slite Me API
  slug: slite-me-api
- description: The Notes API from Slite — 8 operation(s) for notes.
  name: Slite Notes API
  slug: slite-notes-api
- description: The Search Notes API from Slite — 1 operation(s) for search notes.
  name: Slite Search Notes API
  slug: slite-search-notes-api
- description: The Users API from Slite — 2 operation(s) for users.
  name: Slite Users API
  slug: slite-users-api
artifact_total: 74
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/slite-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/slite-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.slite.com/
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.slite.com/openapi.json
- group: auth
  title: ''
  type: Authentication
  url: https://developers.slite.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sliteteam
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/sliteteam/slite-api-js-examples
- group: company
  title: ''
  type: Blog
  url: https://slite.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://slite.com/changelog
- group: operate
  title: ''
  type: Status
  url: https://status.slite.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/slitehq
- group: other
  title: ''
  type: X
  url: https://twitter.com/slitehq
- group: commercial
  title: ''
  type: Plans
  url: plans/slite-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/slite-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/slite-finops.yml
created: '2026-06-13'
description: Slite is a collaborative documentation and knowledge base platform with a REST API for managing notes, channels, documents, templates, and team knowledge bases. It enables asynchronous work through AI-powered search, document creation, and automated knowledge management workflows. The Slite Public API provides programmatic access to workspaces using Bearer token authentication and follows the OpenAPI v3.0 standard.
examples:
- key_count: 4
  name: Ask
  slug: ask
- key_count: 4
  name: Createnote
  slug: createNote
- key_count: 4
  name: Delete Index
  slug: delete-index
- key_count: 4
  name: Flagnoteasoutdated
  slug: flagNoteAsOutdated
- key_count: 4
  name: Getgroupbyid
  slug: getGroupById
- key_count: 4
  name: Getnotebyid
  slug: getNoteById
- key_count: 4
  name: Getnotechildren
  slug: getNoteChildren
- key_count: 4
  name: Getuserbyid
  slug: getUserById
- key_count: 4
  name: Index
  slug: index
- key_count: 4
  name: List Index
  slug: list-index
- key_count: 4
  name: Listnotes
  slug: listNotes
- key_count: 4
  name: Me
  slug: me
- key_count: 4
  name: Searchgroups
  slug: searchGroups
- key_count: 4
  name: Searchnotes
  slug: searchNotes
- key_count: 4
  name: Searchusers
  slug: searchUsers
- key_count: 4
  name: Updatenote
  slug: updateNote
- key_count: 4
  name: Updatenotearchivedstate
  slug: updateNoteArchivedState
- key_count: 4
  name: Updatenoteowner
  slug: updateNoteOwner
- key_count: 4
  name: Verifynote
  slug: verifyNote
finops:
- name: Slite Finops
  service_category: ''
  slug: slite-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/slite.png
json_schemas:
- name: AnswerAndSources
  property_count: 2
  slug: AnswerAndSources
- name: AskDisabledError
  property_count: 5
  slug: AskDisabledError
- name: AskQuotaExceededError
  property_count: 7
  slug: AskQuotaExceededError
- name: AskRateLimitedError
  property_count: 5
  slug: AskRateLimitedError
- name: DeletedNoteResult
  property_count: 0
  slug: DeletedNoteResult
- name: ExportedNote
  property_count: 2
  slug: ExportedNote
- name: FieldErrors
  property_count: 0
  slug: FieldErrors
- name: Group
  property_count: 3
  slug: Group
- name: Html
  property_count: 0
  slug: Html
- name: KnowledgeManagementFirst
  property_count: 0
  slug: KnowledgeManagementFirst
- name: ListHitsPerPage
  property_count: 0
  slug: ListHitsPerPage
- name: ListNotesOrderBy
  property_count: 0
  slug: ListNotesOrderBy
- name: ListPage
  property_count: 0
  slug: ListPage
- name: ListResult
  property_count: 3
  slug: ListResult
- name: Markdown
  property_count: 0
  slug: Markdown
- name: Me
  property_count: 4
  slug: Me
- name: Note
  property_count: 14
  slug: Note
- name: NoteContentFormat
  property_count: 0
  slug: NoteContentFormat
- name: NoteOwner
  property_count: 2
  slug: NoteOwner
- name: NoteWithContent
  property_count: 0
  slug: NoteWithContent
- name: ObjectType
  property_count: 0
  slug: ObjectType
- name: PaginatedGroups
  property_count: 4
  slug: PaginatedGroups
- name: PaginatedNotes
  property_count: 4
  slug: PaginatedNotes
- name: PaginatedUsers
  property_count: 4
  slug: PaginatedUsers
- name: PublicApiAuthError
  property_count: 2
  slug: PublicApiAuthError
- name: PublicApiDisabledError
  property_count: 2
  slug: PublicApiDisabledError
- name: PublicApiError
  property_count: 2
  slug: PublicApiError
- name: PublicApiFieldValidationError
  property_count: 3
  slug: PublicApiFieldValidationError
- name: PublicApiNotFoundError
  property_count: 2
  slug: PublicApiNotFoundError
- name: PublicApiRateLimitError
  property_count: 2
  slug: PublicApiRateLimitError
- name: PublicApiReviewState
  property_count: 0
  slug: PublicApiReviewState
- name: Record_string.unknown_
  property_count: 0
  slug: Record_string.unknown_
- name: SearchNoteHit
  property_count: 11
  slug: SearchNoteHit
- name: SearchNoteHitsPerPage
  property_count: 0
  slug: SearchNoteHitsPerPage
- name: SearchNotePage
  property_count: 0
  slug: SearchNotePage
- name: SearchNoteResult
  property_count: 3
  slug: SearchNoteResult
- name: SearchNoteType
  property_count: 0
  slug: SearchNoteType
- name: Source
  property_count: 5
  slug: Source
- name: User
  property_count: 6
  slug: User
jsonld:
- class_count: 0
  name: Api Context
  property_count: 0
  slug: api
- class_count: 30
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-06-13'
name: Slite
nav: Providers
network: true
overview: 'Slite publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Ask API, Groups API, Knowledge Management API, and 4 more. Tagged areas include Documentation, Knowledge Base, Collaboration, Notes, and Team.


  The Slite catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Slite''s developer surface includes authentication, documentation, engineering blog, changelog, status page, and 11 more developer resources.'
plans:
- name: Slite Plans Pricing
  plan_count: 3
  slug: slite-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 0
  name: Slite Rate Limits
  slug: slite-rate-limits
rules:
- name: Slite API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: slite-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.7
  delta: -4.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 50.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/slite/refs/heads/main/screenshots/slite-2026-06-20T194030.png
security:
- kind: authentication
  name: Slite Authentication
  slug: slite-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Slite Domain Security
  slug: slite-domain-security
  summary_line: TLSv1.3 · DMARC
slug: slite
tags:
- Documentation
- Knowledge Base
- Collaboration
- Notes
- Team
- Asynchronous Work
- AI
- Search
---
