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
api_count: 1
apis:
- description: API documentation for CeQur Simplicity wearable insulin patch platform.
  name: CeQur API
  slug: cequr-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cequr/refs/heads/main/hosts/cequr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cequr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cequr/refs/heads/main/vendors/cequr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cequr-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://myceqursimplicity.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://myceqursimplicity.com/pricedup-casino-no-deposit-bonus-opportunities-in-the-uk/
- group: other
  title: ''
  type: Leadership
  url: https://myceqursimplicity.com/leadership/
- group: start
  title: ''
  type: GettingStarted
  url: https://myceqursimplicity.com/getting-started/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cequr/refs/heads/main/security/cequr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cequr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://myceqursimplicity.com
coverage:
  checked: '2026-10-07'
  detail: Developer docs are served as a JavaScript‑rendered site, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://myceqursimplicity.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: CeQur is a Swiss medical device company founded in 2008 that develops the CeQur Simplicity wearable insulin patch, a needle‑free, patch‑based solution for mealtime insulin delivery. The device provides discreet, convenient bolus dosing for people on multiple daily injections, with extended wear up to seven days and options for 1‑unit and 2‑unit dosing. CeQur has raised significant Series D/E funding and operates globally, focusing on improving diabetes management through innovative, patient‑centric technology.
image: https://myceqursimplicity.com/wp-content/uploads/Website-Banner_Rich-03_762x400.jpg
layout: provider
modified: '2026-10-07'
name: Cequr
nav: Providers
network: true
overview: 'Cequr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Diabetes, WearableTech, and InsulinPatch.


  Cequr''s developer surface includes pricing, getting-started guide, and 6 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cequr Domain Security
  slug: cequr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cequr
tags:
- Company
- Medical Devices
- Diabetes
- WearableTech
- InsulinPatch
website: https://myceqursimplicity.com
---
