---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: documented
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Beta documentation for the kvCORE Public API V2, which is currently invite‑only for partners.
  name: kvCORE Public API V2
  slug: kvcore-public-api-v2
- description: 'Inside Real Estate (kvCORE / BoldTrail) API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Inside Real Estate (kvCORE / BoldTrail) API
  slug: kvcore-api
artifact_total: 9
common:
- group: auth
  href: https://artifacts.apis.io/kvcore/well-known/kvcore-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kvcore-status-security.txt
- group: design
  href: https://artifacts.apis.io/kvcore/rules/kvcore-rules.yml
  title: ''
  type: Spectral
  url: rules/kvcore-rules.yml
- group: design
  href: https://artifacts.apis.io/kvcore/json-ld/kvcore-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kvcore-context.jsonld
- group: design
  href: https://artifacts.apis.io/kvcore/vocabulary/kvcore-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kvcore-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/kvcore/data-model/kvcore-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kvcore-data-model.yml
- group: auth
  href: https://artifacts.apis.io/kvcore/security/kvcore-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/kvcore-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kvcore/authentication/kvcore-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kvcore-authentication.yml
- group: design
  href: https://artifacts.apis.io/kvcore/errors/kvcore-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kvcore-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kvcore/conformance/kvcore-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kvcore-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kvcore/llms/kvcore-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kvcore-llms.txt
- group: auth
  href: https://artifacts.apis.io/kvcore/well-known/kvcore-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kvcore-support-security.txt
- group: auth
  href: https://artifacts.apis.io/kvcore/well-known/kvcore-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kvcore-help-security.txt
- group: agent
  href: https://artifacts.apis.io/kvcore/well-known/kvcore-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kvcore-well-known.yml
- group: other
  href: https://artifacts.apis.io/kvcore/hosts/kvcore-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kvcore-hosts.yml
- group: other
  href: https://artifacts.apis.io/kvcore/vendors/kvcore-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kvcore-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.insiderealestate.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.insiderealestate.com/en/articles/8723046-getting-started-with-boldtrail-recruit
- group: docs
  title: ''
  type: Documentation
  url: https://developer.insiderealestate.com/
- group: auth
  href: https://artifacts.apis.io/kvcore/security/kvcore-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kvcore-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kvcore/security/kvcore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kvcore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://insiderealestate.com/
- group: operate
  title: ''
  type: Support
  url: https://insiderealestate.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://insiderealestate.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://insiderealestate.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://resources.insiderealestate.com/press-releases
- group: start
  title: ''
  type: SignUp
  url: http://app.boldtrail.com
coverage:
  checked: '2026-10-28'
  detail: API documentation indicates the kvCORE Public API is invite‑only for partners and not publicly accessible.
  evidence:
  - status: 200
    url: https://developer.insiderealestate.com/boldtrail-api-docs/docs/request-access
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Inside Real Estate (kvCORE / BoldTrail) provides an all‑in‑one technology platform for real‑estate brokerages, agents, and teams. It offers a suite of SaaS tools—including lead generation, CRM, marketing automation, and transaction management—to help businesses grow, improve efficiency, and stay competitive. The company emphasizes continuous innovation, integration across its BoldTrail products, and support for over 400,000 users.
image: https://insiderealestate.com/wp-content/uploads/2025/01/ire-corp-header-img.webp
json_schemas:
- name: PostWebhooktestRequest
  property_count: 3
  slug: kvcore-post-webhooktest-request
jsonld:
- class_count: 1
  name: Kvcore Context
  property_count: 3
  slug: kvcore-context
layout: provider
modified: '2026-10-28'
name: Inside Real Estate (kvCORE / BoldTrail)
nav: Providers
network: true
overview: 'Inside Real Estate (kvCORE / BoldTrail) is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Software-as-a-Service, CRM, and Lead Generation.


  The Inside Real Estate (kvCORE / BoldTrail) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Inside Real Estate (kvCORE / BoldTrail)''s developer surface includes authentication, getting-started guide, documentation, support, engineering blog, signup flow, and 20 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: Inside Real Estate (kvCORE / BoldTrail) API Rules
  rule_count: 28
  severity_counts:
    error: 26
    hint: 0
    info: 1
    warn: 1
  slug: kvcore-rules
scopes:
- name: Kvcore Scopes
  scope_count: 0
  slug: kvcore-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 17.1
    contract_governance: 35.6
    contract_quality: 16.5
    developer_ergonomics: 26.2
    discoverability: 64.3
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 36.2
  provenance:
    conformance: first-party
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
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kvcore/kvcore-2026-11-03T134609.png
security:
- kind: authentication
  name: Kvcore Authentication
  slug: kvcore-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Kvcore Domain Security
  slug: kvcore-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Kvcore Vulnerability Disclosure
  slug: kvcore-vulnerability-disclosure
  summary_line: no policy recorded
slug: kvcore
tags:
- Company
- Real Estate
- Software-as-a-Service
- CRM
- Lead Generation
- Marketing Automation
website: https://insiderealestate.com/
---
