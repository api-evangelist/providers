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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for BlackBoiler contract review platform
  name: BlackBoiler API
  slug: blackboiler-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/blackboiler/refs/heads/main/plans/blackboiler-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blackboiler-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blackboiler/refs/heads/main/llms/blackboiler-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blackboiler-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackboiler/refs/heads/main/hosts/blackboiler-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blackboiler-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackboiler/refs/heads/main/vendors/blackboiler-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blackboiler-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blackboiler.com/terms/
- group: auth
  title: ''
  type: Security
  url: https://blackboiler.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blackboiler.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://blackboiler.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://blackboiler.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BlackBoiler
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackboiler/refs/heads/main/security/blackboiler-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blackboiler-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blackboiler.com/
coverage:
  checked: '2026-09-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found at common API endpoints.
  evidence:
  - status: error
    url: https://api.blackboiler.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: BlackBoiler provides AI-powered contract review software that automatically applies a company’s playbook, prior redlines, and approved language as first‑pass tracked changes in Microsoft Word. The platform leverages patented NLP technology to improve contract review speed and consistency, offering features such as playbook‑driven markup, SOC 2 compliance reporting, and integration with legal workflows. Founded in 2016, BlackBoiler serves legal teams, law firms, and enterprises seeking automated, standards‑based contract editing.
image: https://blackboiler.com/redesign/assets/og/ai-review.webp
layout: provider
modified: '2026-09-29'
name: BlackBoiler
nav: Providers
network: true
overview: 'BlackBoiler publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Tech, Artificial Intelligence, Contract Automation, Software-as-a-Service, and Enterprise.


  BlackBoiler''s developer surface includes pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Blackboiler Plans Pricing
  plan_count: 3
  slug: blackboiler-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blackboiler Domain Security
  slug: blackboiler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blackboiler
tags:
- Legal Tech
- Artificial Intelligence
- Contract Automation
- Software-as-a-Service
- Enterprise
website: https://blackboiler.com/
---
