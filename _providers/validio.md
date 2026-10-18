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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Data quality and observability API
  name: Validio API
  slug: validio-api-2
- baseURL: https://YOUR-INSTALLATION.validio.io
  baseurl_source: declared
  description: The Export API from Validio — 1 operation(s) for export.
  name: Validio Export API
  slug: validio-export-api
artifact_total: 8
asyncapis:
- description: ''
  name: Validio Webhooks
  slug: validio-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/validio/refs/heads/main/rules/validio-rules.yml
  title: ''
  type: Spectral
  url: rules/validio-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/validio/refs/heads/main/json-ld/validio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/validio-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/validio/refs/heads/main/vocabulary/validio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/validio-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/validio/refs/heads/main/asyncapi/validio-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/validio-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/validio/refs/heads/main/data-model/validio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/validio-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/validio/refs/heads/main/cli/validio-cli.yml
  title: ''
  type: CLI
  url: cli/validio-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/validio/refs/heads/main/changelog/validio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/validio-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://validio.io/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/validio/refs/heads/main/conformance/validio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/validio-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/validio/refs/heads/main/llms/validio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/validio-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/validio/refs/heads/main/well-known/validio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/validio-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/validio/refs/heads/main/hosts/validio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/validio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/validio/refs/heads/main/vendors/validio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/validio-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://validio.io/security
- group: company
  title: ''
  type: Newsroom
  url: https://validio.io/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.validio.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.validio.io/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/validio/refs/heads/main/security/validio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/validio-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/validio/refs/heads/main/security/validio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/validio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://validio.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.validio.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.validio.io/docs/validio-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.validio.io/docs/what-is-validio
- group: company
  title: ''
  type: Blog
  url: https://validio.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://validio.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://validio.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://validio.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://validio.io/status
coverage:
  detail: API reference page renders a JavaScript SPA with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://dev.validio.io/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: Validio provides an agentic data quality, observability, and lineage platform for enterprises. Their solution enables real‑time anomaly detection, comprehensive data lineage tracing, and AI‑driven insights across data assets. Targeting industries such as banking, manufacturing, logistics, and gaming, Validio helps organizations meet regulatory compliance while improving data reliability and operational efficiency. The platform offers modular use‑cases including data quality monitoring, business metrics monitoring, machine‑learning AI integration, and customer‑facing data products, all delivered via a cloud‑native SaaS model.
image: https://images.prismic.io/validio/Z1bmkJbqstJ98OOl_SEOimage.jpg?auto=format,compress
json_schemas:
- name: GetApiExportV1V1IdResponse
  property_count: 9
  slug: validio-get-api-export-v1-v1-id-response
jsonld:
- class_count: 1
  name: Validio Context
  property_count: 5
  slug: validio-context
layout: provider
modified: '2026-10-15'
name: Validio
nav: Providers
network: true
overview: 'Validio is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Export API, and 1 more. Tagged areas include Company, Data Quality, Observability, Lineage, and Artificial Intelligence.


  The Validio catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Validio''s developer surface includes CLI, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 21 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Validio API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: validio-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 26.9
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 50.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Validio Domain Security
  slug: validio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Validio Trust Center
  slug: validio-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: validio
tags:
- Company
- Data Quality
- Observability
- Lineage
- Artificial Intelligence
website: https://validio.io/
---
