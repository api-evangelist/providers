---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://risc.googleapis.com
  baseurl_source: spec
  description: Programmatic access to Google Patents data via Google APIs.
  name: Google Patents API
  slug: google-patents-api
- baseURL: https://risc.googleapis.com
  baseurl_source: declared
  description: The Repos API from Google Patents — 1 operation(s) for repos.
  name: Google Patents Repos API
  slug: google-patents-repos-api
- baseURL: https://risc.googleapis.com
  baseurl_source: declared
  description: The V1Beta API from Google Patents — 2 operation(s) for v1beta.
  name: Google Patents V1Beta API
  slug: google-patents-v1beta-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/google-patents/rules/google-patents-rules.yml
  title: ''
  type: Spectral
  url: rules/google-patents-rules.yml
- group: design
  href: https://artifacts.apis.io/google-patents/json-ld/google-patents-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-patents-context.jsonld
- group: design
  href: https://artifacts.apis.io/google-patents/vocabulary/google-patents-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/google-patents-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/google-patents/data-model/google-patents-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-patents-data-model.yml
- group: design
  href: https://artifacts.apis.io/google-patents/conformance/google-patents-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-patents-conformance.yml
- group: auth
  href: https://artifacts.apis.io/google-patents/well-known/google-patents-google-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/google-patents-google-security.txt
- group: agent
  href: https://artifacts.apis.io/google-patents/well-known/google-patents-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-patents-well-known.yml
- group: other
  href: https://artifacts.apis.io/google-patents/hosts/google-patents-hosts.yml
  title: ''
  type: Hosts
  url: hosts/google-patents-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: auth
  title: ''
  type: Security
  url: https://accounts.google.com/ServiceLogin?hl=en-US&continue=https://myaccount.google.com/intro/security
- group: start
  title: ''
  type: Sandbox
  url: https://play.google.com/console/about/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: start
  title: ''
  type: Login
  url: https://accounts.google.com/v3/signin/identifier?continue=https://docs.google.com/&emr=1&followup=https://docs.google.com/&osid=1&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-939064257:1791850558360691
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.googleblog.com/
- group: auth
  href: https://artifacts.apis.io/google-patents/security/google-patents-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-patents-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-patents/security/google-patents-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-patents-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://patents.google.com/
coverage:
  checked: '2026-10-12'
  detail: The Google Patents site returns only a JavaScript shell with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://patents.google.com/
  - status: 200
    url: https://developers.google.com/patents
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Google Patents is a free public search engine provided by Google that allows users to search the full text of patents and patent applications from around the world. It aggregates data from multiple patent offices, offering advanced search filters, citation analysis, and the ability to view legal status and family information. The service is accessible via a web interface and supports programmatic access through Google’s broader APIs ecosystem, enabling developers to integrate patent data into their applications for research, analytics, and intellectual property management.
json_schemas:
- name: PostV1BetaModelsGemini35FlashGeneratecontentRequest
  property_count: 1
  slug: google-patents-post-v1-beta-models-gemini35-flash-generatecontent-request
jsonld:
- class_count: 1
  name: Google Patents Context
  property_count: 1
  slug: google-patents-context
layout: provider
modified: '2026-10-12'
name: Google Patents
nav: Providers
network: true
overview: 'Google Patents is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Repos API, V1Beta API, and 1 more. Tagged areas include Company, Patents, Search, Intellectual Property, and Google.


  The Google Patents catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Patents'' developer surface includes sandbox, documentation, and 16 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Google Patents API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: google-patents-rules
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.2
    catalog_earned_first_party: 0.0
    catalog_gap: 65.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 27.6
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 22.6
    discoverability: 58.9
    operational_transparency: 5.3
  previous_composite: 28.3
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
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-patents/google-patents-2026-11-03T132937.png
security:
- kind: domain-security
  name: Google Patents Domain Security
  slug: google-patents-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Google Patents Vulnerability Disclosure
  slug: google-patents-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-patents
tags:
- Company
- Patents
- Search
- Intellectual Property
- Google
website: https://patents.google.com/
---
