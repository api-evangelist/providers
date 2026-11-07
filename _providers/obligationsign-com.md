---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
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
    error_semantics: false
    event_surface_described: unknown
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
  score: 26.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Obligationsign platform as described in documentation.
  name: Obligationsign API
  slug: obligationsign-api
- baseURL: https://api.obligationsign.com
  baseurl_source: declared
  description: 'obligationsign-com API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: obligationsign-com API
  slug: obligationsign-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/obligationsign-com/plans/obligationsign-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/obligationsign-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/obligationsign-com/rules/obligationsign-com-rules.yml
  title: ''
  type: Spectral
  url: rules/obligationsign-com-rules.yml
- group: design
  href: https://artifacts.apis.io/obligationsign-com/json-ld/obligationsign-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/obligationsign-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/obligationsign-com/vocabulary/obligationsign-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/obligationsign-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/obligationsign-com/data-model/obligationsign-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/obligationsign-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/obligationsign-com/changelog/obligationsign-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/obligationsign-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://obligationsign.com/compliance/
- group: auth
  href: https://artifacts.apis.io/obligationsign-com/authentication/obligationsign-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/obligationsign-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/obligationsign-com/conformance/obligationsign-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/obligationsign-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/obligationsign-com/well-known/obligationsign-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/obligationsign-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/obligationsign-com/hosts/obligationsign-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/obligationsign-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/obligationsign-com/vendors/obligationsign-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/obligationsign-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://obligationsign.com/integrate/webhooks/index.html
- group: auth
  title: ''
  type: Security
  url: https://obligationsign.com/security/index.html
- group: build
  title: ''
  type: SDKs
  url: https://obligationsign.com/integrate/sdks/index.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://obligationsign.com/docs/changelog/index.html
- group: auth
  href: https://artifacts.apis.io/obligationsign-com/security/obligationsign-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/obligationsign-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/obligationsign-com/security/obligationsign-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/obligationsign-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/obligationsign-com/security/obligationsign-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/obligationsign-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://obligationsign.com/
- group: docs
  title: ''
  type: Documentation
  url: https://obligationsign.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://obligationsign.com/start/index.html
- group: commercial
  title: ''
  type: Pricing
  url: https://obligationsign.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://obligationsign.com/legal/
created: '2026-10-30'
description: ObligationSign provides governance infrastructure for autonomous AI systems, offering cryptographic accountability and immutable proof of decisions. Their platform includes hardware-backed signing, consensus protocols, and a dashboard for real-time risk monitoring, targeting sectors like supply chain, finance, cybersecurity, and infrastructure.
json_schemas:
- name: PostAutoRegisterRequest
  property_count: 1
  slug: obligationsign-com-post-auto-register-request
- name: PostAutoRegisterResponse
  property_count: 5
  slug: obligationsign-com-post-auto-register-response
- name: PostWebhooksRequest
  property_count: 2
  slug: obligationsign-com-post-webhooks-request
jsonld:
- class_count: 3
  name: Obligationsign Com Context
  property_count: 8
  slug: obligationsign-com-context
layout: provider
modified: '2026-10-30'
name: obligationsign-com
nav: Providers
network: true
overview: 'obligationsign-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Governance, Security, and Infrastructure.


  The obligationsign-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  obligationsign-com''s developer surface includes changelog, authentication, documentation, getting-started guide, pricing, and 19 more developer resources.'
plans:
- name: Obligationsign Com Plans Pricing
  plan_count: 6
  slug: obligationsign-com-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: obligationsign-com API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: obligationsign-com-rules
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.0
    catalog_earned_first_party: 12.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 53.9
    contract_governance: 33.3
    contract_quality: 20.4
    developer_ergonomics: 29.8
    discoverability: 53.6
    operational_transparency: 17.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 42.1
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
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/obligationsign-com/obligationsign-com-2026-11-03T140408.png
security:
- kind: authentication
  name: Obligationsign Com Authentication
  slug: obligationsign-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Obligationsign Com Domain Security
  slug: obligationsign-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Obligationsign Com Vulnerability Disclosure
  slug: obligationsign-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Obligationsign Com Trust Center
  slug: obligationsign-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: obligationsign-com
tags:
- Company
- Artificial Intelligence
- Governance
- Security
- Infrastructure
website: https://obligationsign.com/
---
