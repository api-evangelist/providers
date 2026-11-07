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
api_count: 1
apis:
- description: DashThis provides automated marketing reporting software with integrations to over 30 marketing tools.
  name: DashThis API
  slug: dashthis-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dashthis-com/plans/dashthis-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dashthis-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dashthis-com/changelog/dashthis-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dashthis-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/dashthis-com/conformance/dashthis-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dashthis-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/dashthis-com/hosts/dashthis-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dashthis-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dashthis-com/vendors/dashthis-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dashthis-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dashthis.com/terms-and-conditions/
- group: auth
  title: ''
  type: Security
  url: https://dashthis.com/app/admin/security/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dashthis.com/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://help.dashthis.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DashThis
- group: auth
  href: https://artifacts.apis.io/dashthis-com/security/dashthis-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dashthis-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dashthis.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://dashthis.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://dashthis.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://dashthis.com/about/
coverage:
  checked: '2026-11-04'
  detail: The provider's documentation pages are HTML without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://dashthis.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: DashThis provides automated marketing reporting software that connects to over 30 marketing tools, allowing agencies and teams to create client‑ready dashboards in minutes. The platform emphasizes ease‑of‑use, fast data aggregation, and dedicated support, aiming to simplify reporting workflows for digital marketers.
image: https://dashthis.com/media/5446/website_og-1.png
layout: provider
modified: '2026-11-04'
name: DashThis
nav: Providers
network: true
overview: 'DashThis is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing Reporting, Dashboard Software, Agency Tools, White Label Reporting, and AI Insights.


  DashThis'' developer surface includes changelog, documentation, pricing, engineering blog, getting-started guide, and 10 more developer resources.'
plans:
- name: Dashthis Com Plans Pricing
  plan_count: 8
  slug: dashthis-com-plans-pricing
random_paper: 20
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dashthis Com Domain Security
  slug: dashthis-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dashthis-com
tags:
- Marketing Reporting
- Dashboard Software
- Agency Tools
- White Label Reporting
- AI Insights
- Integration
website: https://dashthis.com/
---
