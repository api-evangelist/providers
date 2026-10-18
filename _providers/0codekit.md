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
api_count: 6
apis:
- description: API for 0CodeKit low-code platform
  name: 0CodeKit API
  slug: 0codekit-api-2
- description: The Ai API from relyon — 1 operation(s) for ai.
  name: relyon AI API
  slug: 0codekit-ai-api
- description: The Docs API from relyon — 1 operation(s) for docs.
  name: relyon Docs API
  slug: 0codekit-docs-api
- description: The Image API from relyon — 1 operation(s) for image.
  name: relyon Image API
  slug: 0codekit-image-api
- description: The Mcp API from relyon — 3 operation(s) for mcp.
  name: relyon MCP API
  slug: 0codekit-mcp-api
- description: The Pdf API from relyon — 1 operation(s) for pdf.
  name: relyon PDF API
  slug: 0codekit-pdf-api
artifact_total: 17
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/0codekit/refs/heads/main/plans/0codekit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/0codekit-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/0codekit/refs/heads/main/rules/0codekit-rules.yml
  title: ''
  type: Spectral
  url: rules/0codekit-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/0codekit/refs/heads/main/json-ld/0codekit-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/0codekit-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/0codekit/refs/heads/main/vocabulary/0codekit-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/0codekit-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/0codekit/refs/heads/main/data-model/0codekit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/0codekit-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/0codekit/refs/heads/main/authentication/0codekit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/0codekit-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/0codekit/refs/heads/main/conformance/0codekit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/0codekit-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/0codekit/refs/heads/main/well-known/0codekit-prod-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/0codekit-prod-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/0codekit/refs/heads/main/well-known/0codekit-my-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/0codekit-my-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/0codekit/refs/heads/main/well-known/0codekit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/0codekit-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/0codekit/refs/heads/main/hosts/0codekit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/0codekit-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/0codekit/refs/heads/main/vendors/0codekit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/0codekit-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.0codekit.com/support
- group: start
  title: ''
  type: Login
  url: https://my.0codekit.com/en/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/0codekit
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.0codekit.com/category/getting-started/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/0codekit/refs/heads/main/security/0codekit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/0codekit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.0codekit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.0codekit.com/
- group: company
  title: ''
  type: Blog
  url: https://www.0codekit.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.0codekit.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.0codekit.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.0codekit.com/legal/privacy-policy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://0codekit.com/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Relyon, operating under the brand 0CodeKit, offers a low‑code and no‑code platform enabling users to convert PDFs, execute code snippets, and integrate AI services without extensive programming. The suite includes PDF conversion, OCR, code execution in Python and JavaScript, image manipulation, and transcription tools, targeting tech‑savvy professionals and developers seeking rapid prototyping and automation.
image: https://cdn.prod.website-files.com/679e16442439d38e1efcc5c3/6867a7a1afbfac5e2a872223_Tutorial%20013.png
json_schemas:
- name: GetDocsResponse
  property_count: 2
  slug: 0codekit-get-docs-response
- name: GetMcpListResponse
  property_count: 2
  slug: 0codekit-get-mcp-list-response
- name: PostAiPdfocrResponse
  property_count: 5
  slug: 0codekit-post-ai-pdfocr-response
- name: PostImageImageidRequest
  property_count: 5
  slug: 0codekit-post-image-imageid-request
- name: PostPdfPdfidRequest
  property_count: 2
  slug: 0codekit-post-pdf-pdfid-request
- name: PostPdfPdfidResponse
  property_count: 5
  slug: 0codekit-post-pdf-pdfid-response
jsonld:
- class_count: 11
  name: 0Codekit Context
  property_count: 12
  slug: 0codekit-context
layout: provider
modified: '2026-10-15'
name: relyon
nav: Providers
network: true
overview: 'relyon is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including AI API, Docs API, Image API, and 3 more. Tagged areas include Company, Low-Code, No-Code, PDF Tools, and AI Integration.


  The relyon catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  relyon''s developer surface includes authentication, support, getting-started guide, documentation, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: 0Codekit Plans Pricing
  plan_count: 8
  slug: 0codekit-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: relyon API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: 0codekit-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 24.4
    developer_ergonomics: 40.5
    discoverability: 62.5
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
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
- kind: authentication
  name: 0Codekit Authentication
  slug: 0codekit-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 0Codekit Domain Security
  slug: 0codekit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: 0codekit
tags:
- Company
- Low-Code
- No-Code
- PDF Tools
- AI Integration
website: https://www.0codekit.com/
---
