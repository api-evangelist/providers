---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
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
  score: 38.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Lenz Io Agentic Access
  operation_count: 24
  slug: lenz-io-agentic-access
  summary_line: 24 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://lenz.io
  baseurl_source: declared
  description: Your credit balance, the price list, and rate-limit usage.
  name: lenz-io Account API
  slug: lenz-io-account-api
- baseURL: https://lenz.io
  baseurl_source: declared
  description: Ask follow-up questions grounded on an existing verification.
  name: lenz-io Ask API
  slug: lenz-io-ask-api
- baseURL: https://lenz.io
  baseurl_source: declared
  description: Fast panel verdict on a claim, with the pages the reviewers looked at. Sync, typically 10-25s; allow 45s for the response.
  name: lenz-io Assess API
  slug: lenz-io-assess-api
- baseURL: https://lenz.io
  baseurl_source: declared
  description: 'Check whether each cited source says what a draft attributes to it: from a draft with its links, or from statement-source pairs. Async; 1 credit per checked citation, and a source that could not be ch'
  name: lenz-io Citecheck API
  slug: lenz-io-citecheck-api
- baseURL: https://lenz.io
  baseurl_source: declared
  description: Machine-readable index of the API root.
  name: lenz-io Discovery API
  slug: lenz-io-discovery-api
- baseURL: https://lenz.io
  baseurl_source: declared
  description: Pull verifiable claims out of any text. Costs no credits; fair-use cap 1,000/account/day.
  name: lenz-io Extract API
  slug: lenz-io-extract-api
- baseURL: https://lenz.io
  baseurl_source: declared
  description: The Lenz — AI Fact Checking API API from lenz-io — 0 operation(s) for lenz — ai fact checking api.
  name: lenz-io Lenz — AI Fact Checking API
  slug: lenz-io-lenz-ai-fact-checking-api-api
- baseURL: https://lenz.io
  baseurl_source: declared
  description: Browse the public catalog of verifications. No API key required.
  name: lenz-io Library API
  slug: lenz-io-library-api
- baseURL: https://lenz.io
  baseurl_source: declared
  description: 'The whole recipe in one call: find the claims in a draft, quick-check each, deep-check the ones that look wrong or uncertain, and get the issues back with suggested rewrites. Async, two to four minute'
  name: lenz-io Review API
  slug: lenz-io-review-api
- baseURL: https://lenz.io
  baseurl_source: declared
  description: List, fetch, delete, and toggle visibility on stored verifications.
  name: lenz-io Verifications API
  slug: lenz-io-verifications-api
- baseURL: https://lenz.io
  baseurl_source: declared
  description: The full investigation, with verified citations. Async, ~90s. Submit one claim or a batch, poll status, and resolve a needs_input interrupt with select.
  name: lenz-io Verify API
  slug: lenz-io-verify-api
artifact_total: 28
asyncapis:
- description: ''
  name: Lenz Io Webhooks
  slug: lenz-io-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/lenz-io/agentic-access/lenz-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lenz-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/lenz-io/plans/lenz-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lenz-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/lenz-io/rules/lenz-io-rules.yml
  title: ''
  type: Spectral
  url: rules/lenz-io-rules.yml
- group: design
  href: https://artifacts.apis.io/lenz-io/json-ld/lenz-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lenz-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/lenz-io/vocabulary/lenz-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lenz-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/lenz-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lenz-io/asyncapi/lenz-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lenz-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/lenz-io/data-model/lenz-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lenz-io-data-model.yml
- group: build
  href: https://artifacts.apis.io/lenz-io/cli/lenz-io-cli.yml
  title: ''
  type: CLI
  url: cli/lenz-io-cli.yml
- group: auth
  href: https://artifacts.apis.io/lenz-io/authentication/lenz-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lenz-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/lenz-io/errors/lenz-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lenz-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lenz-io/conformance/lenz-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lenz-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lenz-io/llms/lenz-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lenz-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/lenz-io/well-known/lenz-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lenz-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/lenz-io/hosts/lenz-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lenz-io-hosts.yml
- group: build
  href: https://artifacts.apis.io/lenz-io/packages/lenz-io-packages.yml
  title: ''
  type: SDKs
  url: packages/lenz-io-packages.yml
- group: build
  href: https://artifacts.apis.io/lenz-io/packages/lenz-io-packages.yml
  title: ''
  type: Packages
  url: packages/lenz-io-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lenzhq
- group: auth
  href: https://artifacts.apis.io/lenz-io/security/lenz-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lenz-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lenz.io/
- group: docs
  title: ''
  type: Documentation
  url: https://lenz.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://lenz.io/api/v1/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://lenz.io/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://lenz.io/plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lenz.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lenz.io/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://lenz.io/mcp
  - status: 200
    url: https://lenz.io/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Lenz provides an audit‑grade AI fact‑checking API that verifies factual claims in AI‑generated or human‑written text against independent sources. It offers a multi‑model verification pipeline, reviewer panels, and detailed source citations to ensure trustworthy outputs. The service includes a free trial, tiered pricing, and integrations with major AI models like Claude and ChatGPT, targeting enterprises needing reliable AI content validation.
image: https://lenz.io/media/og-image.png?v=9
json_schemas:
- name: ClaimDetailOutLegacy
  property_count: 20
  slug: lenz-io-claim-detail-out-legacy
- name: ClaimDetailOut
  property_count: 20
  slug: lenz-io-claim-detail-out
- name: ReviewFullOutLegacy
  property_count: 21
  slug: lenz-io-review-full-out-legacy
- name: ReviewFullOut
  property_count: 21
  slug: lenz-io-review-full-out
- name: ReviewIssuesOutLegacy
  property_count: 19
  slug: lenz-io-review-issues-out-legacy
- name: ReviewIssuesOut
  property_count: 19
  slug: lenz-io-review-issues-out
jsonld:
- class_count: 120
  name: Lenz Io Context
  property_count: 252
  slug: lenz-io-context
layout: provider
modified: '2026-10-30'
name: lenz-io
nav: Providers
network: true
overview: 'lenz-io publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Ask API, Assess API, and 8 more. Tagged areas include Artificial Intelligence, Fact Checking, Enterprise, and Audit.


  The lenz-io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  lenz-io''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, pricing, and 20 more developer resources.'
plans:
- name: Lenz Io Plans Pricing
  plan_count: 5
  slug: lenz-io-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Lenz Io Rate Limits
  slug: lenz-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: lenz-io API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: lenz-io-rules
scopes:
- name: Lenz Io Scopes
  scope_count: 0
  slug: lenz-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 32
    catalog_earned: 63.8
    catalog_earned_first_party: 20.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 64.5
    developer_ergonomics: 46.9
    discoverability: 48.2
    operational_transparency: 31.6
  previous_composite: 56.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lenz-io/lenz-io-2026-11-03T134810.png
security:
- kind: authentication
  name: Lenz Io Authentication
  slug: lenz-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Lenz Io Domain Security
  slug: lenz-io-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: assessment
  slug: lenz-io-assessment
- name: lenz-io-review-skill
  slug: lenz-io-review-skill
slug: lenz-io
tags:
- Artificial Intelligence
- Fact Checking
- Enterprise
- Audit
website: https://lenz.io/
---
