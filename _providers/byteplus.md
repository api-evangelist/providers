---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.8
  scored_at: '2026-10-04'
api_count: 2
apis:
- description: API reference for BytePlus services as listed in the documentation.
  name: BytePlus API
  slug: byteplus-api-2
- baseURL: https://ecs.cn-beijing.byteplusapi.com.cn
  baseurl_source: declared
  description: The BytePlus API API from BytePlus — 1 operation(s) for byteplus api.
  name: BytePlus BytePlus API
  slug: byteplus-byteplus-api-api
artifact_total: 8
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/rules/byteplus-rules.yml
  title: ''
  type: Spectral
  url: rules/byteplus-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/json-ld/byteplus-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/byteplus-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/vocabulary/byteplus-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/byteplus-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/data-model/byteplus-data-model.yml
  title: ''
  type: DataModel
  url: data-model/byteplus-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.byteplus.com/en/trust
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/security/byteplus-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/byteplus-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/conformance/byteplus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/byteplus-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/llms/byteplus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/byteplus-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/well-known/byteplus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/byteplus-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/hosts/byteplus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/byteplus-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/vendors/byteplus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/byteplus-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/packages/byteplus-packages.yml
  title: ''
  type: SDKs
  url: packages/byteplus-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/packages/byteplus-packages.yml
  title: ''
  type: Packages
  url: packages/byteplus-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/security/byteplus-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/byteplus-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/security/byteplus-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/byteplus-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/byteplus/refs/heads/main/security/byteplus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/byteplus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.byteplus.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.byteplus.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.byteplus.com/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.byteplus.com/api-explorer
- group: start
  title: ''
  type: GettingStarted
  url: https://www.byteplus.com/en/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.byteplus.com/en/support-hub
- group: company
  title: ''
  type: Blog
  url: https://www.byteplus.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.byteplus.com/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.byteplus.com/en/legal/docs/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.byteplus.com/en/legal/docs/privacy-policy
coverage:
  checked: '2026-10-03'
  detail: API explorer pages render via JavaScript and return HTML shells, no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://api.byteplus.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: BytePlus provides AI-native cloud services enabling enterprises to integrate advanced machine learning models for vision, speech, and recommendation into their applications. The platform offers a suite of products such as ModelArk, BytePlus Voice, and Kickart, delivering scalable inference, data analytics, and media processing capabilities. Founded as a technology arm of ByteDance, BytePlus serves global customers across industries, emphasizing performance, security, and ease of integration through robust APIs and developer tools.
json_schemas:
- name: GetResponse
  property_count: 2
  slug: byteplus-get-response
jsonld:
- class_count: 1
  name: Byteplus Context
  property_count: 2
  slug: byteplus-context
layout: provider
modified: '2026-10-03'
name: BytePlus
nav: Providers
network: true
overview: 'BytePlus publishes 2 APIs on the [APIs.io](https://apis.io/) network, including BytePlus API, and 1 more. Tagged areas include Artificial Intelligence, Cloud, Enterprise, Machine Learning, and Platform.


  The BytePlus catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BytePlus'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
random_paper: 8
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: BytePlus API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: byteplus-rules
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 46.2
    catalog_earned_first_party: 0.0
    catalog_gap: 68.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 18.5
    developer_ergonomics: 52.4
    discoverability: 60.7
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Byteplus Domain Security
  slug: byteplus-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Byteplus Vulnerability Disclosure
  slug: byteplus-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Byteplus Trust Center
  slug: byteplus-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, PCI DSS, CSA STAR
slug: byteplus
tags:
- Artificial Intelligence
- Cloud
- Enterprise
- Machine Learning
- Platform
website: https://www.byteplus.com
---
