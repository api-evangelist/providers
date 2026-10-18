---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: tado provides a REST API for accessing thermostat and climate data, documented in their help center.
  name: tado API
  slug: tado-api-2
- baseURL: https://login.tado.com
  baseurl_source: declared
  description: The Me API from tado — 1 operation(s) for me.
  name: tado Me API
  slug: tado-me-api
- baseURL: https://login.tado.com
  baseurl_source: declared
  description: The Oauth2 API from tado — 1 operation(s) for oauth2.
  name: tado Oauth2 API
  slug: tado-oauth2-api
artifact_total: 8
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/rules/tado-rules.yml
  title: ''
  type: Spectral
  url: rules/tado-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/json-ld/tado-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tado-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/vocabulary/tado-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tado-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/data-model/tado-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tado-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/security/tado-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tado-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/conformance/tado-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tado-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/llms/tado-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tado-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/well-known/tado-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tado-support-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/well-known/tado-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tado-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/well-known/tado-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tado-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/well-known/tado-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tado-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/hosts/tado-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tado-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/vendors/tado-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tado-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tado.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.tado.com/de/newsletter/sign-up
- group: company
  title: ''
  type: Newsroom
  url: https://www.tado.com/en/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/security/tado-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tado-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tado/refs/heads/main/security/tado-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tado-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tado.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tado.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://www.tado.com/en
- group: docs
  title: ''
  type: APIReference
  url: https://www.tado.com/en
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tado.com/en
- group: operate
  title: ''
  type: Support
  url: https://help.tado.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.tado.com/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tado.com/en/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tado.com/en/legal/privacy-policy
coverage:
  checked: '2026-10-13'
  detail: Help center pages describe rate limits but no machine‑readable OpenAPI or other contract is available.
  evidence:
  - status: 200
    url: https://help.tado.com/en/articles/12165739-limitation-for-rest-api-usage.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: tado provides smart heating and cooling solutions that enable users to control thermostats, radiators, boilers, underfloor heating, and air conditioners via a mobile app. The platform offers energy savings of up to 22% on average, integrates with smart EV charging, and supports smart energy tariffs. With a focus on user-friendly automation, tado helps households reduce heating costs and improve comfort through intelligent climate control.
image: https://cdn.prod.website-files.com/673cb42d9d8ef472d0dacc28/67a0852c8af3b17fb7861937_tado_logo.avif
json_schemas:
- name: PostOauth2Oauth2IdResponse
  property_count: 6
  slug: tado-post-oauth2-oauth2-id-response
jsonld:
- class_count: 1
  name: Tado Context
  property_count: 6
  slug: tado-context
layout: provider
modified: '2026-10-13'
name: tado
nav: Providers
network: true
overview: 'tado is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Me API, Oauth2 API, and 1 more. Tagged areas include Company, Smart Home, Heating, EnergySaving, and IoT.


  The tado catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tado''s developer surface includes signup flow, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: tado API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: tado-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 51.2
    catalog_earned_first_party: 0.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 18.6
    developer_ergonomics: 45.2
    discoverability: 71.4
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Tado Domain Security
  slug: tado-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tado Vulnerability Disclosure
  slug: tado-vulnerability-disclosure
  summary_line: no policy recorded
slug: tado
tags:
- Company
- Smart Home
- Heating
- EnergySaving
- IoT
website: https://www.tado.com
---
