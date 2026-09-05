---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medix-infusion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://medixinfusion.com/
- group: operate
  title: ''
  type: Support
  url: https://medixinfusion.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://medixinfusion.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://medixinfusion.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/medix-infusion
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medix-infusion-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/medix-infusion-conformance.yml
coverage:
  checked: '2026-08-25'
  detail: Medix Infusion runs ambulatory infusion suites and in-home infusion nursing — the product is clinical care billed through a patient's medical or pharmacy benefit — and its entire public surface is one WordPress marketing site with no /developers, /docs or /api path; the only machine-readable thing on the domain is the default WordPress wp-json REST index that ships with the CMS.
  evidence:
  - status: 404
    url: https://medixinfusion.com/developers
  - status: 404
    url: https://medixinfusion.com/openapi.json
  - status: 404
    url: https://medixinfusion.com/graphql
  - status: 404
    url: https://medixinfusion.com/.well-known/agent-card.json
  - status: 200
    url: https://medixinfusion.com/llms.txt
  - status: 200
    url: https://medixinfusion.com/wp-json
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'Medix Infusion, Inc. is a technology-enabled infusion care provider headquartered in Addison, Texas, that administers infusion and injectable therapies — anti-infectives, biologics, IVIG and other specialty medications — to chronically and acutely ill patients through a network of ambulatory infusion suites and in the home. The company concentrates on rural, suburban and other under-served markets, coordinating benefits investigation, prior authorization, scheduling, pharmacy and nursing around each referral, and is accredited by the Accreditation Commission for Health Care (ACHC). It raised a $35M Series B led by Echo Health Ventures in January 2023 alongside existing investor Noro-Moseley Partners. Medix Infusion operates as a care-delivery organization: it publishes no developer portal, no API documentation and no machine-readable API contract on any public host as of this profile.'
image: https://medixinfusion.com/wp-content/uploads/2023/01/medix-infusion-logo-horizontal.svg
layout: provider
modified: '2026-08-25'
name: Medix Infusion
nav: Providers
network: true
overview: 'Medix Infusion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Infusion Therapy, Specialty Pharmacy, and Home Health.


  Medix Infusion''s developer surface includes support and 7 more developer resources.'
plans:
- name: Medix Infusion Plans Pricing
  plan_count: 0
  slug: medix-infusion-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Medix Infusion Rate Limits
  slug: medix-infusion-rate-limits
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medix-infusion/refs/heads/main/screenshots/medix-infusion-2026-09-02T150455.png
security:
- kind: domain-security
  name: Medix Infusion Domain Security
  slug: medix-infusion-domain-security
  summary_line: TLSv1.3 · DMARC
slug: medix-infusion
tags:
- Company
- Healthcare
- Infusion Therapy
- Specialty Pharmacy
- Home Health
- Ambulatory Care
- Patient Care
- Texas
website: https://medixinfusion.com/
---
