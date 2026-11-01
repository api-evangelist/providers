---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: unknown
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 64
  human_in_the_loop: 0
  name: Signdocs Com Br Agentic Access
  operation_count: 104
  slug: signdocs-com-br-agentic-access
  summary_line: 104 operations · 64 acting
api_count: 1
apis:
- baseURL: https://api.signdocs.com.br
  baseurl_source: declared
  description: Obtenção de tokens de acesso OAuth2.
  name: signdocs-com-br Authentication API
  slug: signdocs-com-br-authentication-api
- baseURL: https://api.signdocs.com.br
  baseurl_source: declared
  description: Upload, confirmação e download de documentos vinculados a transações.
  name: signdocs-com-br Documents API
  slug: signdocs-com-br-documents-api
- baseURL: https://api.signdocs.com.br
  baseurl_source: declared
  description: Envelopes para assinatura com múltiplos signatários. Um envelope agrupa sessões de assinatura sobre o mesmo documento, suportando fluxos paralelos ou sequenciais.
  name: signdocs-com-br Envelopes API
  slug: signdocs-com-br-envelopes-api
- baseURL: https://api.signdocs.com.br
  baseurl_source: declared
  description: Consulta de pacotes de evidência criptograficamente assinados.
  name: signdocs-com-br Evidence API
  slug: signdocs-com-br-evidence-api
- baseURL: https://api.signdocs.com.br
  baseurl_source: declared
  description: Verificação de disponibilidade e histórico de saúde da API.
  name: signdocs-com-br Health API
  slug: signdocs-com-br-health-api
- baseURL: https://api.signdocs.com.br
  baseurl_source: declared
  description: Preparação e conclusão de assinatura digital com certificado ICP-Brasil A1.
  name: signdocs-com-br Signing API
  slug: signdocs-com-br-signing-api
- baseURL: https://api.signdocs.com.br
  baseurl_source: declared
  description: Sessões de assinatura (Assinatura Expressa). Abstração de alto nível que cria transação, etapas, documento e token de embed em uma única chamada. Retorna uma URL e clientSecret para integração via red
  name: signdocs-com-br Signing Sessions API
  slug: signdocs-com-br-signingsessions-api
- baseURL: https://api.signdocs.com.br
  baseurl_source: declared
  description: Listagem, início e conclusão de etapas de verificação de identidade.
  name: signdocs-com-br Steps API
  slug: signdocs-com-br-steps-api
- baseURL: https://api.signdocs.com.br
  baseurl_source: declared
  description: Criação, consulta, cancelamento e finalização de transações de assinatura.
  name: signdocs-com-br Transactions API
  slug: signdocs-com-br-transactions-api
- baseURL: https://api.signdocs.com.br
  baseurl_source: declared
  description: Sessões de Confiança. Autenticação verificável para qualquer ação digital — sem necessidade de documento PDF. Mesma máquina de estado e mesmo pacote de evidências das SigningSessions, mas com `purpose
  name: signdocs-com-br Trust Sessions API
  slug: signdocs-com-br-trustsessions-api
- baseURL: https://api.signdocs.com.br
  baseurl_source: declared
  description: Gerenciamento de enrollment biométrico de usuários.
  name: signdocs-com-br Users API
  slug: signdocs-com-br-users-api
- baseURL: https://api.signdocs.com.br
  baseurl_source: declared
  description: Verificação pública de evidências de assinatura.
  name: signdocs-com-br Verification API
  slug: signdocs-com-br-verification-api
- baseURL: https://api.signdocs.com.br
  baseurl_source: declared
  description: Registro, listagem, remoção e teste de webhooks para notificações de eventos.
  name: signdocs-com-br Webhooks API
  slug: signdocs-com-br-webhooks-api
- baseURL: https://api.signdocs.com.br
  baseurl_source: declared
  description: Operações em grupos de documentos com múltiplos signatários.
  name: signdocs-com-br Document Groups API
  slug: signdocs-com-br-document-groups-api
artifact_total: 33
asyncapis:
- description: ''
  name: Signdocs Com Br Webhooks
  slug: signdocs-com-br-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/signdocs-com-br/agentic-access/signdocs-com-br-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/signdocs-com-br-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/signdocs-com-br/rate-limits/signdocs-com-br-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/signdocs-com-br-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/signdocs-com-br/rules/signdocs-com-br-rules.yml
  title: ''
  type: Spectral
  url: rules/signdocs-com-br-rules.yml
- group: design
  href: https://artifacts.apis.io/signdocs-com-br/json-ld/signdocs-com-br-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/signdocs-com-br-context.jsonld
- group: design
  href: https://artifacts.apis.io/signdocs-com-br/vocabulary/signdocs-com-br-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/signdocs-com-br-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/signdocs-com-br/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/signdocs-com-br/asyncapi/signdocs-com-br-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/signdocs-com-br-webhooks.yml
- group: design
  href: https://artifacts.apis.io/signdocs-com-br/data-model/signdocs-com-br-data-model.yml
  title: ''
  type: DataModel
  url: data-model/signdocs-com-br-data-model.yml
- group: design
  href: https://artifacts.apis.io/signdocs-com-br/conventions/signdocs-com-br-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/signdocs-com-br-conventions.yml
- group: design
  href: https://artifacts.apis.io/signdocs-com-br/conventions/signdocs-com-br-conventions.yml
  title: ''
  type: Conventions
  url: conventions/signdocs-com-br-conventions.yml
- group: start
  href: https://artifacts.apis.io/signdocs-com-br/sandbox/signdocs-com-br-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/signdocs-com-br-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://signdocs.com.br/divulgacao-responsavel.html
- group: auth
  href: https://artifacts.apis.io/signdocs-com-br/authentication/signdocs-com-br-authentication.yml
  title: ''
  type: Authentication
  url: authentication/signdocs-com-br-authentication.yml
- group: design
  href: https://artifacts.apis.io/signdocs-com-br/errors/signdocs-com-br-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/signdocs-com-br-problem-types.yml
- group: design
  href: https://artifacts.apis.io/signdocs-com-br/conformance/signdocs-com-br-conformance.yml
  title: ''
  type: Conformance
  url: conformance/signdocs-com-br-conformance.yml
- group: agent
  href: https://artifacts.apis.io/signdocs-com-br/llms/signdocs-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/signdocs-com-br-llms.txt
- group: auth
  href: https://artifacts.apis.io/signdocs-com-br/well-known/signdocs-com-br-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/signdocs-com-br-www-security.txt
- group: auth
  href: https://artifacts.apis.io/signdocs-com-br/well-known/signdocs-com-br-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/signdocs-com-br-security.txt
- group: agent
  href: https://artifacts.apis.io/signdocs-com-br/well-known/signdocs-com-br-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/signdocs-com-br-well-known.yml
- group: other
  href: https://artifacts.apis.io/signdocs-com-br/hosts/signdocs-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/signdocs-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/signdocs-com-br/vendors/signdocs-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/signdocs-com-br-vendors.yml
- group: build
  href: https://artifacts.apis.io/signdocs-com-br/packages/signdocs-com-br-packages.yml
  title: ''
  type: SDKs
  url: packages/signdocs-com-br-packages.yml
- group: build
  href: https://artifacts.apis.io/signdocs-com-br/packages/signdocs-com-br-packages.yml
  title: ''
  type: Packages
  url: packages/signdocs-com-br-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.signdocs.com.br/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/signdocsbrasil
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.signdocs.com.br/guias/solucao-fornecedores.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.signdocs.com.br`
- group: docs
  title: ''
  type: APIReference
  url: https://docs.signdocs.com.br/
