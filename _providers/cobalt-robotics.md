---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 14.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Cobalt Robotics platform providing security monitoring and robot control.
  name: Cobalt Robotics API
  slug: cobalt-robotics-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cobalt-robotics/refs/heads/main/llms/cobalt-robotics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cobalt-robotics-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cobalt-robotics/refs/heads/main/well-known/cobalt-robotics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cobalt-robotics-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cobalt-robotics/refs/heads/main/hosts/cobalt-robotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cobalt-robotics-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cobaltai.com/terms-of-use/
- group: start
  title: ''
  type: SignUp
  url: https://www.cobaltai.com/register-for-free-2025-isc-west/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cobaltai.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.cobaltai.com/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cobalt-robotics/refs/heads/main/security/cobalt-robotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cobalt-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cobaltai.com/
coverage:
  checked: '2026-10-09'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.cobaltai.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Cobalt Robotics provides AI‑powered physical security monitoring and autonomous security robots. Their platform integrates video, access control, and edge devices, using AI handlers to detect, reason, and act on events such as tailgating, gun detection, and alarm management, delivering autonomous patrols and 24/7 monitoring for enterprises.
image: https://www.cobaltai.com/wp-content/uploads/2024/01/5.-Specialist-at-CCC-scaled.jpg
layout: provider
modified: '2026-10-09'
name: Cobalt Robotics
nav: Providers
network: true
overview: 'Cobalt Robotics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Artificial Intelligence, Robotics, PhysicalSecurity, and Enterprise.


  Cobalt Robotics'' developer surface includes signup flow and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cobalt Robotics Domain Security
  slug: cobalt-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cobalt-robotics
tags:
- Security
- Artificial Intelligence
- Robotics
- PhysicalSecurity
- Enterprise
website: https://www.cobaltai.com/
---
