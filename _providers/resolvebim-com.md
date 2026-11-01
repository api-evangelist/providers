---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/resolvebim-com/conformance/resolvebim-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/resolvebim-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/resolvebim-com/llms/resolvebim-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/resolvebim-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/resolvebim-com/well-known/resolvebim-com-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/resolvebim-com-support-security.txt
- group: agent
  href: https://artifacts.apis.io/resolvebim-com/well-known/resolvebim-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/resolvebim-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/resolvebim-com/hosts/resolvebim-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/resolvebim-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/resolvebim-com/vendors/resolvebim-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/resolvebim-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.resolvebim.com/legal/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.resolvebim.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.resolvebim.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.resolvebim.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.resolvebim.com/login
- group: company
  title: ''
  type: Blog
  url: https://blog.resolvebim.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.resolvebim.com/blog/navisworks-vr-headset-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.resolvebim.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ResolveBIM
- group: auth
  href: https://artifacts.apis.io/resolvebim-com/security/resolvebim-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/resolvebim-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.resolvebim.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://app.resolvebim.com/mcp
  - status: 200
    url: https://www.resolvebim.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Resolve provides construction teams with high‑performance Building Information Modeling (BIM) tools that run on iPad, web browsers, and immersive VR. Its products—Resolve Field and Resolve VR—enable field crews, superintendents, owners, and reviewers to access large, federated models, verify measurements, and conduct issue tracking without specialized training. The platform integrates with Autodesk Construction Cloud, Procore, and Revizto to keep models and issues synchronized across workflows.
image: https://cdn.prod.website-files.com/6944b77e6e6e77b07879dee5/69c585906986f2efc39fd8d0_c9c0667c81c64d06e54074cf4197ca63_Resolve%20Trial%20-%20OG.png
layout: provider
modified: '2026-10-24'
name: Resolve
nav: Providers
network: true
overview: 'Resolve is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include BIM, VR Collaboration, Integration, Procore, and Autodesk.


  Resolve''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Resolvebim Com Domain Security
  slug: resolvebim-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: resolvebim-com
tags:
- BIM
- VR Collaboration
- Integration
- Procore
- Autodesk
website: https://www.resolvebim.com
---
