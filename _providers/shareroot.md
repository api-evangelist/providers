---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shareroot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shareroot.co
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ShareRoot
- group: build
  title: ''
  type: Packages
  url: packages/shareroot-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shareroot-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/shareroot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shareroot-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: 'ShareRoot Ltd was renamed Opyl Limited (ASX: OPL) after its December 2019 AGM and the brand was wound down — ludomade.com 301-redirects to opyl.ai, thesocialscience.com.au no longer resolves, no api/developer/docs/app subdomain of shareroot.co exists in DNS, the ShareRoot GitHub organization has had no push since 2017, and shareroot.co itself is a stale legacy site whose last readable archived pages (2024) show a UGC marketing brochure with injected SEO-spam and no developer program anywhere on it.'
  evidence:
  - status: 202
    url: https://shareroot.co/openapi.json
  - status: 301
    url: https://ludomade.com/
  - status: 200
    url: https://web.archive.org/web/20240713162126/https://www.shareroot.co/products/
  - status: 200
    url: https://api.github.com/orgs/ShareRoot/repos
  reason: defunct
  state: none
created: '2026-07-17'
description: 'ShareRoot was a user-generated content (UGC) marketing platform and, as ShareRoot Ltd (ASX: SRO), an Australian listed group headquartered in St Kilda, Victoria. Its brands were the ShareRoot platform for legally acquiring, organising and displaying UGC and brand-ambassador content (social walls, Facebook tabs, contests, experiential galleries and UGC on product pages), The Social Science, a marketing agency for Australia''s life sciences and health technology sectors, and Ludomade, a digital-experience studio doing web design, mobile games, VR/AR and experiential activations. Shareholders approved a rename to Opyl Limited (ASX: OPL) at the December 2019 annual general meeting, and the group repositioned into artificial intelligence for clinical trials and digital health; ludomade.com now redirects to opyl.ai. ShareRoot never published a developer program, API documentation, machine-readable specification or client SDK, and shareroot.co is now a stale legacy site sitting behind
  a bot challenge. This profile captures the company identity, a live domain-security probe, a recorded-absence well-known probe, and the two first-party open-source npm utilities the ShareRoot engineering team published in 2016.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shareroot.png
layout: provider
modified: '2026-08-12'
name: ShareRoot
nav: Providers
network: true
overview: ShareRoot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Social-Media, User Generated Content, and Digital Experience.
plans:
- name: Shareroot Plans Pricing
  plan_count: 0
  slug: shareroot-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Shareroot Rate Limits
  slug: shareroot-rate-limits
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Shareroot Domain Security
  slug: shareroot-domain-security
  summary_line: TLSv1.3
slug: shareroot
tags:
- Company
- Marketing
- Social-Media
- User Generated Content
- Digital Experience
- Advertising
website: https://shareroot.co
---
