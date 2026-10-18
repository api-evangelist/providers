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
- description: Legal case management platform API (not publicly documented)
  name: CloudLex API
  slug: cloudlex-api
artifact_total: 2
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cloudlexinc/refs/heads/main/changelog/cloudlexinc-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cloudlexinc-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudlexinc/refs/heads/main/llms/cloudlexinc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudlexinc-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudlexinc/refs/heads/main/hosts/cloudlexinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudlexinc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudlexinc/refs/heads/main/vendors/cloudlexinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudlexinc-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudlex.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.cloudlex.com/release-notes/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudlexinc/refs/heads/main/security/cloudlexinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudlexinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudlex.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.cloudlex.com
  - status: 403
    url: https://equityzen.com/company/cloudlexinc
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: CloudLex provides an end‑to‑end personal injury management platform for plaintiff personal injury law firms. The software unifies intake, case management, client communication, litigation, and settlement workflows, and includes built‑in AI tools and optional paralegal services. It is purpose‑built for personal injury practices of all sizes.
image: https://www.cloudlex.com/wp-content/uploads/2023/07/cloudlex-legal-software.jpg
layout: provider
modified: '2026-10-09'
name: Cloudlexinc
nav: Providers
network: true
overview: 'Cloudlexinc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Personal Injury, Legal Practice Management, Law Firm Software, and Paralegal Services.


  Cloudlexinc''s developer surface includes changelog and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 15.8
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
  name: Cloudlexinc Domain Security
  slug: cloudlexinc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cloudlexinc
tags:
- Personal Injury
- Legal Practice Management
- Law Firm Software
- Paralegal Services
website: https://www.cloudlex.com
---
