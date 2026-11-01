---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Docsmint Com Agentic Access
  operation_count: 82
  slug: docsmint-com-agentic-access
  summary_line: 82 operations · 44 acting
api_count: 1
apis:
- description: Self-hosted AI-native knowledge workspace API.
  name: DocsMint API
  slug: docsmint-api
- description: Operator maintenance endpoints (reindex, embedding stats, provider health) — API key protected
  name: docsmint-com Admin API
  slug: docsmint-com-admin-api
- description: The Attachments API from docsmint-com — 3 operation(s) for attachments.
  name: docsmint-com Attachments API
  slug: docsmint-com-attachments-api
- description: Authentication endpoints
  name: docsmint-com Auth API
  slug: docsmint-com-auth-api
- description: Category management for folders and documents
  name: docsmint-com Categories API
  slug: docsmint-com-categories-api
- description: The Csrf Token API from docsmint-com — 1 operation(s) for csrf token.
  name: docsmint-com Csrf Token API
  slug: docsmint-com-csrf-token-api
- description: Document CRUD and search
  name: docsmint-com Documents API
  slug: docsmint-com-documents-api
- description: Folder management
  name: docsmint-com Folders API
  slug: docsmint-com-folders-api
- description: GraphRAG entity and relationship queries (AGE)
  name: docsmint-com Graph API
  slug: docsmint-com-graph-api
- description: The Health API from docsmint-com — 1 operation(s) for health.
  name: docsmint-com Health API
  slug: docsmint-com-health-api
- description: The Keys API from docsmint-com — 4 operation(s) for keys.
  name: docsmint-com Keys API
  slug: docsmint-com-keys-api
- description: The Plugins API from docsmint-com — 2 operation(s) for plugins.
  name: docsmint-com Plugins API
  slug: docsmint-com-plugins-api
- description: Hybrid full-text + semantic search
  name: docsmint-com Search API
  slug: docsmint-com-search-api
- description: Sharing and guest access
  name: docsmint-com Share API
  slug: docsmint-com-share-api
- description: Tag management
  name: docsmint-com Tags API
  slug: docsmint-com-tags-api
- description: The Trash API from docsmint-com — 3 operation(s) for trash.
  name: docsmint-com Trash API
  slug: docsmint-com-trash-api
- description: The Webhooks API from docsmint-com — 1 operation(s) for webhooks.
  name: docsmint-com Webhooks API
  slug: docsmint-com-webhooks-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/docsmint-com/agentic-access/docsmint-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/docsmint-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/docsmint-com/plans/docsmint-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docsmint-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/docsmint-com/rules/docsmint-com-rules.yml
  title: ''
  type: Spectral
  url: rules/docsmint-com-rules.yml
- group: design
  href: https://artifacts.apis.io/docsmint-com/json-ld/docsmint-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/docsmint-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/docsmint-com/vocabulary/docsmint-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/docsmint-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/docsmint-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/docsmint-com/data-model/docsmint-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/docsmint-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/docsmint-com/changelog/docsmint-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/docsmint-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/docsmint-com/authentication/docsmint-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/docsmint-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/docsmint-com/errors/docsmint-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/docsmint-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/docsmint-com/conformance/docsmint-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docsmint-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docsmint-com/llms/docsmint-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docsmint-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/docsmint-com/mcp/docsmint-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/docsmint-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/docsmint-com/well-known/docsmint-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/docsmint-com-security.txt
- group: agent
  href: https://artifacts.apis.io/docsmint-com/well-known/docsmint-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docsmint-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/docsmint-com/hosts/docsmint-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docsmint-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/docsmint-com/vendors/docsmint-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docsmint-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/docsmint-com/packages/docsmint-com-packages.yml
  title: ''
  type: SDKs
  url: packages/docsmint-com-packages.yml
- group: build
  href: https://artifacts.apis.io/docsmint-com/packages/docsmint-com-packages.yml
  title: ''
  type: Packages
  url: packages/docsmint-com-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://docsmint.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://docsmint.com/releases
- group: auth
  href: https://artifacts.apis.io/docsmint-com/security/docsmint-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/docsmint-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/docsmint-com/security/docsmint-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docsmint-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docsmint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docsmint.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docsmint.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docsmint.com/#features
- group: operate
  title: ''
  type: Support
  url: https://docsmint.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://docsmint.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://docsmint.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docsmint.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docsmint.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HiAi-gg
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://docsmint.com/mcp
  - status: 200
    url: https://docsmint.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: DocsMint provides a SaaS platform that lets teams create, edit, and organize documents while leveraging AI-powered search and assistance. Users can store knowledge, collaborate in real time, and integrate the workspace with AI tools for content generation, summarization, and retrieval, all within a secure, cloud‑based environment.
image: https://docsmint.com/apple-touch-icon.png
jsonld:
- class_count: 11
  name: Docsmint Com Context
  property_count: 39
  slug: docsmint-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at docsmint.com.
  name: docsmint-com MCP Server
  slug: docsmint-com-mcp-yml
modified: '2026-10-30'
name: docsmint-com
nav: Providers
network: true
overview: 'docsmint-com publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Attachments API, Auth API, and 14 more. Tagged areas include AI, Document-Management, Knowledge-Base, SaaS, and Collaboration.


  The docsmint-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  docsmint-com''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, pricing, and 26 more developer resources.'
plans:
- name: Docsmint Com Plans Pricing
  plan_count: 3
  slug: docsmint-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Docsmint Com Rate Limits
  slug: docsmint-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: docsmint-com API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 2
  slug: docsmint-com-rules
scopes:
- name: Docsmint Com Scopes
  scope_count: 0
  slug: docsmint-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.5
    catalog_earned_first_party: 0.0
    catalog_gap: 40.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 47.0
    developer_ergonomics: 58.8
    discoverability: 56.7
    operational_transparency: 31.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Docsmint Com Authentication
  slug: docsmint-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Docsmint Com Domain Security
  slug: docsmint-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Docsmint Com Vulnerability Disclosure
  slug: docsmint-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: docsmint-com
tags:
- AI
- Document-Management
- Knowledge-Base
- SaaS
- Collaboration
website: https://docsmint.com/
---
