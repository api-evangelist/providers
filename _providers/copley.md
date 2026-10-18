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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/copley/refs/heads/main/llms/copley-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/copley-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/copley/refs/heads/main/hosts/copley-hosts.yml
  title: ''
  type: Hosts
  url: hosts/copley-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/copley/refs/heads/main/vendors/copley-vendors.yml
  title: ''
  type: Vendors
  url: vendors/copley-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/copley/refs/heads/main/security/copley-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/copley-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.copley.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.copley.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.copley.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.copley.com/legal/privacy/
- group: operate
  title: ''
  type: Support
  url: https://landing.copley.com/talk-to-sales
- group: company
  title: ''
  type: Blog
  url: https://www.copley.com/company.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.copley.com/signin
- group: start
  title: ''
  type: GettingStarted
  url: https://www.copley.com/what-is-demand-engineering.html
- group: start
  title: ''
  type: SignUp
  url: https://landing.copley.com/request-a-demo
coverage:
  checked: '2026-10-11'
  detail: The provider's openapi.json endpoint returns HTML instead of a machine‑readable spec.
  evidence:
  - status: 200
    url: https://app.copley.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Copley provides an AI Operating System for Demand Engineering, enabling companies to automate and optimize their marketing, sales, and product development processes through AI-driven analysis, planning, creation, and iteration of campaigns. The platform connects data from CRM, ad platforms, and analytics to generate actionable insights and continuously improve performance across channels.
image: https://www.copley.com/assets/og.png
layout: provider
modified: '2026-10-10'
name: Copley
nav: Providers
network: true
overview: 'Copley is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, Demand Engineering, Platform, and Software-as-a-Service.


  Copley''s developer surface includes documentation, support, engineering blog, getting-started guide, signup flow, and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Copley Domain Security
  slug: copley-domain-security
  summary_line: TLSv1.3 · DMARC
slug: copley
tags:
- Artificial Intelligence
- Marketing
- Demand Engineering
- Platform
- Software-as-a-Service
- Company
website: https://www.copley.com/
---
