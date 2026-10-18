---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Compasscoffee e‑commerce platform
  name: Compasscoffee API
  slug: compasscoffee-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/compasscoffee/refs/heads/main/llms/compasscoffee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/compasscoffee-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/compasscoffee/refs/heads/main/well-known/compasscoffee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/compasscoffee-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/compasscoffee/refs/heads/main/hosts/compasscoffee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compasscoffee-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/compasscoffee/refs/heads/main/vendors/compasscoffee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/compasscoffee-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.compasscoffee.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.compasscoffee.com/policies/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/compasscoffee/refs/heads/main/security/compasscoffee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compasscoffee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.compasscoffee.com
created: '2026-10-09'
description: Compasscoffee is a Washington, D.C.-based specialty coffee roaster and retailer offering a range of freshly roasted beans, single‑serve pods, and ready‑to‑drink coffee. Their online store provides subscription options, bulk purchases, and a loyalty program, while their physical cafés serve espresso drinks and pastries. The company emphasizes sustainable sourcing, direct trade relationships with farmers, and community engagement through coffee education and events.
image: http://www.compasscoffee.com/cdn/shop/files/2022_Compass_Coffee_Circle_Logo_12fd250c-18cc-4371-b0b5-bdce827e569d.png?v=1661638717
layout: provider
modified: '2026-10-09'
name: Compasscoffee
nav: Providers
network: true
overview: Compasscoffee is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Coffee, Specialty, Retail, Subscription, and WashingtonDC.
random_paper: 10
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 73.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Compasscoffee Domain Security
  slug: compasscoffee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: compasscoffee
tags:
- Coffee
- Specialty
- Retail
- Subscription
- WashingtonDC
website: https://www.compasscoffee.com
---
