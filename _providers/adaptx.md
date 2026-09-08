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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.adaptx.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adaptx.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.adaptx.com/request-info
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MDmetrix
- group: company
  title: ''
  type: Newsroom
  url: https://www.adaptx.com/news
- group: auth
  title: ''
  type: Compliance
  url: conformance/adaptx-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adaptx-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adaptx-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adaptx-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adaptx-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adaptx-rate-limits.yml
coverage:
  checked: '2026-09-07'
  detail: AdaptX sells a hosted clinical-analytics application that its own team wires into a health system's EMR under contract — its 74-URL sitemap contains no developer, API, or docs page, /developers /api /docs all 404, and api./app./developer./docs.adaptx.com do not resolve in public DNS at all, so there is no developer program to gate or to read.
  evidence:
  - status: 404
    url: https://www.adaptx.com/developers
  - status: 404
    url: https://www.adaptx.com/docs
  - status: 404
    url: https://www.adaptx.com/openapi.json
  - status: 404
    url: https://www.adaptx.com/.well-known/api-catalog
  - status: 200
    url: https://www.adaptx.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-09-07'
description: AdaptX is a Seattle-based clinical performance management company (founded 2016 as MDMetrix, renamed AdaptX in 2021) whose self-serve platform reads a hospital's existing electronic medical record data and turns it into near-real-time analytics that clinical, quality, operational and finance leaders use to measure and reduce clinical variation. Customers include Seattle Children's, Memorial Hermann, Children's Minnesota, USA Health and Kittitas Valley Healthcare, with published case studies covering surgical capacity, emergency department time-to-triage, length of stay, anesthetic greenhouse-gas reduction and health-equity stratification. The product is delivered as a hosted SaaS application on AWS to contracted health systems; as of this profiling pass AdaptX publishes no public developer portal, API reference, or machine-readable API description.
image: https://cdn.prod.website-files.com/60a92df620b4624c09b5ac26/60fdb4f81a5ab2a0549dfbd7_Adaptx_webclip-01.png
layout: provider
modified: '2026-09-07'
name: AdaptX
nav: Providers
network: true
overview: 'AdaptX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Healthcare Analytics, Clinical Data, and Electronic Medical Records.


  AdaptX''s developer surface includes support and 10 more developer resources.'
plans:
- name: Adaptx Plans Pricing
  plan_count: 0
  slug: adaptx-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Adaptx Rate Limits
  slug: adaptx-rate-limits
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adaptx Domain Security
  slug: adaptx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adaptx
tags:
- Company
- Health Care
- Healthcare Analytics
- Clinical Data
- Electronic Medical Records
- Hospital Operations
- Quality Improvement
- Business Intelligence
- SaaS
- Seattle
website: https://www.adaptx.com/
---
