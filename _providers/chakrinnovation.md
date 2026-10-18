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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chakrinnovation/refs/heads/main/llms/chakrinnovation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chakrinnovation-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chakrinnovation/refs/heads/main/hosts/chakrinnovation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chakrinnovation-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chakr.in/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chakrinnovation/refs/heads/main/security/chakrinnovation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chakrinnovation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chakr.in
- group: docs
  title: ''
  type: Documentation
  url: https://chakr.in/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://chakr.in/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://chakr.in/posts/
coverage:
  checked: 2026-10-08 'Chakr Innovation Pvt. Ltd. is an Indian cleantech startup focused on emission reduction technologies for diesel generators and industrial applications. Founded by IIT Delhi graduates, the company offers products such as Chakr Shield, a CPCB Type‑Approved Retrofit Emission Control Device that can cut diesel generator emissions by up to 90%, along with energy storage and air‑purification solutions. It serves industries and cities aiming to improve air quality and meet strict environmental standards, and has received recognition from the United Nations, WWF, and Forbes.'
  detail: The website https://chakr.in returns HTML with no machine‑readable API specification or developer documentation.
  evidence:
  - status: 200
    url: https://chakr.in
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Chakr Innovation manufactures retrofit emission control devices (RECD) and related clean‑air technologies for diesel generators, including the Chakr Shield, Dual Fuel Kit 2.0, DeNOx, DeSmog dust suppression, and real‑time emission monitoring systems. It also offers aluminium‑air battery energy storage solutions. Its customers are large corporates, industrial facilities, real‑estate developers, institutions and public‑sector organisations across India that need to meet air‑quality regulations.
image: https://chakr.in/wp-content/uploads/2025/07/logo-CI-2-1024x1024.png
layout: provider
modified: '2026-10-08'
name: Chakrinnovation
nav: Providers
network: true
overview: 'Chakrinnovation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cleantech, Emission Reduction, India, and Startups.


  Chakrinnovation''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chakrinnovation Domain Security
  slug: chakrinnovation-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chakrinnovation
tags:
- Company
- Cleantech
- Emission Reduction
- India
- Startups
website: https://chakr.in
---
