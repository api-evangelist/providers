---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Documentation and reference for Khronos standards and APIs.
  name: Khronos Registry
  slug: khronos-registry
artifact_total: 5
common:
- group: auth
  title: ''
  type: Security
  url: https://www.khronos.org/about/security#bounty
- group: agent
  href: https://artifacts.apis.io/the-khronos-group-inc/llms/the-khronos-group-inc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/the-khronos-group-inc-llms.txt
- group: auth
  href: https://artifacts.apis.io/the-khronos-group-inc/well-known/the-khronos-group-inc-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/the-khronos-group-inc-security.txt
- group: agent
  href: https://artifacts.apis.io/the-khronos-group-inc/well-known/the-khronos-group-inc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/the-khronos-group-inc-well-known.yml
- group: other
  href: https://artifacts.apis.io/the-khronos-group-inc/hosts/the-khronos-group-inc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/the-khronos-group-inc-hosts.yml
- group: other
  href: https://artifacts.apis.io/the-khronos-group-inc/vendors/the-khronos-group-inc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/the-khronos-group-inc-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.khronos.org/
- group: company
  title: ''
  type: Newsroom
  url: https://www.khronos.org/news/
- group: auth
  href: https://artifacts.apis.io/the-khronos-group-inc/security/the-khronos-group-inc-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/the-khronos-group-inc-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/the-khronos-group-inc/security/the-khronos-group-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-khronos-group-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.khronos.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.khronos.org/members/
- group: docs
  title: ''
  type: Documentation
  url: https://registry.khronos.org/
- group: docs
  title: ''
  type: APIReference
  url: https://registry.khronos.org/
- group: operate
  title: ''
  type: Support
  url: https://www.khronos.org/about/technical-support/
- group: company
  title: ''
  type: Blog
  url: https://www.khronos.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KhronosGroup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.khronos.org/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.khronos.org/legal/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.khronos.org/members/
- group: start
  title: ''
  type: SignUp
  url: https://www.khronos.org/members/
coverage:
  checked: '2026-10-29'
  detail: The Khronos Group provides documentation of its standards but no publicly accessible OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://www.khronos.org/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: The Khronos Group, Inc. is an open, member-driven consortium that develops royalty‑free open standards for 3D graphics, virtual and augmented reality, parallel computing, machine learning, vision processing, and the metaverse. It hosts a portfolio of industry standards such as OpenGL, Vulkan, OpenCL, OpenXR, WebGL, glTF, and many safety‑critical derivatives, supporting over 130 member organizations across 58 active standards in 21 countries.
image: https://www.khronos.org/assets/css/images/khronos-logo.svg
layout: provider
modified: '2026-10-29'
name: The Khronos Group, Inc.
nav: Providers
network: true
overview: 'The Khronos Group, Inc. is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Standard, Graphics, AR/VR, and Compute.


  The Khronos Group, Inc.''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
random_paper: 11
scopes:
- name: The Khronos Group Inc Scopes
  scope_count: 0
  slug: the-khronos-group-inc-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.5
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 65.2
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/the-khronos-group-inc/the-khronos-group-inc-2026-11-03T144540.png
security:
- kind: authentication
  name: The Khronos Group Inc Authentication
  slug: the-khronos-group-inc-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: The Khronos Group Inc Domain Security
  slug: the-khronos-group-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: The Khronos Group Inc Vulnerability Disclosure
  slug: the-khronos-group-inc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: the-khronos-group-inc
tags:
- Company
- Open Standard
- Graphics
- AR/VR
- Compute
- Consortium
website: https://www.khronos.org/
---
