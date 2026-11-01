---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 33
  human_in_the_loop: 3
  name: Satohub Ai Agentic Access
  operation_count: 100
  slug: satohub-ai-agentic-access
  summary_line: 100 operations · 33 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: Weekly on-chain measurements per venue, chain and lifecycle stage. Nothing in these responses may be summed — read each venue's unit first.
  name: satohub-ai Agent Economy API
  slug: satohub-ai-agent-economy-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: Embeddable badges — SVG, or the shields.io endpoint-badge JSON. No key, hotlinkable.
  name: satohub-ai Badges API
  slug: satohub-ai-badges-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: 'Sato Check: what a package, MCP server, skill, repo or x402 endpoint can do with an agent''s keys and funds. A profile describes what was read and run, with dates — never a safety rating.'
  name: satohub-ai Check API
  slug: satohub-ai-check-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: Maintainers proving control of a listing they own.
  name: satohub-ai Claims API
  slug: satohub-ai-claims-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: 'create-sato-agent: a runnable agent repo from a goal, generated from a nightly-checked template. The goal is never stored.'
  name: satohub-ai Create API
  slug: satohub-ai-create-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: The catalog of components agents are built from.
  name: satohub-ai Directory API
  slug: satohub-ai-directory-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: 'Per-agent ERC-8004 checks: what each registered agent declares and whether its declared endpoints answered Sato Hub''s daily check, plus the evidence documents behind Sato Hub''s onchain attestations. R'
  name: satohub-ai Erc8004 API
  slug: satohub-ai-erc8004-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: Published agent packages. A listing is a public VIEW of one sealed, immutable version — allowlisted version fields plus secret-scanned owner fields, bound to the version's digest. Public reads need no
  name: satohub-ai Listings API
  slug: satohub-ai-listings-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: One check before an agent installs, connects or pays. A verdict names what was checked and when — never that anything is safe.
  name: satohub-ai Preflight API
  slug: satohub-ai-preflight-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: 'Private agent projects and their immutable sealed versions. Owner-only: every operation resolves the owner from the Privy bearer, never from a body field, and a caller who does not own the object gets'
  name: satohub-ai Projects API
  slug: satohub-ai-projects-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: Registered onchain agents and their passports.
  name: satohub-ai Registry API
  slug: satohub-ai-registry-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: Map a repository URL or package name to its listing. Exact match only.
  name: satohub-ai Resolve API
  slug: satohub-ai-resolve-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: 'Sato Route. A route is a RECOMMENDATION: the venue is chosen by liveness, verification state and quoted price as those fields read on the date in `checked_at`, and `chosen_by` names every field it was'
  name: satohub-ai Route API
  slug: satohub-ai-route-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: 'Sato Bot. A goal in plain words in, a BUILD PLAN out: the goal restated, a stack of real directory listings each carrying its Sato Score and `sato_url`, a deploy spec and a Preflight verdict per item,'
  name: satohub-ai Satobot API
  slug: satohub-ai-satobot-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: 'Sato Scan: a reading of a payee address, and the marks Sato Scan holds, before money moves. A reading describes what was found and what was not checked; no record on an address is not a statement that'
  name: satohub-ai Scan API
  slug: satohub-ai-scan-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: Response signing. Every Preflight verdict and every Sato Route decision is returned with a detached Ed25519 signature — `Sato-Signature` over the exact response bytes plus `Sato-Signed-At`, and the sa
  name: satohub-ai Signing API
  slug: satohub-ai-signing-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: Crypto-relevant agent skills with static disclosures — what a skill declares and does. Descriptions, never safety verdicts.
  name: satohub-ai Skills API
  slug: satohub-ai-skills-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: Sato Swap. One call chooses the venue, discloses that venue's own fee sentence verbatim, checks four targets — both tokens, the venue endpoint and the recipient — against the caller's policy, simulate
  name: satohub-ai Swap API
  slug: satohub-ai-swap-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: Incremental mirroring.
  name: satohub-ai Sync API
  slug: satohub-ai-sync-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: The x402 API from satohub-ai — 3 operation(s) for x402.
  name: satohub-ai X402 API
  slug: satohub-ai-x402-api
- baseURL: https://satohub.ai
  baseurl_source: declared
  description: An evidence-ranked index of the sellers who take x402 payments. Every reading is dated and carries its method; `unknown` means no reading is held, never a failure.
  name: satohub-ai X402 Merchants API
  slug: satohub-ai-x402-merchants-api
