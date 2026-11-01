---
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
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.ivalt.com
  baseurl_source: declared
  description: 'iVALT API as documented publicly: 46 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: iVALT API
  slug: ivalt-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/ivalt/rules/ivalt-rules.yml
  title: ''
  type: Spectral
  url: rules/ivalt-rules.yml
- group: design
  href: https://artifacts.apis.io/ivalt/json-ld/ivalt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ivalt-context.jsonld
- group: design
  href: https://artifacts.apis.io/ivalt/vocabulary/ivalt-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ivalt-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ivalt/data-model/ivalt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ivalt-data-model.yml
- group: auth
  href: https://artifacts.apis.io/ivalt/authentication/ivalt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ivalt-authentication.yml
- group: design
  href: https://artifacts.apis.io/ivalt/conformance/ivalt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ivalt-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ivalt/llms/ivalt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ivalt-llms.txt
- group: other
  href: https://artifacts.apis.io/ivalt/hosts/ivalt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ivalt-hosts.yml
- group: other
  href: https://artifacts.apis.io/ivalt/vendors/ivalt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ivalt-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.ivalt.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.ivalt.com/products/getting-started
- group: auth
  href: https://artifacts.apis.io/ivalt/security/ivalt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ivalt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ivalt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ivalt.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ivalt.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ivalt.com/privacy
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.ivalt.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: iVALT provides a platform that cryptographically proves human authority for AI-driven and high‑value digital actions. By integrating a control plane that verifies a human’s intent before execution, iVALT aims to close gaps in identity, access management, and workflow security. The service offers components such as DocuID, OnDemand ID, and AI Agent Authority to support enterprises in securing privileged transactions and AI interactions.
image: https://www.ivalt.com/images/og-default.png
json_schemas:
- name: PostAdminPublicApiBiometricGeoFenceAuthResultsRequest
  property_count: 5
  slug: ivalt-post-admin-public-api-biometric-geo-fence-auth-results-request
- name: PostAdminPublicApiBiometricGeoFenceAuthResultsResponse
  property_count: 5
  slug: ivalt-post-admin-public-api-biometric-geo-fence-auth-results-response
- name: PostAdminPublicApiVerifyUserRequest
  property_count: 2
  slug: ivalt-post-admin-public-api-verify-user-request
- name: PostAdminPublicApiVerifyUserResponse
  property_count: 5
  slug: ivalt-post-admin-public-api-verify-user-response
- name: PostBiometricGeoFenceAuthResultsRequest
  property_count: 7
  slug: ivalt-post-biometric-geo-fence-auth-results-request
- name: PostVerifyUserRequest
  property_count: 2
  slug: ivalt-post-verify-user-request
jsonld:
- class_count: 9
  name: Ivalt Context
  property_count: 11
  slug: ivalt-context
layout: provider
modified: '2026-10-28'
name: iVALT
nav: Providers
network: true
overview: 'iVALT is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Identity, Security, and HumanAuthority.


  The iVALT catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  iVALT''s developer surface includes authentication, getting-started guide, documentation, and 13 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: iVALT API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: ivalt-rules
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 19.7
    contract_quality: 25.4
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 22
      marker_coverage: 100.0
      total: 22
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ivalt Authentication
  slug: ivalt-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ivalt Domain Security
  slug: ivalt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ivalt
tags:
- Company
- AI
- Identity
- Security
- HumanAuthority
website: https://www.ivalt.com/
---
