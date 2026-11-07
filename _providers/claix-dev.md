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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Hosted, remote Model Context Protocol server (Streamable HTTP and legacy SSE) exposing the REST contract as dot-named tools - claix.schemas.*, claix.extract.*, claix.agent.*, claix.convert.json_to_exc
  name: Claix MCP Server
  slug: claix-mcp-server
- description: Native Agent-to-Agent (A2A 0.3) JSON-RPC agent at /a2a with a public agent card at /.well-known/agent-card.json declaring 20 skills, each bound by the provider to its OpenAPI operation. message/send w
  name: Claix A2A Agent
  slug: claix-a2a-agent
- baseURL: https://claix.dev/api
  baseurl_source: declared
  description: Extracción de datos estructurados a partir de documentos de texto (.docx, .txt, .md, .rtf)
  name: Claix Documento a JSON API
  slug: claix-dev-documento-a-json-api
- baseURL: https://claix.dev/api
  baseurl_source: declared
  description: Creación y borrado de espacios de conocimiento, y preguntas cruzadas sobre todos los documentos vigentes agrupados en uno de ellos. El formato de entrada y salida de las preguntas es el mismo que en l
  name: Claix Espacios de Conocimiento API
  slug: claix-dev-espacios-de-conocimiento-api
- baseURL: https://claix.dev/api
  baseurl_source: declared
  description: Conversión de archivos Excel/CSV a JSON estructurado
  name: Claix Excel a JSON API
  slug: claix-dev-excel-a-json-api
- baseURL: https://claix.dev/api
  baseurl_source: declared
  description: Extracción de datos estructurados a partir de imágenes (.jpeg, .jpg, .png, .webp, .heic, .heif)
  name: Claix Imagen a JSON API
  slug: claix-dev-imagen-a-json-api
- baseURL: https://claix.dev/api
  baseurl_source: declared
  description: Conversión de datos JSON a archivos Excel binarios
  name: Claix JSON a Excel API
  slug: claix-dev-json-a-excel-api
- baseURL: https://claix.dev/api
  baseurl_source: declared
  description: 'Extracción estructurada más razonamiento semántico en una sola llamada. Requiere schema con is_agent_mode activado y agent_definition configurada. URLs públicas: POST /agent/excel-json, /agent/pdf-jso'
  name: Claix Modo Agente API
  slug: claix-dev-modo-agente-api
- baseURL: https://claix.dev/api
  baseurl_source: declared
  description: Extracción de datos estructurados a partir de archivos PDF
  name: Claix PDF a JSON API
  slug: claix-dev-pdf-a-json-api
- baseURL: https://claix.dev/api
  baseurl_source: declared
  description: Consulta de los schemas creados en la cuenta
  name: Claix Schemas API
  slug: claix-dev-schemas-api
- baseURL: https://claix.dev/api
  baseurl_source: declared
  description: Extracción de datos estructurados a partir de texto plano, HTML o XML ya procesado (campo content, sin archivo)
  name: Claix Texto a JSON API
  slug: claix-dev-texto-a-json-api
- baseURL: https://claix.dev/api
  baseurl_source: declared
  description: 'Consulta de contenido bruto, preguntas o borrado de un documento persistido (markdown_content) identificado por document_id. URLs públicas: GET https://claix.dev/get-document/{document_id}; POST https'
  name: Claix Ventana de Contexto API
  slug: claix-dev-ventana-de-contexto-api
- baseURL: https://www.claix.dev/mcp
  baseurl_source: declared
  description: Extracción de datos estructurados a partir de audio hablado (.mp3, .wav, .m4a, .ogg)
  name: Claix Audio a JSON API
  slug: claix-dev-audio-a-json-api
- baseURL: https://www.claix.dev/mcp
  baseurl_source: declared
  description: Conversión de archivos a Markdown, sin schema. Mismos formatos que los endpoints de extracción a JSON. space_id es opcional. PDF digital, Excel, documentos de texto y txt/HTML/XML se convierten en loc
  name: Claix Markdown API
  slug: claix-dev-markdown-api
artifact_total: 27
asyncapis:
- description: ''
  name: Claix Dev Webhooks
  slug: claix-dev-webhooks
common:
- group: other
  href: https://artifacts.apis.io/claix-dev/capabilities/claix-dev-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/claix-dev-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/claix-dev/plans/claix-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/claix-dev-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/claix-dev/rate-limits/claix-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/claix-dev-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/claix-dev/overlays/claix-dev-servers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/claix-dev-servers-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/claix-dev/security/claix-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claix-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.claix.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.claix.dev/documentation/excel-to-json
