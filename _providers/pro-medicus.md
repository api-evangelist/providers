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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/pro-medicus/conformance/pro-medicus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pro-medicus-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pro-medicus/well-known/pro-medicus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pro-medicus-well-known.yml
- group: other
  href: https://artifacts.apis.io/pro-medicus/hosts/pro-medicus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pro-medicus-hosts.yml
- group: auth
  href: https://artifacts.apis.io/pro-medicus/security/pro-medicus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pro-medicus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.promed.com.au/
- group: company
  title: ''
  type: About
  url: https://www.promed.com.au/about/
- group: operate
  title: ''
  type: Support
  url: https://www.promed.com.au/support/
- group: operate
  title: ''
  type: Contact
  url: https://www.promed.com.au/contact/
- group: company
  title: ''
  type: Newsroom
  url: https://www.promed.com.au/news/
- group: other
  title: ''
  type: Events
  url: https://www.promed.com.au/events/
- group: other
  title: ''
  type: Leadership
  url: https://www.promed.com.au/about/management/
- group: auth
  title: ''
  type: Compliance
  url: https://www.promed.com.au/about/compliance/
- group: company
  title: ''
  type: Investors
  url: https://www.promed.com.au/investors/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.promed.com.au/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.promed.com.au/privacy-statement/
created: '2026-10-22'
description: 'Pro Medicus Limited (promed.com.au) is an Australian imaging IT provider delivering services and solutions to hospitals, imaging centres and healthcare groups worldwide. It builds radiology information systems (RIS), picture archiving and communication systems (PACS) and advanced visualization software under the Visage brand: Visage RIS, Visage RIS/PACS, Visage 7, Visage Ease Pro and Visage Ease. No public developer API, API documentation or developer portal was found on its website. Originally surfaced via the API Evangelist harvest backlog (australia-apidays-2026).'
image: https://www.promed.com.au/wp-content/uploads/2015/02/Retina.png
layout: provider
modified: '2026-10-22'
name: Pro Medicus
nav: Providers
network: true
overview: 'Pro Medicus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Imaging, Radiology, and PACS.


  Pro Medicus'' developer surface includes support and 14 more developer resources.'
plans:
- name: Pro Medicus Plans Pricing
  plan_count: 0
  slug: pro-medicus-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Pro Medicus Rate Limits
  slug: pro-medicus-rate-limits
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 51.8
    operational_transparency: 0.0
  previous_composite: 12.9
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pro Medicus Domain Security
  slug: pro-medicus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pro-medicus
tags:
- Company
- Healthcare
- Medical Imaging
- Radiology
- PACS
- RIS
- Health IT
- Australia
website: https://www.promed.com.au/
---
