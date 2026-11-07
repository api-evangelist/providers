---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/askqa-app/hosts/askqa-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askqa-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/askqa-app/vendors/askqa-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askqa-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askqa.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askqa.app/privacy
- group: auth
  href: https://artifacts.apis.io/askqa-app/security/askqa-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askqa-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askqa.app/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI or other machine‑readable contract discovered at the API host.
  evidence:
  - status: 522
    url: https://api.askqa.app/openapi.json
  - status: 522
    url: https://api.askqa.app/openapi.yaml
  - status: 522
    url: https://api.askqa.app/swagger.json
  - status: 522
    url: https://api.askqa.app/v1/openapi.json
  - status: 522
    url: https://api.askqa.app/api-docs
  - status: 522
    url: https://api.askqa.app/docs
  - status: 522
    url: https://api.askqa.app/redoc
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ASKQA provides a business automation studio that builds and runs WhatsApp bots, workflows, document processing, dashboards, and custom applications for enterprises. Their platform automates customer support, sales, bookings, invoicing, reporting, and monitoring across industries such as retail, finance, healthcare, and logistics. By integrating AI agents and low‑code tools, ASKQA enables companies to streamline repetitive tasks, improve response times, and gain insights from data without extensive coding.
image: https://askqa.app/assets/askqa-og.png?v=2
layout: provider
modified: '2026-11-01'
name: ASKQA
nav: Providers
network: true
overview: ASKQA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, WhatsApp bots, Workflows, Reporting, and Customer Service.
random_paper: 7
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 8.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Askqa App Domain Security
  slug: askqa-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: askqa-app
tags:
- Automation
- WhatsApp bots
- Workflows
- Reporting
- Customer Service
- Integration
- Business Software
website: https://askqa.app/
---
