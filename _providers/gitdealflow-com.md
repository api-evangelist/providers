---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Gitdealflow Com Agentic Access
  operation_count: 37
  slug: gitdealflow-com-agentic-access
  summary_line: 37 operations · 1 acting
api_count: 1
apis:
- description: Hosted Model Context Protocol server (protocol 2025-06-18, Streamable HTTP) exposing 12 read-only tools, 3 resources and 7 prompts over the same signal panel; also shipped as the npm stdio package @gi
  name: VC Deal Flow Signal MCP Server
  slug: vc-deal-flow-signal-mcp-server
- description: Agent-to-Agent (A2A 0.3.0) JSON-RPC 2.0 endpoint implementing message/send, tasks/get and tasks/cancel over the signal panel, executing synchronously; discovered via the agent card served at /.well-kn
  name: GitDealFlow A2A Agent
  slug: gitdealflow-a2a-agent
- description: 'Microsoft NLWeb-compatible conversational endpoint: POST a natural-language query and receive schema.org-typed JSON-LD (ItemList, Organization, Article, Dataset or WebPage). GET returns the request-sc'
  name: GitDealFlow NLWeb Endpoint
  slug: gitdealflow-nlweb-endpoint
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: Agent / MCP discovery surfaces
  name: GitDealFlow Agents API
  phrasing_intents:
  - id: getAgentsCatalog
    intent: Get the MCP and A2A skill catalog
    question: Which skills does the GitDealFlow agent expose over MCP or A2A?
  - id: getAgentTools
    intent: Get tool definitions for LLM tool use
    question: Can I drop ready-made JSON Schema tool definitions straight into my LLM agent?
  - id: getAgentsV1
    intent: Get the versioned v1 agent skill catalog
    question: Is there a version-pinned v1 URL for the agent skill catalog?
  - id: getOpenapiV1
    intent: Get the versioned v1 OpenAPI descriptor
    question: Where is the versioned v1 OpenAPI document for this API?
  phrasing_ops: 4
  slug: gitdealflow-com-agents-api
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: Citation-ready Q&A retrieval
  name: GitDealFlow Answer API
  phrasing_intents:
  - id: getAnswer
    intent: Get the single best answer to a question
    question: How can I get one citation-ready answer to a question about startup signals?
  - id: askQuestion
    intent: Get ranked candidate answers to a question
    question: Can I see several ranked candidate answers instead of just one?
  - id: getDiligenceDossier
    intent: Get a public-source diligence dossier on a company
    question: Who acquired this company and which funds publicly backed it?
  - id: getAnswersCorpus
    intent: Download the full Q&A corpus
    question: Can I download every agent query and FAQ for offline embedding?
  - id: getAnswersV1
    intent: Download the Q&A corpus from the v1 path
    question: Is there a versioned v1 URL for the full answers corpus?
  - id: getFaqV1
    intent: Get the curated standalone FAQ corpus
    question: Which curated FAQ entries have stable slugs that are safe to cite?
  phrasing_ops: 6
  slug: gitdealflow-com-answer-api
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: SVG badges for embeds
  name: GitDealFlow Badges API
  phrasing_intents:
  - id: getScoutBadge
    intent: Get a Scout Score badge for a GitHub user
    question: Can I show a GitHub user's Scout Score as an SVG badge?
  - id: getBuiltWithBadge
    intent: Get the Built with VC Deal Flow Signal badge
    question: Is there a 'Built with VC Deal Flow Signal' badge I can put on my project?
  - id: getMomentumBadge
    intent: Get a momentum badge for a repository
    question: Can I display a repo's engineering momentum as a badge?
  phrasing_ops: 3
  slug: gitdealflow-com-badges-api
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: The brand API from GitDealFlow — 1 operation(s) for brand.
  name: GitDealFlow Brand API
  phrasing_intents:
  - id: getSocialMascotV1
    intent: Get the social mascot brand bible
    question: What voice and tone rules does the Data Nerd mascot follow?
  phrasing_ops: 1
  slug: gitdealflow-com-brand-api
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: The business-model API from GitDealFlow — 1 operation(s) for business-model.
  name: GitDealFlow Business Model API
  phrasing_intents:
  - id: getAffiliatesV1
    intent: Get affiliate program terms and swipe kit
    question: What commission does the affiliate program pay?
  phrasing_ops: 1
  slug: gitdealflow-com-business-model-api
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: Reference-manager exports
  name: GitDealFlow Citation API
  phrasing_intents:
  - id: getCitation
    intent: Export a citation for a finding or paper
    question: How do I cite the SSRN paper in my reference manager?
  phrasing_ops: 1
  slug: gitdealflow-com-citation-api
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: The community API from GitDealFlow — 1 operation(s) for community.
  name: GitDealFlow Community API
  phrasing_intents:
  - id: getMembersV1
    intent: Get the Charter Cohort roster and leaderboard
    question: Who's on the Charter Cohort 2026 roster and how are they ranked?
  phrasing_ops: 1
  slug: gitdealflow-com-community-api
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: Paid per-request enriched signals
  name: GitDealFlow Deep Signal API
  phrasing_intents:
  - id: getDeepSignal
    intent: Get a paid deep enriched signal for a startup
    question: Can I get a composite score, sector percentile and thesis for a startup using credits?
  - id: getDeepSignalX402
    intent: Get a deep signal paid per call via x402
    question: Can my agent pay per call in USDC on Base without an API key?
  - id: getDeepSignalSolanaTerms
    intent: Get Solana payment instructions for credits
    question: What wallet, mint and amount do I need to buy deep-signal credits with Solana?
  - id: redeemDeepSignalSolana
    intent: Redeem a Solana USDC payment for credits
    question: I've sent USDC on Solana, how do I turn it into deep-signal credits?
  - id: getCredits
    intent: Check the credit balance for an API key
    question: How many deep-signal credits are left on my API key?
  phrasing_ops: 5
  slug: gitdealflow-com-deep-signal-api
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: Controlled-vocabulary term definitions
  name: GitDealFlow Glossary API
  phrasing_intents:
  - id: getGlossaryV1
    intent: Get the controlled-vocabulary glossary
    question: What do the terms used in signals, sectors and methodology mean?
  phrasing_ops: 1
  slug: gitdealflow-com-glossary-api
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: Open prediction markets
  name: GitDealFlow Markets API
  phrasing_intents:
  - id: getMarket
    intent: Get an open prediction market and its candidates
    question: What's the question and resolver for this prediction market?
  phrasing_ops: 1
  slug: gitdealflow-com-markets-api
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: Pricing, changelog, dataset
  name: GitDealFlow Meta API
  phrasing_intents:
  - id: getChangelog
    intent: Get the machine-readable changelog
    question: What changed recently in GitDealFlow?
  - id: getPricing
    intent: Get the pricing table
    question: What pricing tiers are offered and how much do they cost?
  - id: getChangelogV1
    intent: Get the changelog from the v1 path
    question: Can I pin to a versioned v1 URL for the changelog?
  phrasing_ops: 3
  slug: gitdealflow-com-meta-api
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: Reproducible signal-computation methodology
  name: GitDealFlow Methodology API
  phrasing_intents:
  - id: getMethodologyV1
    intent: Get the signal-computation methodology
    question: How are startup engineering signals computed step by step?
  phrasing_ops: 1
  slug: gitdealflow-com-methodology-api
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: Scout score receipts and prediction
  name: GitDealFlow Scout API
  phrasing_intents:
  - id: getScoutReceipts
    intent: Get a GitHub user's Scout Score
    question: How many future unicorns did a GitHub user star before they took off?
  - id: getScoutPrediction
    intent: Predict which startups a user will bet on next
    question: Which tracked startups is a GitHub user likely to star next?
  phrasing_ops: 2
  slug: gitdealflow-com-scout-api
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: On-site search across all content
  name: GitDealFlow Search API
  phrasing_intents:
  - id: llmsSearch
    intent: Search all site content
    question: Can I search startups, sectors, blog posts and FAQs in one query?
  phrasing_ops: 1
  slug: gitdealflow-com-search-api
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: Startup engineering acceleration data
  name: GitDealFlow Signals API
  phrasing_intents:
  - id: getSignals
    intent: Get the current startup signals snapshot
    question: Which startups are trending this period by commit velocity?
  - id: getSignalsCSV
    intent: Download the signals snapshot as CSV
    question: Can I get the startup signals snapshot as a spreadsheet-friendly CSV?
  - id: getSingleSignal
    intent: Get the signal for one startup
    question: What's the engineering signal for a specific startup?
  - id: getDatasetJsonl
    intent: Download the per-startup NDJSON dataset
    question: Can I stream the full per-startup dataset into pandas or DuckDB?
  - id: getSignalsV1
    intent: Get the signals snapshot from the v1 path
    question: Is there a versioned v1 URL for the signals JSON snapshot?
  - id: getDatasetJsonlV1
    intent: Download the NDJSON dataset from the v1 path
    question: Can I pin to a versioned v1 URL for the NDJSON dataset?
  phrasing_ops: 6
  slug: gitdealflow-com-signals-api
