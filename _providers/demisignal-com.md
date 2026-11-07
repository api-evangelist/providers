---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Free HTTP API documented on the DemiSignal MCP server page; GET /api/v1/check?domain= returns as JSON the same email-authentication check as the check_domain MCP tool (DMARC, SPF, DKIM, MX, BIMI and M
  name: DemiSignal Check API
  slug: demisignal-check-api
- description: 'Remote MCP server over streamable HTTP at https://demisignal.com/mcp with three read-only tools (check_domain, generate_spf_record, generate_dmarc_record); usable with no account, or with a free dsk_ '
  name: DemiSignal MCP Server
  slug: demisignal-mcp-server
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/demisignal-com/rate-limits/demisignal-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/demisignal-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/demisignal-com/plans/demisignal-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/demisignal-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/demisignal-com/conventions/demisignal-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/demisignal-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/demisignal-com/authentication/demisignal-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/demisignal-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/demisignal-com/lifecycle/demisignal-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/demisignal-com-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/demisignal-com/mcp/demisignal-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/demisignal-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/demisignal-com/well-known/demisignal-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/demisignal-com-security.txt
- group: agent
  href: https://artifacts.apis.io/demisignal-com/well-known/demisignal-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/demisignal-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/demisignal-com/hosts/demisignal-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/demisignal-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/demisignal-com/vendors/demisignal-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/demisignal-com-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://demisignal.com/guides/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://demisignal.com/guides/providers
- group: auth
  href: https://artifacts.apis.io/demisignal-com/security/demisignal-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/demisignal-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/demisignal-com/security/demisignal-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/demisignal-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://demisignal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://demisignal.com/guides
- group: commercial
  title: ''
  type: Pricing
  url: https://demisignal.com/pricing
- group: start
  title: ''
  type: Login
  url: https://demisignal.com/auth/login
- group: operate
  title: ''
  type: Support
  url: https://demisignal.com/contact
- group: auth
  title: ''
  type: Security
  url: https://demisignal.com/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://demisignal.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://demisignal.com/legal/privacy
created: '2026-11-05'
description: DemiSignal (operated by Demi Solutions OÜ) is an email-authentication checking and monitoring service at demisignal.com. It runs free scans of a domain's published SPF, DKIM, DMARC, MX, BIMI and MTA-STS records, offers free SPF/DMARC/DKIM generators, an SPF flattener and a DMARC report analyzer, and sells paid plans (Starter, Pro, Agency) that collect DMARC aggregate reports to show sending sources, authentication results and change alerts. It also publishes a remote MCP server (com.demisignal/mcp in the MCP registry) so AI assistants can check domains and generate records.
examples:
- key_count: 1
  name: Demisignal Com Check Unauthenticated 401
  slug: demisignal-com-check-unauthenticated-401
image: https://demisignal.com/social/demisignal-og.png?v=7a76ed9752f9
json_schemas:
- name: check_domain input
  property_count: 2
  slug: demisignal-com-check-domain-input
- name: check_domain output
  property_count: 10
  slug: demisignal-com-check-domain-output
- name: generate_dmarc_record input
  property_count: 6
  slug: demisignal-com-generate-dmarc-record-input
- name: generate_dmarc_record output
  property_count: 4
  slug: demisignal-com-generate-dmarc-record-output
- name: generate_spf_record input
  property_count: 7
  slug: demisignal-com-generate-spf-record-input
- name: generate_spf_record output
  property_count: 6
  slug: demisignal-com-generate-spf-record-output
layout: provider
mcp_servers:
- description: 'Email authentication tools for a domain. check_domain looks up the domain''s live DNS and grades its DMARC, SPF, DKIM, MX, BIMI and MTA-STS records. generate_spf_record and generate_dmarc_record build '
  name: DemiSignal MCP Server
  slug: demisignal-mcp-server
modified: '2026-11-05'
name: DemiSignal
nav: Providers
network: true
overview: 'DemiSignal is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email Authentication, DMARC, SPF, and DKIM.


  DemiSignal''s developer surface includes authentication, API reference, getting-started guide, documentation, pricing, support, and 16 more developer resources.'
plans:
- name: Demisignal Com Plans Pricing
  plan_count: 4
  slug: demisignal-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Demisignal Com Rate Limits
  slug: demisignal-com-rate-limits
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 65.0
    operational_transparency: 31.6
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Demisignal Com Authentication
  slug: demisignal-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Demisignal Com Domain Security
  slug: demisignal-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Demisignal Com Vulnerability Disclosure
  slug: demisignal-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: demisignal-com
tags:
- Company
- Email Authentication
- DMARC
- SPF
- DKIM
- Email Security
- DNS
- Domain Monitoring
- MCP
website: https://demisignal.com/
---
