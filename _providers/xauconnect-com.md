---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Xauconnect Com Agentic Access
  operation_count: 13
  slug: xauconnect-com-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- baseURL: https://xauconnect.com/api
  baseurl_source: declared
  description: Swap recording for admin analytics
  name: XAUConnect Analytics API
  slug: xauconnect-com-analytics-api
- baseURL: https://xauconnect.com/api
  baseurl_source: declared
  description: Cross-chain bridge routes
  name: XAUConnect Cross Chain API
  slug: xauconnect-com-cross-chain-api
- baseURL: https://xauconnect.com/api
  baseurl_source: declared
  description: Chains, tokens, settings
  name: XAUConnect Meta API
  slug: xauconnect-com-meta-api
- baseURL: https://xauconnect.com/api
  baseurl_source: declared
  description: Same-chain quotes and execution payloads
  name: XAUConnect Swap API
  slug: xauconnect-com-swap-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/xauconnect-com/agentic-access/xauconnect-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xauconnect-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/xauconnect-com/rate-limits/xauconnect-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/xauconnect-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/xauconnect-com/rules/xauconnect-com-rules.yml
  title: ''
  type: Spectral
  url: rules/xauconnect-com-rules.yml
- group: design
  href: https://artifacts.apis.io/xauconnect-com/vocabulary/xauconnect-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/xauconnect-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/xauconnect-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/xauconnect-com/changelog/xauconnect-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/xauconnect-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/xauconnect-com/authentication/xauconnect-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xauconnect-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/xauconnect-com/conformance/xauconnect-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xauconnect-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/xauconnect-com/llms/xauconnect-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xauconnect-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/xauconnect-com/well-known/xauconnect-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xauconnect-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/xauconnect-com/hosts/xauconnect-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xauconnect-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/xauconnect-com/vendors/xauconnect-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xauconnect-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xauconnect.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xauconnect.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://xauconnect.com/developers/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://xauconnect.com/developers/api
- group: auth
  href: https://artifacts.apis.io/xauconnect-com/security/xauconnect-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xauconnect-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xauconnect.com/
- group: docs
  title: ''
  type: Documentation
  url: https://xauconnect.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://xauconnect.com/learn
- group: company
  title: ''
  type: Blog
  url: https://xauconnect.com/learn
created: '2026-11-05'
description: XAUConnect is a platform that enables the launch of tokenized assets on the Solana blockchain using a Gold Curve bonding mechanism. Users can create and trade token pools with a minimum of 10 SOL or 750 USDC, after which the pool graduates into a locked market. The service offers a launchpad, swap, buy‑sell, liquidity, and discovery tools, targeting DeFi traders and projects seeking to bootstrap token liquidity on Solana. It emphasizes fast onboarding, automated market making, and integration with the broader Solana ecosystem.
image: https://xauconnect.com/brand/og-image.png?v=3
layout: provider
modified: '2026-11-05'
name: XAUConnect
nav: Providers
network: true
overview: 'XAUConnect publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Cross Chain API, Meta API, and 1 more. Tagged areas include Fintech, DeFi, Blockchain, Token Launch, and Solana.


  The XAUConnect catalog on APIs.io includes 1 Spectral governance ruleset.


  XAUConnect''s developer surface includes changelog, authentication, API reference, documentation, getting-started guide, engineering blog, and 15 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 2
  name: Xauconnect Com Rate Limits
  slug: xauconnect-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: XAUConnect API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: xauconnect-com-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 41.0
    developer_ergonomics: 49.3
    discoverability: 66.1
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Xauconnect Com Authentication
  slug: xauconnect-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Xauconnect Com Domain Security
  slug: xauconnect-com-domain-security
  summary_line: TLSv1.3
slug: xauconnect-com
tags:
- Fintech
- DeFi
- Blockchain
- Token Launch
- Solana
website: https://xauconnect.com/
---
