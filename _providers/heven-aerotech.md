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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heven-aerotech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hevenaerotech.com/
- group: company
  title: ''
  type: Blog
  url: https://hevenaerotech.com/resources/?tab=blogs
- group: company
  title: ''
  type: BlogRSS
  url: https://hevenaerotech.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hevenaerotech.com/wp-content/uploads/2026/08/Website-Terms-of-Use-Accessibility-Policy-Aug-26.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hevenaerotech.com/wp-content/uploads/2026/05/Privacy-Policy_HAI-13MAY26-5.pdf
- group: operate
  title: ''
  type: Contact
  url: https://hevenaerotech.com/contact-us/
- group: company
  title: ''
  type: About
  url: https://hevenaerotech.com/company/
- group: company
  title: ''
  type: Careers
  url: https://hevenaerotech.com/work-with-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hevenaerotech/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Hevenaerotech
- group: design
  title: ''
  type: Conformance
  url: conformance/heven-aerotech-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/heven-aerotech-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/heven-aerotech-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/heven-aerotech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/heven-aerotech-rate-limits.yml
coverage:
  checked: '2026-08-22'
  detail: 'Heven AeroTech is an aerospace hardware manufacturer whose product is the airframe: its entire web presence is a 15-page WordPress marketing site whose only machine-readable endpoint is the CMS''s own /wp-json/, with no api./docs./developer./portal. subdomain resolving in DNS and no /developers/, /api/ or /docs page in its sitemap.'
  evidence:
  - status: 404
    url: https://hevenaerotech.com/openapi.json
  - status: 404
    url: https://hevenaerotech.com/.well-known/agent-card.json
  - status: 404
    url: https://hevenaerotech.com/developers/
  - status: 200
    url: https://hevenaerotech.com/sitemap_index.xml
  - status: 200
    url: https://hevenaerotech.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'Heven AeroTech (formerly Heven Drones) is a Dulles, Virginia headquartered manufacturer of hydrogen fuel-cell powered, runway-independent unmanned aircraft systems built for defense, national security and public safety missions. Founded in 2019, the company designs its own hydrogen propulsion stack and ships six named airframes — Raider, Z1, H2D55, Refueler, Atlas and Urban X — marketed on multi-hour endurance, low thermal and acoustic signature, and rapid payload and hydrogen-tank swaps. The Z1 is listed as a Blue UAS Select platform and the H2D55, Raider and Z1 are advertised as NDAA compliant. Heven operates sites in Dulles VA, Bingen WA, Mevo Carmel Israel and Mumbai India, and raised a $100M Series B led by IonQ. Heven AeroTech is a hardware manufacturer: it publishes no public developer program, API, SDK or machine-readable contract.'
image: https://hevenaerotech.com/wp-content/uploads/2026/08/favicon-512x512-1.png
layout: provider
modified: '2026-08-22'
name: Heven AeroTech
nav: Providers
network: true
overview: 'Heven AeroTech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drones, Unmanned Aerial Systems, Aerospace, and Defense.


  Heven AeroTech''s developer surface includes engineering blog, YouTube channel, and 14 more developer resources.'
plans:
- name: Heven Aerotech Plans Pricing
  plan_count: 0
  slug: heven-aerotech-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Heven Aerotech Rate Limits
  slug: heven-aerotech-rate-limits
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.0
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Heven Aerotech Domain Security
  slug: heven-aerotech-domain-security
  summary_line: TLSv1.2 · DMARC
slug: heven-aerotech
tags:
- Company
- Drones
- Unmanned Aerial Systems
- Aerospace
- Defense
- National Security
- Public Safety
- Hydrogen
- Manufacturing
- Hardware
website: https://hevenaerotech.com/
---
