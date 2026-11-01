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
  href: https://artifacts.apis.io/docketwise/plans/docketwise-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docketwise-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/docketwise/llms/docketwise-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docketwise-llms.txt
- group: auth
  href: https://artifacts.apis.io/docketwise/well-known/docketwise-supportcenter-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/docketwise-supportcenter-security.txt
- group: auth
  href: https://artifacts.apis.io/docketwise/well-known/docketwise-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/docketwise-support-security.txt
- group: agent
  href: https://artifacts.apis.io/docketwise/well-known/docketwise-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docketwise-well-known.yml
- group: other
  href: https://artifacts.apis.io/docketwise/hosts/docketwise-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docketwise-hosts.yml
- group: other
  href: https://artifacts.apis.io/docketwise/vendors/docketwise-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docketwise-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.docketwise.com/en/
- group: auth
  title: ''
  type: Security
  url: https://www.docketwise.com/security/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.docketwise.com/events/onboarding/
- group: auth
  href: https://artifacts.apis.io/docketwise/security/docketwise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docketwise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docketwise.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.docketwise.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.docketwise.com/developers/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.docketwise.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.docketwise.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docketwise.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docketwise.com/privacy/
coverage:
  checked: '2026-10-28'
  detail: The developer portal provides only HTML pages without any OpenAPI, AsyncAPI, GraphQL, or other machine‑readable specifications.
  evidence:
  - status: 200
    url: https://www.docketwise.com/developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Docketwise provides cloud-based immigration law practice management software, enabling attorneys to manage cases, clients, and documents efficiently. The platform offers tools for client intake, case tracking, document generation, and collaboration, helping firms streamline immigration workflows and improve client experiences.
image: https://media.ffycdn.net/us/affinipay/x1pDVJrynUxDwgKoUWHj.webp
layout: provider
modified: '2026-10-28'
name: Docketwise
nav: Providers
network: true
overview: 'Docketwise is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Immigration, Law, SaaS, and Software.


  Docketwise''s developer surface includes support, getting-started guide, documentation, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Docketwise Plans Pricing
  plan_count: 3
  slug: docketwise-plans-pricing
random_paper: 18
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 48.2
    operational_transparency: 10.5
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
  name: Docketwise Domain Security
  slug: docketwise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: docketwise
tags:
- Company
- Immigration
- Law
- SaaS
- Software
- Management
website: https://docketwise.com/
---
