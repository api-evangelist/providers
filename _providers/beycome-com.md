---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API reference for Beycome platform
  name: Beycome API
  slug: beycome-api
- description: 'Beycome API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Beycome API
  slug: beycome-com-api
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/beycome-com/well-known/beycome-com-beycome-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beycome-com-beycome-security.txt
- group: design
  href: https://artifacts.apis.io/beycome-com/rules/beycome-com-rules.yml
  title: ''
  type: Spectral
  url: rules/beycome-com-rules.yml
- group: design
  href: https://artifacts.apis.io/beycome-com/vocabulary/beycome-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/beycome-com-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/beycome-com/security/beycome-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/beycome-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/beycome-com/conformance/beycome-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beycome-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/beycome-com/llms/beycome-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beycome-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/beycome-com/well-known/beycome-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beycome-com-www-security.txt
- group: auth
  href: https://artifacts.apis.io/beycome-com/well-known/beycome-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beycome-com-security.txt
- group: agent
  href: https://artifacts.apis.io/beycome-com/well-known/beycome-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beycome-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/beycome-com/hosts/beycome-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beycome-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/beycome-com/vendors/beycome-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beycome-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beycome.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beycome.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.beycome.com/press
- group: start
  title: ''
  type: Login
  url: https://www.beycome.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.beycome.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/beycome
- group: auth
  href: https://artifacts.apis.io/beycome-com/security/beycome-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/beycome-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/beycome-com/security/beycome-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beycome-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beycome.com/
coverage:
  checked: '2026-11-02'
  detail: OpenAPI endpoint requires authentication (401 response) and no public spec is available.
  evidence:
  - status: 401
    url: https://api.beycome.com/openapi
  - status: 401
    url: https://api.beycome.com/openapi.json
  reason: auth-required
  state: gated
created: '2026-11-02'
description: Beycome offers a flat-fee MLS platform that enables homeowners to list and sell their homes without traditional real‑estate agent commissions. For a $99 flat fee, sellers can list on the MLS, receive cash rebates when buying, and manage the entire transaction online, simplifying the process and saving thousands of dollars.
image: https://www.beycome.com/images/social/home2.jpg
layout: provider
modified: '2026-11-02'
name: Beycome
nav: Providers
network: true
overview: 'Beycome is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Fintech, Home Selling, and MLS.


  The Beycome catalog on APIs.io includes 1 Spectral governance ruleset.


  Beycome''s developer surface includes engineering blog and 19 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: Beycome API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: beycome-com-rules
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 1.2
    discoverability: 58.0
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
- kind: domain-security
  name: Beycome Com Domain Security
  slug: beycome-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Beycome Com Vulnerability Disclosure
  slug: beycome-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: beycome-com
tags:
- Company
- Real Estate
- Fintech
- Home Selling
- MLS
- FlatFee
website: https://beycome.com/
---