- group: auth
  href: https://artifacts.apis.io/signdocs-com-br/security/signdocs-com-br-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/signdocs-com-br-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/signdocs-com-br/security/signdocs-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/signdocs-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://signdocs.com.br/
created: '2026-10-31'
description: Signdocs is a Brazilian digital signature platform that enables businesses and individuals to securely sign documents online. The service offers an API for integrating electronic signature capabilities into applications, supporting PDF, Word, and image formats. It provides features such as document tracking, audit trails, and compliance with Brazilian legal standards for electronic signatures. The platform aims to streamline contract workflows, reduce paperwork, and enhance security for digital transactions across various industries.
json_schemas:
- name: AddEnvelopeSessionRequest
  property_count: 8
  slug: signdocs-com-br-add-envelope-session-request
- name: AdvanceSessionRequest
  property_count: 16
  slug: signdocs-com-br-advance-session-request
- name: AdvanceSessionResponse
  property_count: 18
  slug: signdocs-com-br-advance-session-response
- name: CreateSigningSessionRequest
  property_count: 14
  slug: signdocs-com-br-create-signing-session-request
- name: EnvelopeVerificationResponse
  property_count: 13
  slug: signdocs-com-br-envelope-verification-response
- name: StepCompleteRequest
  property_count: 14
  slug: signdocs-com-br-step-complete-request
jsonld:
- class_count: 89
  name: Signdocs Com Br Context
  property_count: 216
  slug: signdocs-com-br-context
layout: provider
modified: '2026-10-31'
name: signdocs-com-br
nav: Providers
network: true
overview: 'signdocs-com-br publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Documents API, Envelopes API, and 11 more. Tagged areas include Company, DigitalSignature, Brazil, API, and DocumentManagement.


  The signdocs-com-br catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  signdocs-com-br''s developer surface includes sandbox, authentication, getting-started guide, API reference, and 27 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 1
  name: Signdocs Com Br Rate Limits
  slug: signdocs-com-br-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: signdocs-com-br API Rules
  rule_count: 18
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 3
  slug: signdocs-com-br-rules
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 82.9
    catalog_earned_first_party: 0.0
    catalog_gap: 32.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 79.1
    contract_quality: 70.5
    developer_ergonomics: 61.2
    discoverability: 62.5
    operational_transparency: 58.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Signdocs Com Br Authentication
  slug: signdocs-com-br-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Signdocs Com Br Domain Security
  slug: signdocs-com-br-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Signdocs Com Br Vulnerability Disclosure
  slug: signdocs-com-br-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: signdocs-com-br-envelopes-signing-workflow
  slug: signdocs-com-br-envelopes-signing-workflow
- name: signdocs-com-br-manage-webhooks
  slug: signdocs-com-br-manage-webhooks
- name: signdocs-com-br-signing-session-flow
  slug: signdocs-com-br-signing-session-flow
- name: signdocs-com-br-transactions-create-and-finalize
  slug: signdocs-com-br-transactions-create-and-finalize
- name: signdocs-com-br-upload-and-download-document
  slug: signdocs-com-br-upload-and-download-document
slug: signdocs-com-br
tags:
- Company
- DigitalSignature
- Brazil
- API
- DocumentManagement
website: https://signdocs.com.br/
---
