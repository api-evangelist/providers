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
    agent_skills: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.2
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: REST API for AI-powered document search and Q&A across building documentation, plus management of buildings, documents, building owners, reports, and building categories. Supports SSE streaming on the
  name: Findable Partner API
  slug: findable-partner-api
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/security/findable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/findable-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.findable.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.findable.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.findable.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.findable.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.findable.ai/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.findable.ai/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/findable-no
- group: start
  title: ''
  type: Login
  url: https://app.findable.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.findable.ai/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.findable.ai/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.findable.ai/en/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/mcp/findable-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/findable-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/authentication/findable-authentication.yml
  title: ''
  type: Authentication
  url: authentication/findable-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/packages/findable-packages.yml
  title: ''
  type: Packages
  url: packages/findable-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/packages/findable-packages.yml
  title: ''
  type: SDKs
  url: packages/findable-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/components/findable-components.yml
  title: ''
  type: Components
  url: components/findable-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/sandbox/findable-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/findable-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/conventions/findable-conventions.yml
  title: ''
  type: Conventions
  url: conventions/findable-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/errors/findable-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/findable-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/lifecycle/findable-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/findable-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/changelog/findable-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/findable-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/conformance/findable-conformance.yml
  title: ''
  type: Conformance
  url: conformance/findable-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.findable.ai/en/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/security/findable-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/findable-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/data-model/findable-data-model.yml
  title: ''
  type: DataModel
  url: data-model/findable-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/llms/findable-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/findable-llms.txt
created: '2026-07-17'
description: Findable is an AI-powered building intelligence platform (findable.ai, formerly findable.no) that makes construction and property documentation searchable, structured, and audit-ready. It uses AI to classify building documents against standards such as BS 9991 and NS 3451, detect missing or expiring documents, support Golden Thread / Building Safety Act compliance, and answer natural-language questions across a building's documentation. Findable exposes a Partner API (api.findable.ai) for document search and AI Q&A, a hosted MCP server (mcp.findable.ai) with ~28 tools, and official TypeScript SDK and React component libraries. Used by 150+ property organizations across Norway and the UK.
image: https://www.findable.ai/images/logos/findable-logo-dark.png
layout: provider
mcp_servers:
- description: ''
  name: Findable MCP Server
  slug: findable-mcp-server
modified: '2026-07-19'
name: Findable
nav: Providers
network: true
overview: 'Findable publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Building Intelligence, PropTech, Facilities Management, and Building Documentation.


  Findable''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 20 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.7
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.0
    operational_transparency: 18.4
  previous_composite: 35.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/screenshots/findable-2026-07-25T214513.png
security:
- kind: authentication
  name: Findable Authentication
  slug: findable-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Findable Domain Security
  slug: findable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Findable Trust Center
  slug: findable-trust-center
  summary_line: ISO/IEC 27001:2022, SOC 2 Type I
slug: findable
tags:
- Company
- Building Intelligence
- PropTech
- Facilities Management
- Building Documentation
- Compliance
- Artificial Intelligence
- Document Search
- Construction
website: https://www.findable.ai
---
