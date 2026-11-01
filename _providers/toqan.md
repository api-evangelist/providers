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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: operate
  href: https://artifacts.apis.io/toqan/changelog/toqan-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/toqan-changelog.yml
- group: other
  href: https://artifacts.apis.io/toqan/hosts/toqan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/toqan-hosts.yml
- group: other
  href: https://artifacts.apis.io/toqan/vendors/toqan-vendors.yml
  title: ''
  type: Vendors
  url: vendors/toqan-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://toqan.ai/legal/terms-of-use/
- group: start
  title: ''
  type: SignUp
  url: https://toqan.ai/sign-up-redirect/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://toqan.ai/legal/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/toqan/security/toqan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/toqan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://toqan.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.toqan.ai/mcp
  - status: 200
    url: https://toqan.ai/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Toqan provides an AI‑powered workspace that lets companies create internal applications, dashboards, automated reports, knowledge bases, and scheduled tasks without writing code. The platform connects to existing tools such as Slack, Google Drive, Gmail, Notion, and other data sources via MCP and OAuth. It is offered to SMBs and enterprise customers across industries including legal, security, restaurants, and hotels.
image: https://toqan.ai/images/home/hero-ui.png
layout: provider
modified: '2026-10-21'
name: Toqan
nav: Providers
network: true
overview: 'Toqan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI workspace, Low‑code automation, Internal tools, Knowledge base, and Hospitality.


  Toqan''s developer surface includes changelog, signup flow, and 6 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Toqan Domain Security
  slug: toqan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: toqan
tags:
- AI workspace
- Low‑code automation
- Internal tools
- Knowledge base
- Hospitality
website: https://toqan.ai/
---
