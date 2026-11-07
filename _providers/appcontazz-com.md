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
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/appcontazz-com/llms/appcontazz-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appcontazz-com-llms.txt
- group: other
  href: https://artifacts.apis.io/appcontazz-com/hosts/appcontazz-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appcontazz-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/appcontazz-com/vendors/appcontazz-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appcontazz-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/appcontazz-com/security/appcontazz-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appcontazz-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appcontazz.com/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's site.
  evidence:
  - status: 200
    url: https://appcontazz.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Contazz provides AI‑driven financial management automation for businesses, integrating Open Finance data from over 149 banks. Features include intelligent billing, automatic reconciliation, fiscal document issuance, and full accounting, all operating in an autopilot mode to streamline cash flow, invoicing, and compliance.
image: https://appcontazz.com/manus-storage/contazz-og-new-1200x630_272da347.png
layout: provider
modified: '2026-11-01'
name: Contazz
nav: Providers
network: true
overview: Contazz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Artificial Intelligence, Automation, Open Finance, and Accounting.
random_paper: 22
score:
  band: minimal
  composite: 2.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 3.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appcontazz Com Domain Security
  slug: appcontazz-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: appcontazz-com
tags:
- Finance
- Artificial Intelligence
- Automation
- Open Finance
- Accounting
- Company
website: https://appcontazz.com/
---
