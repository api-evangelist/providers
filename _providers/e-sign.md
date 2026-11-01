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
api_count: 0
artifact_total: 2
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://esign.co.uk/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://esign.co.uk/privacy/
- group: commercial
  href: https://artifacts.apis.io/e-sign/plans/e-sign-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/e-sign-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/e-sign/llms/e-sign-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/e-sign-llms.txt
- group: other
  href: https://artifacts.apis.io/e-sign/hosts/e-sign-hosts.yml
  title: ''
  type: Hosts
  url: hosts/e-sign-hosts.yml
- group: other
  href: https://artifacts.apis.io/e-sign/vendors/e-sign-vendors.yml
  title: ''
  type: Vendors
  url: vendors/e-sign-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.esign.co.uk/register/
- group: auth
  title: ''
  type: Security
  url: https://www.esign.co.uk/resources/security/
- group: auth
  href: https://artifacts.apis.io/e-sign/security/e-sign-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/e-sign-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://e-sign.co.uk/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.esign.co.uk/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.esign.co.uk/contact-us/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://e-sign.co.uk/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: E‑Sign provides secure, advanced electronic signature solutions for UK and EU organisations, offering legally‑binding, audit‑ready signatures that meet industry regulations such as eIDAS, GDPR, and sector‑specific standards. Their platform supports high‑value transactions across healthcare, finance, legal, government and education, with features like digital certificates, electronic seals, identity verification, and integrated payment processing. The service includes a robust API, extensive integrations (e.g., Microsoft Dynamics, Salesforce, Zapier), and a compliance‑focused Trust Centre, aiming to protect data residency in ISO‑27001‑certified UK data centres.
layout: provider
modified: '2026-10-20'
name: E-Sign
nav: Providers
network: true
overview: 'E-Sign is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ElectronicSignature, Compliance, API, and UK.


  E-Sign''s developer surface includes signup flow, pricing, support, and 9 more developer resources.'
plans:
- name: E Sign Plans Pricing
  plan_count: 4
  slug: e-sign-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: derived
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
  name: E Sign Domain Security
  slug: e-sign-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: e-sign
tags:
- Company
- ElectronicSignature
- Compliance
- API
- UK
website: https://e-sign.co.uk/
---
