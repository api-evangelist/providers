---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for rendering PDFs from HTML + Handlebars templates. Bearer auth, JSON in, PDF bytes out.
  name: pdfzen API
  slug: pdfzen-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/pdfzen-site/llms/pdfzen-site-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pdfzen-site-llms.txt
- group: agent
  href: https://artifacts.apis.io/pdfzen-site/well-known/pdfzen-site-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pdfzen-site-well-known.yml
- group: other
  href: https://artifacts.apis.io/pdfzen-site/hosts/pdfzen-site-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pdfzen-site-hosts.yml
- group: other
  href: https://artifacts.apis.io/pdfzen-site/vendors/pdfzen-site-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pdfzen-site-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://pdfzen.site/dashboard/webhooks
- group: start
  title: ''
  type: Login
  url: https://pdfzen.site/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.pdfzen.site</span
- group: auth
  href: https://artifacts.apis.io/pdfzen-site/security/pdfzen-site-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pdfzen-site-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pdfzen.site/
- group: docs
  title: ''
  type: Documentation
  url: https://pdfzen.site/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://pdfzen.site/docs#getting-started
- group: operate
  title: ''
  type: Support
  url: https://pdfzen.site/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pdfzen.site/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pdfzen.site/legal/privacy
coverage:
  checked: '2026-10-31'
  detail: Documentation is provided as markdown without a published OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://pdfzen.site/docs.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: pdfzen.site provides an HTML‑to‑PDF rendering service via a REST API. Developers can POST HTML or template data to receive PDF bytes, use stored templates, and integrate with AI agents through the x402 pay‑per‑render protocol. The platform offers free starter credits, volume‑based pricing, and browser‑based tools for one‑off PDF tasks. Documentation, SDKs, and webhooks are publicly available.
image: https://pdfzen.site/opengraph-image
layout: provider
modified: '2026-10-30'
name: pdfzen-site
nav: Providers
network: true
overview: 'pdfzen-site is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PDF, Rendering, and HTML.


  pdfzen-site''s developer surface includes documentation, getting-started guide, support, and 11 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 3.9
  previous_composite: 21.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pdfzen-site/pdfzen-site-2026-11-03T141041.png
security:
- kind: domain-security
  name: Pdfzen Site Domain Security
  slug: pdfzen-site-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pdfzen-site
tags:
- Company
- PDF
- Rendering
- HTML
website: https://pdfzen.site/
---
