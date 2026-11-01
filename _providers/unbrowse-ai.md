---
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
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 86
  human_in_the_loop: 6
  name: Unbrowse Ai Agentic Access
  operation_count: 176
  slug: unbrowse-ai-agentic-access
  summary_line: 176 operations · 86 acting · 6 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.unbrowse.ai
  baseurl_source: declared
  description: Who is signed in and what they have used.
  name: unbrowse-ai Account API
  slug: unbrowse-ai-account-api
- baseURL: https://api.unbrowse.ai
  baseurl_source: declared
  description: What the workspace enabled, by app; tool scopes with their own MCP URL (/mcp/{slug}); switch tools off; unpublish and republish.
  name: unbrowse-ai Apps & tools API
  slug: unbrowse-ai-apps-tools-api
- baseURL: https://api.unbrowse.ai
  baseurl_source: declared
  description: Find the tools Unbrowse knows (the user's own and the public index).
  name: unbrowse-ai Capabilities API
  slug: unbrowse-ai-capabilities-api
- baseURL: https://api.unbrowse.ai
  baseurl_source: declared
  description: Apps' own MCP servers (Linear, Notion, GitHub…) and Composio toolkits (Gmail, Calendar…) connected with the person's own account; their tools are called through Unbrowse.
  name: unbrowse-ai Connected apps API
  slug: unbrowse-ai-connected-apps-api
- baseURL: https://api.unbrowse.ai
  baseurl_source: declared
  description: 'Teach Unbrowse a site: it explores the site in the cloud browser and compiles tools.'
  name: unbrowse-ai Indexing API
  slug: unbrowse-ai-indexing-api
- baseURL: https://api.unbrowse.ai
  baseurl_source: declared
  description: Learn a capability from recorded traffic (HAR or traces); read what was learned.
  name: unbrowse-ai Learning API
  slug: unbrowse-ai-learning-api
- baseURL: https://api.unbrowse.ai
  baseurl_source: declared
  description: 'The password manager: logins go in, only masked hints come out. Sites are signed in to by Unbrowse''s browser.'
  name: unbrowse-ai Logins & vault API
  slug: unbrowse-ai-logins-vault-api
- baseURL: https://api.unbrowse.ai
  baseurl_source: declared
  description: 'Every app with its tools, public: search, categories, official MCP servers, agent-readiness.'
  name: unbrowse-ai Marketplace API
  slug: unbrowse-ai-marketplace-api
- baseURL: https://api.unbrowse.ai
  baseurl_source: declared
  description: 'For agent builders: an org, its keys, one workspace per end user, and one-time connect links for end users'' logins.'
  name: unbrowse-ai Orgs API
  slug: unbrowse-ai-orgs-api
- baseURL: https://api.unbrowse.ai
  baseurl_source: declared
  description: 'Read any page by URL (scrape): HTML, markdown, text or links, with its real status and timing.'
  name: unbrowse-ai Pages API
  slug: unbrowse-ai-pages-api
- baseURL: https://api.unbrowse.ai
  baseurl_source: declared
  description: 'Recorded browser sessions: list, read, search and ask across them.'
  name: unbrowse-ai Replays API
  slug: unbrowse-ai-replays-api
- baseURL: https://api.unbrowse.ai
  baseurl_source: declared
  description: 'Do a task on a website: start, follow, answer what it needs, cancel.'
  name: unbrowse-ai Runs API
  slug: unbrowse-ai-runs-api
- baseURL: https://api.unbrowse.ai
  baseurl_source: declared
  description: 'A question in plain words, compiled once into an API: typed params, a pinned tool, the same shape every call, and an optional cache.'
  name: unbrowse-ai Saved queries API
  slug: unbrowse-ai-saved-queries-api
- baseURL: https://api.unbrowse.ai
  baseurl_source: declared
  description: 'The public index: 8,000+ sites, each with its own tools and OpenAPI spec.'
  name: unbrowse-ai Sites API
  slug: unbrowse-ai-sites-api
artifact_total: 32
common:
- group: auth
  href: https://artifacts.apis.io/unbrowse-ai/well-known/unbrowse-ai-blog-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/unbrowse-ai-blog-security.txt
- group: agent
  href: https://artifacts.apis.io/unbrowse-ai/agentic-access/unbrowse-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/unbrowse-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/unbrowse-ai/rules/unbrowse-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/unbrowse-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/unbrowse-ai/json-ld/unbrowse-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/unbrowse-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/unbrowse-ai/vocabulary/unbrowse-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/unbrowse-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/unbrowse-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/unbrowse-ai/data-model/unbrowse-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/unbrowse-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/unbrowse-ai/conventions/unbrowse-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/unbrowse-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/unbrowse-ai/conventions/unbrowse-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/unbrowse-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/unbrowse-ai/authentication/unbrowse-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unbrowse-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/unbrowse-ai/errors/unbrowse-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/unbrowse-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/unbrowse-ai/conformance/unbrowse-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unbrowse-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/unbrowse-ai/llms/unbrowse-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unbrowse-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/unbrowse-ai/well-known/unbrowse-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/unbrowse-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/unbrowse-ai/hosts/unbrowse-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unbrowse-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/unbrowse-ai/vendors/unbrowse-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unbrowse-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://unbrowse.ai/security
- group: start
  title: ''
  type: Login
  url: https://blog.unbrowse.ai/login
- group: auth
  href: https://artifacts.apis.io/unbrowse-ai/scopes/unbrowse-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/unbrowse-ai-scopes.yml
- group: auth
  href: https://artifacts.apis.io/unbrowse-ai/security/unbrowse-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/unbrowse-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/unbrowse-ai/security/unbrowse-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unbrowse-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unbrowse.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://unbrowse.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://unbrowse.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://unbrowse.ai/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://unbrowse.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://unbrowse.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unbrowse-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unbrowse.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unbrowse.ai/privacy
created: '2026-10-30'
description: Unbrowse AI is a platform that enables developers to connect AI agents to a wide range of external services and data sources through a unified API. By providing a simple interface for browsing, searching, and interacting with web content, databases, and third‑party APIs, Unbrowse AI helps accelerate the creation of intelligent applications. The service offers tools for developers to integrate browsing capabilities, manage connections, and leverage AI‑driven automation across domains such as e‑commerce, travel, and knowledge retrieval. It aims to simplify the complexity of web interaction for AI models, delivering a robust, scalable solution for modern AI‑powered workflows.
image: https://unbrowse.ai/og.jpg
json_schemas:
- name: EgressResponse
  property_count: 5
  slug: unbrowse-ai-egress-response
- name: RunRequest
  property_count: 10
  slug: unbrowse-ai-run-request
- name: Run
  property_count: 9
  slug: unbrowse-ai-run
- name: SessionReuse
  property_count: 7
  slug: unbrowse-ai-session-reuse
- name: Sharing
  property_count: 7
  slug: unbrowse-ai-sharing
- name: ToolScope
  property_count: 7
  slug: unbrowse-ai-tool-scope
jsonld:
- class_count: 10
  name: Unbrowse Ai Context
  property_count: 48
  slug: unbrowse-ai-context
layout: provider
modified: '2026-10-30'
name: unbrowse-ai
nav: Providers
network: true
overview: 'unbrowse-ai publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Apps & tools API, Capabilities API, and 11 more. Tagged areas include AI Agents and Developer Tools.


  The unbrowse-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  unbrowse-ai''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, and 25 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: unbrowse-ai API Rules
  rule_count: 18
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 2
  slug: unbrowse-ai-rules
scopes:
- name: Unbrowse Ai Scopes
  scope_count: 1
  slug: unbrowse-ai-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 62.1
    developer_ergonomics: 47.0
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Unbrowse Ai Authentication
  slug: unbrowse-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Unbrowse Ai Domain Security
  slug: unbrowse-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Unbrowse Ai Vulnerability Disclosure
  slug: unbrowse-ai-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 5
skills:
- name: unbrowse-ai-connect-and-call
  slug: unbrowse-ai-connect-and-call
- name: unbrowse-ai-manage-cookies
  slug: unbrowse-ai-manage-cookies
- name: unbrowse-ai-manage-scopes
  slug: unbrowse-ai-manage-scopes
- name: unbrowse-ai-run-task
  slug: unbrowse-ai-run-task
- name: unbrowse-ai-save-and-list-logins
  slug: unbrowse-ai-save-and-list-logins
slug: unbrowse-ai
tags:
- AI Agents
- Developer Tools
website: https://unbrowse.ai/
---