artifact_total: 31
common:
- group: other
  href: https://artifacts.apis.io/gitdealflow-com/overlays/gitdealflow-com-signals-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gitdealflow-com-signals-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/gitdealflow-com/security/gitdealflow-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gitdealflow-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gitdealflow-com/security/gitdealflow-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gitdealflow-com-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/gitdealflow-com/agentic-access/gitdealflow-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gitdealflow-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gitdealflow-com/authentication/gitdealflow-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gitdealflow-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://gitdealflow.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://signals.gitdealflow.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://signals.gitdealflow.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://signals.gitdealflow.com/api/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://signals.gitdealflow.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://signals.gitdealflow.com/support
- group: company
  title: ''
  type: Blog
  url: https://signals.gitdealflow.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://signals.gitdealflow.com/feed.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kindrat86
- group: commercial
  title: ''
  type: Pricing
  url: https://signals.gitdealflow.com/pricing
- group: start
  title: ''
  type: Login
  url: https://signals.gitdealflow.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gitdealflow.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gitdealflow.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://signals.gitdealflow.com/agents/postman-collection.json
- group: operate
  title: ''
  type: StatusPage
  url: https://signals.gitdealflow.com/uptime
- group: operate
  href: https://artifacts.apis.io/gitdealflow-com/changelog/gitdealflow-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gitdealflow-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/gitdealflow-com/lifecycle/gitdealflow-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gitdealflow-com-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/gitdealflow-com/packages/gitdealflow-com-packages.yml
  title: ''
  type: Packages
  url: packages/gitdealflow-com-packages.yml
