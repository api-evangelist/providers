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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-10-17'
api_count: 11
apis:
- baseURL: https://gateway.seven.io
  baseurl_source: declared
  description: The Events API from seven.io — 1 operation(s) for events.
  name: seven.io Events API
  slug: seven-io-events-api
- baseURL: https://gateway.seven.io
  baseurl_source: declared
  description: The Journal API from seven.io — 1 operation(s) for journal.
  name: seven.io Journal API
  slug: seven-io-journal-api
- baseURL: https://gateway.seven.io
  baseurl_source: declared
  description: The Lookup API from seven.io — 1 operation(s) for lookup.
  name: seven.io Lookup API
  slug: seven-io-lookup-api
- baseURL: https://gateway.seven.io
  baseurl_source: declared
  description: The Messages API from seven.io — 1 operation(s) for messages.
  name: seven.io Messages API
  slug: seven-io-messages-api
- baseURL: https://gateway.seven.io
  baseurl_source: declared
  description: The Numbers API from seven.io — 2 operation(s) for numbers.
  name: seven.io Numbers API
  slug: seven-io-numbers-api
- baseURL: https://gateway.seven.io
  baseurl_source: declared
  description: The Rcs API from seven.io — 2 operation(s) for rcs.
  name: seven.io Rcs API
  slug: seven-io-rcs-api
- baseURL: https://gateway.seven.io
  baseurl_source: declared
  description: The Revoke API from seven.io — 1 operation(s) for revoke.
  name: seven.io Revoke API
  slug: seven-io-revoke-api
- baseURL: https://gateway.seven.io
  baseurl_source: declared
  description: The Seven.io API API from seven.io — 2 operation(s) for seven.io api.
  name: seven.io Seven.io API
  slug: seven-io-seven-io-api-api
- baseURL: https://gateway.seven.io
  baseurl_source: declared
  description: The Token API from seven.io — 1 operation(s) for token.
  name: seven.io Token API
  slug: seven-io-token-api
- baseURL: https://gateway.seven.io
  baseurl_source: declared
  description: The Voice API from seven.io — 1 operation(s) for voice.
  name: seven.io Voice API
  slug: seven-io-voice-api
- baseURL: https://gateway.seven.io
  baseurl_source: declared
  description: The Waba API from seven.io — 2 operation(s) for waba.
  name: seven.io Waba API
  slug: seven-io-waba-api
artifact_total: 20
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seven-io/refs/heads/main/rules/seven-io-rules.yml
  title: ''
  type: Spectral
  url: rules/seven-io-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seven-io/refs/heads/main/json-ld/seven-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/seven-io-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seven-io/refs/heads/main/vocabulary/seven-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/seven-io-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seven-io/refs/heads/main/data-model/seven-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/seven-io-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seven-io/refs/heads/main/conformance/seven-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/seven-io-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seven-io/refs/heads/main/hosts/seven-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seven-io-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/seven-io/refs/heads/main/integrations/seven-io-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/seven-io-integration-edges.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.seven.io/en/company/terms/
- group: operate
  title: ''
  type: Support
  url: https://help.seven.io/en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.seven.io/en/company/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.seven.io/prices/
- group: company
  title: ''
  type: Newsroom
  url: https://www.seven.io/en/company/press/
- group: start
  title: ''
  type: Login
  url: https://app.seven.io/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seven-io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.seven.io/en/developer/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.seven.io/en/rcs/rcs-quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seven-io/refs/heads/main/security/seven-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seven-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.seven.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.seven.io/en
- group: auth
  title: ''
  type: Authentication
  url: https://docs.seven.io/en/rest-api/authentication
- group: design
  title: ''
  type: Webhooks
  url: https://docs.seven.io/en/rest-api/webhooks
- group: build
  title: ''
  type: SDKs
  url: https://docs.seven.io/en/rest-api/sdks
- group: company
  title: ''
  type: Blog
  url: https://www.seven.io/en/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.seven.io/en/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.seven.io
created: '2026-10-13'
description: seven.io (formerly sms77) is a German CPaaS provider in Kiel offering a REST API for SMS, voice calls, RCS, WhatsApp, number lookup (HLR/MNP/CNAM), contacts and webhooks.
image: https://www.seven.io/wp-content/uploads/Logo_Prev-1024x220.png
json_schemas:
- name: GetApiApiidIdResponse
  property_count: 7
  slug: seven-io-get-api-apiid-id-response
- name: GetApiApiidResponse
  property_count: 3
  slug: seven-io-get-api-apiid-response
- name: GetApiRcsAgentsResponse
  property_count: 7
  slug: seven-io-get-api-rcs-agents-response
- name: GetApiWabaTemplatesResponse
  property_count: 10
  slug: seven-io-get-api-waba-templates-response
- name: PatchApiApiidResponse
  property_count: 7
  slug: seven-io-patch-api-apiid-response
- name: PostApiApiidEventsRequest
  property_count: 6
  slug: seven-io-post-api-apiid-events-request
jsonld:
- class_count: 26
  name: Seven Io Context
  property_count: 64
  slug: seven-io-context
layout: provider
modified: '2026-10-13'
name: seven.io
nav: Providers
network: true
overview: 'seven.io is listed with 11 APIs on the [APIs.io](https://apis.io/) network, including Events API, Journal API, Lookup API, and 8 more. Tagged areas include Company, SMS, Voice, Messaging, and CPaaS.


  The seven.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  seven.io''s developer surface includes support, pricing, getting-started guide, documentation, authentication, engineering blog, changelog, and 18 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: seven.io API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: seven-io-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 25.4
    developer_ergonomics: 57.1
    discoverability: 64.3
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 20.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Seven Io Domain Security
  slug: seven-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: seven-io
tags:
- Company
- SMS
- Voice
- Messaging
- CPaaS
- Germany
website: https://www.seven.io
---
