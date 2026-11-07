---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Razi Pro Agentic Access
  operation_count: 1
  slug: razi-pro-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Executable developer tools over HTTP. No API key is required; an API key raises rate limits and attributes usage.
  name: razi.pro Tools API
  slug: razi-pro-tools-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/razi-pro/well-known/razi-pro-blog-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/razi-pro-blog-security.txt
- group: agent
  href: https://artifacts.apis.io/razi-pro/agentic-access/razi-pro-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/razi-pro-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/razi-pro/rules/razi-pro-rules.yml
  title: ''
  type: Spectral
  url: rules/razi-pro-rules.yml
- group: auth
  title: ''
  type: Security
  url: https://www.razi.pro/terms-and-conditions
- group: auth
  href: https://artifacts.apis.io/razi-pro/authentication/razi-pro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/razi-pro-authentication.yml
- group: design
  href: https://artifacts.apis.io/razi-pro/errors/razi-pro-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/razi-pro-problem-types.yml
- group: design
  href: https://artifacts.apis.io/razi-pro/conformance/razi-pro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/razi-pro-conformance.yml
- group: agent
  href: https://artifacts.apis.io/razi-pro/llms/razi-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/razi-pro-llms.txt
- group: auth
  href: https://artifacts.apis.io/razi-pro/well-known/razi-pro-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/razi-pro-security.txt
- group: auth
  href: https://artifacts.apis.io/razi-pro/well-known/razi-pro-razi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/razi-pro-razi-security.txt
- group: agent
  href: https://artifacts.apis.io/razi-pro/well-known/razi-pro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/razi-pro-well-known.yml
- group: other
  href: https://artifacts.apis.io/razi-pro/hosts/razi-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/razi-pro-hosts.yml
- group: other
  href: https://artifacts.apis.io/razi-pro/vendors/razi-pro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/razi-pro-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.razi.pro/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.razi.pro/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.razi.pro/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/razikallayi
- group: docs
  title: ''
  type: Documentation
  url: https://www.razi.pro/tools/docs
- group: company
  title: ''
  type: Blog
  url: https://blog.razi.pro/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.razi.pro/help/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://www.razi.pro/developer
- group: auth
  href: https://artifacts.apis.io/razi-pro/security/razi-pro-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/razi-pro-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/razi-pro/security/razi-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/razi-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://razi.pro/
created: '2026-10-29'
description: Razi.pro offers a collection of free developer tools, technical deep‑dives, curated resources, and a weekly newsletter for builders, creators, and developers. The site provides video tutorials, AI tool listings, SEO utilities, and a tech blog covering a wide range of programming topics, aiming to empower the developer community with accessible, high‑quality content and tools.
image: https://www.razi.pro/og-image.jpg
layout: provider
modified: '2026-10-29'
name: razi-pro
nav: Providers
network: true
overview: 'razi-pro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, Tech Blog, Free Resources, Community, and AI Tools.


  The razi-pro catalog on APIs.io includes 1 Spectral governance ruleset.


  razi-pro''s developer surface includes authentication, support, documentation, engineering blog, getting-started guide, API reference, and 19 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: razi-pro API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: razi-pro-rules
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 32.1
    discoverability: 73.2
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.6
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/razi-pro/razi-pro-2026-11-03T141956.png
security:
- kind: authentication
  name: Razi Pro Authentication
  slug: razi-pro-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Razi Pro Domain Security
  slug: razi-pro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Razi Pro Vulnerability Disclosure
  slug: razi-pro-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: razi-pro
tags:
- Developer Tools
- Tech Blog
- Free Resources
- Community
- AI Tools
website: https://razi.pro/
---
