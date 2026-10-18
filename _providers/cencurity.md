---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API documentation for Cencurity, covering proxy architecture and streaming security.
  name: Cencurity API
  slug: cencurity-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cencurity/refs/heads/main/authentication/cencurity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cencurity-authentication.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cencurity/refs/heads/main/hosts/cencurity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cencurity-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cencurity/refs/heads/main/vendors/cencurity-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cencurity-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cencurity.com/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cencurity
- group: docs
  title: ''
  type: Documentation
  url: https://cencurity.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://cencurity.com/docs/getting-started/quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cencurity/refs/heads/main/security/cencurity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cencurity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cencurity.com/
coverage:
  checked: '2026-10-16'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite probing common spec URLs on both the website and API host.
  evidence:
  - status: 404
    url: https://cencurity.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Cencurity provides a security gateway for LLM agents that detects and blocks prompt leakage, secrets, PII, and risky output in real time. It offers centralized dashboards, end‑to‑end log analysis, policy‑first detection, automatic redaction, and audit‑ready reporting. The service integrates with any LLM and IDE and is built for developers who need governed AI coding without disrupting workflows.
layout: provider
modified: '2026-10-16'
name: Cencurity
nav: Providers
network: true
overview: 'Cencurity is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Security, LLM Proxy, Real-time Threat Monitoring, Audit Reporting, and Developer Tools.


  Cencurity''s developer surface includes authentication, documentation, getting-started guide, and 6 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cencurity Authentication
  slug: cencurity-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cencurity Domain Security
  slug: cencurity-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cencurity
tags:
- AI Security
- LLM Proxy
- Real-time Threat Monitoring
- Audit Reporting
- Developer Tools
- Policy Enforcement
website: https://cencurity.com/
---
