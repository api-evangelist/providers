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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vytalize-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vytalizehealth.com/
- group: start
  title: ''
  type: Login
  url: https://app.vytalizehealth.com/
- group: operate
  title: ''
  type: Support
  url: https://www.vytalizehealth.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.vytalizehealth.com/resources/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vytalizehealth.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vytalizehealth
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vytalize-health-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/vytalize-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vytalize-health-rate-limits.yml
coverage:
  checked: '2026-09-04'
  detail: Vytalize Health ships software only to signed-on practice partners through an Entra ID login at app.vytalizehealth.com; the product backend that portal calls (prod-banzai-services.vytalizehealth.com, an AWS ELB) drops public TCP connections on 443 on every published address, and the company's only openly reachable machine-readable API is the marketing site's WordPress REST index at www.vytalizehealth.com/wp-json/, which is CMS infrastructure and not a Vytalize product.
  evidence:
  - status: 0
    url: https://prod-banzai-services.vytalizehealth.com/
  - status: 200
    url: https://www.vytalizehealth.com/page-sitemap.xml
  - status: 404
    url: https://www.vytalizehealth.com/.well-known/api-catalog
  - status: 404
    url: https://www.vytalizehealth.com/openapi.json
  - status: 404
    url: https://app.vytalizehealth.com/.well-known/agent-card.json
  - status: 200
    url: https://www.vytalizehealth.com/wp-json/
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: 'Vytalize Health is a Hoboken, New Jersey based value-based care company that operates as a Medicare Accountable Care Organization (ACO), partnering with independent primary care practices, group practices, community health centers and existing ACOs to move them into risk-bearing Medicare programs. The company pairs shared-savings economics with a technology and clinical services stack: Vytal Insights, a physician-built clinical decision support product that analyzes claims data, clinical notes, hospital admission-discharge-transfer feeds and social determinants of health to surface point-of-care recommendations; Vytal Care, a suite of remote and in-home programs (transitions of care, chronic disease management, home health review) delivered by an interdisciplinary team of RN care managers, health coaches, pharmacists and licensed clinical social workers; and Vytal Network, its specialist, hospital and ancillary provider network layer. Vytalize supports tens of thousands of
  Medicare beneficiaries across multiple states. Its software reaches practice partners through an authenticated web portal at app.vytalizehealth.com rather than through a public developer platform.'
image: https://www.vytalizehealth.com/wp-content/uploads/2018/10/vytalizelogofooter.png
layout: provider
modified: '2026-09-04'
name: Vytalize Health
nav: Providers
network: true
overview: 'Vytalize Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Value Based Care, Accountable Care Organization, and Medicare.


  Vytalize Health''s developer surface includes support, engineering blog, and 8 more developer resources.'
plans:
- name: Vytalize Health Plans Pricing
  plan_count: 0
  slug: vytalize-health-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Vytalize Health Rate Limits
  slug: vytalize-health-rate-limits
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Vytalize Health Authentication
  slug: vytalize-health-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Vytalize Health Domain Security
  slug: vytalize-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vytalize-health
tags:
- Company
- Healthcare
- Value Based Care
- Accountable Care Organization
- Medicare
- Population Health
- Clinical Decision Support
- Care Management
- Health Data
website: https://www.vytalizehealth.com/
---
