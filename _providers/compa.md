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
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/compa/refs/heads/main/plans/compa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/compa-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/compa/refs/heads/main/conformance/compa-conformance.yml
  title: ''
  type: Conformance
  url: conformance/compa-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/compa/refs/heads/main/hosts/compa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compa-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/compa/refs/heads/main/vendors/compa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/compa-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.compa.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.compa.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.compa.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.compa.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.compa.ai/news
- group: docs
  title: ''
  type: Documentation
  url: https://www.compa.ai/guides/the-compensation-analysis-gap
- group: company
  title: ''
  type: Blog
  url: https://www.compa.ai/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/compa/refs/heads/main/security/compa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.compa.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://communityjobs.compa.ai/mcp
  - status: 200
    url: https://www.compa.ai/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Compa Technologies provides AI‑driven compensation intelligence for enterprises. Its platform aggregates live market data, compensation benchmarks, and analytics to help compensation teams make data‑backed pay decisions. Features include analyst and partner AI agents, real‑time market briefs, and integrations with Slack and Claude, serving over 2.8 million employees across 42 countries.
image: https://cdn.prod.website-files.com/6900a44412a9ffeab7804937/6939b86c58c5b9b32a472359_77ab8dee3d7ccc72bdc3ddb00333cb41_Social%20Share%20-%20Home%201.jpg
layout: provider
modified: '2026-10-09'
name: Compa
nav: Providers
network: true
overview: 'Compa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Compensation, Enterprise, and Analytics.


  Compa''s developer surface includes support, pricing, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Compa Plans Pricing
  plan_count: 3
  slug: compa-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Compa Domain Security
  slug: compa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: compa
tags:
- Company
- Artificial Intelligence
- Compensation
- Enterprise
- Analytics
website: https://www.compa.ai/
---
