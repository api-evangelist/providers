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
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/mouseflow/security/mouseflow-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/mouseflow-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/mouseflow/llms/mouseflow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mouseflow-llms.txt
- group: auth
  href: https://artifacts.apis.io/mouseflow/well-known/mouseflow-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mouseflow-help-security.txt
- group: agent
  href: https://artifacts.apis.io/mouseflow/well-known/mouseflow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mouseflow-well-known.yml
- group: other
  href: https://artifacts.apis.io/mouseflow/hosts/mouseflow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mouseflow-hosts.yml
- group: other
  href: https://artifacts.apis.io/mouseflow/vendors/mouseflow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mouseflow-vendors.yml
- group: build
  href: https://artifacts.apis.io/mouseflow/packages/mouseflow-packages.yml
  title: ''
  type: SDKs
  url: packages/mouseflow-packages.yml
- group: build
  href: https://artifacts.apis.io/mouseflow/packages/mouseflow-packages.yml
  title: ''
  type: Packages
  url: packages/mouseflow-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mouseflow.com/legal/terms/
- group: operate
  title: ''
  type: Support
  url: https://help.mouseflow.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mouseflow.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://mouseflow.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://mouseflow.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.mouseflow.com/
- group: auth
  href: https://artifacts.apis.io/mouseflow/security/mouseflow-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mouseflow-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mouseflow/security/mouseflow-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mouseflow-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mouseflow/security/mouseflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mouseflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mouseflow.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.mouseflow.com/mcp
  - status: 403
    url: https://go.mouseflow.com/mcp
  - status: 200
    url: https://mouseflow.com/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Mouseflow provides behavior analytics and session replay tools that help website owners understand user interactions, identify friction points, and improve conversion rates. Their platform offers heatmaps, funnel analysis, AI‑driven insights, and feedback surveys, enabling data‑driven UX optimization for businesses of all sizes.
image: https://mouseflow.com/wp-content/uploads/2022/03/default-meta-image@2x-100-1-scaled.jpg
layout: provider
modified: '2026-10-26'
name: Mouseflow
nav: Providers
network: true
overview: 'Mouseflow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Mouseflow''s developer surface includes support, pricing, engineering blog, documentation, and 14 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 46.4
    operational_transparency: 10.5
  previous_composite: 21.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mouseflow/mouseflow-2026-11-03T135852.png
security:
- kind: domain-security
  name: Mouseflow Domain Security
  slug: mouseflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mouseflow Vulnerability Disclosure
  slug: mouseflow-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Mouseflow Trust Center
  slug: mouseflow-trust-center
  summary_line: trust center published
slug: mouseflow
tags:
- Company
website: https://mouseflow.com/
---
