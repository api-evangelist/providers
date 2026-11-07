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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: doc2mcp product documentation
  name: doc2mcp MCP Service
  slug: mcp
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/doc2mcp-site/hosts/doc2mcp-site-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doc2mcp-site-hosts.yml
- group: other
  href: https://artifacts.apis.io/doc2mcp-site/vendors/doc2mcp-site-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doc2mcp-site-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doc2mcp.site/docs/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doc2mcp.site/docs/privacy
- group: start
  title: ''
  type: Login
  url: https://www.doc2mcp.site/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.doc2mcp.site/docs/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.doc2mcp.site/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/doc2mcp-site/security/doc2mcp-site-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doc2mcp-site-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doc2mcp.site/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.doc2mcp.site/
- group: docs
  title: ''
  type: Documentation
  url: https://www.doc2mcp.site/docs
- group: company
  title: ''
  type: Blog
  url: https://www.doc2mcp.site/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.doc2mcp.site/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doc2mcp
coverage:
  checked: '2026-10-29'
  detail: Docs are public HTML but no OpenAPI/GraphQL/AsyncAPI spec was found at any discovered host.
  evidence:
  - status: 404
    url: https://www.doc2mcp.site/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Doc2MCP provides a service that transforms any API documentation URL into a hosted MCP (Machine-Readable Code Prompt) server that can be consumed by AI agents such as Cursor, Claude, and Windsurf. It offers a no‑install, no‑API‑key solution with a web UI, CLI, marketplace of pre‑built integrations, transparent pricing plans, and open‑source tooling on GitHub. The platform enables developers to quickly generate AI‑ready documentation endpoints, improving code generation accuracy and reducing hallucinations.
image: https://doc2mcp.site/og-image-v2.png
layout: provider
modified: '2026-10-29'
name: doc2mcp-site
nav: Providers
network: true
overview: 'doc2mcp-site is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Documentation, AI Integration, MCP, Developer Tools, and No-Code.


  doc2mcp-site''s developer surface includes changelog, getting-started guide, documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Doc2Mcp Site Plans Pricing
  plan_count: 0
  slug: doc2mcp-site-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Doc2Mcp Site Rate Limits
  slug: doc2mcp-site-rate-limits
scopes:
- name: Doc2Mcp Site Scopes
  scope_count: 0
  slug: doc2mcp-site-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/doc2mcp-site/doc2mcp-site-2026-11-03T130833.png
security:
- kind: authentication
  name: Doc2Mcp Site Authentication
  slug: doc2mcp-site-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Doc2Mcp Site Domain Security
  slug: doc2mcp-site-domain-security
  summary_line: TLSv1.3 · HSTS
slug: doc2mcp-site
tags:
- API Documentation
- AI Integration
- MCP
- Developer Tools
- No-Code
website: https://doc2mcp.site/
---
