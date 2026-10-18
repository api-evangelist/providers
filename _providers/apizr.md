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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
api_count: 8
apis:
- description: API for APIZR integration platform, documented at the developer portal.
  name: APIZR API
  slug: apizr-api
- baseURL: https://auth.api.com
  baseurl_source: declared
  description: The APIZR API API from APIZR — 2 operation(s) for apizr api.
  name: APIZR APIZR API
  slug: apizr-apizr-api-api
- baseURL: https://auth.api.com
  baseurl_source: declared
  description: The Events API from APIZR — 1 operation(s) for events.
  name: APIZR Events API
  slug: apizr-events-api
- baseURL: https://auth.api.com
  baseurl_source: declared
  description: The Flux Test API from APIZR — 1 operation(s) for flux test.
  name: APIZR Flux Test API
  slug: apizr-flux-test-api
- baseURL: https://auth.api.com
  baseurl_source: declared
  description: The Oauth API from APIZR — 1 operation(s) for oauth.
  name: APIZR OAuth API
  slug: apizr-oauth-api
- baseURL: https://auth.api.com
  baseurl_source: declared
  description: The Order API from APIZR — 1 operation(s) for order.
  name: APIZR Order API
  slug: apizr-order-api
- baseURL: https://auth.api.com
  baseurl_source: declared
  description: The Orders API from APIZR — 4 operation(s) for orders.
  name: APIZR Orders API
  slug: apizr-orders-api
- baseURL: https://auth.api.com
  baseurl_source: declared
  description: The Webhooks API from APIZR — 3 operation(s) for webhooks.
  name: APIZR Webhooks API
  slug: apizr-webhooks-api
artifact_total: 15
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apizr/refs/heads/main/rules/apizr-rules.yml
  title: ''
  type: Spectral
  url: rules/apizr-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apizr/refs/heads/main/json-ld/apizr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apizr-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apizr/refs/heads/main/vocabulary/apizr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apizr-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apizr/refs/heads/main/data-model/apizr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apizr-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apizr/refs/heads/main/changelog/apizr-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apizr-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apizr/refs/heads/main/authentication/apizr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apizr-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apizr/refs/heads/main/conformance/apizr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apizr-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apizr/refs/heads/main/llms/apizr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apizr-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apizr/refs/heads/main/hosts/apizr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apizr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apizr/refs/heads/main/vendors/apizr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apizr-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ecosystem.apizr.io/docs/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Apizr
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apizr/refs/heads/main/security/apizr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apizr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apizr.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ecosystem.apizr.io/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://api.management.ecosystem.apizr.io/v1/oauth/authorize?client_id=7c00c7cb-65db-4521-80c7-cb65db6521c7&redirect_uri=https%3A%2F%2Fecosystem.apizr.io%2Fhome
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ecosystem.apizr.io/docs/getting-started/overview
- group: company
  title: ''
  type: Blog
  url: https://apizr.fr/blog
coverage:
  checked: '2026-10-16'
  detail: OpenAPI endpoints returned 403 or 404, and no spec files were found on the docs or API hosts.
  evidence:
  - status: 403
    url: https://api.apizr.io/openapi.json
  - status: 403
    url: https://api.apizr.io/openapi.yaml
  - status: 0
    url: https://api.apizr.fr/openapi.json
  - status: 404
    url: https://api.management.ecosystem.apizr.io/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Apizr is a French iPaaS platform that leverages AI to boost integration workflows. It enables businesses to automate and synchronize data across applications with intelligent workflows, offering features like AI‑assisted mapping, real‑time monitoring, and scalable execution. The platform serves various industries, handling billions of euros in transaction volume and over 100 million executions per month, positioning itself as a modern, AI‑enhanced integration solution for enterprises seeking agile data connectivity.
image: https://apizr.fr/images/og-apizr.jpg
json_schemas:
- name: GetApiApiidResponse
  property_count: 1
  slug: apizr-get-api-apiid-response
- name: PostFluxTestRequest
  property_count: 2
  slug: apizr-post-flux-test-request
- name: PostOauthTokenRequest
  property_count: 1
  slug: apizr-post-oauth-token-request
jsonld:
- class_count: 3
  name: Apizr Context
  property_count: 4
  slug: apizr-context
layout: provider
modified: '2026-10-15'
name: APIZR
nav: Providers
network: true
overview: 'APIZR is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including APIZR API, Events API, Flux Test API, and 5 more. Tagged areas include iPaaS, Artificial Intelligence, Integration, Automation, and French.


  The APIZR catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APIZR''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, and 12 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: APIZR API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: apizr-rules
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 52.4
    discoverability: 69.6
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Apizr Authentication
  slug: apizr-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Apizr Domain Security
  slug: apizr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apizr
tags:
- iPaaS
- Artificial Intelligence
- Integration
- Automation
- French
website: https://apizr.fr/
---
