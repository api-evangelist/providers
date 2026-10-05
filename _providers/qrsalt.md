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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.0
  scored_at: '2026-10-04'
api_count: 8
apis:
- description: QR code generation API documented at QRSalt.
  name: QR Code API
  slug: qr-code-api
- baseURL: https://app.qrsalt.com
  baseurl_source: declared
  description: The Barcode API from QRSalt — 1 operation(s) for barcode.
  name: QRSalt Barcode API
  slug: qrsalt-barcode-api
- baseURL: https://app.qrsalt.com
  baseurl_source: declared
  description: The Codes API from QRSalt — 2 operation(s) for codes.
  name: QRSalt Codes API
  slug: qrsalt-codes-api
- baseURL: https://app.qrsalt.com
  baseurl_source: declared
  description: The Domains API from QRSalt — 1 operation(s) for domains.
  name: QRSalt Domains API
  slug: qrsalt-domains-api
- baseURL: https://app.qrsalt.com
  baseurl_source: declared
  description: The Forms API from QRSalt — 1 operation(s) for forms.
  name: QRSalt Forms API
  slug: qrsalt-forms-api
- baseURL: https://app.qrsalt.com
  baseurl_source: declared
  description: The I API from QRSalt — 1 operation(s) for i.
  name: QRSalt I API
  slug: qrsalt-i-api
- baseURL: https://app.qrsalt.com
  baseurl_source: declared
  description: The Qr API from QRSalt — 3 operation(s) for qr.
  name: QRSalt Qr API
  slug: qrsalt-qr-api
- baseURL: https://app.qrsalt.com
  baseurl_source: declared
  description: The QRSalt API API from QRSalt — 2 operation(s) for qrsalt api.
  name: QRSalt QRSalt API
  slug: qrsalt-qrsalt-api-api
artifact_total: 19
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/qrsalt/refs/heads/main/plans/qrsalt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qrsalt-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qrsalt/refs/heads/main/rules/qrsalt-rules.yml
  title: ''
  type: Spectral
  url: rules/qrsalt-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qrsalt/refs/heads/main/json-ld/qrsalt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/qrsalt-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qrsalt/refs/heads/main/vocabulary/qrsalt-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/qrsalt-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qrsalt/refs/heads/main/data-model/qrsalt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qrsalt-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qrsalt/refs/heads/main/conformance/qrsalt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qrsalt-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qrsalt/refs/heads/main/llms/qrsalt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qrsalt-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qrsalt/refs/heads/main/mcp/qrsalt-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/qrsalt-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qrsalt/refs/heads/main/well-known/qrsalt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/qrsalt-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qrsalt/refs/heads/main/hosts/qrsalt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qrsalt-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qrsalt/refs/heads/main/vendors/qrsalt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qrsalt-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://app.qrsalt.com/dashboard/webhooks
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qrsalt/refs/heads/main/security/qrsalt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qrsalt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qrsalt.com/qr-code-api
- group: docs
  title: ''
  type: Documentation
  url: https://qrsalt.com/qr-code-api/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://qrsalt.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qrsalt.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qrsalt.com/legal/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.qrsalt.com/register?next=%2Fdashboard%2Fapi
- group: operate
  title: ''
  type: Support
  url: https://qrsalt.com/about
coverage:
  checked: '2026-10-03'
  detail: QRSalt provides API documentation but no OpenAPI or other machine‑readable contract is publicly available.
  evidence:
  - status: 200
    url: https://qrsalt.com/qr-code-api/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: QRSalt provides QR code and barcode generation services, offering both static free codes and dynamic codes with short links, scan analytics, custom domains, and GS1 Digital Link support. The platform includes a free endpoint for rendering QR codes without an API key, as well as paid plans for editable, trackable codes, and additional features like QR menus, forms, and bulk generation. Documentation and pricing are available on their site, and a bearer key is used for authenticated API access via app.qrsalt.com.
image: https://qrsalt.com/opengraph-image.png?24c24df84fa08fac
json_schemas:
- name: PatchApiV1V1IdIdRequest
  property_count: 2
  slug: qrsalt-patch-api-v1-v1-id-id-request
- name: PostApiQrRequest
  property_count: 3
  slug: qrsalt-post-api-qr-request
- name: PostApiV1CodesBulkRequest
  property_count: 2
  slug: qrsalt-post-api-v1-codes-bulk-request
- name: PostApiV1DomainsIdCheckResponse
  property_count: 1
  slug: qrsalt-post-api-v1-domains-id-check-response
- name: PostApiV1V1IdRequest
  property_count: 3
  slug: qrsalt-post-api-v1-v1-id-request
- name: PostApiV1V1IdResponse
  property_count: 3
  slug: qrsalt-post-api-v1-v1-id-response
jsonld:
- class_count: 10
  name: Qrsalt Context
  property_count: 14
  slug: qrsalt-context
layout: provider
mcp_servers:
- description: Remote MCP server at qrsalt.com.
  name: QRSalt MCP Server
  slug: qrsalt-mcp-yml
modified: '2026-10-03'
name: QRSalt
nav: Providers
network: true
overview: 'QRSalt publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Barcode API, Codes API, Domains API, and 5 more. Tagged areas include QR Codes, Barcodes, Analytics, and Dynamic links.


  The QRSalt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  QRSalt''s developer surface includes documentation, pricing, signup flow, support, and 16 more developer resources.'
plans:
- name: Qrsalt Plans Pricing
  plan_count: 4
  slug: qrsalt-plans-pricing
random_paper: 3
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: QRSalt API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: qrsalt-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 14.3
    discoverability: 63.3
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Qrsalt Domain Security
  slug: qrsalt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qrsalt
tags:
- QR Codes
- Barcodes
- Analytics
- Dynamic links
website: https://qrsalt.com/qr-code-api
---
