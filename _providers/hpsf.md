---
access_model:
  confidence: medium
  label: Anonymous, keyless read access. GET https://hpsf.io/wp-json/tribe/events/v1/events returns 200 with no credential. Writes require WordPress Application Passwords, which are not offered to the public.
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://hpsf.io/wp-json/tribe/events/v1/events
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the High Performance Software Foundation website at hpsf.io: the route index of the site''s content management system, catalogued as one site surface rather t'
  name: High Performance Software Foundation Website (WordPress REST)
  slug: hpsf-io-website-wordpress-rest
artifact_total: 9
asyncapis:
- description: ''
  name: Hpsf Event Surface
  slug: hpsf-event-surface
common:
- group: company
  title: ''
  type: Website
  url: https://www.hpsf.io/
- group: company
  title: ''
  type: About
  url: https://hpsf.io/about/
- group: docs
  title: ''
  type: Documentation
  url: https://hpsf.io/projects/
- group: docs
  title: ''
  type: APIReference
  url: https://hpsf.io/wp-json/tribe/events/v1/doc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hpsfoundation
- group: company
  title: ''
  type: Blog
  url: https://hpsf.io/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://hpsf.io/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/HPSF
- group: company
  title: ''
  type: Bluesky
  url: https://bsky.app/profile/hpsf.bsky.social
- group: operate
  title: ''
  type: Slack
  url: https://join.slack.com/t/hpsf/shared_invite/zt-3p95c8ety-_IW77jGKG35KgmFDGuDbsg
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.linuxfoundation.org/en/
- group: operate
  title: ''
  type: Contact
  url: https://hpsf.io/contact/
- group: start
  title: ''
  type: SignUp
  url: https://enrollment.lfx.linuxfoundation.org/?project=hpsf
- group: commercial
  title: ''
  type: Pricing
  url: https://hpsf.io/join/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linuxfoundation.org/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/legal/privacy-policy
- group: other
  title: ''
  type: Charter
  url: https://github.com/hpsfoundation/foundation/blob/main/charter.md
- group: other
  title: ''
  type: Governance
  url: https://hpsf.io/tac/
- group: agent
  href: https://artifacts.apis.io/hpsf/well-known/hpsf-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hpsf-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: https://hpsf.io/robots.txt
- group: agent
  href: https://artifacts.apis.io/hpsf/llms/hpsf-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hpsf-llms.txt
- group: auth
  href: https://artifacts.apis.io/hpsf/authentication/hpsf-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hpsf-authentication.yml
- group: design
  href: https://artifacts.apis.io/hpsf/conventions/hpsf-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hpsf-conventions.yml
- group: design
  href: https://artifacts.apis.io/hpsf/conformance/hpsf-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hpsf-conformance.yml
- group: design
  href: https://artifacts.apis.io/hpsf/lifecycle/hpsf-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hpsf-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hpsf/errors/hpsf-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hpsf-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hpsf/data-model/hpsf-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hpsf-data-model.yml
- group: build
  href: https://artifacts.apis.io/hpsf/examples/hpsf-examples.yml
  title: ''
  type: Examples
  url: examples/hpsf-examples.yml
- group: build
  href: https://artifacts.apis.io/hpsf/packages/hpsf-packages.yml
  title: ''
  type: Packages
  url: packages/hpsf-packages.yml
- group: commercial
  href: https://artifacts.apis.io/hpsf/plans/hpsf-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hpsf-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hpsf/rate-limits/hpsf-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hpsf-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/hpsf/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/hpsf/security/hpsf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hpsf-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/hpsf/mcp/hpsf-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/hpsf-mcp.yml
created: '2026-03-16'
description: 'The High Performance Software Foundation (HPSF) is a Linux Foundation project and neutral hub for open source high performance computing software, founded in 2024 and governed by a Governing Board, a Technical Advisory Council (TAC) and an Outreach Committee. HPSF hosts and supports a portable core software stack for HPC - including Spack, Kokkos, Apptainer, E4S, HPX, Charliecloud, Chapel, Viskores, Flux Framework and Wi4MPI - across Core, Established and Emerging project stages, and runs HPSFcon alongside a presence at SC and CppCon. Organizations join at Premier, General or Associate tier; projects apply to the TAC. HPSF publishes no developer program and ships no SDKs, but hpsf.io is a machine-readable surface in its own right: it serves an RFC 9727 /.well-known/api-catalog linkset, an llms.txt, a Content-Signal AI usage preference in robots.txt, and two live OpenAPI documents describing a publicly callable events API covering HPSF conferences, venues, organizers and event
  taxonomies. The WordPress wp/v2 content routes are advertised in the namespace list but are disabled on this installation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hpsf.png
layout: provider
modified: '2026-09-13'
name: High Performance Software Foundation
nav: Providers
network: true
overview: 'High Performance Software Foundation publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include HPC, Linux Foundation, Open Source, Scientific Computing, and Foundations.


  The High Performance Software Foundation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  High Performance Software Foundation''s developer surface includes documentation, API reference, engineering blog, support, signup flow, pricing, authentication, and 27 more developer resources.'
plans:
- name: Hpsf Plans Pricing
  plan_count: 0
  slug: hpsf-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Hpsf Rate Limits
  slug: hpsf-rate-limits
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 45.3
    developer_ergonomics: 32.7
    discoverability: 64.3
    operational_transparency: 5.3
  previous_composite: 37.8
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hpsf/hpsf-2026-06-20T182854.png
security:
- kind: authentication
  name: Hpsf Authentication
  slug: hpsf-authentication
  summary_line: none/http · 2 schemes
- kind: domain-security
  name: Hpsf Domain Security
  slug: hpsf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: hpsf-discover-surface
  slug: hpsf-discover-surface
- name: hpsf-map-venues
  slug: hpsf-map-venues
- name: hpsf-track-conferences
  slug: hpsf-track-conferences
slug: hpsf
tags:
- HPC
- Linux Foundation
- Open Source
- Scientific Computing
- Foundations
- Supercomputing
- Open Governance
- Event
- Conferences
- Research Computing
- Non-Profit
website: https://www.hpsf.io/
---
