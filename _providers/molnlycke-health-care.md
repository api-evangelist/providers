---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/molnlycke-health-care/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/molnlycke-health-care/refs/heads/main/hosts/molnlycke-health-care-hosts.yml
  title: ''
  type: Hosts
  url: hosts/molnlycke-health-care-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/molnlycke-health-care/refs/heads/main/vendors/molnlycke-health-care-vendors.yml
  title: ''
  type: Vendors
  url: vendors/molnlycke-health-care-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.molnlycke.com/corporate/privacy-centre/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://www.molnlycke.com/en-us/us/campaign/wound-care/avance-solo-2/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.molnlycke.com/corporate/privacy-centre/
- group: company
  title: ''
  type: Newsroom
  url: https://www.molnlycke.com/corporate/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/molnlycke-health-care/refs/heads/main/security/molnlycke-health-care-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/molnlycke-health-care-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.molnlycke.com/
coverage:
  checked: '2026-10-12'
  detail: Developer portal at https://portal.molnlycke.com is a JavaScript‑rendered single‑page app with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 404
    url: https://portal.molnlycke.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Molnlycke Health Care is a world‑leading MedTech company based in Sweden, providing innovative wound‑care and surgical solutions. It focuses on improving patient outcomes and supporting healthcare professionals with high‑quality products, sustainability initiatives, and extensive clinical expertise. The company’s corporate site offers information on its portfolio, sustainability, careers, and investor relations, reflecting its commitment to advancing healthcare worldwide.
image: https://www.molnlycke.com/contentassets/47fd1dd669f74ebe834bfd7eaeef45c8/market_home_01.mp4
layout: provider
modified: '2026-10-12'
name: Molnlycke Health Care
nav: Providers
network: true
overview: 'Molnlycke Health Care is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Technology, WoundCare, SurgicalSolutions, and Sustainability.


  Molnlycke Health Care''s developer surface includes support and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.2
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Molnlycke Health Care Domain Security
  slug: molnlycke-health-care-domain-security
  summary_line: TLSv1.3 · DMARC
slug: molnlycke-health-care
tags:
- Company
- Medical Technology
- WoundCare
- SurgicalSolutions
- Sustainability
website: https://www.molnlycke.com/
---
