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
api_count: 1
apis:
- description: Datawisp provides a no‑code analytics platform accessible via a web UI; no public machine‑readable API contract was found.
  name: Datawisp API
  slug: datawisp-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/datawisp/conformance/datawisp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datawisp-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datawisp/llms/datawisp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datawisp-llms.txt
- group: agent
  href: https://artifacts.apis.io/datawisp/well-known/datawisp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datawisp-well-known.yml
- group: other
  href: https://artifacts.apis.io/datawisp/hosts/datawisp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datawisp-hosts.yml
- group: other
  href: https://artifacts.apis.io/datawisp/vendors/datawisp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datawisp-vendors.yml
- group: build
  href: https://artifacts.apis.io/datawisp/packages/datawisp-packages.yml
  title: ''
  type: SDKs
  url: packages/datawisp-packages.yml
- group: build
  href: https://artifacts.apis.io/datawisp/packages/datawisp-packages.yml
  title: ''
  type: Packages
  url: packages/datawisp-packages.yml
- group: auth
  href: https://artifacts.apis.io/datawisp/security/datawisp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datawisp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.datawisp.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datawisp.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datawisp.io/datawisp-overview.md
coverage:
  checked: '2026-10-22'
  detail: Documentation is served via Gitbook with markdown twin pattern, but no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://docs.datawisp.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Datawisp is a no‑code analytics platform that enables users to analyze data and discover insights without technical expertise. It offers a node‑based interface for building data‑processing pipelines, AI‑powered assistance via Wispy for natural‑language chart creation, real‑time collaboration, and sharing capabilities. The platform runs in the browser and supports a variety of data blocks for filtering, sorting, visualizing, and more, targeting both technical and non‑technical users.
image: https://docs.datawisp.io/~gitbook/ogimage/sovnM6sCRiQcugOrzaFW
layout: provider
modified: '2026-10-22'
name: Datawisp
nav: Providers
network: true
overview: 'Datawisp is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, No-Code, Data Visualization, Collaboration, and AI Assistant.


  Datawisp''s developer surface includes documentation, getting-started guide, and 9 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datawisp Domain Security
  slug: datawisp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datawisp
tags:
- Analytics
- No-Code
- Data Visualization
- Collaboration
- AI Assistant
website: https://docs.datawisp.io/
---
