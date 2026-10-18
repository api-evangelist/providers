---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Sahifa Agentic Access
  operation_count: 4
  slug: sahifa-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 4
apis:
- baseURL: https://api.sahifa.dev
  baseurl_source: declared
  description: HTML or a URL to PDF, PDFShift v3 compatible
  name: Sahifa PDF API
  slug: sahifa-pdf-api
- baseURL: https://api.sahifa.dev
  baseurl_source: declared
  description: Screenshots of a URL or HTML, ScreenshotOne compatible
  name: Sahifa Screenshots API
  slug: sahifa-screenshots-api
- baseURL: https://api.sahifa.dev
  baseurl_source: declared
  description: Service health
  name: Sahifa Status API
  slug: sahifa-status-api
artifact_total: 8
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/agentic-access/sahifa-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sahifa-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/rules/sahifa-rules.yml
  title: ''
  type: Spectral
  url: rules/sahifa-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/json-ld/sahifa-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sahifa-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/vocabulary/sahifa-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sahifa-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/data-model/sahifa-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sahifa-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/changelog/sahifa-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sahifa-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/authentication/sahifa-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sahifa-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/errors/sahifa-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sahifa-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/conformance/sahifa-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sahifa-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/hosts/sahifa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sahifa-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/packages/sahifa-packages.yml
  title: ''
  type: SDKs
  url: packages/sahifa-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/packages/sahifa-packages.yml
  title: ''
  type: Packages
  url: packages/sahifa-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sahifa.dev/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sahifa.dev/en/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://sahifa.dev/en/docs/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/security/sahifa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sahifa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sahifa.dev/en/
- group: docs
  title: ''
  type: Documentation
  url: https://sahifa.dev/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://sahifa.dev/en/docs/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://sahifa.dev/en/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://sahifa.dev/en/contact
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/llms/sahifa-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sahifa-llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://sahifa.dev/en/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://stats.uptimerobot.com/5fFpK4UvT9
- group: auth
  title: ''
  type: Compliance
  url: https://sahifa.dev/en/docs/compliance
- group: other
  title: ''
  type: DataResidency
  url: https://sahifa.dev/en/data-residency
created: '2026-09-28'
description: Sahifa provides a PDF and screenshot API hosted in Saudi Arabia, converting HTML to PDF and web pages to images. It runs on Oracle Cloud in Jeddah, ensuring data never leaves the Kingdom. The service offers a free sandbox tier and paid plans for businesses needing secure, localized document rendering.
jsonld:
- class_count: 1
  name: Sahifa Context
  property_count: 2
  slug: sahifa-context
layout: provider
modified: '2026-10-08'
name: Sahifa
nav: Providers
network: true
overview: 'Sahifa publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: PDF API, Screenshots API, and Status API. Tagged areas include Company, PDF, Screenshots, Saudi Arabia, and Cloud.


  The Sahifa catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sahifa''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, pricing, and 19 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Sahifa API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: sahifa-rules
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.7
  facets:
    access_clarity: 39.5
    contract_governance: 22.0
    contract_quality: 54.6
    developer_ergonomics: 52.4
    discoverability: 75.0
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - saudi-arabia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/sahifa/refs/heads/main/screenshots/sahifa-2026-10-11T125502.png
security:
- kind: authentication
  name: Sahifa Authentication
  slug: sahifa-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Sahifa Domain Security
  slug: sahifa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sahifa
tags:
- Company
- PDF
- Screenshots
- Saudi Arabia
- Cloud
website: https://sahifa.dev/en/
---