- group: docs
  title: ''
  type: APIReference
  url: https://www.claix.dev/documentation/excel-to-json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.claix.dev/documentation/sdks
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.claix.dev/dashboard
- group: start
  title: ''
  type: SignUp
  url: https://www.claix.dev/register
- group: start
  title: ''
  type: Login
  url: https://www.claix.dev/login
- group: company
  title: ''
  type: Blog
  url: https://www.claix.dev/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.claix.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.claix.dev/privacy
- group: agent
  href: https://artifacts.apis.io/claix-dev/llms/claix-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claix-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/claix-dev/well-known/claix-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claix-dev-well-known.yml
- group: build
  href: https://artifacts.apis.io/claix-dev/packages/claix-dev-packages.yml
  title: ''
  type: Packages
  url: packages/claix-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/claix-dev/packages/claix-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/claix-dev-packages.yml
- group: design
  href: https://artifacts.apis.io/claix-dev/conformance/claix-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/claix-dev-conformance.yml
- group: design
  href: https://artifacts.apis.io/claix-dev/lifecycle/claix-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/claix-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/claix-dev/components/claix-dev-components.yml
  title: ''
  type: Components
  url: components/claix-dev-components.yml
- group: agent
  href: https://artifacts.apis.io/claix-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/claix-dev/regulatory/claix-dev-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/claix-dev-regulatory-posture.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://www.claix.dev/dpa
- group: operate
  title: ''
  type: IncidentNotification
  url: https://www.claix.dev/dpa
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.claix.dev/privacy
created: '2026-09-19'
description: 'Claix is a Madrid-based B2B document intelligence API that converts PDFs, Excel/CSV, Word and text documents and images into strictly typed JSON against customer-defined schemas, keeps extracted documents as queryable context for AI agents (single-document and knowledge-space Q&A with deterministic nulls), and exposes one 20-operation contract three ways: REST (OpenAPI 3.0.3), a hosted MCP server at /mcp, and a native A2A agent at /a2a with a published, conformant agent card. Pay-as-you-go in euros after 100 free calls, with a free BYOK mode; official Python SDK and n8n node.'
finops:
- has_sources: true
  method: derived
  name: Claix Dev Finops
  primary_unit: ''
  service_category: ''
  slug: claix-dev-finops
  template: true
image: https://www.claix.dev/claix-logo.png
layout: provider
mcp_servers:
- description: 'Claix ships a hosted, remote MCP server on its own domain. The documented URL is https://claix.dev/mcp; the apex answers 308 to https://www.claix.dev/mcp, which is the URL an MCP client actually ends '
  name: Claix MCP Server
  slug: claix
modified: '2026-09-19'
name: Claix
nav: Providers
network: true
overview: 'Claix publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Documento a JSON API, Espacios de Conocimiento API, Excel a JSON API, and 11 more. Tagged areas include Document Processing, Data Extraction, Document Intelligence, PDF, and Excel.


  The Claix catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Claix''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, and 22 more developer resources.'
plans:
- name: Claix Dev Plans Pricing
  plan_count: 2
  slug: claix-dev-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Claix Dev Rate Limits
  slug: claix-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Claix API Rules
  rule_count: 65
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 6
  slug: claix-dev-rules
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 57.5
    catalog_earned_first_party: 16.0
    catalog_gap: 57.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 38.2
    contract_governance: 31.8
    contract_quality: 59.2
    developer_ergonomics: 41.1
    discoverability: 75.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 55.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 50.0
      total: 24
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/claix-dev/claix-dev-2026-10-11T103026.png
security:
- kind: authentication
  name: Claix Dev Authentication
  slug: claix-dev-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Claix Dev Domain Security
  slug: claix-dev-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 5
skills:
- name: Extract with Agent mode reasoning
  slug: claix-dev-agent-mode-extraction
- name: Persist a document and ask it questions
  slug: claix-dev-ask-a-persisted-document
- name: Create a schema and extract a document
  slug: claix-dev-create-schema-and-extract
- name: Export JSON records to an Excel file
  slug: claix-dev-export-json-to-excel
- name: Group documents in a knowledge space and query them together
  slug: claix-dev-knowledge-space-qa
slug: claix-dev
tags:
- Document Processing
- Data Extraction
- Document Intelligence
- PDF
- Excel
- OCR
- Structured Data
- AI Agents
- MCP
- A2A
- Spain
- Company
website: https://www.claix.dev/
---
