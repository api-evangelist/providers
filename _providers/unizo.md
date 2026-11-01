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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://unizo.ai/trust/
- group: agent
  href: https://artifacts.apis.io/unizo/llms/unizo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unizo-llms.txt
- group: other
  href: https://artifacts.apis.io/unizo/hosts/unizo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unizo-hosts.yml
- group: other
  href: https://artifacts.apis.io/unizo/vendors/unizo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unizo-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unizo.ai/privacy/
- group: auth
  href: https://artifacts.apis.io/unizo/security/unizo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/unizo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/unizo/security/unizo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unizo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unizo.ai/
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, or MCP spec found at api.unizo.ai despite probing common spec endpoints.
  evidence:
  - status: 503
    url: https://api.unizo.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Unizo is an AI-native exposure management platform that helps organizations continuously reduce risk by automating the identification, analysis, and remediation of security findings. Its solution loop connects exposure analysts, live security context, and verification closure to provide real‑time insights and actionable plans, integrating with existing toolchains to modernize vulnerability management and operationalize CTEM processes.
image: https://unizo.ai/assets/img/og-default.png
layout: provider
modified: '2026-10-19'
name: Unizo
nav: Providers
network: true
overview: Unizo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Security, Exposure Management, Platform, and Company.
random_paper: 13
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Unizo Domain Security
  slug: unizo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Unizo Trust Center
  slug: unizo-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: unizo
tags:
- Artificial Intelligence
- Security
- Exposure Management
- Platform
- Company
website: https://unizo.ai/
---
