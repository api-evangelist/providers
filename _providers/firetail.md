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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'FireTail API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: FireTail API
  slug: firetail-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/firetail/rules/firetail-rules.yml
  title: ''
  type: Spectral
  url: rules/firetail-rules.yml
- group: design
  href: https://artifacts.apis.io/firetail/json-ld/firetail-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/firetail-context.jsonld
- group: design
  href: https://artifacts.apis.io/firetail/vocabulary/firetail-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/firetail-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/firetail/data-model/firetail-data-model.yml
  title: ''
  type: DataModel
  url: data-model/firetail-data-model.yml
- group: design
  href: https://artifacts.apis.io/firetail/conventions/firetail-conventions.yml
  title: ''
  type: Conventions
  url: conventions/firetail-conventions.yml
- group: auth
  href: https://artifacts.apis.io/firetail/security/firetail-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/firetail-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/firetail/authentication/firetail-authentication.yml
  title: ''
  type: Authentication
  url: authentication/firetail-authentication.yml
- group: design
  href: https://artifacts.apis.io/firetail/conformance/firetail-conformance.yml
  title: ''
  type: Conformance
  url: conformance/firetail-conformance.yml
- group: agent
  href: https://artifacts.apis.io/firetail/llms/firetail-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/firetail-llms.txt
- group: other
  href: https://artifacts.apis.io/firetail/hosts/firetail-hosts.yml
  title: ''
  type: Hosts
  url: hosts/firetail-hosts.yml
- group: other
  href: https://artifacts.apis.io/firetail/vendors/firetail-vendors.yml
  title: ''
  type: Vendors
  url: vendors/firetail-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.firetail.ai/team/alan-fagan
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.firetail.ai/releases/
- group: auth
  href: https://artifacts.apis.io/firetail/security/firetail-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/firetail-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/firetail/security/firetail-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/firetail-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.firetail.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.firetail.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.firetail.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firetail
- group: docs
  title: ''
  type: APIReference
  url: https://docs.firetail.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.firetail.ai/docs/getting-started/intro/
- group: company
  title: ''
  type: Blog
  url: https://www.firetail.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.firetail.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.firetail.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.firetail.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.firetail.ai/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.firetail.ai/schedule-your-demo
created: '2026-10-20'
description: FireTail provides an AI Security & Governance Platform that helps organizations discover, assess, and protect AI usage across applications and user environments. The solution offers centralized AI logging, shadow AI elimination, posture management, detection and response, and governance tools aligned with regulations such as the EU AI Act. It delivers comprehensive visibility, risk assessment, and policy enforcement to ensure secure AI adoption, supported by integrations, a public API, and resources like blogs, webinars, and documentation.
image: https://cdn.prod.website-files.com/62b077764e7780df74b8ff3f/68dce534f41d762da4575e42_FireTail%20AI%20Security%20%26%20Governance%20Platform.png
json_schemas:
- name: PostOauthTokenResponse
  property_count: 2
  slug: firetail-post-oauth-token-response
jsonld:
- class_count: 1
  name: Firetail Context
  property_count: 2
  slug: firetail-context
layout: provider
modified: '2026-10-20'
name: FireTail
nav: Providers
network: true
overview: 'FireTail is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Security, Governance, Platform, and Cloud.


  The FireTail catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FireTail''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 20 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: FireTail API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: firetail-rules
scopes:
- name: Firetail Scopes
  scope_count: 0
  slug: firetail-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.0
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 17.1
    developer_ergonomics: 34.5
    discoverability: 65.2
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 40.6
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
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/firetail/firetail-2026-11-03T132048.png
security:
- kind: authentication
  name: Firetail Authentication
  slug: firetail-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Firetail Domain Security
  slug: firetail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Firetail Vulnerability Disclosure
  slug: firetail-vulnerability-disclosure
  summary_line: no policy recorded
slug: firetail
tags:
- Artificial Intelligence
- Security
- Governance
- Platform
- Cloud
website: https://www.firetail.ai/
---
