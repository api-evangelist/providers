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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.8
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bitcall Agentic Access
  operation_count: 1
  slug: bitcall-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Rent numbers and receive one-time passcodes via the Bitcall OTP API.
  name: OTP
  slug: otp
artifact_total: 6
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bitcall/refs/heads/main/agentic-access/bitcall-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bitcall-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bitcall/refs/heads/main/rate-limits/bitcall-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bitcall-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitcall/refs/heads/main/rules/bitcall-rules.yml
  title: ''
  type: Spectral
  url: rules/bitcall-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitcall/refs/heads/main/conventions/bitcall-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bitcall-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitcall/refs/heads/main/authentication/bitcall-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bitcall-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitcall/refs/heads/main/conformance/bitcall-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bitcall-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bitcall/refs/heads/main/llms/bitcall-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitcall-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitcall/refs/heads/main/hosts/bitcall-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitcall-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitcall/refs/heads/main/vendors/bitcall-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitcall-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitcall.io/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://bitcall.io/help-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitcall.io/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://panel.bitcall.io/en/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.bitcall.io
- group: company
  title: ''
  type: Blog
  url: https://bitcall.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bitcall.io/docs/quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitcall/refs/heads/main/security/bitcall-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitcall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitcall.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bitcall.io
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://bitcall.io
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Bitcall provides a self‑service telecom platform offering cheap international voice termination, virtual numbers, SMS OTP verification, eSIM data plans, HLR/number lookup and account balance services, all accessible via a unified API key. Users can rent numbers, send bulk SMS, obtain one‑time passcodes, and manage eSIM subscriptions through the Bitcall API gateway.
image: https://bitcall.io/images/og/bitcall-home-en.jpg
layout: provider
modified: '2026-10-03'
name: Bitcall
nav: Providers
network: true
overview: 'Bitcall publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, VoIP, SMS, and eSIM.


  The Bitcall catalog on APIs.io includes 1 Spectral governance ruleset.


  Bitcall''s developer surface includes authentication, support, engineering blog, getting-started guide, documentation, and 14 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 1
  name: Bitcall Rate Limits
  slug: bitcall-rate-limits
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Bitcall API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: bitcall-rules
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.5
    catalog_earned_first_party: 8.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 64.3
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 20.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bitcall Authentication
  slug: bitcall-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bitcall Domain Security
  slug: bitcall-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bitcall
tags:
- Telecommunications
- VoIP
- SMS
- eSIM
website: https://bitcall.io
---
