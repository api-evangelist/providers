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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/betterskillsinc/refs/heads/main/llms/betterskillsinc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/betterskillsinc-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/betterskillsinc/refs/heads/main/hosts/betterskillsinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betterskillsinc-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://www.better-skills.com/blog/index.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/betterskillsinc/refs/heads/main/security/betterskillsinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betterskillsinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.better-skills.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/betterskillsinc
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: Betterskillsinc provides ITIL, COBIT, ISO and other professional certification training courses in Portugal. It offers a range of certification programs, including ITIL 4 Foundation, Managing Professional, Strategic Leader, and various ISO standards, targeting individuals and organizations seeking to improve their IT service management and governance capabilities.
image: https://better-skills.com/images/logo-better-skills.webp
layout: provider
modified: '2026-09-28'
name: Betterskillsinc
nav: Providers
network: true
overview: 'Betterskillsinc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Training, ITIL, ISO, and Certification.


  Betterskillsinc''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Betterskillsinc Domain Security
  slug: betterskillsinc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: betterskillsinc
tags:
- Education
- Training
- ITIL
- ISO
- Certification
website: https://www.better-skills.com
---
