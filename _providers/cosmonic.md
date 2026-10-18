---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 12.9
  scored_at: '2026-10-17'
api_count: 11
apis:
- description: API reference for Cosmonic Control custom resource definitions across the control.cosmonic.io and runtime.wasmcloud.dev API groups.
  name: Cosmonic Control API
  slug: cosmonic-control-api
- baseURL: https://raw.githubusercontent.com
  baseurl_source: declared
  description: The Cosmonic API API from Cosmonic — 2 operation(s) for cosmonic api.
  name: Cosmonic Cosmonic API
  slug: cosmonic-cosmonic-api-api
- baseURL: https://raw.githubusercontent.com
  baseurl_source: declared
  description: The Cosmonic Labs API from Cosmonic — 1 operation(s) for cosmonic labs.
  name: Cosmonic Cosmonic Labs API
  slug: cosmonic-cosmonic-labs-api
- baseURL: https://raw.githubusercontent.com
  baseurl_source: declared
  description: The Detect API from Cosmonic — 1 operation(s) for detect.
  name: Cosmonic Detect API
  slug: cosmonic-detect-api
- baseURL: https://raw.githubusercontent.com
  baseurl_source: declared
  description: The Error API from Cosmonic — 1 operation(s) for error.
  name: Cosmonic Error API
  slug: cosmonic-error-api
- baseURL: https://raw.githubusercontent.com
  baseurl_source: declared
  description: The Form API from Cosmonic — 1 operation(s) for form.
  name: Cosmonic Form API
  slug: cosmonic-form-api
- baseURL: https://raw.githubusercontent.com
  baseurl_source: declared
  description: The Headers API from Cosmonic — 1 operation(s) for headers.
  name: Cosmonic Headers API
  slug: cosmonic-headers-api
- baseURL: https://raw.githubusercontent.com
  baseurl_source: declared
  description: The Myfile API from Cosmonic — 1 operation(s) for myfile.
  name: Cosmonic Myfile API
  slug: cosmonic-myfile-api
- baseURL: https://raw.githubusercontent.com
  baseurl_source: declared
  description: The Pkiops API from Cosmonic — 1 operation(s) for pkiops.
  name: Cosmonic Pkiops API
  slug: cosmonic-pkiops-api
- baseURL: https://raw.githubusercontent.com
  baseurl_source: declared
  description: The Post API from Cosmonic — 1 operation(s) for post.
  name: Cosmonic Post API
  slug: cosmonic-post-api
- baseURL: https://raw.githubusercontent.com
  baseurl_source: declared
  description: The Workloads API from Cosmonic — 1 operation(s) for workloads.
  name: Cosmonic Workloads API
  slug: cosmonic-workloads-api
artifact_total: 18
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosmonic/refs/heads/main/rules/cosmonic-rules.yml
  title: ''
  type: Spectral
  url: rules/cosmonic-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosmonic/refs/heads/main/json-ld/cosmonic-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cosmonic-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosmonic/refs/heads/main/vocabulary/cosmonic-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cosmonic-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosmonic/refs/heads/main/data-model/cosmonic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cosmonic-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosmonic/refs/heads/main/conformance/cosmonic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cosmonic-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cosmonic/refs/heads/main/llms/cosmonic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cosmonic-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cosmonic/refs/heads/main/hosts/cosmonic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cosmonic-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cosmonic/refs/heads/main/vendors/cosmonic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cosmonic-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cosmonic.com/legal/terms-of-use
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wasmcloud
- group: company
  title: ''
  type: Blog
  url: https://cosmonic.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://cosmonic.com/docs/category/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://cosmonic.com/docs/desktop/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cosmonic.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cosmonic/refs/heads/main/security/cosmonic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cosmonic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cosmonic.com
coverage:
  checked: '2026-10-11'
  detail: API reference pages are rendered HTML without a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://cosmonic.com/docs/category/api-reference/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: Cosmonic provides an AI sandbox platform that secures and runs code generated by AI agents. It offers a cross‑platform desktop app and cloud‑hosted control servers, enabling developers to build, test, and deploy sandboxed workloads from laptop to cluster. The service emphasizes capability‑based security, privacy, and easy integration with wasmcloud and other cloud‑native tools.
image: https://cosmonic.com/home/social-card.png
json_schemas:
- name: PostApiDetectRequest
  property_count: 7
  slug: cosmonic-post-api-detect-request
- name: PostMyfileTxtRequest
  property_count: 1
  slug: cosmonic-post-myfile-txt-request
- name: PostMyfileTxtResponse
  property_count: 1
  slug: cosmonic-post-myfile-txt-response
- name: PostV1V1IdRequest
  property_count: 1
  slug: cosmonic-post-v1-v1-id-request
jsonld:
- class_count: 4
  name: Cosmonic Context
  property_count: 10
  slug: cosmonic-context
layout: provider
modified: '2026-10-11'
name: Cosmonic
nav: Providers
network: true
overview: 'Cosmonic is listed with 11 APIs on the [APIs.io](https://apis.io/) network, including Cosmonic API, Cosmonic Labs API, Detect API, and 8 more. Tagged areas include Artificial Intelligence, Sandbox, Cloud, Platform, and Wasm.


  The Cosmonic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cosmonic''s developer surface includes engineering blog, API reference, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Cosmonic API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: cosmonic-rules
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 22.3
    developer_ergonomics: 31.0
    discoverability: 69.6
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Cosmonic Domain Security
  slug: cosmonic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cosmonic
tags:
- Artificial Intelligence
- Sandbox
- Cloud
- Platform
- Wasm
website: https://cosmonic.com
---