- group: build
  href: https://artifacts.apis.io/gitdealflow-com/packages/gitdealflow-com-packages.yml
  title: ''
  type: SDKs
  url: packages/gitdealflow-com-packages.yml
- group: agent
  href: https://artifacts.apis.io/gitdealflow-com/well-known/gitdealflow-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gitdealflow-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/gitdealflow-com/well-known/gitdealflow-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gitdealflow-com-security.txt
- group: other
  href: https://artifacts.apis.io/gitdealflow-com/a2a/gitdealflow-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gitdealflow-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/gitdealflow-com/llms/gitdealflow-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gitdealflow-com-llms.txt
- group: design
  href: https://artifacts.apis.io/gitdealflow-com/conformance/gitdealflow-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gitdealflow-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/gitdealflow-com/conventions/gitdealflow-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gitdealflow-com-conventions.yml
- group: agent
  href: https://artifacts.apis.io/gitdealflow-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gitdealflow-com/components/gitdealflow-com-components.yml
  title: ''
  type: Components
  url: components/gitdealflow-com-components.yml
- group: commercial
  href: https://artifacts.apis.io/gitdealflow-com/plans/gitdealflow-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gitdealflow-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/gitdealflow-com/rate-limits/gitdealflow-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gitdealflow-com-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/gitdealflow-com/regulatory/gitdealflow-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/gitdealflow-com-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/gitdealflow-com/well-known/gitdealflow-com-compliance.json
  title: ''
  type: Subprocessors
  url: well-known/gitdealflow-com-compliance.json
- group: other
  href: https://artifacts.apis.io/gitdealflow-com/well-known/gitdealflow-com-compliance.json
  title: ''
  type: DataResidency
  url: well-known/gitdealflow-com-compliance.json
- group: operate
  href: https://artifacts.apis.io/gitdealflow-com/well-known/gitdealflow-com-compliance.json
  title: ''
  type: IncidentNotification
  url: well-known/gitdealflow-com-compliance.json
