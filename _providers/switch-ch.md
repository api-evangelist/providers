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
  title: ''
  type: Security
  url: https://www.switch.ch/security/SWITCH-CERT.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/switch-ch/refs/heads/main/well-known/switch-ch-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/switch-ch-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/switch-ch/refs/heads/main/well-known/switch-ch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/switch-ch-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/switch-ch/refs/heads/main/hosts/switch-ch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/switch-ch-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.switch.ch/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/switch-ch/refs/heads/main/security/switch-ch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/switch-ch-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/switch-ch/refs/heads/main/security/switch-ch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/switch-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.switch.ch/
- group: docs
  title: ''
  type: Documentation
  url: https://portal.switch.ch/pub/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.switch.ch/
- group: operate
  title: ''
  type: Support
  url: https://www.switch.ch/en/contact
coverage:
  checked: '2026-10-13'
  detail: Documentation portal renders JavaScript shells, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://portal.switch.ch/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Switch is a Swiss non‑profit foundation established in 1987 that provides digital infrastructure, platforms, and services for education and research institutions across Switzerland. It develops secure networking, identity, cloud, and cyber‑security solutions, supports digital transformation, and coordinates collaborative projects among universities and research bodies. Switch also offers incident response and security services to protect the digital ecosystem of Swiss higher education.
layout: provider
modified: '2026-10-13'
name: SWITCH
nav: Providers
network: true
overview: 'SWITCH is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Infrastructure, Open Source, and Security.


  SWITCH''s developer surface includes documentation, support, and 9 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 44.6
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Switch Ch Domain Security
  slug: switch-ch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Switch Ch Vulnerability Disclosure
  slug: switch-ch-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: switch-ch
tags:
- Company
- Education
- Infrastructure
- Open Source
- Security
website: https://www.switch.ch/
---
