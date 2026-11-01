---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Mochify App Agentic Access
  operation_count: 8
  slug: mochify-app-agentic-access
  summary_line: 8 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.mochify.app
  baseurl_source: declared
  description: Text-to-image generation (paid plans)
  name: mochify-app Generate API
  slug: mochify-app-generate-api
- baseURL: https://api.mochify.app
  baseurl_source: declared
  description: Compress, convert, resize, crop, and transform a single image
  name: mochify-app Image API
  slug: mochify-app-image-api
- baseURL: https://api.mochify.app
  baseurl_source: declared
  description: Service health
  name: mochify-app Meta API
  slug: mochify-app-meta-api
- baseURL: https://api.mochify.app
  baseurl_source: declared
  description: Rasterize a PDF to images, split it into single-page PDFs, or combine images into a PDF
  name: mochify-app PDF API
  slug: mochify-app-pdf-api
- baseURL: https://api.mochify.app
  baseurl_source: declared
  description: Chunked upload for large images on unreliable connections; feeds the same pipeline as /v1/squish
  name: mochify-app Upload API
  slug: mochify-app-upload-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/mochify-app/agentic-access/mochify-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mochify-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/mochify-app/plans/mochify-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mochify-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mochify-app/rules/mochify-app-rules.yml
  title: ''
  type: Spectral
  url: rules/mochify-app-rules.yml
- group: design
  href: https://artifacts.apis.io/mochify-app/vocabulary/mochify-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mochify-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/mochify-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/mochify-app/authentication/mochify-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mochify-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/mochify-app/errors/mochify-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mochify-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mochify-app/conformance/mochify-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mochify-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mochify-app/llms/mochify-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mochify-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/mochify-app/well-known/mochify-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mochify-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/mochify-app/hosts/mochify-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mochify-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/mochify-app/vendors/mochify-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mochify-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mochify.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mochify.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://mochify.app/pricing
- group: start
  title: ''
  type: Login
  url: https://mochify.app/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tliesnham
- group: docs
  title: ''
  type: Documentation
  url: https://mochify.app/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.mochify.app</div
- group: auth
  href: https://artifacts.apis.io/mochify-app/security/mochify-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mochify-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mochify.app/
created: '2026-10-30'
description: Mochify provides AI‑native image, video, and PDF compression via a Rust binary, a web app, a Chrome extension, and a hosted REST API. It offers a free tier with three operations per month without authentication, and paid plans with API keys for higher limits. The service emphasizes privacy, processing files locally or in‑browser without retaining data, and integrates with Claude and other agents for seamless workflow automation.
image: https://mochify.app/og/home.png
layout: provider
modified: '2026-10-30'
name: mochify-app
nav: Providers
network: true
overview: 'mochify-app publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Generate API, Image API, Meta API, and 2 more. Tagged areas include Company, ImageCompression, VideoCompression, PDFCompression, and AI.


  The mochify-app catalog on APIs.io includes 1 Spectral governance ruleset.


  mochify-app''s developer surface includes authentication, pricing, documentation, and 18 more developer resources.'
plans:
- name: Mochify App Plans Pricing
  plan_count: 5
  slug: mochify-app-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: mochify-app API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: mochify-app-rules
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 49.7
    developer_ergonomics: 32.7
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mochify App Authentication
  slug: mochify-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mochify App Domain Security
  slug: mochify-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: mochify-app-image-compress-and-check-quota
  slug: mochify-app-image-compress-and-check-quota
- name: mochify-app-upload-chunked
  slug: mochify-app-upload-chunked
slug: mochify-app
tags:
- Company
- ImageCompression
- VideoCompression
- PDFCompression
- AI
- PrivacyFocused
website: https://mochify.app/
---
