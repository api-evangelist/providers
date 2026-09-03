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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Padlet Agentic Access
  operation_count: 10
  slug: padlet-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.padlet.dev/v1
  baseurl_source: declared
  description: The AI Recipe Boards API from Padlet — 2 operation(s) for ai recipe boards.
  name: Padlet AI Recipe Boards API
  slug: padlet-ai-recipe-boards-api
- baseURL: https://api.padlet.dev/v1
  baseurl_source: declared
  description: The Boards API from Padlet — 1 operation(s) for boards.
  name: Padlet Boards API
  slug: padlet-boards-api
- baseURL: https://api.padlet.dev/v1
  baseurl_source: declared
  description: The Comments API from Padlet — 1 operation(s) for comments.
  name: Padlet Comments API
  slug: padlet-comments-api
- baseURL: https://api.padlet.dev/v1
  baseurl_source: declared
  description: The Organizations API from Padlet — 2 operation(s) for organizations.
  name: Padlet Organizations API
  slug: padlet-organizations-api
- baseURL: https://api.padlet.dev/v1
  baseurl_source: declared
  description: The Posts API from Padlet — 2 operation(s) for posts.
  name: Padlet Posts API
  slug: padlet-posts-api
- baseURL: https://api.padlet.dev/v1
  baseurl_source: declared
  description: The Reactions API from Padlet — 1 operation(s) for reactions.
  name: Padlet Reactions API
  slug: padlet-reactions-api
- baseURL: https://api.padlet.dev/v1
  baseurl_source: declared
  description: The Users API from Padlet — 1 operation(s) for users.
  name: Padlet Users API
  slug: padlet-users-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Padlet AI Recipe Boards API
  slug: open-padlet-ai-recipe-boards-api
- collection_type: open
  name: Padlet AI Recipe Boards API
  slug: open-padlet-boards-api
- collection_type: open
  name: Padlet AI Recipe Boards Comments API
  slug: open-padlet-comments-api
- collection_type: open
  name: Padlet AI Recipe Boards Organizations API
  slug: open-padlet-organizations-api
- collection_type: open
  name: Padlet AI Recipe Boards Posts API
  slug: open-padlet-posts-api
- collection_type: open
  name: Padlet AI Recipe Boards Reactions API
  slug: open-padlet-reactions-api
- collection_type: open
  name: Padlet AI Recipe Boards Users API
  slug: open-padlet-users-api
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/padlet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/padlet-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/padlet-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/padlet-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://padlet.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.padlet.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.padlet.dev/reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.padlet.dev/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.padlet.dev/reference/authentication
- group: operate
  title: ''
  type: Support
  url: https://padlet.help/
- group: commercial
  title: ''
  type: Pricing
  url: https://padlet.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://padlet.com/auth/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://padlet.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.padlet.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.padlet.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/padlet-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/padlet-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/padlet-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/padlet-security.txt
- group: auth
  title: ''
  type: Security
  url: https://padlet.com/.well-known/security.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/padlet-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/padlet-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/padlet-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/padlet-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/padlet-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/padlet-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/padlet-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Padlet is a collaborative visual platform of boards and canvases ("padlets") used across education and creative work to collect, organize, and share posts, images, links, and files. Its public REST API (api.padlet.dev, JSON:API) lets paying users read boards with their sections, posts, comments, and reactions, create posts, comments, and reactions, generate AI recipe boards, and read user and organization data — authenticated with an x-api-key header. Padlet also runs an official OAuth-protected MCP server at mcp.padlet.com for agent access.
image: https://elvis.padletcdn.com/1/atat/e_1/appBY8jxCUCf4JUUZ/tblANzywOAIDDHQsQ/recwXBCnX3ozCHYBU/fldKQAixAlmwWEnhk/0
layout: provider
mcp_servers:
- description: ''
  name: Padlet MCP Server
  slug: padlet-mcp-server
modified: '2026-07-20'
name: Padlet
nav: Providers
network: true
overview: 'Padlet publishes 7 APIs on the [APIs.io](https://apis.io/) network, including AI Recipe Boards API, Boards API, Comments API, and 4 more. Tagged areas include Collaboration, Education, Visual Collaboration, Content, and Boards.


  Padlet''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 21 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 1
  name: Padlet Rate Limits
  slug: padlet-rate-limits
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 55.4
    developer_ergonomics: 45.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 49.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/padlet/refs/heads/main/screenshots/padlet-2026-08-07T191252.png
security:
- kind: authentication
  name: Padlet Authentication
  slug: padlet-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Padlet Domain Security
  slug: padlet-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Padlet Vulnerability Disclosure
  slug: padlet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: padlet
tags:
- Collaboration
- Education
- Visual Collaboration
- Content
- Boards
- Productivity
- JSON:API
- MCP
- EdTech
website: https://padlet.com/
---
