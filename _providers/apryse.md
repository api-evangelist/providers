---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/apryse/plans/apryse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apryse-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apryse/conformance/apryse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apryse-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apryse/llms/apryse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apryse-llms.txt
- group: agent
  href: https://artifacts.apis.io/apryse/well-known/apryse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apryse-well-known.yml
- group: other
  href: https://artifacts.apis.io/apryse/hosts/apryse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apryse-hosts.yml
- group: other
  href: https://artifacts.apis.io/apryse/vendors/apryse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apryse-vendors.yml
- group: build
  href: https://artifacts.apis.io/apryse/packages/apryse-packages.yml
  title: ''
  type: SDKs
  url: packages/apryse-packages.yml
- group: build
  href: https://artifacts.apis.io/apryse/packages/apryse-packages.yml
  title: ''
  type: Packages
  url: packages/apryse-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://apryse.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apryse.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ApryseSDK
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apryse.com/guides/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://apryse.com/releases
- group: auth
  href: https://artifacts.apis.io/apryse/security/apryse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apryse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apryse.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apryse.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apryse.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://apryse.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://apryse.com/blog
coverage:
  checked: '2026-11-01'
  detail: Documentation site renders via GitBook JavaScript, preventing machine-readable spec retrieval.
  evidence:
  - status: 200
    url: https://docs.apryse.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Apryse provides document processing technology for developers, offering SDKs for web, server, mobile, and data capture. Their platform enables creating, editing, converting, and securing PDFs and other documents, with integrations for Salesforce, Mendix, and more. Apryse (formerly PDFTron) focuses on developer-friendly APIs and tools to embed viewing, editing, and advanced document features into applications.
image: https://apryse.com/img/apryse-preview-image.png
layout: provider
modified: '2026-11-01'
name: Apryse
nav: Providers
network: true
overview: 'Apryse is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Document Processing, SDK, and PDF.


  Apryse''s developer surface includes support, getting-started guide, changelog, documentation, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Apryse Plans Pricing
  plan_count: 2
  slug: apryse-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 39.3
    operational_transparency: 10.5
  previous_composite: 27.1
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apryse Domain Security
  slug: apryse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apryse
tags:
- Company
- Document Processing
- SDK
- PDF
website: https://apryse.com
---
