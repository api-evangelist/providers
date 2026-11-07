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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: NodeSource provides APIs for its N|Solid runtime, monitoring, and services, documented at the NodeSource documentation site.
  name: NodeSource API
  slug: nodesource-api-2
- baseURL: https://deb.nodesource.com
  baseurl_source: declared
  description: 'NodeSource API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: NodeSource API
  slug: nodesource-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/nodesource/plans/nodesource-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nodesource-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/nodesource/rules/nodesource-rules.yml
  title: ''
  type: Spectral
  url: rules/nodesource-rules.yml
- group: design
  href: https://artifacts.apis.io/nodesource/vocabulary/nodesource-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nodesource-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/nodesource/conformance/nodesource-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nodesource-conformance.yml
- group: other
  href: https://artifacts.apis.io/nodesource/hosts/nodesource-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nodesource-hosts.yml
- group: other
  href: https://artifacts.apis.io/nodesource/vendors/nodesource-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nodesource-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.nodesource.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nodesource.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.nodesource.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rw-ns
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nodesource.com:443/docs/nsolid/quickstart/local
- group: auth
  href: https://artifacts.apis.io/nodesource/security/nodesource-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nodesource-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nodesource.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nodesource.com
- group: company
  title: ''
  type: Blog
  url: https://www.nodesource.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nodesource.com/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nodesource.com
coverage:
  checked: '2026-10-29'
  detail: Docs site serves OpenAPI endpoints as HTML pages, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://docs.nodesource.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: NodeSource provides enterprise-grade Node.js support, performance monitoring, and security tools. Their offerings include N|Solid runtime, AI-powered Copilot, professional services, training, and managed upgrades. They help organizations run high‑performance, secure Node.js applications at scale, with solutions for observability, security, and cloud‑native deployments.
image: https://nodesource.com/assets/social-share/nodesource-home.jpg
layout: provider
modified: '2026-10-29'
name: NodeSource
nav: Providers
network: true
overview: 'NodeSource is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Node.js, Enterprise, Monitoring, and Security.


  The NodeSource catalog on APIs.io includes 1 Spectral governance ruleset.


  NodeSource''s developer surface includes support, getting-started guide, documentation, engineering blog, pricing, API reference, and 11 more developer resources.'
plans:
- name: Nodesource Plans Pricing
  plan_count: 4
  slug: nodesource-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: NodeSource API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: nodesource-rules
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 17.9
    discoverability: 58.0
    operational_transparency: 2.6
  previous_composite: 29.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/nodesource/nodesource-2026-11-03T140243.png
security:
- kind: domain-security
  name: Nodesource Domain Security
  slug: nodesource-domain-security
  summary_line: TLSv1.2 · DMARC
slug: nodesource
tags:
- Company
- Node.js
- Enterprise
- Monitoring
- Security
- Performance
website: https://www.nodesource.com
---
