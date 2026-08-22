---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Documented, versioned REST API (/api/v1/*) for checking IPs, retrieving blacklist feeds and report history, and submitting abuse reports. Uses X-Secret-Token header authentication with role-based rate
  name: SniffCat REST API
  slug: sniffcat-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sniffcat-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sniffcat-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sniffcat.com/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://sniffcat.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://sniffcat.com/documentation/api
- group: start
  title: ''
  type: GettingStarted
  url: https://sniffcat.com/documentation/api
- group: operate
  title: ''
  type: Support
  url: https://sniffcat.com/tickets
- group: operate
  title: ''
  type: HelpCenter
  url: https://discord.gg/S7NDzCzQTg
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SniffCatDB
- group: start
  title: ''
  type: SignUp
  url: https://sniffcat.com/register
- group: start
  title: ''
  type: Login
  url: https://sniffcat.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sniffcat.com/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sniffcat.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sniffcat-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sniffcat-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sniffcat-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sniffcat-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sniffcat-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sniffcat-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/sniffcat-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sniffcat-packages.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sniffcat-report-categories.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sniffcat-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sniffcat-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sniffcat-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sniffcat-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sniffcat-security.txt
- group: auth
  title: ''
  type: Security
  url: security/sniffcat-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sniffcat-llms.txt
created: '2026-08-19'
description: 'SniffCat is a privacy-focused IP abuse database and OSINT threat-intelligence platform built by Polish developer Sefinek, positioned as a community-moderated AbuseIPDB alternative. Sysadmins, hosting providers, ISPs and security researchers report malicious IP addresses against a published 27-term abuse-category vocabulary, and consume the resulting reputation data through a free, versioned REST API at api.sniffcat.com: abuse-confidence lookups, per-IP report history, and score-ordered blocklist feeds in JSON or plain text for direct firewall ingestion. Entitlement is role-based rather than paid, with published daily quotas per operation and trust levels that weight how much each reporter moves an IP''s score. The platform is in Early Access / open beta and publishes no machine-readable contract.'
image: https://sniffcat.com/images/og-preview.jpg
layout: provider
modified: '2026-08-19'
name: SniffCat
nav: Providers
network: true
overview: 'SniffCat publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include threat-intelligence, ip-reputation, abuse-database, cybersecurity, and osint.


  SniffCat''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, sandbox, and 22 more developer resources.'
plans:
- name: Sniffcat Plans Pricing
  plan_count: 0
  slug: sniffcat-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 11
  name: Sniffcat Rate Limits
  slug: sniffcat-rate-limits
score:
  band: thin
  composite: 36.7
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 19.7
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 19.7
    operational_transparency: 63.2
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: authentication
  name: Sniffcat Authentication
  slug: sniffcat-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sniffcat Domain Security
  slug: sniffcat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sniffcat Vulnerability Disclosure
  slug: sniffcat-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sniffcat
tags:
- threat-intelligence
- ip-reputation
- abuse-database
- cybersecurity
- osint
- network-security
- sysadmin-tools
- blocklist
- abuse-reporting
- ip-blocklist
- ip-intelligence
- threat-feeds
website: https://sniffcat.com/documentation
---
