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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://markovo.net
  baseurl_source: declared
  description: File-to-Markdown conversion API
  name: Markovo Conversion API
  slug: markovo-conversion-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/markovo-net/plans/markovo-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/markovo-net-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/markovo-net/cli/markovo-net-cli.yml
  title: ''
  type: CLI
  url: cli/markovo-net-cli.yml
- group: design
  href: https://artifacts.apis.io/markovo-net/conformance/markovo-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/markovo-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/markovo-net/llms/markovo-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/markovo-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/markovo-net/well-known/markovo-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/markovo-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/markovo-net/hosts/markovo-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/markovo-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/markovo-net/vendors/markovo-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/markovo-net-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://markovo.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://markovo.net/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://markovo.net/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://markovo.net/docs
- group: company
  title: ''
  type: Blog
  url: https://markovo.net/blog
- group: auth
  href: https://artifacts.apis.io/markovo-net/security/markovo-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/markovo-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://markovo.net/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://markovo.net/openapi.json
  - status: 401
    url: https://markovo.net/mcp
  - status: 200
    url: https://markovo.net/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Markovo provides an online file-to-text conversion platform that transforms PDFs, Word documents, PowerPoint presentations, images, and various other formats into plain text, Markdown, or Word files. Users can upload files via the web interface, choose output formats, and receive clean, searchable text suitable for note‑taking, research, or AI processing. The service offers a free starter tier and paid plans for higher volume and advanced features, emphasizing ease of use and fast conversion.
image: https://markovo.net/brand/markovo-social.png
layout: provider
modified: '2026-10-30'
name: markovo-net
nav: Providers
network: true
overview: 'markovo-net is listed with 1 API on the [APIs.io](https://apis.io/) network: Markovo Conversion API. Tagged areas include Company, FileConversion, TextProcessing, SaaS, and API.


  markovo-net''s developer surface includes CLI, pricing, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Markovo Net Plans Pricing
  plan_count: 3
  slug: markovo-net-plans-pricing
random_paper: 11
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 24.0
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Markovo Net Domain Security
  slug: markovo-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: markovo-net
tags:
- Company
- FileConversion
- TextProcessing
- SaaS
- API
- Productivity
website: https://markovo.net/
---
