---
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 65.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 82
  human_in_the_loop: 0
  name: Vaquill Ai Agentic Access
  operation_count: 185
  slug: vaquill-ai-agentic-access
  summary_line: 185 operations · 82 acting
api_count: 6
apis:
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: Law-change alerts. Subscribe to a **board** (a tracked corpus source, identified by `corpusType` plus an optional `state`) and get a webhook or email whenever it refreshes with real changes, naming th
  name: Vaquill AI Board Watches API
  slug: vaquill-ai-board-watches-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: The dated events across a matter's documents, as one timeline, with duplicate and date-conflict flags.
  name: Vaquill AI Chronology API
  slug: vaquill-ai-chronology-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: The people and companies matters are filed under. Synchronous CRUD.
  name: Vaquill AI Clients API
  slug: vaquill-ai-clients-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: Diffing two documents in a matter into structural changes, with a substantive-versus-cosmetic judgment and a downloadable redline.
  name: Vaquill AI Comparisons API
  slug: vaquill-ai-comparisons-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: 'Checking one document against one regulation''s requirement checklist: a verdict per requirement with the article it comes from, the gaps, and what to do about them. Only regulations with a real checkl'
  name: Vaquill AI Compliance API
  slug: vaquill-ai-compliance-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: 'Your own credit balance: what is spendable right now, where it came from, and what is about to expire. Free and never charged, so it is safe to poll for low-balance alerting or to pre-flight a batch j'
  name: Vaquill AI Credits API
  slug: vaquill-ai-credits-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: 'Files in a matter: their metadata, their ingested text, and the original bytes. A document is only usable by retrieval, drafting and review once its status is `succeeded`.'
  name: Vaquill AI Documents API
  slug: vaquill-ai-documents-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: Generating, revising and exporting draft documents. Bodies come out as sections and go in as markdown; the editor's own format is never on the wire. Rendered files come from the export route.
  name: Vaquill AI Drafting API
  slug: vaquill-ai-drafting-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: 'The cross-document fact ledger for a matter: what every document in it asserts, coalesced and cited back to its source passages.'
  name: Vaquill AI Facts API
  slug: vaquill-ai-facts-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: Organization inside and across matters. The same folders the web app shows, so one created here appears in the customer's browser.
  name: Vaquill AI Folders API
  slug: vaquill-ai-folders-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: The India Credits API from Vaquill AI — 1 operation(s) for india credits.
  name: Vaquill AI India Credits API
  slug: vaquill-ai-india-credits-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: The India Pricing API from Vaquill AI — 1 operation(s) for india pricing.
  name: Vaquill AI India Pricing API
  slug: vaquill-ai-india-pricing-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: The Indian Acts and Legislation API from Vaquill AI — 17 operation(s) for indian acts and legislation.
  name: Vaquill AI Indian Acts and Legislation API
  slug: vaquill-ai-indian-acts-and-legislation-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: 'Spreadsheet-style extraction across many documents: rows are documents, columns are questions, cells are answers with verified citations. Building a grid is free; running it is what costs.'
  name: Vaquill AI Matrices API
  slug: vaquill-ai-matrices-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: A citation-backed summary of everything filed to a matter, generated on demand and readable claim by claim.
  name: Vaquill AI Matter summary API
  slug: vaquill-ai-matter-summary-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: The unit of work everything else hangs off. A matter scopes documents, drafts, reviews, comparisons and matrices, and it is what a credential's access is checked against.
  name: Vaquill AI Matters API
  slug: vaquill-ai-matters-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: Screening one inbound NDA against ten standard criteria and, where you name one, your own NDA playbook. Answers `green`, `yellow` or `red` with the reasoning per criterion, plus a report you can forwa
  name: Vaquill AI NDA triage API
  slug: vaquill-ai-nda-triage-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: 'The one job envelope. Every long-running call answers `202` with an operation, and polling this resource is the only way to learn it finished: there are no webhooks. Five statuses, no synonyms.'
  name: Vaquill AI Operations API
  slug: vaquill-ai-operations-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: The organization's negotiating positions, per contract type, and the starter templates to build them from. A playbook is the input a contract review is measured against.
  name: Vaquill AI Playbooks API
  slug: vaquill-ai-playbooks-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: Credit pricing and conversion rates. No authentication required. 1 credit = $0.01 USD.
  name: Vaquill AI Pricing API
  slug: vaquill-ai-pricing-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: 'Asking legal questions and getting grounded, cited answers. This API does NOT stream: an ask answers `202` and you poll the operation, then read the answer off the message it points at. Conversation s'
  name: Vaquill AI Research API
  slug: vaquill-ai-research-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: 'Reviewing one contract against a playbook: clause analysis, redlines, flags, liability exposure and a reported sign-off gate. Export applies the redlines as native Word tracked changes.'
  name: Vaquill AI Reviews API
  slug: vaquill-ai-reviews-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: Getting files in. One presigned multipart flow at every size, with the bytes going straight to storage and never through this API. Initiate, PUT each part, then complete.
  name: Vaquill AI Uploads API
  slug: vaquill-ai-uploads-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: 'State session laws: the acts of each legislature as they were enacted, chapter by chapter, before they are folded into a code. A session law is what the governor signs. It carries the act''s own text, '
  name: Vaquill AI US Session Laws API
  slug: vaquill-ai-us-session-laws-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: Search and retrieve US primary law. Covers the United States Code and the Statutes at Large, the Code of Federal Regulations and its annual editions, state statutory codes and administrative regulatio
  name: Vaquill AI US Statutes API
  slug: vaquill-ai-us-statutes-api
