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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/karolinska-institutet/refs/heads/main/security/karolinska-institutet-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/karolinska-institutet-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/karolinska-institutet/refs/heads/main/well-known/karolinska-institutet-utbildning-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/karolinska-institutet-utbildning-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/karolinska-institutet/refs/heads/main/well-known/karolinska-institutet-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/karolinska-institutet-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/karolinska-institutet/refs/heads/main/well-known/karolinska-institutet-nyheter-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/karolinska-institutet-nyheter-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/karolinska-institutet/refs/heads/main/well-known/karolinska-institutet-medarbetare-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/karolinska-institutet-medarbetare-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/karolinska-institutet/refs/heads/main/well-known/karolinska-institutet-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/karolinska-institutet-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/karolinska-institutet/refs/heads/main/hosts/karolinska-institutet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/karolinska-institutet-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/karolinska-institutet/refs/heads/main/security/karolinska-institutet-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/karolinska-institutet-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/karolinska-institutet/refs/heads/main/security/karolinska-institutet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/karolinska-institutet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ki.se/
coverage:
  checked: '2026-10-15'
  detail: Karolinska Institutet provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://ki.se/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Karolinska Institutet (KI) is a world‑leading medical university in Stockholm, Sweden, focused on education, research and innovation in health and medicine. It operates a large network of hospitals, conducts Nobel‑prize‑winning biomedical research, and offers extensive academic programmes. KI provides open data portals, research APIs, and digital services for students, staff and collaborators, reflecting its commitment to transparency and scientific advancement.
layout: provider
modified: '2026-10-15'
name: Karolinska Institutet
nav: Providers
network: true
overview: Karolinska Institutet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Research, Healthcare, and Sweden.
random_paper: 11
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Karolinska Institutet Domain Security
  slug: karolinska-institutet-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Karolinska Institutet Vulnerability Disclosure
  slug: karolinska-institutet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: karolinska-institutet
tags:
- Company
- Education
- Research
- Healthcare
- Sweden
website: https://ki.se/
---
