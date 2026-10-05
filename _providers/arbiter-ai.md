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
api_count: 1
apis:
- description: API documentation for Arbiter AI platform, providing care orchestration services.
  name: Arbiter AI API
  slug: arbiter-ai-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arbiter-ai/refs/heads/main/well-known/arbiter-ai-itsm-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arbiter-ai-itsm-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arbiter-ai/refs/heads/main/well-known/arbiter-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arbiter-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arbiter-ai/refs/heads/main/hosts/arbiter-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arbiter-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arbiter.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arbiter.ai/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.arbiter.ai/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.arbiter.ai/team/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.arbiter.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arbiter-ai/refs/heads/main/security/arbiter-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arbiter-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arbiter.ai/
coverage:
  checked: 2026-09-25
  detail: Developer portal at https://dev.arbiter.ai/ renders documentation via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://dev.arbiter.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Arbiter AI is an agentic care orchestration platform that closes the last‑mile gaps in population health. It activates members through personalized multimodal outreach—AI video, SMS, voice, and portal—and returns verified clinical records proving care was completed, with licensed nurses in the loop. Trusted by leading health organizations, Arbiter delivers auditable outcomes at scale.
image: https://arbiter.ai/og/open-graph-image-arbiter.png
layout: provider
modified: '2026-09-25'
name: Arbiter AI
nav: Providers
network: true
overview: 'Arbiter AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Artificial Intelligence, Care Orchestration, Population Health, and Platform.


  Arbiter AI''s developer surface includes documentation and 9 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arbiter Ai Domain Security
  slug: arbiter-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: arbiter-ai
tags:
- Healthcare
- Artificial Intelligence
- Care Orchestration
- Population Health
- Platform
website: https://www.arbiter.ai/
---
