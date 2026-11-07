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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/distributionos-dev/conformance/distributionos-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/distributionos-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/distributionos-dev/well-known/distributionos-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/distributionos-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/distributionos-dev/hosts/distributionos-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/distributionos-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/distributionos-dev/vendors/distributionos-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/distributionos-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://distributionos.dev/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://distributionos.dev/legal/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://distributionos.dev/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://distributionos.dev/login
- group: docs
  title: ''
  type: Documentation
  url: https://distributionos.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://distributionos.dev/blog
- group: auth
  href: https://artifacts.apis.io/distributionos-dev/security/distributionos-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/distributionos-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://distributionos.dev/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://distributionos.dev/api/mcp
  - status: 200
    url: https://distributionos.dev/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: DistributionOS provides marketing context and distribution memory for AI‑assisted coding tools like Codex and Claude. It helps indie app builders capture product details, audience insights, research briefs, and tracking checklists, turning shipped work into reusable marketing assets. The platform offers a visual workflow linking Brain Doc context, agent activity, and results, enabling better promotion of apps built with AI.
image: https://distributionos.dev/social/distributionos-home-og.png
layout: provider
modified: '2026-11-05'
name: DistributionOS
nav: Providers
network: true
overview: 'DistributionOS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing, Analytics, and MCP.


  DistributionOS''s developer surface includes support, documentation, engineering blog, and 9 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Distributionos Dev Domain Security
  slug: distributionos-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: distributionos-dev
tags:
- Marketing
- Analytics
- MCP
website: https://distributionos.dev/
---
