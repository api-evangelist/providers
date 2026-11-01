---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Duo provides cloud-based multi-factor authentication and identity security solutions.
  name: Duo API
  slug: duo-api
artifact_total: 8
common:
- group: operate
  href: https://artifacts.apis.io/duo/rate-limits/duo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/duo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/duo/plans/duo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/duo-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/duo/rules/duo-rules.yml
  title: ''
  type: Spectral
  url: rules/duo-rules.yml
- group: design
  href: https://artifacts.apis.io/duo/json-ld/duo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/duo-context.jsonld
- group: design
  href: https://artifacts.apis.io/duo/vocabulary/duo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/duo-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/duo/data-model/duo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/duo-data-model.yml
- group: operate
  href: https://artifacts.apis.io/duo/changelog/duo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/duo-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://duo.com/support/security-and-reliability
- group: auth
  title: ''
  type: Security
  url: https://duo.com/about/security-and-reliability/security-response
- group: operate
  href: https://artifacts.apis.io/duo/lifecycle/duo-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/duo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/duo/lifecycle/duo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/duo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/duo/conformance/duo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/duo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/duo/llms/duo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/duo-llms.txt
- group: auth
  href: https://artifacts.apis.io/duo/well-known/duo-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/duo-status-security.txt
- group: auth
  href: https://artifacts.apis.io/duo/well-known/duo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/duo-security.txt
- group: agent
  href: https://artifacts.apis.io/duo/well-known/duo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/duo-well-known.yml
- group: other
  href: https://artifacts.apis.io/duo/hosts/duo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/duo-hosts.yml
- group: other
  href: https://artifacts.apis.io/duo/vendors/duo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/duo-vendors.yml
- group: build
  href: https://artifacts.apis.io/duo/packages/duo-packages.yml
  title: ''
  type: SDKs
  url: packages/duo-packages.yml
- group: build
  href: https://artifacts.apis.io/duo/packages/duo-packages.yml
  title: ''
  type: Packages
  url: packages/duo-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.duo.com/
- group: start
  title: ''
  type: SignUp
  url: https://signup.duo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ecosystem.duo.com/onboarding/developer
- group: auth
  href: https://artifacts.apis.io/duo/security/duo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/duo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/duo/security/duo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/duo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/duo/security/duo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/duo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://duo.com
- group: docs
  title: ''
  type: Documentation
  url: https://duo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://duo.com/docs/authapi
- group: start
  title: ''
  type: GettingStarted
  url: https://duo.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.duo.com
- group: company
  title: ''
  type: Blog
  url: https://duo.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/duosecurity
- group: commercial
  title: ''
  type: Pricing
  url: https://duo.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://duo.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://duo.com/privacy
coverage:
  checked: '2026-10-25'
  detail: Docs site https://docs.duo.com returns no machine-readable spec and appears to be JavaScript-rendered.
  evidence:
  - status: null
    url: https://docs.duo.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Duo provides cloud-based multi-factor authentication and identity security solutions, helping organizations protect access to applications and data. Their platform offers MFA, single sign‑on, device trust, passwordless login, and security intelligence, serving enterprises, SMBs, government, and MSPs worldwide. Duo’s services include a robust admin console, detailed reporting, and integrations with thousands of applications, enabling secure, seamless user experiences across on‑premises and cloud environments.
image: https://duo.com/assets/img/seo-images/social-share-home.jpg
jsonld:
- class_count: 7
  name: Duo Context
  property_count: 18
  slug: duo-context
layout: provider
modified: '2026-10-24'
name: Duo
nav: Providers
network: true
overview: 'Duo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Multi-Factor Authentication, Identity Management, Cloud Services, and Enterprise.


  The Duo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Duo''s developer surface includes changelog, signup flow, documentation, API reference, getting-started guide, support, engineering blog, and 29 more developer resources.'
plans:
- name: Duo Plans Pricing
  plan_count: 4
  slug: duo-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Duo Rate Limits
  slug: duo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Duo API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: duo-rules
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 68.8
    catalog_earned_first_party: 20.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 16.3
    developer_ergonomics: 52.4
    discoverability: 57.1
    operational_transparency: 76.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
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
- kind: domain-security
  name: Duo Domain Security
  slug: duo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Duo Vulnerability Disclosure
  slug: duo-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Duo Trust Center
  slug: duo-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: duo
tags:
- Security
- Multi-Factor Authentication
- Identity Management
- Cloud Services
- Enterprise
website: https://duo.com
---
