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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aquifer-motion/refs/heads/main/plans/aquifer-motion-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aquifer-motion-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquifer-motion/refs/heads/main/hosts/aquifer-motion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aquifer-motion-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquifer-motion/refs/heads/main/vendors/aquifer-motion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aquifer-motion-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aquifermotion.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aquifermotion.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aquifermotion.com/plans
- group: company
  title: ''
  type: Blog
  url: https://www.aquifermotion.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aquifer-motion/refs/heads/main/security/aquifer-motion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aquifer-motion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aquifermotion.com/
coverage:
  checked: 2026-09-25
  detail: No public API documentation or machine‑readable contract was found for Aquifer Motion.
  evidence:
  - status: 0
    url: https://api.aquifermotion.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: Aquifer Motion provides an instant animation platform enabling brands and creators to produce studio‑quality animated videos quickly, without needing animation expertise. The SaaS solution offers text‑to‑animation, automatic lip‑sync, facial expressions, body movements, and export options for social media, marketing, education, and entertainment, empowering teams to create dynamic content at scale.
layout: provider
modified: '2026-09-25'
name: Aquifer Motion
nav: Providers
network: true
overview: 'Aquifer Motion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Animation, Software-as-a-Service, Media, Marketing, and Education.


  Aquifer Motion''s developer surface includes pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Aquifer Motion Plans Pricing
  plan_count: 4
  slug: aquifer-motion-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aquifer Motion Domain Security
  slug: aquifer-motion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aquifer-motion
tags:
- Animation
- Software-as-a-Service
- Media
- Marketing
- Education
- Company
website: https://www.aquifermotion.com/
---
