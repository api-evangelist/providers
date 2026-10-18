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
- description: ControlRooms AI platform API (no public spec discovered).
  name: ControlRooms API
  slug: controlrooms-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlrooms-ai/refs/heads/main/hosts/controlrooms-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/controlrooms-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlrooms-ai/refs/heads/main/vendors/controlrooms-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/controlrooms-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.controlrooms.ai/terms-of-service-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.controlrooms.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/controlrooms
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlrooms-ai/refs/heads/main/security/controlrooms-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/controlrooms-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.controlrooms.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.controlrooms.ai/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: ControlRooms.ai provides an agentic troubleshooting system for energy and chemical plant operations. It uses large harmony models to detect anomalies before traditional alarms fire, offering proactive advice, logging, and AI‑drafted shift summaries. The platform integrates with existing DCS, Teams, and mobile apps to help operators mitigate issues early, improving safety and efficiency across refining, fertilizers, petrochemicals, and related sectors.
image: https://www.controlrooms.ai/assets/og-image.1a7c7cd1.jpg
layout: provider
modified: '2026-10-10'
name: ControlRooms.ai
nav: Providers
network: true
overview: ControlRooms.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Anomaly Detection, Plant Operations, and AI Troubleshooting.
random_paper: 14
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Controlrooms Ai Domain Security
  slug: controlrooms-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: controlrooms-ai
tags:
- Anomaly Detection
- Plant Operations
- AI Troubleshooting
website: https://www.controlrooms.ai/
---
