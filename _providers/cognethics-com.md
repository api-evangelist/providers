---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public REST API for the Cognethics platform offering sandbox endpoints, MCP OAuth/API-key registration, and OpenID discovery.
  name: Cognethics Developer API
  slug: cognethics-developer-api
- baseURL: https://platform.cognethics.com
  baseurl_source: declared
  description: 'Public REST API for the Cognethics platform: developer sandbox endpoints, MCP OAuth/API-key registration, and OpenID discovery. Workspaces are provisioned for an identified principal — request one at '
  name: Cognethics Developer API .well-known API
  slug: cognethics-developer-api-well-known-api
artifact_total: 9
asyncapis:
- description: ''
  name: Cognethics Com Webhooks
  slug: cognethics-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/cognethics-com/rules/cognethics-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cognethics-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cognethics-com/vocabulary/cognethics-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cognethics-com-vocabulary.yml
- group: commercial
  href: https://artifacts.apis.io/cognethics-com/plans/cognethics-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cognethics-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cognethics-com/asyncapi/cognethics-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cognethics-com-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/cognethics-com/changelog/cognethics-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cognethics-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cognethics.com/trust/
- group: auth
  href: https://artifacts.apis.io/cognethics-com/authentication/cognethics-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cognethics-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/cognethics-com/errors/cognethics-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cognethics-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cognethics-com/conformance/cognethics-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cognethics-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cognethics-com/llms/cognethics-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cognethics-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/cognethics-com/well-known/cognethics-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cognethics-com-security.txt
- group: auth
  href: https://artifacts.apis.io/cognethics-com/well-known/cognethics-com-platform-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cognethics-com-platform-security.txt
- group: auth
  href: https://artifacts.apis.io/cognethics-com/well-known/cognethics-com-developers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cognethics-com-developers-security.txt
- group: agent
  href: https://artifacts.apis.io/cognethics-com/well-known/cognethics-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cognethics-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cognethics-com/hosts/cognethics-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cognethics-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cognethics-com/vendors/cognethics-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cognethics-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cognethics.com/terms
- group: auth
  title: ''
  type: Security
  url: https://cognethics.com/products/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cognethics.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cognethics.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cognethics.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cognethics.com/quickstart/mcp/
- group: auth
  href: https://artifacts.apis.io/cognethics-com/security/cognethics-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cognethics-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cognethics-com/security/cognethics-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cognethics-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cognethics-com/security/cognethics-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cognethics-com-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://cognethics.com/platform/
- group: company
  title: ''
  type: Website
  url: https://cognethics.com/
created: '2026-11-04'
description: Cognethics provides a governed agent‑run enterprise operating system that centralises a company’s knowledge and decision‑making. It offers a single source of truth where one employee with perfect memory and sound judgment can feed the whole organisation, enabling agents to answer queries with source‑linked evidence. The platform emphasizes security, privacy, and compliance, targeting enterprises seeking AI‑augmented operations.
image: https://cognethics.com/og-cognethics.png
layout: provider
modified: '2026-11-04'
name: Cognethics
nav: Providers
network: true
overview: 'Cognethics publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Developer API .well-known API, and 1 more. Tagged areas include Enterprise, Artificial Intelligence, Knowledge Management, Security, and Compliance.


  The Cognethics catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Cognethics'' developer surface includes changelog, authentication, pricing, getting-started guide, documentation, and 22 more developer resources.'
plans:
- name: Cognethics Com Plans Pricing
  plan_count: 3
  slug: cognethics-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Cognethics API Rules
  rule_count: 63
  severity_counts:
    error: 61
    hint: 0
    info: 1
    warn: 1
  slug: cognethics-com-rules
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 35.6
    contract_quality: 59.5
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 34.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cognethics Com Authentication
  slug: cognethics-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Cognethics Com Domain Security
  slug: cognethics-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cognethics Com Vulnerability Disclosure
  slug: cognethics-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cognethics Com Trust Center
  slug: cognethics-com-trust-center
  summary_line: HIPAA, GDPR
slug: cognethics-com
tags:
- Enterprise
- Artificial Intelligence
- Knowledge Management
- Security
- Compliance
website: https://cognethics.com/
---
