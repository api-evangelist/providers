---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.1
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Beenverified Agentic Access
  operation_count: 2
  slug: beenverified-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.beenverified.com
  baseurl_source: declared
  description: The append API from Beenverified — 1 operation(s) for append.
  name: Beenverified Append API
  slug: beenverified-append-api
- baseURL: https://api.beenverified.com
  baseurl_source: declared
  description: The append_sandbox API from Beenverified — 1 operation(s) for append_sandbox.
  name: Beenverified Append Sandbox API
  slug: beenverified-append-sandbox-api
artifact_total: 6
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beenverified/refs/heads/main/agentic-access/beenverified-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/beenverified-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beenverified/refs/heads/main/rules/beenverified-rules.yml
  title: ''
  type: Spectral
  url: rules/beenverified-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beenverified/refs/heads/main/errors/beenverified-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beenverified-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beenverified/refs/heads/main/conformance/beenverified-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beenverified-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beenverified/refs/heads/main/well-known/beenverified-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beenverified-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beenverified/refs/heads/main/well-known/beenverified-business-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beenverified-business-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beenverified/refs/heads/main/well-known/beenverified-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beenverified-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beenverified/refs/heads/main/hosts/beenverified-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beenverified-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beenverified/refs/heads/main/vendors/beenverified-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beenverified-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beenverified.com/faq/terms-conditions/
- group: auth
  title: ''
  type: Security
  url: https://www.beenverified.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beenverified.com/faq/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.beenverified.com/press/
- group: start
  title: ''
  type: Login
  url: https://www.beenverified.com/login
- group: other
  title: ''
  type: Leadership
  url: https://www.beenverified.com/about/leadership/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.beenverified.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beenverified/refs/heads/main/security/beenverified-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/beenverified-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beenverified/refs/heads/main/security/beenverified-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beenverified-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.beenverified.com
- group: operate
  title: ''
  type: Support
  url: https://support.beenverified.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.beenverified.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.beenverified.com/articles/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://support.beenverified.com/mcp
  - status: 403
    url: https://apidocs.beenverified.com/mcp
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: BeenVerified provides a consumer‑focused platform that aggregates public records, people search, reverse phone lookup, email lookup, address lookup, vehicle lookup, and other background‑check services. Users can access a wide range of data sources to verify identities, locate individuals, and obtain contact information, all through a web interface and mobile apps. The service emphasizes ease of use, comprehensive coverage, and compliance with privacy regulations.
layout: provider
modified: '2026-09-27'
name: Beenverified
nav: Providers
network: true
overview: 'Beenverified publishes 2 APIs on the [APIs.io](https://apis.io/) network: Append API and Append Sandbox API. Tagged areas include Company, Background Checks, People Search, Data API, and Consumer Services.


  The Beenverified catalog on APIs.io includes 1 Spectral governance ruleset.


  Beenverified''s developer surface includes API reference, support, pricing, engineering blog, and 18 more developer resources.'
random_paper: 2
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Beenverified API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: beenverified-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 45.9
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 10.5
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
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Beenverified Domain Security
  slug: beenverified-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Beenverified Vulnerability Disclosure
  slug: beenverified-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: beenverified
tags:
- Company
- Background Checks
- People Search
- Data API
- Consumer Services
website: https://www.beenverified.com
---
