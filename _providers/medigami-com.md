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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Medigami health technology services, providing imaging data and analytics integration.
  name: Medigami API
  slug: medigami-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/medigami-com/plans/medigami-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/medigami-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/medigami-com/security/medigami-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/medigami-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/medigami-com/llms/medigami-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/medigami-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/medigami-com/well-known/medigami-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/medigami-com-security.txt
- group: auth
  href: https://artifacts.apis.io/medigami-com/well-known/medigami-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/medigami-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/medigami-com/well-known/medigami-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/medigami-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/medigami-com/hosts/medigami-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/medigami-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/medigami-com/vendors/medigami-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/medigami-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://medigami.com/guides/glp1-costs
- group: auth
  href: https://artifacts.apis.io/medigami-com/security/medigami-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/medigami-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/medigami-com/security/medigami-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/medigami-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://medigami.com/
coverage:
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://medigami.com/guides/glp1-costs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Medigami is a health technology company focused on providing innovative medical imaging solutions and data analytics platforms for healthcare providers. The company offers a suite of APIs that enable integration of imaging data, patient records, and analytics dashboards, facilitating streamlined workflows and improved diagnostic accuracy. Medigami’s services aim to enhance interoperability across radiology systems, support AI-driven image analysis, and deliver secure, compliant data exchange for hospitals and clinics.
image: https://medigami.com/icon-192.png
layout: provider
modified: '2026-10-30'
name: medigami-com
nav: Providers
network: true
overview: 'medigami-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include HealthTech, Imaging, DataAnalytics, API, and Healthcare.


  medigami-com''s developer surface includes documentation and 11 more developer resources.'
plans:
- name: Medigami Com Plans Pricing
  plan_count: 4
  slug: medigami-com-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Medigami Com Domain Security
  slug: medigami-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Medigami Com Vulnerability Disclosure
  slug: medigami-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: medigami-com
tags:
- HealthTech
- Imaging
- DataAnalytics
- API
- Healthcare
website: https://medigami.com/
---