- baseURL: https://api.vaquill.ai/api/v1
  baseurl_source: declared
  description: Multi-step analyses from a fixed catalogue. Read a definition to learn what documents and inputs it takes, launch a run inside a matter, then download the artifacts it produces.
  name: Vaquill AI Workflows API
  slug: vaquill-ai-workflows-api
artifact_total: 57
asyncapis:
- description: ''
  name: Vaquill Ai Webhooks
  slug: vaquill-ai-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/asyncapi/vaquill-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/vaquill-ai-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/agentic-access/vaquill-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vaquill-ai-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/rate-limits/vaquill-ai-workspace-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vaquill-ai-workspace-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/rate-limits/vaquill-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vaquill-ai-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/plans/vaquill-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vaquill-ai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/rules/vaquill-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/vaquill-ai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/json-ld/vaquill-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vaquill-ai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/vocabulary/vaquill-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vaquill-ai-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/data-model/vaquill-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vaquill-ai-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/changelog/vaquill-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/vaquill-ai-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/conventions/vaquill-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/vaquill-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/conventions/vaquill-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vaquill-ai-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/sandbox/vaquill-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/vaquill-ai-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/authentication/vaquill-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vaquill-ai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/scopes/vaquill-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/vaquill-ai-scopes.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/lifecycle/vaquill-ai-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/vaquill-ai-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/lifecycle/vaquill-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vaquill-ai-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/errors/vaquill-ai-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/vaquill-ai-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/errors/vaquill-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vaquill-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/conformance/vaquill-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vaquill-ai-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/overlays/vaquill-ai-india-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vaquill-ai-india-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/llms/vaquill-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vaquill-ai-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/llms/vaquill-ai-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vaquill-ai-docs-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/mcp/vaquill-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/vaquill-ai-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/mcp/vaquill-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/vaquill-ai-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/well-known/vaquill-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vaquill-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/hosts/vaquill-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vaquill-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/vendors/vaquill-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vaquill-ai-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/packages/vaquill-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/vaquill-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/packages/vaquill-ai-packages.yml
  title: ''
  type: Packages
  url: packages/vaquill-ai-packages.yml
- group: company
  title: ''
  type: Website
  url: https://www.vaquill.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.vaquill.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.vaquill.ai/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://www.vaquill.ai/docs/api-reference/us-statutes/search-us-statutes-constitutions-court-rules-and-executive-actions
- group: start
  title: ''
  type: GettingStarted
  url: https://www.vaquill.ai/docs/api-guide/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.vaquill.ai/docs/api-guide/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vaquill.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.vaquill.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vaquill-AI
- group: operate
  title: ''
  type: Support
  url: https://www.vaquill.ai/support
- group: start
  title: ''
  type: SignUp
  url: https://app.vaquill.ai/auth/signup
- group: start
  title: ''
  type: Login
  url: https://app.vaquill.ai/auth/login
- group: start
  title: ''
  type: Sandbox
  url: https://www.vaquill.ai/playground
- group: auth
  title: ''
  type: Security
  url: https://www.vaquill.ai/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vaquill.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vaquill.ai/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/security/vaquill-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/vaquill-ai-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/security/vaquill-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vaquill-ai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/security/vaquill-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vaquill-ai-domain-security.yml
