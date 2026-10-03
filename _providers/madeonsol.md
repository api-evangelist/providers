---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.7
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Madeonsol Agentic Access
  operation_count: 35
  slug: madeonsol-agentic-access
  summary_line: 35 operations
api_count: 1
apis:
- description: Pay-per-call on-chain intelligence API for Solana and Robinhood Chain, providing KOL signals, feeds, leaderboards, and token analytics.
  name: MadeOnSol API
  slug: madeonsol-api
- baseURL: https://madeonsol.com
  baseurl_source: spec
  description: The Robinhood Chain API from MadeOnSol — 10 operation(s) for robinhood chain.
  name: MadeOnSol Robinhood Chain API
  slug: madeonsol-robinhood-chain-api
- baseURL: https://madeonsol.com
  baseurl_source: spec
  description: The Solana API from MadeOnSol — 25 operation(s) for solana.
  name: MadeOnSol Solana API
  slug: madeonsol-solana-api
artifact_total: 10
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/agentic-access/madeonsol-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/madeonsol-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/plans/madeonsol-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/madeonsol-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/rules/madeonsol-rules.yml
  title: ''
  type: Spectral
  url: rules/madeonsol-rules.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/cli/madeonsol-cli.yml
  title: ''
  type: CLI
  url: cli/madeonsol-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/changelog/madeonsol-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/madeonsol-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/conventions/madeonsol-conventions.yml
  title: ''
  type: Conventions
  url: conventions/madeonsol-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://madeonsol.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/authentication/madeonsol-authentication.yml
  title: ''
  type: Authentication
  url: authentication/madeonsol-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/errors/madeonsol-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/madeonsol-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/conformance/madeonsol-conformance.yml
  title: ''
  type: Conformance
  url: conformance/madeonsol-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/llms/madeonsol-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/madeonsol-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/well-known/madeonsol-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/madeonsol-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/well-known/madeonsol-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/madeonsol-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/hosts/madeonsol-hosts.yml
  title: ''
  type: Hosts
  url: hosts/madeonsol-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/vendors/madeonsol-vendors.yml
  title: ''
  type: Vendors
  url: vendors/madeonsol-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/packages/madeonsol-packages.yml
  title: ''
  type: Packages
  url: packages/madeonsol-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://madeonsol.com/status
- group: auth
  title: ''
  type: Security
  url: https://madeonsol.com/security
- group: build
  title: ''
  type: SDKs
  url: https://madeonsol.com/best/sdks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/madeonsol
- group: start
  title: ''
  type: DeveloperPortal
  url: https://madeonsol.com/developer
- group: operate
  title: ''
  type: ChangeLog
  url: https://madeonsol.com/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/security/madeonsol-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/madeonsol-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/security/madeonsol-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/madeonsol-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/madeonsol/refs/heads/main/security/madeonsol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/madeonsol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://madeonsol.com
- group: docs
  title: ''
  type: Documentation
  url: https://madeonsol.com/api-docs
- group: operate
  title: ''
  type: Support
  url: https://madeonsol.com/about
- group: company
  title: ''
  type: Blog
  url: https://madeonsol.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://madeonsol.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://madeonsol.com/auth/login?next=%2F
- group: commercial
  title: ''
  type: TermsOfService
  url: https://madeonsol.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://madeonsol.com/privacy
created: '2026-09-28'
description: MadeOnSol provides on-chain intelligence APIs for Solana and Robinhood Chain, offering real-time KOL wallet tracking, deployer reputation scoring, and all-DEX trade streams. It also hosts a directory of tools and a developer API with SDKs and a pay-per-call x402 model.
image: https://madeonsol.com/opengraph-image?v=3
layout: provider
modified: '2026-09-28'
name: MadeOnSol
nav: Providers
network: true
overview: 'MadeOnSol publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Robinhood Chain API, Solana API, and 1 more. Tagged areas include Blockchain, Analytics, Solana, and Robinhood Chain.


  The MadeOnSol catalog on APIs.io includes 1 Spectral governance ruleset.


  MadeOnSol''s developer surface includes CLI, changelog, authentication, documentation, support, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Madeonsol Plans Pricing
  plan_count: 5
  slug: madeonsol-plans-pricing
random_paper: 16
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: MadeOnSol API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: madeonsol-rules
score:
  band: strong
  composite: 56.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.8
    catalog_earned_first_party: 12.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 15.9
    contract_quality: 44.9
    developer_ergonomics: 52.4
    discoverability: 55.4
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Madeonsol Authentication
  slug: madeonsol-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Madeonsol Domain Security
  slug: madeonsol-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Madeonsol Vulnerability Disclosure
  slug: madeonsol-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Madeonsol Trust Center
  slug: madeonsol-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: madeonsol
tags:
- Blockchain
- Analytics
- Solana
- Robinhood Chain
website: https://madeonsol.com
---
