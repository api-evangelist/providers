---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/merico-dev/plans/merico-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/merico-dev-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/merico-dev/hosts/merico-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/merico-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/merico-dev/vendors/merico-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/merico-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/merico-dev/security/merico-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/merico-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.devinsight.ai
- group: company
  title: ''
  type: Blog
  url: https://www.devinsight.ai/blog/home
- group: commercial
  title: ''
  type: Pricing
  url: https://www.devinsight.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.devinsight.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.devinsight.ai/privacy-policy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://merico.dev
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: DevInsight provides an engineering intelligence platform that ingests and analyzes data from DevOps tools such as GitHub and Jira to deliver DORA metrics, dashboards, alerts and reports. It serves engineering teams and leaders who need to measure, visualize and improve DevOps performance and throughput. The platform includes the open‑source Apache DevLake data platform for custom queries and integrations.
layout: provider
modified: '2026-10-28'
name: Merico
nav: Providers
network: true
overview: 'Merico is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Technology, Analytics, DeveloperTools, DevOps, and SoftwareEngineering.


  Merico''s developer surface includes engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Merico Dev Plans Pricing
  plan_count: 1
  slug: merico-dev-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Merico Dev Domain Security
  slug: merico-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: merico-dev
tags:
- Technology
- Analytics
- DeveloperTools
- DevOps
- SoftwareEngineering
website: https://www.devinsight.ai
---