artifact_total: 36
common:
- group: agent
  href: https://artifacts.apis.io/satohub-ai/agentic-access/satohub-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/satohub-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/satohub-ai/rules/satohub-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/satohub-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/satohub-ai/json-ld/satohub-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/satohub-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/satohub-ai/vocabulary/satohub-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/satohub-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/satohub-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/satohub-ai/data-model/satohub-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/satohub-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/satohub-ai/authentication/satohub-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/satohub-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/satohub-ai/lifecycle/satohub-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/satohub-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/satohub-ai/errors/satohub-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/satohub-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/satohub-ai/conformance/satohub-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/satohub-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/satohub-ai/llms/satohub-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/satohub-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/satohub-ai/mcp/satohub-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/satohub-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/satohub-ai/well-known/satohub-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/satohub-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/satohub-ai/well-known/satohub-ai-ethereum-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/satohub-ai-ethereum-security.txt
- group: agent
  href: https://artifacts.apis.io/satohub-ai/well-known/satohub-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/satohub-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/satohub-ai/hosts/satohub-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/satohub-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/satohub-ai/vendors/satohub-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/satohub-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/satohub-ai/packages/satohub-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/satohub-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/satohub-ai/packages/satohub-ai-packages.yml
  title: ''
  type: Packages
  url: packages/satohub-ai-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://satohub.ai/status
- group: start
  title: ''
  type: SignUp
  url: https://satohub.ai/agents/register
- group: auth
  title: ''
  type: Security
  url: https://satohub.ai/security
- group: company
  title: ''
  type: Newsroom
  url: https://satohub.ai/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://satohub.ai/changelog
- group: auth
  href: https://artifacts.apis.io/satohub-ai/security/satohub-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/satohub-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/satohub-ai/security/satohub-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/satohub-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://satohub.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://satohub.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://satohub.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://satohub.ai/docs
- group: operate
  title: ''
  type: Support
  url: https://satohub.ai/about
- group: company
  title: ''
  type: Blog
  url: https://satohub.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/satohubai
- group: commercial
  title: ''
  type: Pricing
  url: https://satohub.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://satohub.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://satohub.ai/privacy
created: '2026-10-30'
description: Sato Hub is a daily-rebuilt, evidence-scored index of on‑chain AI agents, listing frameworks, MCP servers, wallets, payment rails and data tools. It provides install checks, agent‑economy metrics, and a searchable directory of 488 scored listings across 28 chains. The platform has no token and is dedicated to transparent AI agent tooling.
image: https://satohub.ai/brand/satohub-logo-1024.png
json_schemas:
- name: interpretation
  property_count: 4
  slug: satohub-ai-interpretation
- name: needs-input
  property_count: 6
  slug: satohub-ai-needs-input
- name: scan-recipient
  property_count: 0
  slug: satohub-ai-scan-recipient
- name: swap-receipt
  property_count: 0
  slug: satohub-ai-swap-receipt
- name: token-resolve
  property_count: 0
  slug: satohub-ai-token-resolve
- name: Sealed agent version (sato.version/v1)
  property_count: 21
  slug: satohub-ai-version
jsonld:
- class_count: 3
  name: Satohub Ai Context
  property_count: 31
  slug: satohub-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at satohub.ai.
  name: satohub-ai MCP Server
  slug: satohub-ai-mcp-yml
modified: '2026-10-30'
name: satohub-ai
nav: Providers
network: true
overview: 'satohub-ai publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Economy API, Badges API, Check API, and 18 more. Tagged areas include Company, AI, Blockchain, Crypto, and Agent.


  The satohub-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  satohub-ai''s developer surface includes authentication, signup flow, changelog, documentation, API reference, getting-started guide, support, and 29 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: satohub-ai API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 2
  slug: satohub-ai-rules
scopes:
- name: Satohub Ai Scopes
  scope_count: 0
  slug: satohub-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 61.0
    developer_ergonomics: 56.5
    discoverability: 66.7
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
    skills: derived
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
  name: Satohub Ai Authentication
  slug: satohub-ai-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Satohub Ai Domain Security
  slug: satohub-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Satohub Ai Vulnerability Disclosure
  slug: satohub-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-directory-json
  slug: satohub-ai-get-directory-json
slug: satohub-ai
tags:
- Company
- AI
- Blockchain
- Crypto
- Agent
website: https://satohub.ai/
---
