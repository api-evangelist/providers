---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 73
  human_in_the_loop: 2
  name: Short Io Agentic Access
  operation_count: 106
  slug: short-io-agentic-access
  summary_line: 106 operations · 73 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.short.io
  baseurl_source: declared
  description: The Audit API from Short.io — 1 operation(s) for audit.
  name: Short.io Audit API
  slug: short-io-audit-api
- baseURL: https://api.short.io
  baseurl_source: declared
  description: The Domain DNS API from Short.io — 1 operation(s) for domain dns.
  name: Short.io Domain DNS API
  slug: short-io-domain-dns-api
- baseURL: https://api.short.io
  baseurl_source: declared
  description: The Domains API from Short.io — 18 operation(s) for domains.
  name: Short.io Domains API
  slug: short-io-domains-api
- baseURL: https://api.short.io
  baseurl_source: declared
  description: The Link Bundles API from Short.io — 7 operation(s) for link bundles.
  name: Short.io Link Bundles API
  slug: short-io-link-bundles-api
- baseURL: https://api.short.io
  baseurl_source: declared
  description: The Link Duplication API from Short.io — 1 operation(s) for link duplication.
  name: Short.io Link Duplication API
  slug: short-io-link-duplication-api
- baseURL: https://api.short.io
  baseurl_source: declared
  description: The Link Management API from Short.io — 25 operation(s) for link management.
  name: Short.io Link Management API
  slug: short-io-link-management-api
- baseURL: https://api.short.io
  baseurl_source: declared
  description: The Link queries API from Short.io — 11 operation(s) for link queries.
  name: Short.io Link queries API
  slug: short-io-link-queries-api
- baseURL: https://api.short.io
  baseurl_source: declared
  description: The Link Targeting API from Short.io — 7 operation(s) for link targeting.
  name: Short.io Link Targeting API
  slug: short-io-link-targeting-api
- baseURL: https://api.short.io
  baseurl_source: declared
  description: The Organizations API from Short.io — 1 operation(s) for organizations.
  name: Short.io Organizations API
  slug: short-io-organizations-api
- baseURL: https://api.short.io
  baseurl_source: declared
  description: The Posts API from Short.io — 3 operation(s) for posts.
  name: Short.io Posts API
  slug: short-io-posts-api
- baseURL: https://api.short.io
  baseurl_source: declared
  description: The QR Codes API from Short.io — 4 operation(s) for qr codes.
  name: Short.io QR Codes API
  slug: short-io-qr-codes-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/short-io/agentic-access/short-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/short-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/short-io/plans/short-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/short-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/short-io/rules/short-io-rules.yml
  title: ''
  type: Spectral
  url: rules/short-io-rules.yml
- group: design
  href: https://artifacts.apis.io/short-io/vocabulary/short-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/short-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/short-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/short-io/changelog/short-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/short-io-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.short.io/
- group: auth
  href: https://artifacts.apis.io/short-io/security/short-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/short-io-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/short-io/errors/short-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/short-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/short-io/conformance/short-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/short-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/short-io/llms/short-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/short-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/short-io/well-known/short-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/short-io-security.txt
- group: agent
  href: https://artifacts.apis.io/short-io/well-known/short-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/short-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/short-io/hosts/short-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/short-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/short-io/vendors/short-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/short-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/short-io/packages/short-io-packages.yml
  title: ''
  type: SDKs
  url: packages/short-io-packages.yml
- group: build
  href: https://artifacts.apis.io/short-io/packages/short-io-packages.yml
  title: ''
  type: Packages
  url: packages/short-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://short.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://short.io/privacy
- group: start
  title: ''
  type: Login
  url: https://app.short.io/public/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.short.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.short.io/changelog
- group: auth
  href: https://artifacts.apis.io/short-io/authentication/short-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/short-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/short-io/security/short-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/short-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/short-io/security/short-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/short-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/short-io/security/short-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/short-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://short.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.short.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.short.io/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.short.io/category/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://short.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.short.io
created: '2026-10-26'
description: Short.io provides a URL shortening platform with custom domains, detailed analytics, QR code generation, and deep link debugging. It serves businesses and developers with integrations, enterprise features, and a robust API for creating, managing, and tracking short links across multiple domains and campaigns.
image: https://short.io/images/og-image-default.png
layout: provider
modified: '2026-10-26'
name: Short.io
nav: Providers
network: true
overview: 'Short.io publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit API, Domain DNS API, Domains API, and 8 more. Tagged areas include URL-shortening, Analytics, QR-codes, Enterprise, and Integrations.


  The Short.io catalog on APIs.io includes 1 Spectral governance ruleset.


  Short.io''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 25 more developer resources.'
plans:
- name: Short Io Plans Pricing
  plan_count: 5
  slug: short-io-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Short.io API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 3
  slug: short-io-rules
score:
  band: strong
  composite: 58.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 47.0
    developer_ergonomics: 61.3
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Short Io Authentication
  slug: short-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Short Io Domain Security
  slug: short-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Short Io Vulnerability Disclosure
  slug: short-io-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Short Io Trust Center
  slug: short-io-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 4
skills:
- name: short-io-create-bundle-with-links
  slug: short-io-create-bundle-with-links
- name: short-io-create-link-and-qr
  slug: short-io-create-link-and-qr
- name: short-io-link-targeting-setup
  slug: short-io-link-targeting-setup
- name: short-io-qr-code-link-management
  slug: short-io-qr-code-link-management
slug: short-io
tags:
- URL-shortening
- Analytics
- QR-codes
- Enterprise
- Integrations
website: https://short.io/
---
