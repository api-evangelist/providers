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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: 2Captcha provides a CAPTCHA solving service with a REST API documented at the API Docs page.
  name: 2Captcha API
  slug: 2captcha-api-2
- baseURL: https://api.2captcha.com
  baseurl_source: declared
  description: '2captcha API as documented publicly: 42 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: 2captcha API
  slug: 2captcha-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/2captcha/plans/2captcha-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/2captcha-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/2captcha/rules/2captcha-rules.yml
  title: ''
  type: Spectral
  url: rules/2captcha-rules.yml
- group: design
  href: https://artifacts.apis.io/2captcha/json-ld/2captcha-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/2captcha-context.jsonld
- group: design
  href: https://artifacts.apis.io/2captcha/vocabulary/2captcha-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/2captcha-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/2captcha/data-model/2captcha-data-model.yml
  title: ''
  type: DataModel
  url: data-model/2captcha-data-model.yml
- group: design
  href: https://artifacts.apis.io/2captcha/conformance/2captcha-conformance.yml
  title: ''
  type: Conformance
  url: conformance/2captcha-conformance.yml
- group: agent
  href: https://artifacts.apis.io/2captcha/llms/2captcha-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/2captcha-llms.txt
- group: other
  href: https://artifacts.apis.io/2captcha/hosts/2captcha-hosts.yml
  title: ''
  type: Hosts
  url: hosts/2captcha-hosts.yml
- group: other
  href: https://artifacts.apis.io/2captcha/vendors/2captcha-vendors.yml
  title: ''
  type: Vendors
  url: vendors/2captcha-vendors.yml
- group: build
  href: https://artifacts.apis.io/2captcha/packages/2captcha-packages.yml
  title: ''
  type: SDKs
  url: packages/2captcha-packages.yml
- group: build
  href: https://artifacts.apis.io/2captcha/packages/2captcha-packages.yml
  title: ''
  type: Packages
  url: packages/2captcha-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://2captcha.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://2captcha.com/support/enterprise
- group: operate
  title: ''
  type: StatusPage
  url: https://status.2captcha.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://2captcha.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://2captcha.com/pricing
- group: start
  title: ''
  type: Login
  url: https://2captcha.com/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/2captcha
- group: company
  title: ''
  type: Blog
  url: https://2captcha.com/blog
- group: auth
  href: https://artifacts.apis.io/2captcha/security/2captcha-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/2captcha-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://2captcha.com/
coverage:
  checked: '2026-10-28'
  detail: API documentation page returns HTML without a discoverable OpenAPI or other contract.
  evidence:
  - status: 404
    url: https://api.2captcha.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: 2captcha provides an API that solves a wide range of captchas, including reCAPTCHA v2, v3, Enterprise, Cloudflare Turnstile, Arkose Labs, and many image and audio captchas. The service is used by developers, QA engineers, and data‑extraction tools to automate captcha bypass in software, testing frameworks, and web‑scraping applications. It offers both AI‑based automatic solving and human fallback for difficult cases, with pricing per 1,000 solved captchas.
json_schemas:
- name: GetBrowserAccountsResponse
  property_count: 2
  slug: 2captcha-get-browser-accounts-response
- name: GetBrowserResponse
  property_count: 5
  slug: 2captcha-get-browser-response
- name: GetFingerprintGenerateResponse
  property_count: 8
  slug: 2captcha-get-fingerprint-generate-response
- name: GetFingerprintRandomResponse
  property_count: 7
  slug: 2captcha-get-fingerprint-random-response
- name: PostImportCookiesRequest
  property_count: 6
  slug: 2captcha-post-import-cookies-request
- name: PostTasksRequestRequest
  property_count: 7
  slug: 2captcha-post-tasks-request-request
jsonld:
- class_count: 49
  name: 2Captcha Context
  property_count: 61
  slug: 2captcha-context
layout: provider
modified: '2026-10-28'
name: 2captcha
nav: Providers
network: true
overview: '2captcha is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Captcha Solving, API, Automation, Web Scraping, and Data Extraction.


  The 2captcha catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  2captcha''s developer surface includes support, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: 2Captcha Plans Pricing
  plan_count: 5
  slug: 2captcha-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: 2captcha API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: 2captcha-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 24.9
    developer_ergonomics: 14.3
    discoverability: 62.5
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 17
      marker_coverage: 100.0
      total: 17
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 2Captcha Domain Security
  slug: 2captcha-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 2captcha
tags:
- Captcha Solving
- API
- Automation
- Web Scraping
- Data Extraction
website: https://2captcha.com/
---
