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
- description: CopiaFacts Fax Send API as documented in the Copia API reference manual.
  name: CopiaFacts Fax Send API
  slug: copiafacts-fax-send-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/copia/refs/heads/main/hosts/copia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/copia-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/copia/refs/heads/main/security/copia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/copia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.copia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.copia.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.copia.com/support/
- group: docs
  title: ''
  type: APIReference
  url: https://www.copia.com/support/refmanual91/copiafactsapi.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.copia.com/developers/
- group: company
  title: ''
  type: Blog
  url: https://blog.copia.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.copia.com/privacy.html
coverage:
  detail: The API reference manual is delivered as a JavaScript‑rendered HTML page with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.copia.com/support/refmanual91/copiafactsapi.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-10'
description: Copia provides enterprise fax server software and Fax over IP solutions, enabling organizations to deploy, control, and integrate high‑volume fax workflows on‑premises, virtualized or hosted environments. With over 37 years in business, Copia’s platform supports SIP/T.38, PBX integration, email‑to‑fax, and custom application interfaces, offering flexible deployment, cost control, and data security for enterprises across various industries.
image: https://www.copia.com/graphx/social/copia-share.jpg
layout: provider
modified: '2026-10-10'
name: Copia
nav: Providers
network: true
overview: 'Copia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fax, Enterprise Software, Communications, and On-Premises.


  Copia''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 5 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Copia Domain Security
  slug: copia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: copia
tags:
- Company
- Fax
- Enterprise Software
- Communications
- On-Premises
website: https://www.copia.com/
---