- group: other
  href: https://artifacts.apis.io/gitdealflow-com/well-known/gitdealflow-com-ai-policy.json
  title: ''
  type: AITransparency
  url: well-known/gitdealflow-com-ai-policy.json
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://gitdealflow.com/privacy
- group: auth
  href: https://artifacts.apis.io/gitdealflow-com/security/gitdealflow-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/gitdealflow-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gitdealflow-com/scopes/gitdealflow-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gitdealflow-com-scopes.yml
- group: other
  href: https://artifacts.apis.io/gitdealflow-com/well-known/gitdealflow-com-compliance.json
  title: ''
  type: ExitAssistance
  url: well-known/gitdealflow-com-compliance.json
created: '2026-09-19'
description: GitDealFlow (also published as VC Deal Flow Signal) is a deal-flow signal tool for angel, scout and seed investors that reads public GitHub engineering activity across 400+ venture-backed startup organizations in 15 sectors and ranks the ones accelerating, historically 3-6 weeks before a fundraise announcement. The data is published free under CC BY 4.0 through a no-auth REST API described by an OpenAPI 3.1 document, a hosted MCP server (Streamable HTTP plus an npm stdio package), an A2A JSON-RPC agent with a published agent card, an NLWeb endpoint, JSON/CSV/ NDJSON bulk exports and an RSS feed, with one paid deep-signal endpoint metered by credit-pack key or x402 USDC micropayments. Operated pseudonymously from Cyprus by "The Data Nerd"; methodology published on SSRN.
finops:
- has_sources: true
  method: derived
  name: Gitdealflow Com Finops
  primary_unit: get_deep_signal call
  service_category: ''
  slug: gitdealflow-com-finops
  template: false
image: https://signals.gitdealflow.com/icon.png
layout: provider
mcp_servers:
- description: Remote MCP server at signals.gitdealflow.com over HTTP; 12 tools listed.
  name: GitDealFlow MCP Server
  slug: vc-deal-flow-signal
modified: '2026-09-19'
name: GitDealFlow
nav: Providers
network: true
overview: 'GitDealFlow publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Answer API, Badges API, and 15 more. Tagged areas include Venture Capital, Deal Flow, Startups, GitHub, and Alternative Data.


  The GitDealFlow catalog on APIs.io includes 1 Spectral governance ruleset.


  GitDealFlow''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 36 more developer resources.'
plans:
- name: Gitdealflow Com Plans Pricing
  plan_count: 14
  slug: gitdealflow-com-plans-pricing
- name: Gitdealflow Com Price Estimates
  plan_count: 0
  slug: gitdealflow-com-price-estimates
random_paper: 22
rate_limits:
- limit_count: 4
  name: Gitdealflow Com Rate Limits
  slug: gitdealflow-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: GitDealFlow API Rules
  rule_count: 59
  severity_counts:
    error: 56
    hint: 0
    info: 2
    warn: 1
  slug: gitdealflow-com-rules
scopes:
- name: Gitdealflow Com Scopes
  scope_count: 1
  slug: gitdealflow-com-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 60.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.2
  facets:
    access_clarity: 61.8
    contract_governance: 31.8
    contract_quality: 52.2
    developer_ergonomics: 51.2
    discoverability: 75.0
    operational_transparency: 60.5
  previous_composite: 71.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 15
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 55.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gitdealflow-com/gitdealflow-com-2026-10-11T104918.png
security:
- kind: authentication
  name: Gitdealflow Com Authentication
  slug: gitdealflow-com-authentication
  summary_line: none/http-bearer/x402-payment/oauth2-client-credentials · 4 schemes
- kind: domain-security
  name: Gitdealflow Com Domain Security
  slug: gitdealflow-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gitdealflow Com Vulnerability Disclosure
  slug: gitdealflow-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 2
skills:
- name: gitdealflow-lookup-startup-signal-rest
  slug: gitdealflow-com-lookup-startup-signal
- name: gitdealflow-vc-signals
  slug: gitdealflow-com-vc-signals
slug: gitdealflow-com
tags:
- Venture Capital
- Deal Flow
- Startups
- GitHub
- Alternative Data
- Investing
- MCP
- Agents
- Developer Tools
- A2A
website: https://gitdealflow.com/
---
