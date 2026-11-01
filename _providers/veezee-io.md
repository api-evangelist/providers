---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
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
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 59.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Veezee Io Agentic Access
  operation_count: 23
  slug: veezee-io-agentic-access
  summary_line: 23 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.veezee.io
  baseurl_source: declared
  description: The Checkout API from veezee-io — 1 operation(s) for checkout.
  name: veezee-io Checkout API
  slug: veezee-io-checkout-api
- baseURL: https://api.veezee.io
  baseurl_source: declared
  description: The Claim API from veezee-io — 1 operation(s) for claim.
  name: veezee-io Claim API
  slug: veezee-io-claim-api
- baseURL: https://api.veezee.io
  baseurl_source: declared
  description: The Keys API from veezee-io — 1 operation(s) for keys.
  name: veezee-io Keys API
  slug: veezee-io-keys-api
- baseURL: https://api.veezee.io
  baseurl_source: declared
  description: The Portal API from veezee-io — 1 operation(s) for portal.
  name: veezee-io Portal API
  slug: veezee-io-portal-api
- baseURL: https://api.veezee.io
  baseurl_source: declared
  description: The Recover API from veezee-io — 1 operation(s) for recover.
  name: veezee-io Recover API
  slug: veezee-io-recover-api
- baseURL: https://api.veezee.io
  baseurl_source: declared
  description: The Reddit API from veezee-io — 6 operation(s) for reddit.
  name: veezee-io Reddit API
  slug: veezee-io-reddit-api
- baseURL: https://api.veezee.io
  baseurl_source: declared
  description: The Rekey API from veezee-io — 1 operation(s) for rekey.
  name: veezee-io Rekey API
  slug: veezee-io-rekey-api
- baseURL: https://api.veezee.io
  baseurl_source: declared
  description: The Usage API from veezee-io — 1 operation(s) for usage.
  name: veezee-io Usage API
  slug: veezee-io-usage-api
- baseURL: https://api.veezee.io
  baseurl_source: declared
  description: The X API from veezee-io — 5 operation(s) for x.
  name: veezee-io X API
  slug: veezee-io-x-api
- baseURL: https://api.veezee.io
  baseurl_source: declared
  description: The Linked In API from veezee-io — 5 operation(s) for linked in.
  name: veezee-io Linked In API
  slug: veezee-io-linked-in-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/veezee-io/agentic-access/veezee-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/veezee-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/veezee-io/rate-limits/veezee-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/veezee-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/veezee-io/plans/veezee-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/veezee-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/veezee-io/rules/veezee-io-rules.yml
  title: ''
  type: Spectral
  url: rules/veezee-io-rules.yml
- group: design
  href: https://artifacts.apis.io/veezee-io/json-ld/veezee-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/veezee-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/veezee-io/vocabulary/veezee-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/veezee-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/veezee-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/veezee-io/data-model/veezee-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/veezee-io-data-model.yml
- group: build
  href: https://artifacts.apis.io/veezee-io/cli/veezee-io-cli.yml
  title: ''
  type: CLI
  url: cli/veezee-io-cli.yml
- group: operate
  href: https://artifacts.apis.io/veezee-io/changelog/veezee-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/veezee-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/veezee-io/conventions/veezee-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/veezee-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/veezee-io/conventions/veezee-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/veezee-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/veezee-io/security/veezee-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/veezee-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/veezee-io/authentication/veezee-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/veezee-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/veezee-io/lifecycle/veezee-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/veezee-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/veezee-io/errors/veezee-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/veezee-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/veezee-io/conformance/veezee-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/veezee-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/veezee-io/llms/veezee-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/veezee-io-llms.txt
- group: other
  href: https://artifacts.apis.io/veezee-io/a2a/veezee-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/veezee-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/veezee-io/mcp/veezee-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/veezee-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/veezee-io/well-known/veezee-io-specification-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/veezee-io-specification-security.txt
- group: auth
  href: https://artifacts.apis.io/veezee-io/well-known/veezee-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/veezee-io-security.txt
- group: agent
  href: https://artifacts.apis.io/veezee-io/well-known/veezee-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/veezee-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/veezee-io/hosts/veezee-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/veezee-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/veezee-io/vendors/veezee-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/veezee-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/veezee-io/packages/veezee-io-packages.yml
  title: ''
  type: Packages
  url: packages/veezee-io-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://veezee.io/trust
- group: operate
  title: ''
  type: StatusPage
  url: https://veezee.io/status
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@veezee/sdk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veezeehq
- group: operate
  title: ''
  type: ChangeLog
  url: https://veezee.io/changelog
- group: auth
  href: https://artifacts.apis.io/veezee-io/security/veezee-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/veezee-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/veezee-io/security/veezee-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/veezee-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://veezee.io/
- group: docs
  title: ''
  type: Documentation
  url: https://veezee.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://veezee.io/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://veezee.io/#quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://veezee.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://veezee.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://veezee.io/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://veezee.io/docs
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://veezee.io/openapi.json
  - status: 401
    url: https://mcp.veezee.io/mcp
  - status: 200
    url: https://veezee.io/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: 'LinkedIn, Reddit, and X (formerly Twitter) data for AI agents: people search, profile enrichment, discussion search, and recency sweeps over MCP or REST. No signup: your agent mints its own free key in one call.'
image: https://veezee.io/og.png
json_schemas:
- name: person_envelope
  property_count: 9
  slug: veezee-io-person-envelope
- name: reddit_search_envelope
  property_count: 9
  slug: veezee-io-reddit-search-envelope
- name: reddit_thread_envelope
  property_count: 9
  slug: veezee-io-reddit-thread-envelope
- name: reddit_user_envelope
  property_count: 9
  slug: veezee-io-reddit-user-envelope
- name: x_search_envelope
  property_count: 9
  slug: veezee-io-x-search-envelope
- name: x_tweet_envelope
  property_count: 9
  slug: veezee-io-x-tweet-envelope
jsonld:
- class_count: 16
  name: Veezee Io Context
  property_count: 20
  slug: veezee-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.veezee.io.
  name: veezee-io MCP Server
  slug: veezee-io-mcp-yml
modified: '2026-10-29'
name: veezee-io
nav: Providers
network: true
overview: 'veezee-io publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Checkout API, Claim API, Keys API, and 7 more. Tagged areas include AI, Data, Enrichment, SocialMedia, and Search.


  The veezee-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  veezee-io''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, pricing, and 34 more developer resources.'
plans:
- name: Veezee Io Plans Pricing
  plan_count: 4
  slug: veezee-io-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Veezee Io Rate Limits
  slug: veezee-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: veezee-io API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: veezee-io-rules
scopes:
- name: Veezee Io Scopes
  scope_count: 0
  slug: veezee-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 30
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 22.0
    contract_quality: 64.9
    developer_ergonomics: 66.1
    discoverability: 65.0
    operational_transparency: 68.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Veezee Io Authentication
  slug: veezee-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Veezee Io Domain Security
  slug: veezee-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Veezee Io Vulnerability Disclosure
  slug: veezee-io-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: mint-key
  slug: veezee-io-mintkey-skill
slug: veezee-io
tags:
- AI
- Data
- Enrichment
- SocialMedia
- Search
website: https://veezee.io/
---
