---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: ConsentEase provides GDPR and CCPA cookie consent management APIs as documented at https://docs.consentease.io/.
  name: ConsentEase API
  slug: consentease-api
- baseURL: https://consentease.io
  baseurl_source: declared
  description: 'ConsentEase API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: ConsentEase API
  slug: consentease-io-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/consentease-io/plans/consentease-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/consentease-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/consentease-io/rules/consentease-io-rules.yml
  title: ''
  type: Spectral
  url: rules/consentease-io-rules.yml
- group: design
  href: https://artifacts.apis.io/consentease-io/json-ld/consentease-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/consentease-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/consentease-io/vocabulary/consentease-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/consentease-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/consentease-io/data-model/consentease-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/consentease-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/consentease-io/authentication/consentease-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/consentease-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/consentease-io/conformance/consentease-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/consentease-io-conformance.yml
- group: other
  href: https://artifacts.apis.io/consentease-io/hosts/consentease-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/consentease-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://consentease.io/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.consentease.io/
- group: operate
  title: ''
  type: Roadmap
  url: https://consentease.io/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://consentease.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://consentease.io/pricing
- group: start
  title: ''
  type: Login
  url: https://consentease.io/sign-in
- group: company
  title: ''
  type: Blog
  url: https://consentease.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.consentease.io/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.consentease.io/
- group: auth
  href: https://artifacts.apis.io/consentease-io/security/consentease-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/consentease-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://consentease.io/
coverage:
  checked: '2026-11-04'
  detail: Docs at https://docs.consentease.io/ are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.consentease.io/quickstart
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: ConsentEase provides affordable GDPR and CCPA cookie consent management for small businesses. The service offers a simple banner that can be installed in two minutes, with pricing starting at €9 per site per month for the first ten sites, then €7 thereafter. It supports Google Consent Mode v2, has no pageview limits, and includes features like policy generation and analytics integration. Founded in 2024, ConsentEase aims to simplify privacy compliance for SMEs.
image: https://consentease.io/og-images/v1/en-home.png
json_schemas:
- name: GetSitesIdComplianceResponse
  property_count: 9
  slug: consentease-io-get-sites-id-compliance-response
- name: GetSitesIdEmbedResponse
  property_count: 3
  slug: consentease-io-get-sites-id-embed-response
- name: PostConsentRequest
  property_count: 10
  slug: consentease-io-post-consent-request
- name: PostSitesIdCookiesRequest
  property_count: 4
  slug: consentease-io-post-sites-id-cookies-request
- name: PostSitesIdInstallationCheckResponse
  property_count: 11
  slug: consentease-io-post-sites-id-installation-check-response
- name: PostSitesSetupResponse
  property_count: 12
  slug: consentease-io-post-sites-setup-response
jsonld:
- class_count: 23
  name: Consentease Io Context
  property_count: 48
  slug: consentease-io-context
layout: provider
modified: '2026-11-04'
name: ConsentEase
nav: Providers
network: true
overview: 'ConsentEase is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GDPR, CCPA, Cookie Consent, and Small Business.


  The ConsentEase catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ConsentEase''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, and 14 more developer resources.'
plans:
- name: Consentease Io Plans Pricing
  plan_count: 8
  slug: consentease-io-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: ConsentEase API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: consentease-io-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Consentease Io Authentication
  slug: consentease-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Consentease Io Domain Security
  slug: consentease-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: consentease-io
tags:
- Company
- GDPR
- CCPA
- Cookie Consent
- Small Business
website: https://consentease.io/
---
