---
agent_readiness:
  band: agent-ready
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API de consulta de CNPJ a partir dos dados abertos da Receita Federal.
  name: CNPJ Lookup API
  slug: cnpj-lookup-api
- baseURL: https://apipj.com.br
  baseurl_source: spec
  description: Assinaturas (Stripe; Asaas como alternativa)
  name: apipj (MASTER BI TECNOLOGIA LTDA) Billing API
  slug: apipj-billing-api
- baseURL: https://apipj.com.br
  baseurl_source: spec
  description: Chaves de API
  name: apipj (MASTER BI TECNOLOGIA LTDA) Chaves API
  slug: apipj-chaves-api
- baseURL: https://apipj.com.br
  baseurl_source: spec
  description: Consulta de CNPJ (exige chave de API ou sessão do site)
  name: apipj (MASTER BI TECNOLOGIA LTDA) Consulta API
  slug: apipj-consulta-api
- baseURL: https://apipj.com.br
  baseurl_source: spec
  description: Cadastro, login e perfil (sessão por cookie)
  name: apipj (MASTER BI TECNOLOGIA LTDA) Conta API
  slug: apipj-conta-api
- baseURL: https://apipj.com.br
  baseurl_source: spec
  description: Rotas internas (webhooks)
  name: apipj (MASTER BI TECNOLOGIA LTDA) Interno API
  slug: apipj-interno-api
- baseURL: https://apipj.com.br
  baseurl_source: spec
  description: Sem autenticação
  name: apipj (MASTER BI TECNOLOGIA LTDA) Público API
  slug: apipj-p-blico-api
artifact_total: 9
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apipj/refs/heads/main/rules/apipj-rules.yml
  title: ''
  type: Spectral
  url: rules/apipj-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apipj/refs/heads/main/vocabulary/apipj-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apipj-vocabulary.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/apipj/refs/heads/main/sandbox/apipj-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/apipj-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apipj/refs/heads/main/conformance/apipj-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apipj-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apipj/refs/heads/main/llms/apipj-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apipj-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apipj/refs/heads/main/well-known/apipj-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apipj-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apipj/refs/heads/main/hosts/apipj-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apipj-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apipj/refs/heads/main/packages/apipj-packages.yml
  title: ''
  type: SDKs
  url: packages/apipj-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apipj/refs/heads/main/packages/apipj-packages.yml
  title: ''
  type: Packages
  url: packages/apipj-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://apipj.com.br/sandbox
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apipj/refs/heads/main/security/apipj-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apipj-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apipj.com.br
- group: docs
  title: ''
  type: Documentation
  url: https://apipj.com.br/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://apipj.com.br/precos
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apipj.com.br/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apipj.com.br/privacidade
- group: operate
  title: ''
  type: StatusPage
  url: https://apipj.com.br/status
- group: start
  title: ''
  type: GettingStarted
  url: https://apipj.com.br/guias
created: '2026-10-14'
description: apipj (MASTER BI TECNOLOGIA LTDA) provides a public API for Brazilian CNPJ company registry lookup. It offers free access up to 50,000 queries per month and paid plans for higher volume. The API returns detailed company information such as legal name, registration status, address with IBGE code, activity, partners, Simples and MEI status, all in JSON directly from the Receita Federal dataset as of September 2026.
image: https://apipj.com.br/assets/og.png
layout: provider
modified: '2026-10-14'
name: apipj (MASTER BI TECNOLOGIA LTDA)
nav: Providers
network: true
overview: 'apipj (MASTER BI TECNOLOGIA LTDA) publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Chaves API, Consulta API, and 4 more. Tagged areas include Company, Brazil, CNPJ, Registry, and Public APIs.


  The apipj (MASTER BI TECNOLOGIA LTDA) catalog on APIs.io includes 1 Spectral governance ruleset.


  apipj (MASTER BI TECNOLOGIA LTDA)''s developer surface includes sandbox, documentation, pricing, getting-started guide, and 14 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: apipj (MASTER BI TECNOLOGIA LTDA) API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: apipj-rules
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 47.8
    developer_ergonomics: 35.7
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
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
  name: Apipj Domain Security
  slug: apipj-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: apipj
tags:
- Company
- Brazil
- CNPJ
- Registry
- Public APIs
website: https://apipj.com.br
---
