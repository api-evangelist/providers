---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.1
  scored_at: '2026-09-18'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tgatlas Agentic Access
  operation_count: 3
  slug: tgatlas-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://telegram155.p.rapidapi.com/v1
  baseurl_source: declared
  description: Read-only REST API over public Telegram data with 19 GET endpoints behind the RapidAPI gateway. Public OpenAPI 3.1 contract; key-based auth via RapidAPI headers; free tier available.
  name: ChannelIndex Telegram Channel Data API
  slug: channelindex-telegram-channel-data-api
artifact_total: 11
collections:
- collection_type: postman
  name: tgAtlas — Telegram Channel Data API
  slug: postman-tgatlas
common:
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/openapi/tgatlas-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/tgatlas-openapi.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/overlays/tgatlas-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tgatlas-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/vocabulary/tgatlas-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/tgatlas-vocabulary.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/postman/tgatlas.postman_collection.json
  title: ''
  type: Postman
  url: postman/tgatlas.postman_collection.json
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/plans/tgatlas-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tgatlas-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/rate-limits/tgatlas-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tgatlas-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/finops/tgatlas-finops.yml
  title: ''
  type: FinOps
  url: finops/tgatlas-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/rules/tgatlas-spectral-rules.yaml
  title: ''
  type: SpectralRules
  url: rules/tgatlas-spectral-rules.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/authentication/tgatlas-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tgatlas-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/errors/tgatlas-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tgatlas-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/conventions/tgatlas-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tgatlas-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/data-model/tgatlas-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tgatlas-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/conformance/tgatlas-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tgatlas-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/lifecycle/tgatlas-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tgatlas-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://channelindex.starnikovoleg.workers.dev/status
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/lifecycle/tgatlas-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/tgatlas-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/changelog/tgatlas-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tgatlas-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/well-known/tgatlas-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tgatlas-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/well-known/tgatlas-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tgatlas-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/llms/tgatlas-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tgatlas-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/mcp/tgatlas-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tgatlas-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/agentic-access/tgatlas-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tgatlas-agentic-access.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/packages/tgatlas-packages.yml
  title: ''
  type: Packages
  url: packages/tgatlas-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/security/tgatlas-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tgatlas-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/security/tgatlas-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tgatlas-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tgatlas/refs/heads/main/security/tgatlas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tgatlas-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://channelindex.starnikovoleg.workers.dev/api
- group: docs
  title: ''
  type: Documentation
  url: https://channelindex.starnikovoleg.workers.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://channelindex.starnikovoleg.workers.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://channelindex.starnikovoleg.workers.dev/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://channelindex.starnikovoleg.workers.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://rapidapi.com/starnikovoleg/api/telegram155
- group: commercial
  title: ''
  type: TermsOfService
  url: https://channelindex.starnikovoleg.workers.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://channelindex.starnikovoleg.workers.dev/privacy
- group: operate
  title: ''
  type: Support
  url: https://channelindex.starnikovoleg.workers.dev/about
- group: company
  title: ''
  type: Blog
  url: https://channelindex.starnikovoleg.workers.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/starnikovoleg
- group: company
  title: ''
  type: Website
  url: https://channelindex.starnikovoleg.workers.dev
created: '2026-09-16'
description: 'A read-only HTTP API over public Telegram data: resolve @usernames to numeric IDs, read channel size/description, walk post history with per-post views/forwards, pull Telegram similar-channel recommendations, and search the public directory. No phone number or MTProto session required. Auth via RapidAPI gateway headers. Also ships channelindex-mcp, a local/stdio MCP server wrapping the same REST API. The provider publishes an unusually complete machine-readable surface: OpenAPI 3.1, an Overlay, a domain vocabulary, a Postman collection, plans, rate limits and a FinOps mapping, plus llms.txt, security.txt and an api-onboarding descriptor.'
finops:
- name: Tgatlas Finops
  service_category: API
  slug: tgatlas-finops
image: https://channelindex.starnikovoleg.workers.dev/logo.svg
layout: provider
mcp_servers:
- description: First-party MCP server that wraps the tgAtlas Telegram REST API for agents. Returns channel profiles (subscribers, description, creation date, verification/scam flags, posting cadence), Telegram's own
  name: ChannelIndex (tgAtlas) MCP Server
  slug: channelindex-tgatlas-mcp-server
modified: '2026-09-16'
name: ChannelIndex (tgAtlas)
nav: Providers
network: true
overview: 'ChannelIndex (tgAtlas) publishes 1 API on the [APIs.io](https://apis.io/) network: ChannelIndex Telegram Channel Data API. Tagged areas include Telegram, Public Channels, Social-Media, Social Monitoring, and Messaging.


  The ChannelIndex (tgAtlas) catalog on APIs.io includes 1 Spectral governance ruleset.


  ChannelIndex (tgAtlas)''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Tgatlas Plans Pricing
  plan_count: 4
  slug: tgatlas-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 8
  name: Tgatlas Rate Limits
  slug: tgatlas-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: ChannelIndex (tgAtlas) API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 2
  slug: tgatlas-spectral-rules
score:
  band: exemplar
  composite: 71.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 87.0
    catalog_earned_first_party: 0.0
    catalog_gap: 28.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 69.7
    contract_quality: 57.0
    developer_ergonomics: 63.7
    discoverability: 75.9
    operational_transparency: 86.8
  previous_composite: 71.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Tgatlas Authentication
  slug: tgatlas-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Tgatlas Domain Security
  slug: tgatlas-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tgatlas Vulnerability Disclosure
  slug: tgatlas-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tgatlas
tags:
- Telegram
- Public Channels
- Social-Media
- Social Monitoring
- Messaging
- Directory
- Search
- Analytics
- OSINT
- Market Research
- AI-agent context
website: https://channelindex.starnikovoleg.workers.dev
---
