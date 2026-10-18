---
access_model:
  confidence: low
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://api.urantia.dev
  baseurl_source: declared
  description: The Audio API from Urantia Papers — 1 operation(s) for audio.
  name: Urantia Papers Audio API
  slug: urantia-papers-audio-api
- baseURL: https://api.urantia.dev
  baseurl_source: declared
  description: The Bible API from Urantia Papers — 6 operation(s) for bible.
  name: Urantia Papers Bible API
  slug: urantia-papers-bible-api
- baseURL: https://api.urantia.dev
  baseurl_source: declared
  description: The Citation API from Urantia Papers — 1 operation(s) for citation.
  name: Urantia Papers Citation API
  slug: urantia-papers-citation-api
- baseURL: https://api.urantia.dev
  baseurl_source: declared
  description: The Embeddings API from Urantia Papers — 2 operation(s) for embeddings.
  name: Urantia Papers Embeddings API
  slug: urantia-papers-embeddings-api
- baseURL: https://api.urantia.dev
  baseurl_source: declared
  description: The Entities API from Urantia Papers — 3 operation(s) for entities.
  name: Urantia Papers Entities API
  slug: urantia-papers-entities-api
- baseURL: https://api.urantia.dev
  baseurl_source: declared
  description: The Feedback API from Urantia Papers — 1 operation(s) for feedback.
  name: Urantia Papers Feedback API
  slug: urantia-papers-feedback-api
- baseURL: https://api.urantia.dev
  baseurl_source: declared
  description: The Languages API from Urantia Papers — 1 operation(s) for languages.
  name: Urantia Papers Languages API
  slug: urantia-papers-languages-api
- baseURL: https://api.urantia.dev
  baseurl_source: declared
  description: The OG Images API from Urantia Papers — 1 operation(s) for og images.
  name: Urantia Papers OG Images API
  slug: urantia-papers-og-images-api
- baseURL: https://api.urantia.dev
  baseurl_source: declared
  description: The Papers API from Urantia Papers — 3 operation(s) for papers.
  name: Urantia Papers Papers API
  slug: urantia-papers-papers-api
- baseURL: https://api.urantia.dev
  baseurl_source: declared
  description: The Paragraphs API from Urantia Papers — 3 operation(s) for paragraphs.
  name: Urantia Papers Paragraphs API
  slug: urantia-papers-paragraphs-api
- baseURL: https://api.urantia.dev
  baseurl_source: declared
  description: The Search API from Urantia Papers — 2 operation(s) for search.
  name: Urantia Papers Search API
  slug: urantia-papers-search-api
- baseURL: https://api.urantia.dev
  baseurl_source: declared
  description: The Table of Contents API from Urantia Papers — 1 operation(s) for table of contents.
  name: Urantia Papers Table of Contents API
  slug: urantia-papers-table-of-contents-api
- baseURL: https://api.urantia.dev
  baseurl_source: declared
  description: The Tools API from Urantia Papers — 2 operation(s) for tools.
  name: Urantia Papers Tools API
  slug: urantia-papers-tools-api
artifact_total: 15
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/urantia-papers/refs/heads/main/mcp/urantia-papers-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/urantia-papers-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://api.urantia.dev/mcp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/urantia-papers/refs/heads/main/a2a/urantia-papers-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/urantia-papers-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/urantia-papers/refs/heads/main/security/urantia-papers-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/urantia-papers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://urantia.dev
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: operate
  title: ''
  type: Support
  url: https://docs.urantia.dev/help
- group: docs
  title: ''
  type: Documentation
  url: https://docs.urantia.dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.urantia.dev/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.urantia.dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.urantia.dev/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.urantia.dev/privacy-policy
- group: commercial
  title: ''
  type: License
  url: https://github.com/urantia-hub/urantia-dev-api/blob/main/LICENSE
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/urantia-hub
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/urantia-hub/urantia-dev-api
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.urantia.dev/llms.txt
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/urantia-hub/urantia-papers-claude-code-plugin/tree/main/skills
- group: other
  title: ''
  type: APICatalog
  url: https://api.urantia.dev/.well-known/api-catalog
- group: agent
  title: ''
  type: MCPServerCard
  url: https://api.urantia.dev/.well-known/mcp/server-card.json
- group: other
  title: ''
  type: ContentSignal
  url: https://api.urantia.dev/robots.txt
created: '2026-05-28'
description: 'A read-only REST API and MCP server for the Urantia Papers: papers, sections, and paragraphs by reference, keyword and semantic search, named entities, and cross-references to public domain texts of the world''s religions. The MCP server covers the Papers and the Bible for now. The content endpoints are read-only and need no key.'
layout: provider
mcp_servers:
- description: Remote MCP server at api.urantia.dev over streamable HTTP; 19 tools listed.
  name: Urantia Papers API
  slug: urantia-papers-api
modified: '2026-10-05'
name: Urantia Papers
nav: Providers
network: true
overview: 'Urantia Papers publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio API, Bible API, Citation API, and 10 more. Tagged areas include Books, Public APIs, and A2A.


  Urantia Papers'' developer surface includes support, documentation, changelog, and 17 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 26.1
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 47.8
    developer_ergonomics: 20.7
    discoverability: 80.0
    operational_transparency: 36.8
  previous_composite: 6.1
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/urantia-papers/refs/heads/main/screenshots/urantia-papers-2026-06-20T200543.png
security:
- kind: domain-security
  name: Urantia Papers Domain Security
  slug: urantia-papers-domain-security
  summary_line: TLSv1.3 · HSTS
slug: urantia-papers
tags:
- Books
- Public APIs
- A2A
website: https://urantia.dev
---
