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
artifact_total: 1
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/biobotsurgicalpteltd/refs/heads/main/conformance/biobotsurgicalpteltd-conformance.yml
  title: ''
  type: Conformance
  url: conformance/biobotsurgicalpteltd-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biobotsurgicalpteltd/refs/heads/main/hosts/biobotsurgicalpteltd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biobotsurgicalpteltd-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biobotsurgicalpteltd/refs/heads/main/security/biobotsurgicalpteltd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biobotsurgicalpteltd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biobotsurgical.com
- group: docs
  title: ''
  type: Documentation
  url: https://biobotsurgical.com/technology/
- group: company
  title: ''
  type: About
  url: https://biobotsurgical.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://biobotsurgical.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biobotsurgical.com/privacy-policy
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/biobotsurgical
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/biobotmonalisa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/biobot-surgical-pte-ltd/
coverage:
  checked: '2026-09-28'
  detail: Documentation pages are rendered via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://biobotsurgical.com/technology/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Biobot Surgical Pte Ltd is a Singapore‑based medical technology company focused on robotic‑assisted prostate biopsy and treatment solutions. Their flagship Mona Lisa system provides sub‑millimetre accuracy for transperineal procedures, aiming to improve cancer detection and patient outcomes. With regulatory clearances across the US, EU, China and Australia, the company reports over 23,000 procedures performed worldwide and a growing pipeline of new indications and digital health services.
image: https://biobotsurgical.com/wp-content/uploads/2024/02/Biobot_Logo_WEB_BLACK.svg
layout: provider
modified: '2026-09-28'
name: Biobotsurgicalpteltd
nav: Providers
network: true
overview: 'Biobotsurgicalpteltd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical, Robotics, Healthcare, and Singapore.


  Biobotsurgicalpteltd''s developer surface includes documentation and 10 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biobotsurgicalpteltd Domain Security
  slug: biobotsurgicalpteltd-domain-security
  summary_line: TLSv1.3 · DMARC
slug: biobotsurgicalpteltd
tags:
- Company
- Medical
- Robotics
- Healthcare
- Singapore
website: https://biobotsurgical.com
---
