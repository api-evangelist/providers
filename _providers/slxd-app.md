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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API reference for AI API Pricing.
  name: AI API Pricing
  slug: ai-api-pricing
- baseURL: https://lmsmcp.slxd.app
  baseurl_source: declared
  description: 'slxd-app API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: slxd-app API
  slug: slxd-app-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/slxd-app/rules/slxd-app-rules.yml
  title: ''
  type: Spectral
  url: rules/slxd-app-rules.yml
- group: design
  href: https://artifacts.apis.io/slxd-app/vocabulary/slxd-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/slxd-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/slxd-app/conformance/slxd-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/slxd-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/slxd-app/mcp/slxd-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/slxd-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/slxd-app/well-known/slxd-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/slxd-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/slxd-app/hosts/slxd-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/slxd-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/slxd-app/vendors/slxd-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/slxd-app-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.slxd.app
- group: start
  title: ''
  type: Login
  url: https://account.slxd.app/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://slxd.app/en/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://slxd.app/en/docs/aiapipricing/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://slxd.app/en/docs/creator/getting-started/create-account
- group: auth
  href: https://artifacts.apis.io/slxd-app/security/slxd-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/slxd-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://slxd.app/
- group: docs
  title: ''
  type: Documentation
  url: https://slxd.app/en/docs
- group: company
  title: ''
  type: Blog
  url: https://slxd.app/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://slxd.app/en/pricing
- group: operate
  title: ''
  type: Roadmap
  url: https://slxd.app/en/roadmap
- group: operate
  title: ''
  type: Support
  url: https://slxd.app/en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://slxd.app/en/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://slxd.app/en/legal/privacy
coverage:
  checked: '2026-10-29'
  detail: The API reference page is a JavaScript‑rendered SPA with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://slxd.app/en/docs/aiapipricing/api-reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: SLXD is a SaaS platform that provides a suite for designing learning experiences. It enables teams to create, manage, and deliver educational content through a web application and API. The service offers documentation, pricing plans, a blog, and a public roadmap, supporting integration and customization for organizations seeking collaborative learning solutions.
image: https://slxd.app/en/opengraph-image-1t30ir?15561b1948eb9551
layout: provider
mcp_servers:
- description: Remote MCP server at aiapipricing.slxd.app.
  name: slxd-app MCP Server
  slug: slxd-app-mcp-yml
modified: '2026-10-29'
name: slxd-app
nav: Providers
network: true
overview: 'slxd-app is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Learning, Education, Software-as-a-Service, and Platform.


  The slxd-app catalog on APIs.io includes 1 Spectral governance ruleset.


  slxd-app''s developer surface includes changelog, API reference, getting-started guide, documentation, engineering blog, pricing, support, and 14 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: slxd-app API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: slxd-app-rules
scopes:
- name: Slxd App Scopes
  scope_count: 0
  slug: slxd-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.0
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 17.9
    discoverability: 60.0
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 33.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/slxd-app/slxd-app-2026-11-03T143333.png
security:
- kind: authentication
  name: Slxd App Authentication
  slug: slxd-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Slxd App Domain Security
  slug: slxd-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: slxd-app
tags:
- Company
- Learning
- Education
- Software-as-a-Service
- Platform
- Collaboration
website: https://slxd.app/
---
