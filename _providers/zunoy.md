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
    event_surface_described: unknown
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
  score: 7.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/zunoy/plans/zunoy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zunoy-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/zunoy/llms/zunoy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zunoy-llms.txt
- group: other
  href: https://artifacts.apis.io/zunoy/hosts/zunoy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zunoy-hosts.yml
- group: other
  href: https://artifacts.apis.io/zunoy/vendors/zunoy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zunoy-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://zunoy.com/bugtracker/integrations/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zunoy.com/policies/terms-and-conditions
- group: start
  title: ''
  type: Sandbox
  url: https://zunoy.com/sandbox
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zunoy.com/policies/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://zunoy.com/mockapi/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Zunoy
- group: auth
  href: https://artifacts.apis.io/zunoy/security/zunoy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zunoy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zunoy.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://zunoy.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Zunoy provides a cloud‑based platform for real‑time data integration, API management, and analytics. It enables businesses to connect, orchestrate, and monitor APIs across hybrid environments, offering features such as traffic routing, security policies, and detailed usage insights. The platform targets developers and enterprises seeking scalable API solutions with robust monitoring and governance capabilities.
image: https://zunoy.com/og/home.png
layout: provider
modified: '2026-10-21'
name: Zunoy
nav: Providers
network: true
overview: 'Zunoy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include API Management, Integration, Cloud Platform, Analytics, and Real-time.


  Zunoy''s developer surface includes sandbox, pricing, and 10 more developer resources.'
plans:
- name: Zunoy Plans Pricing
  plan_count: 4
  slug: zunoy-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 13.2
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
  name: Zunoy Domain Security
  slug: zunoy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zunoy
tags:
- API Management
- Integration
- Cloud Platform
- Analytics
- Real-time
website: https://zunoy.com/
---
