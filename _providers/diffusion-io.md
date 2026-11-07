---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/diffusion-io/llms/diffusion-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/diffusion-io-llms.txt
- group: other
  href: https://artifacts.apis.io/diffusion-io/hosts/diffusion-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diffusion-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/diffusion-io/vendors/diffusion-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/diffusion-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/diffusion-io/security/diffusion-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diffusion-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diffusion.io
- group: company
  title: ''
  type: Blog
  url: https://diffusion.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://diffusion.io/about
- group: operate
  title: ''
  type: Support
  url: https://diffusion.io/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/diffusioninc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://diffusion.io/privacy
coverage:
  checked: '2026-10-29'
  detail: Standard OpenAPI discovery URLs on diffusion.io and app.diffusion.io returned 404 or HTML login pages, and api.diffusion.io did not resolve.
  evidence:
  - status: 404
    url: https://diffusion.io/openapi.json
  - status: 200
    url: https://app.diffusion.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Diffusion AI, Inc. builds large‑scale software factories that transform high‑context, complex enterprise work into repeatable, automated systems. Founded by Justin McCarthy, formerly of StrongDM, the company delivers AI‑enhanced platforms enabling organizations to design, operate, and extend bespoke digital workflows across global operations. It serves enterprises in Silicon Valley, Europe, and India, offering consulting, tooling, and managed services to accelerate digital transformation and operational efficiency.
image: https://diffusion.io/favicon.svg
layout: provider
modified: '2026-10-29'
name: Diffusion
nav: Providers
network: true
overview: 'Diffusion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise, SoftwareFactory, Artificial Intelligence, Automation, and Platform.


  Diffusion''s developer surface includes engineering blog, getting-started guide, support, and 7 more developer resources.'
plans:
- name: Diffusion Io Plans Pricing
  plan_count: 0
  slug: diffusion-io-plans-pricing
random_paper: 4
scopes:
- name: Diffusion Io Scopes
  scope_count: 0
  slug: diffusion-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 55.4
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.6
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/diffusion-io/diffusion-io-2026-11-03T130721.png
security:
- kind: authentication
  name: Diffusion Io Authentication
  slug: diffusion-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Diffusion Io Domain Security
  slug: diffusion-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: diffusion-io
tags:
- Enterprise
- SoftwareFactory
- Artificial Intelligence
- Automation
- Platform
website: https://diffusion.io
---
