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
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for managing fiscal documents in Brazil, as described in the documentation.
  name: Brasil NFe API
  slug: brasil-nfe-api
- baseURL: https://api.brasilnfe.com.br
  baseurl_source: declared
  description: 'brasilnfe-com-br API as documented publicly: 25 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: brasilnfe-com-br API
  slug: brasilnfe-com-br-api
artifact_total: 13
asyncapis:
- description: ''
  name: Brasilnfe Com Br Webhooks
  slug: brasilnfe-com-br-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/brasilnfe-com-br/rate-limits/brasilnfe-com-br-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/brasilnfe-com-br-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/brasilnfe-com-br/rules/brasilnfe-com-br-rules.yml
  title: ''
  type: Spectral
  url: rules/brasilnfe-com-br-rules.yml
- group: design
  href: https://artifacts.apis.io/brasilnfe-com-br/json-ld/brasilnfe-com-br-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/brasilnfe-com-br-context.jsonld
- group: design
  href: https://artifacts.apis.io/brasilnfe-com-br/vocabulary/brasilnfe-com-br-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brasilnfe-com-br-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/brasilnfe-com-br/asyncapi/brasilnfe-com-br-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/brasilnfe-com-br-webhooks.yml
- group: design
  href: https://artifacts.apis.io/brasilnfe-com-br/data-model/brasilnfe-com-br-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brasilnfe-com-br-data-model.yml
- group: design
  href: https://artifacts.apis.io/brasilnfe-com-br/conformance/brasilnfe-com-br-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brasilnfe-com-br-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brasilnfe-com-br/llms/brasilnfe-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brasilnfe-com-br-llms.txt
- group: agent
  href: https://artifacts.apis.io/brasilnfe-com-br/well-known/brasilnfe-com-br-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brasilnfe-com-br-well-known.yml
- group: other
  href: https://artifacts.apis.io/brasilnfe-com-br/hosts/brasilnfe-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brasilnfe-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/brasilnfe-com-br/vendors/brasilnfe-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brasilnfe-com-br-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.brasilnfe.com.br/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.brasilnfe.com.br/home/terms/
- group: auth
  title: ''
  type: Security
  url: https://www.brasilnfe.com.br/security
- group: start
  title: ''
  type: Login
  url: https://api.brasilnfe.com.br/Account/Login/?register=true
- group: auth
  href: https://artifacts.apis.io/brasilnfe-com-br/security/brasilnfe-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brasilnfe-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brasilnfe.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://www.brasilnfe.com.br/docs
- group: operate
  title: ''
  type: Support
  url: https://www.brasilnfe.com.br/legal/privacidade
created: '2026-10-30'
description: Brasil NFe provides a comprehensive REST API for issuing electronic invoices (NF-e, NFC-e, NFS-e, CT-e, MDF-e, DC-e) and related tax documents in Brazil. The platform offers services such as tax calculation, document generation, and integration with government tax authorities, targeting businesses needing automated fiscal compliance. It includes endpoints for product catalogs, pricing, AI assistance, and developer documentation, supporting multiple programming languages via SDKs.
image: https://www.brasilnfe.com.br/assets/maxsuel.webp
json_schemas:
- name: PostServicesFiscalBuscarnotafiscalservicoResponse
  property_count: 13
  slug: brasilnfe-com-br-post-services-fiscal-buscarnotafiscalservico-response
- name: PostServicesFiscalConsultargnreResponse
  property_count: 18
  slug: brasilnfe-com-br-post-services-fiscal-consultargnre-response
- name: PostServicesFiscalEnviarconhecimentotransporteRequest
  property_count: 25
  slug: brasilnfe-com-br-post-services-fiscal-enviarconhecimentotransporte-request
- name: PostServicesFiscalEnviardeclaracaoconteudoRequest
  property_count: 20
  slug: brasilnfe-com-br-post-services-fiscal-enviardeclaracaoconteudo-request
- name: PostServicesFiscalEnviarnotafiscalservicoRequest
  property_count: 3
  slug: brasilnfe-com-br-post-services-fiscal-enviarnotafiscalservico-request
- name: PostServicesFiscalEnviarnotafiscalservicoResponse
  property_count: 20
  slug: brasilnfe-com-br-post-services-fiscal-enviarnotafiscalservico-response
jsonld:
- class_count: 38
  name: Brasilnfe Com Br Context
  property_count: 156
  slug: brasilnfe-com-br-context
layout: provider
modified: '2026-10-30'
name: brasilnfe-com-br
nav: Providers
network: true
overview: 'brasilnfe-com-br is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Tax, Invoicing, and API.


  The brasilnfe-com-br catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  brasilnfe-com-br''s developer surface includes documentation, support, and 17 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 1
  name: Brasilnfe Com Br Rate Limits
  slug: brasilnfe-com-br-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: brasilnfe-com-br API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: brasilnfe-com-br-rules
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 77.2
    catalog_earned_first_party: 0.0
    catalog_gap: 37.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 70.9
    contract_quality: 55.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 37.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brasilnfe Com Br Domain Security
  slug: brasilnfe-com-br-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brasilnfe-com-br
tags:
- Company
- Finance
- Tax
- Invoicing
- API
website: https://www.brasilnfe.com.br/
---
