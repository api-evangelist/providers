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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Pyas Webhooks
  slug: pyas-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/pyas/plans/pyas-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pyas-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pyas/asyncapi/pyas-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/pyas-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/pyas/llms/pyas-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pyas-llms.txt
- group: agent
  href: https://artifacts.apis.io/pyas/well-known/pyas-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pyas-well-known.yml
- group: other
  href: https://artifacts.apis.io/pyas/hosts/pyas-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pyas-hosts.yml
- group: other
  href: https://artifacts.apis.io/pyas/vendors/pyas-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pyas-vendors.yml
- group: build
  href: https://artifacts.apis.io/pyas/packages/pyas-packages.yml
  title: ''
  type: SDKs
  url: packages/pyas-packages.yml
- group: build
  href: https://artifacts.apis.io/pyas/packages/pyas-packages.yml
  title: ''
  type: Packages
  url: packages/pyas-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pyas.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pyas.io/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pyas.io/getting-started-with-pyas
- group: auth
  href: https://artifacts.apis.io/pyas/security/pyas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pyas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pyas.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pyas.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://pyas.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://pyas.io/blog
- group: operate
  title: ''
  type: Support
  url: https://pyas.io/support
coverage:
  checked: '2026-10-21'
  detail: Documentation at https://docs.pyas.io/ is a Gitbook site rendered via JavaScript, providing no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.pyas.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: BrutForce Technologies, operating under the brand Pyas, provides a Calendar Integrations API that enables startups to quickly embed Google Calendar, Microsoft Outlook, Zoom, and Google Meet scheduling and video conferencing capabilities. The platform offers a unified API to manage events, attendees, and meeting links, reducing development time from months to minutes. It targets SaaS startups seeking seamless calendar and video integration.
image: https://www.pyas.io/static/pyas-logo.svg
layout: provider
modified: '2026-10-21'
name: BrutForce Technologies
nav: Providers
network: true
overview: 'BrutForce Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Calendar, Integration, API, and Startup.


  The BrutForce Technologies catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  BrutForce Technologies'' developer surface includes getting-started guide, documentation, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Pyas Plans Pricing
  plan_count: 4
  slug: pyas-plans-pricing
random_paper: 13
score:
  band: thin
  composite: 35.2
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
    contract_quality: 39.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 7.9
  provenance:
    mcp: derived
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
  name: Pyas Domain Security
  slug: pyas-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pyas
tags:
- Company
- Calendar
- Integration
- API
- Startup
- SaaS
website: https://pyas.io/
---
