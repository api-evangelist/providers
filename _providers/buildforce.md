---
agent_readiness:
  band: agent-aware
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Buildforce platform, providing access to contractor and worker services.
  name: Buildforce API
  slug: buildforce-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/buildforce/refs/heads/main/plans/buildforce-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buildforce-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/buildforce/refs/heads/main/llms/buildforce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buildforce-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buildforce/refs/heads/main/well-known/buildforce-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buildforce-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/buildforce/refs/heads/main/well-known/buildforce-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buildforce-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/buildforce/refs/heads/main/hosts/buildforce-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildforce-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/buildforce/refs/heads/main/vendors/buildforce-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buildforce-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buildforce.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.buildforce.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buildforce.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.buildforce.com/contractor/pricing
- group: start
  title: ''
  type: Login
  url: https://worker-app.buildforce.com/sign-in
- group: company
  title: ''
  type: Blog
  url: https://www.buildforce.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.buildforce.com/faq/how-can-electrical-contractors-improve-their-onboarding-process
- group: docs
  title: ''
  type: Documentation
  url: https://help.buildforce.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buildforce/refs/heads/main/security/buildforce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildforce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.buildforce.com
coverage:
  checked: '2026-10-06'
  detail: No OpenAPI or other machine‑readable contract found at the API host despite probing known endpoints.
  evidence:
  - status: 404
    url: https://api.buildforce.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Buildforce provides a platform to staff and manage electricians, offering tools for hiring, project scheduling, time tracking, and workforce management. The easy‑to‑use solution helps contractors keep projects on schedule and within budget, backed by ongoing support from their team.
image: https://cdn.prod.website-files.com/65483d86257c910f7758cfa0/66036c0dbb6c7cff7d699d82_why_buildforce_contractor_opengraph.webp
layout: provider
modified: '2026-10-06'
name: Buildforce
nav: Providers
network: true
overview: 'Buildforce is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Staffing, WorkforceManagement, Electricians, and Construction.


  Buildforce''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
plans:
- name: Buildforce Plans Pricing
  plan_count: 2
  slug: buildforce-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 64.3
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buildforce Domain Security
  slug: buildforce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buildforce
tags:
- Company
- Staffing
- WorkforceManagement
- Electricians
- Construction
website: https://www.buildforce.com
---