created: '2026-10-07'
description: 'Vaquill AI is US primary law data infrastructure: a credit-metered Legal Data API over the US Code, the CFR, every state and territory statutory code, regulations, constitutions, court rules, session laws, agency guidance and executive orders (5M+ sections, 54 jurisdictions), a sibling India API over central and state legislation, a Legal Workspace API for driving matters, documents, drafting, review and compliance checks from your own backend, and a hosted MCP server (OAuth or API key) with a local uvx package and a Claude Code plugin. Three OpenAPI 3.1 documents are published on api.vaquill.ai, and the Open US Law corpus is released on GitHub under CC BY-NC 4.0.'
image: https://www.vaquill.ai/opengraph-image?e9fbcdc281d37e49
json_schemas:
- name: ActCitedByResponse
  property_count: 15
  slug: vaquill-ai-act-cited-by-response
- name: ActSearchRequest
  property_count: 17
  slug: vaquill-ai-act-search-request
- name: ActStatusResponse
  property_count: 26
  slug: vaquill-ai-act-status-response
- name: ActSubordinateResponse
  property_count: 15
  slug: vaquill-ai-act-subordinate-response
- name: ActTextResponse
  property_count: 13
  slug: vaquill-ai-act-text-response
- name: AskRequest
  property_count: 15
  slug: vaquill-ai-ask-request
- name: ComplianceCheck
  property_count: 21
  slug: vaquill-ai-compliance-check
- name: CreateWatchRequest
  property_count: 8
  slug: vaquill-ai-create-watch-request
- name: ExternalCreditBalanceResponse
  property_count: 9
  slug: vaquill-ai-external-credit-balance-response
- name: Matter
  property_count: 20
  slug: vaquill-ai-matter
- name: NdaTriage
  property_count: 22
  slug: vaquill-ai-nda-triage
- name: ReviewCreateRequest
  property_count: 14
  slug: vaquill-ai-review-create-request
- name: Review
  property_count: 23
  slug: vaquill-ai-review
- name: SessionLawBodyResponse
  property_count: 25
  slug: vaquill-ai-session-law-body-response
- name: SessionLawResponse
  property_count: 46
  slug: vaquill-ai-session-law-response
- name: StatuteBodyResponse
  property_count: 20
  slug: vaquill-ai-statute-body-response
- name: StatuteCountRequest
  property_count: 9
  slug: vaquill-ai-statute-count-request
- name: StatuteSearchRequest
  property_count: 24
  slug: vaquill-ai-statute-search-request
jsonld:
- class_count: 120
  name: Vaquill Ai Context
  property_count: 429
  slug: vaquill-ai-context
layout: provider
mcp_servers:
- description: 'Hosted and local MCP server over the Vaquill Developer API (US primary law: statutes, regulations, constitutions, court rules, session laws, agency guidance, plus law-change watches) with a separate m'
  name: Vaquill MCP Server
  slug: vaquill-mcp-server
modified: '2026-10-07'
name: Vaquill AI
nav: Providers
network: true
overview: 'Vaquill AI publishes 26 API contracts indexed on the [APIs.io](https://apis.io/) network, including Board Watches API, Chronology API, Clients API, and 23 more. Tagged areas include Legal, Statutes, Regulations, Legal Research, and Law.


  The Vaquill AI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Vaquill AI''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, pricing, and 43 more developer resources.'
plans:
- name: Vaquill Ai Plans Pricing
  plan_count: 1
  slug: vaquill-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Vaquill Ai Rate Limits
  slug: vaquill-ai-rate-limits
- limit_count: 19
  name: Vaquill Ai Workspace Rate Limits
  slug: vaquill-ai-workspace-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Vaquill AI API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 3
  slug: vaquill-ai-rules
scopes:
- name: Vaquill Ai Scopes
  scope_count: 38
  slug: vaquill-ai-scopes
  summary_line: 38 scopes
score:
  band: exemplar
  composite: 71.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 81.8
    catalog_earned_first_party: 16.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 73.7
    contract_governance: 22.0
    contract_quality: 74.3
    developer_ergonomics: 73.2
    discoverability: 80.0
    operational_transparency: 68.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 70.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 3.8
      total: 26
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 45.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/vaquill-ai/refs/heads/main/screenshots/vaquill-ai-2026-10-11T132844.png
security:
- kind: authentication
  name: Vaquill Ai Authentication
  slug: vaquill-ai-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Vaquill Ai Domain Security
  slug: vaquill-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Vaquill Ai Vulnerability Disclosure
  slug: vaquill-ai-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Vaquill Ai Trust Center
  slug: vaquill-ai-trust-center
  summary_line: trust center published
slug: vaquill-ai
tags:
- Legal
- Statutes
- Regulations
- Legal Research
- Law
- Compliance
- Legal Tech
- Government Data
- MCP
- India
- Contracts
website: https://www.vaquill.ai
---
