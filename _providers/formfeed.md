---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 80
  human_in_the_loop: 0
  name: Formfeed Agentic Access
  operation_count: 122
  slug: formfeed-agentic-access
  summary_line: 122 operations · 80 acting
api_count: 2
apis:
- baseURL: https://api.formfeed.dev/v1
  baseurl_source: declared
  description: Workspace, plan and usage.
  name: Formfeed Account API
  slug: formfeed-account-api
- baseURL: https://api.formfeed.dev/v1
  baseurl_source: declared
  description: 'The organisation''s brand kit: colours, fonts, logos and legal footer every template sees as `brand`.'
  name: Formfeed Brand API
  slug: formfeed-brand-api
- baseURL: https://api.formfeed.dev/v1
  baseurl_source: declared
  description: Migration shim for apitemplate.io clients.
  name: Formfeed Compat API
  slug: formfeed-compat-api
- baseURL: https://api.formfeed.dev/v1
  baseurl_source: declared
  description: Workspace assets such as images and fonts.
  name: Formfeed Files API
  slug: formfeed-files-api
- baseURL: https://api.formfeed.dev/v1
  baseurl_source: declared
  description: Shared partials of the organisation, included by name from every template of the same engine.
  name: Formfeed Partials API
  slug: formfeed-partials-api
- baseURL: https://api.formfeed.dev/v1
  baseurl_source: declared
  description: Merge, protect, watermark and inspect PDFs.
  name: Formfeed PDF tools API
  slug: formfeed-pdf-tools-api
- baseURL: https://api.formfeed.dev/v1
  baseurl_source: declared
  description: Render PDFs and images from templates, HTML or URLs.
  name: Formfeed Renders API
  slug: formfeed-renders-api
- baseURL: https://api.formfeed.dev/v1
  baseurl_source: declared
  description: Manage templates and versions (templates as code).
  name: Formfeed Templates API
  slug: formfeed-templates-api
- baseURL: https://api.formfeed.dev/v1
  baseurl_source: declared
  description: Event delivery to your endpoints.
  name: Formfeed Webhooks API
  slug: formfeed-webhooks-api
artifact_total: 25
asyncapis:
- description: ''
  name: Formfeed Webhooks
  slug: formfeed-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/agentic-access/formfeed-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/formfeed-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/rate-limits/formfeed-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/formfeed-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/plans/formfeed-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/formfeed-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/rules/formfeed-rules.yml
  title: ''
  type: Spectral
  url: rules/formfeed-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/json-ld/formfeed-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/formfeed-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/vocabulary/formfeed-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/formfeed-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/asyncapi/formfeed-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/formfeed-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/data-model/formfeed-data-model.yml
  title: ''
  type: DataModel
  url: data-model/formfeed-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/cli/formfeed-cli.yml
  title: ''
  type: CLI
  url: cli/formfeed-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/changelog/formfeed-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/formfeed-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/conventions/formfeed-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/formfeed-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/conventions/formfeed-conventions.yml
  title: ''
  type: Conventions
  url: conventions/formfeed-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://formfeed.dev/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/authentication/formfeed-authentication.yml
  title: ''
  type: Authentication
  url: authentication/formfeed-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/errors/formfeed-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/formfeed-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/conformance/formfeed-conformance.yml
  title: ''
  type: Conformance
  url: conformance/formfeed-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/overlays/formfeed-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/formfeed-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/llms/formfeed-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/formfeed-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/well-known/formfeed-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/formfeed-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/well-known/formfeed-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/formfeed-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/hosts/formfeed-hosts.yml
  title: ''
  type: Hosts
  url: hosts/formfeed-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/vendors/formfeed-vendors.yml
  title: ''
  type: Vendors
  url: vendors/formfeed-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/packages/formfeed-packages.yml
  title: ''
  type: SDKs
  url: packages/formfeed-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/packages/formfeed-packages.yml
  title: ''
  type: Packages
  url: packages/formfeed-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://formfeed.dev/support
- group: auth
  title: ''
  type: Security
  url: https://formfeed.dev/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://formfeed.dev/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.formfeed.dev/getting-started/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.formfeed.dev/api/reference/formfeed
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/security/formfeed-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/formfeed-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/security/formfeed-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/formfeed-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/formfeed/refs/heads/main/security/formfeed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/formfeed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://formfeed.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formfeed.dev/api/overview
- group: company
  title: ''
  type: Blog
  url: https://formfeed.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://formfeed.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://formfeed.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://formfeed.dev/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.formfeed.dev
- group: start
  title: ''
  type: SignUp
  url: https://formfeed.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://app.formfeed.dev/en/sign-in
created: '2026-09-28'
description: Formfeed offers a PDF and image generation API that lets developers render templates written in Jinja2, Liquid, or Handlebars into PDFs, PNGs, and other formats. It can also convert Word and PowerPoint files. The service runs in Frankfurt with EU‑only data residency and provides a free tier of 100 units per month. SDKs are available for TypeScript and Python, a CLI exists, and there is MCP integration for AI agents. Features include batch rendering, webhook notifications, versioned templates, and a visual editor for designing documents.
image: https://formfeed.dev/app-screenshots/en/editor.webp
json_schemas:
- name: Brand
  property_count: 9
  slug: formfeed-brand
- name: RenderRequest
  property_count: 22
  slug: formfeed-render-request
- name: Render
  property_count: 21
  slug: formfeed-render
- name: StorageConnectionPut
  property_count: 13
  slug: formfeed-storage-connection-put
- name: StorageConnection
  property_count: 20
  slug: formfeed-storage-connection
- name: TemplateVersionCreate
  property_count: 13
  slug: formfeed-template-version-create
jsonld:
- class_count: 30
  name: Formfeed Context
  property_count: 140
  slug: formfeed-context
layout: provider
modified: '2026-09-28'
name: Formfeed
nav: Providers
network: true
overview: 'Formfeed publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Brand API, Compat API, and 6 more. Tagged areas include PDF, Image Generation, Templates, Developer Tools, and Software-as-a-Service.


  The Formfeed catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Formfeed''s developer surface includes CLI, changelog, authentication, support, getting-started guide, API reference, documentation, and 35 more developer resources.'
plans:
- name: Formfeed Plans Pricing
  plan_count: 5
  slug: formfeed-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Formfeed Rate Limits
  slug: formfeed-rate-limits
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Formfeed API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: formfeed-rules
score:
  band: exemplar
  composite: 75.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 71.1
    developer_ergonomics: 63.7
    discoverability: 73.2
    operational_transparency: 81.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 33.3
security:
- kind: authentication
  name: Formfeed Authentication
  slug: formfeed-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Formfeed Domain Security
  slug: formfeed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Formfeed Vulnerability Disclosure
  slug: formfeed-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Formfeed Trust Center
  slug: formfeed-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: formfeed
tags:
- PDF
- Image Generation
- Templates
- Developer Tools
- Software-as-a-Service
website: https://formfeed.dev/
---
