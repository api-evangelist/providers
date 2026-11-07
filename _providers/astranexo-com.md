---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: documented
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 66.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 68
  human_in_the_loop: 2
  name: Astranexo Com Agentic Access
  operation_count: 188
  slug: astranexo-com-agentic-access
  summary_line: 188 operations · 68 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://aster.astranexo.com/api/v1
  baseurl_source: declared
  description: Archeion, el archivo fiscal de 5 años; exportaciones e importaciones.
  name: Astranexo Archivo API
  slug: astranexo-com-archivo-api
- baseURL: https://aster.astranexo.com/api/v1
  baseurl_source: declared
  description: Catálogos públicos de Hacienda (CABYS, partidas arancelarias, ubicaciones y tablas de códigos FE 4.4).
  name: Astranexo Catálogos API
  slug: astranexo-com-cat-logos-api
- baseURL: https://aster.astranexo.com/api/v1
  baseurl_source: declared
  description: Claves de cuenta y de organización.
  name: Astranexo Claves API
  slug: astranexo-com-claves-api-api
- baseURL: https://aster.astranexo.com/api/v1
  baseurl_source: declared
  description: Cuenta, plan, consumo del período y lista pública de precios.
  name: Astranexo Cuenta y uso API
  slug: astranexo-com-cuenta-y-uso-api
- baseURL: https://aster.astranexo.com/api/v1
  baseurl_source: declared
  description: Emisión, consulta, descarga, envío por correo y anulación de comprobantes electrónicos.
  name: Astranexo Documentos API
  slug: astranexo-com-documentos-api
- baseURL: https://aster.astranexo.com/api/v1
  baseurl_source: declared
  description: Salud del servicio.
  name: Astranexo Estado API
  slug: astranexo-com-estado-api
- baseURL: https://aster.astranexo.com/api/v1
  baseurl_source: declared
  description: Estado de Hacienda, consultas de comprobantes y registro de contribuyentes.
  name: Astranexo Hacienda API
  slug: astranexo-com-hacienda-api
- baseURL: https://aster.astranexo.com/api/v1
  baseurl_source: declared
  description: Aceptación, aceptación parcial o rechazo de comprobantes recibidos de proveedores.
  name: Astranexo Mensajes receptor API
  slug: astranexo-com-mensajes-receptor-api
- baseURL: https://aster.astranexo.com/api/v1
  baseurl_source: declared
  description: Contribuyentes de la cuenta, su perfil, certificado de firma, consecutivos y marca.
  name: Astranexo Organizaciones API
  slug: astranexo-com-organizaciones-api
- baseURL: https://aster.astranexo.com/api/v1
  baseurl_source: declared
  description: Clientes guardados de la organización.
  name: Astranexo Receptores API
  slug: astranexo-com-receptores-api
- baseURL: https://aster.astranexo.com/api/v1
  baseurl_source: declared
  description: Tipo de cambio de referencia, histórico y por entidad financiera.
  name: Astranexo Tipo de cambio API
  slug: astranexo-com-tipo-de-cambio-api
- baseURL: https://aster.astranexo.com/api/v1
  baseurl_source: declared
  description: Notificaciones firmadas de cambios de estado de los documentos.
  name: Astranexo Webhooks API
  slug: astranexo-com-webhooks-api
artifact_total: 29
asyncapis:
- description: ''
  name: Astranexo Com Webhooks
  slug: astranexo-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/astranexo-com/agentic-access/astranexo-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/astranexo-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/astranexo-com/rate-limits/astranexo-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/astranexo-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/astranexo-com/plans/astranexo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/astranexo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/astranexo-com/rules/astranexo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/astranexo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/astranexo-com/json-ld/astranexo-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/astranexo-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/astranexo-com/vocabulary/astranexo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/astranexo-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/astranexo-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/astranexo-com/asyncapi/astranexo-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/astranexo-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/astranexo-com/data-model/astranexo-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/astranexo-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/astranexo-com/changelog/astranexo-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/astranexo-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/astranexo-com/conventions/astranexo-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/astranexo-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/astranexo-com/conventions/astranexo-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/astranexo-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/astranexo-com/authentication/astranexo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/astranexo-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/astranexo-com/scopes/astranexo-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/astranexo-com-scopes.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.astranexo.com/dashboard
- group: design
  href: https://artifacts.apis.io/astranexo-com/lifecycle/astranexo-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/astranexo-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/astranexo-com/errors/astranexo-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/astranexo-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/astranexo-com/conformance/astranexo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/astranexo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/astranexo-com/llms/astranexo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astranexo-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/astranexo-com/well-known/astranexo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/astranexo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/astranexo-com/hosts/astranexo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astranexo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/astranexo-com/vendors/astranexo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astranexo-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/astranexo-com/security/astranexo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astranexo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://astranexo.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astranexo.com/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://astranexo.com/en#contacto
created: '2026-11-01'
description: Astranexo is a business software provider offering solutions such as Astra, MiClub, AstraChat, WaBot, and Aster. Their platform delivers invoicing, inventory, client management, and work order tools, focusing on clear interfaces and people‑centric design. The company emphasizes customizable development and integrates chat and WhatsApp bot functionalities.
image: https://astranexo.com/images/astranexo-logo.svg
json_schemas:
- name: ApiKeyInput
  property_count: 5
  slug: astranexo-com-api-key-input
- name: CertificateVerification
  property_count: 3
  slug: astranexo-com-certificate-verification
- name: Document
  property_count: 28
  slug: astranexo-com-document
- name: ElectronicDocumentRequest
  property_count: 12
  slug: astranexo-com-electronic-document-request
- name: ExonetAuthorization
  property_count: 14
  slug: astranexo-com-exonet-authorization
- name: ReceptorMessageRequest
  property_count: 18
  slug: astranexo-com-receptor-message-request
jsonld:
- class_count: 93
  name: Astranexo Com Context
  property_count: 316
  slug: astranexo-com-context
layout: provider
modified: '2026-11-01'
name: Astranexo
nav: Providers
network: true
overview: 'Astranexo publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Archivo API, Catálogos API, Claves API, and 9 more. Tagged areas include Software, Business, Software-as-a-Service, Spanish, and CRM.


  The Astranexo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Astranexo''s developer surface includes changelog, authentication, support, and 23 more developer resources.'
plans:
- name: Astranexo Com Plans Pricing
  plan_count: 5
  slug: astranexo-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 6
  name: Astranexo Com Rate Limits
  slug: astranexo-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Astranexo API Rules
  rule_count: 64
  severity_counts:
    error: 49
    hint: 0
    info: 3
    warn: 12
  slug: astranexo-com-rules
scopes:
- name: Astranexo Com Scopes
  scope_count: 25
  slug: astranexo-com-scopes
  summary_line: 25 scopes
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 74.6
    developer_ergonomics: 20.7
    discoverability: 66.1
    operational_transparency: 63.2
  previous_composite: 54.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Astranexo Com Authentication
  slug: astranexo-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Astranexo Com Domain Security
  slug: astranexo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: get-status
  slug: get-status
- name: list-plans
  slug: list-plans
slug: astranexo-com
tags:
- Software
- Business
- Software-as-a-Service
- Spanish
- CRM
website: https://astranexo.com/
---
