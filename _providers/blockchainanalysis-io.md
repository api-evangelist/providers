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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Compliance API providing wallet screening, KYT, and other crypto compliance checks.
  name: BlockchainAnalysis API
  slug: blockchainanalysis-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/blockchainanalysis-io/rate-limits/blockchainanalysis-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/blockchainanalysis-io-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/blockchainanalysis-io/changelog/blockchainanalysis-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/blockchainanalysis-io-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://blockchainanalysis.io/security-policy.txt
- group: auth
  href: https://artifacts.apis.io/blockchainanalysis-io/authentication/blockchainanalysis-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blockchainanalysis-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/blockchainanalysis-io/conformance/blockchainanalysis-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blockchainanalysis-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blockchainanalysis-io/llms/blockchainanalysis-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blockchainanalysis-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/blockchainanalysis-io/mcp/blockchainanalysis-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blockchainanalysis-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/blockchainanalysis-io/well-known/blockchainanalysis-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blockchainanalysis-io-security.txt
- group: agent
  href: https://artifacts.apis.io/blockchainanalysis-io/well-known/blockchainanalysis-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blockchainanalysis-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/blockchainanalysis-io/hosts/blockchainanalysis-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blockchainanalysis-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/blockchainanalysis-io/vendors/blockchainanalysis-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blockchainanalysis-io-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://blockchainanalysis.io/changelog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockchainanalysis.io/
- group: auth
  href: https://artifacts.apis.io/blockchainanalysis-io/security/blockchainanalysis-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blockchainanalysis-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blockchainanalysis-io/security/blockchainanalysis-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blockchainanalysis-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blockchainanalysis.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://blockchainanalysis.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://blockchainanalysis.io/docs/api-reference/endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://blockchainanalysis.io/docs/getting-started/quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://blockchainanalysis.io/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blockchainanalysis.io/privacy
- group: start
  title: ''
  type: SignUp
  url: https://blockchainanalysis.io/register
- group: operate
  title: ''
  type: Support
  url: https://support.blockchainanalysis.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blockchainanalysis.io/terms
created: '2026-11-02'
description: BlockchainAnalysis.io provides a digital asset compliance platform that screens wallets, analyzes exchange accounts, monitors transactions, and offers regulatory context across 34 jurisdictions and 54 blockchains. The service includes KYT, AML, KYB, name and entity screening, and AI‑powered risk analysis for businesses handling crypto assets.
image: https://blockchainanalysis.io/og-image.png?v=6
layout: provider
mcp_servers:
- description: Remote MCP server at blockchainanalysis.io.
  name: BlockchainAnalysis.io MCP Server
  slug: blockchainanalysis-io-mcp-yml
modified: '2026-11-02'
name: BlockchainAnalysis.io
nav: Providers
network: true
overview: 'BlockchainAnalysis.io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Compliance, Blockchain, AML, and Transaction Monitoring.


  BlockchainAnalysis.io''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Blockchainanalysis Io Plans Pricing
  plan_count: 0
  slug: blockchainanalysis-io-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 9
  name: Blockchainanalysis Io Rate Limits
  slug: blockchainanalysis-io-rate-limits
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 65.0
    operational_transparency: 44.7
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blockchainanalysis Io Authentication
  slug: blockchainanalysis-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Blockchainanalysis Io Domain Security
  slug: blockchainanalysis-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Blockchainanalysis Io Vulnerability Disclosure
  slug: blockchainanalysis-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: blockchainanalysis-io
tags:
- Company
- Compliance
- Blockchain
- AML
- Transaction Monitoring
website: https://blockchainanalysis.io/
---
