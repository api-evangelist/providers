---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 64.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 5
  name: Darwin So Agentic Access
  operation_count: 40
  slug: darwin-so-agentic-access
  summary_line: 40 operations · 19 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.darwin.so/api/v2
  baseurl_source: declared
  description: The Account API from Darwin Technologies, Inc. — 26 operation(s) for account.
  name: Darwin Technologies, Inc. Account API
  slug: darwin-so-account-api
- baseURL: https://api.darwin.so/api/v2
  baseurl_source: declared
  description: The Accounts API from Darwin Technologies, Inc. — 1 operation(s) for accounts.
  name: Darwin Technologies, Inc. Accounts API
  slug: darwin-so-accounts-api
- baseURL: https://api.darwin.so/api/v2
  baseurl_source: declared
  description: The Act API from Darwin Technologies, Inc. — 9 operation(s) for act.
  name: Darwin Technologies, Inc. Act API
  slug: darwin-so-act-api
- baseURL: https://api.darwin.so/api/v2
  baseurl_source: declared
  description: The Search API from Darwin Technologies, Inc. — 1 operation(s) for search.
  name: Darwin Technologies, Inc. Search API
  slug: darwin-so-search-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/darwin-so/agentic-access/darwin-so-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/darwin-so-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/darwin-so/plans/darwin-so-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/darwin-so-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/darwin-so/rules/darwin-so-rules.yml
  title: ''
  type: Spectral
  url: rules/darwin-so-rules.yml
- group: design
  href: https://artifacts.apis.io/darwin-so/json-ld/darwin-so-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/darwin-so-context.jsonld
- group: design
  href: https://artifacts.apis.io/darwin-so/vocabulary/darwin-so-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/darwin-so-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/darwin-so/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/darwin-so/data-model/darwin-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/darwin-so-data-model.yml
- group: operate
  href: https://artifacts.apis.io/darwin-so/changelog/darwin-so-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/darwin-so-changelog.yml
- group: design
  href: https://artifacts.apis.io/darwin-so/conventions/darwin-so-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/darwin-so-conventions.yml
- group: design
  href: https://artifacts.apis.io/darwin-so/conventions/darwin-so-conventions.yml
  title: ''
  type: Conventions
  url: conventions/darwin-so-conventions.yml
- group: design
  href: https://artifacts.apis.io/darwin-so/errors/darwin-so-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/darwin-so-problem-types.yml
- group: design
  href: https://artifacts.apis.io/darwin-so/conformance/darwin-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/darwin-so-conformance.yml
- group: agent
  href: https://artifacts.apis.io/darwin-so/llms/darwin-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/darwin-so-llms.txt
- group: other
  href: https://artifacts.apis.io/darwin-so/a2a/darwin-so-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/darwin-so-a2a.yml
- group: build
  href: https://artifacts.apis.io/darwin-so/mcp/darwin-so-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/darwin-so-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/darwin-so/mcp/darwin-so-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/darwin-so-mcp.yml
- group: agent
  href: https://artifacts.apis.io/darwin-so/well-known/darwin-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/darwin-so-well-known.yml
- group: other
  href: https://artifacts.apis.io/darwin-so/hosts/darwin-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/darwin-so-hosts.yml
- group: other
  href: https://artifacts.apis.io/darwin-so/vendors/darwin-so-vendors.yml
  title: ''
  type: Vendors
  url: vendors/darwin-so-vendors.yml
- group: build
  href: https://artifacts.apis.io/darwin-so/packages/darwin-so-packages.yml
  title: ''
  type: SDKs
  url: packages/darwin-so-packages.yml
- group: build
  href: https://artifacts.apis.io/darwin-so/packages/darwin-so-packages.yml
  title: ''
  type: Packages
  url: packages/darwin-so-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://darwin.so/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://darwin.so/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://darwin.so/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://darwin.so/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/darwin-studios
- group: operate
  title: ''
  type: ChangeLog
  url: https://darwin.so/docs/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://darwin.so/docs/interfaces/darwin/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://dev.darwin.so/
- group: auth
  href: https://artifacts.apis.io/darwin-so/authentication/darwin-so-authentication.yml
  title: ''
  type: Authentication
  url: authentication/darwin-so-authentication.yml
- group: auth
  href: https://artifacts.apis.io/darwin-so/security/darwin-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/darwin-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://darwin.so/
created: '2026-11-04'
description: Darwin Technologies, Inc. builds the agentic web, enabling people and AI to discover, use, and create agents. Their mission is to advance how the world interacts with agents, offering a platform for AI assistants, marketplaces, and productivity apps. The company provides developer tools, documentation, and a network connecting businesses and users to get work done efficiently.
image: https://darwin.so/assets/marketing/darwin/editorial/social/darwin-social-gradient.png
json_schemas:
- name: GetPaymentOptionsResponse
  property_count: 14
  slug: darwin-so-get-payment-options-response
- name: GetThreadResponse
  property_count: 9
  slug: darwin-so-get-thread-response
- name: ListTargetAccountsResponse
  property_count: 2
  slug: darwin-so-list-target-accounts-response
- name: PayResponse
  property_count: 0
  slug: darwin-so-pay-response
- name: SendMessageBody
  property_count: 0
  slug: darwin-so-send-message-body
- name: StartThreadBody
  property_count: 0
  slug: darwin-so-start-thread-body
jsonld:
- class_count: 56
  name: Darwin So Context
  property_count: 155
  slug: darwin-so-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.darwin.so.
  name: Darwin Technologies, Inc. MCP Server
  slug: darwin-so-mcp-yml
modified: '2026-11-04'
name: Darwin Technologies, Inc.
nav: Providers
network: true
overview: 'Darwin Technologies, Inc. publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Accounts API, Act API, and 1 more. Tagged areas include Company, Artificial Intelligence, Platform, Developer Tools, and Marketplace.


  The Darwin Technologies, Inc. catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Darwin Technologies, Inc.''s developer surface includes changelog, pricing, getting-started guide, API reference, authentication, and 27 more developer resources.'
plans:
- name: Darwin So Plans Pricing
  plan_count: 4
  slug: darwin-so-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Darwin Technologies, Inc. API Rules
  rule_count: 56
  severity_counts:
    error: 41
    hint: 0
    info: 4
    warn: 11
  slug: darwin-so-rules
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 64.9
    developer_ergonomics: 39.9
    discoverability: 66.7
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Darwin So Authentication
  slug: darwin-so-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Darwin So Domain Security
  slug: darwin-so-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: darwin-so-start-thread-and-send-message
  slug: darwin-so-start-thread-and-send-message
slug: darwin-so
tags:
- Company
- Artificial Intelligence
- Platform
- Developer Tools
- Marketplace
- Productivity
website: https://darwin.so/
---
