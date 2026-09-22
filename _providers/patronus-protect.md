---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 66.2
  scored_at: '2026-09-21'
api_count: 1
apis:
- baseURL: https://control.patronus.studio/api/v1
  baseurl_source: declared
  description: Public REST Scan API (OpenAPI 3.1, contract v1.2.0). POST /api/v1/scan submits text, a public HTTPS URL, an MCP server, or uploaded documents for prompt-injection, PII/DLP, sensitive-document and agen
  name: Patronus Scan API
  slug: patronus-scan-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://patronus.studio/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.patronus.studio/
- group: start
  title: ''
  type: GettingStarted
  url: https://patronus-protect.github.io/patronus-security/getting-started/quickstart/
- group: commercial
  title: ''
  type: Pricing
  url: https://patronus.studio/pricing
- group: company
  title: ''
  type: Blog
  url: https://patronus.studio/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/patronus-protect
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/patronus-protect/refs/heads/main/packages/patronus-protect-packages.yml
  title: ''
  type: Packages
  url: packages/patronus-protect-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/patronus-protect/refs/heads/main/packages/patronus-protect-packages.yml
  title: ''
  type: SDKs
  url: packages/patronus-protect-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/patronus-protect/refs/heads/main/cli/patronus-protect-cli.yml
  title: ''
  type: CLI
  url: cli/patronus-protect-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/patronus-protect/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/patronus-protect/refs/heads/main/llms/patronus-protect-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/patronus-protect-llms.txt
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/patronus-protect/refs/heads/main/json-schema/patronus-protect-runtime-v1.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/patronus-protect-runtime-v1.schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/patronus-protect/refs/heads/main/conformance/patronus-protect-conformance.yml
  title: ''
  type: Conformance
  url: conformance/patronus-protect-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/patronus-protect/refs/heads/main/plans/patronus-protect-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/patronus-protect-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/patronus-protect/refs/heads/main/changelog/patronus-protect-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/patronus-protect-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/patronus-protect/refs/heads/main/well-known/patronus-protect-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/patronus-protect-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/patronus-protect/refs/heads/main/well-known/patronus-protect-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/patronus-protect-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/patronus-protect/refs/heads/main/security/patronus-protect-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/patronus-protect-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/patronus-protect/refs/heads/main/security/patronus-protect-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/patronus-protect-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/patronus-protect/refs/heads/main/security/patronus-protect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/patronus-protect-domain-security.yml
created: '2026-09-20'
description: Patronus Protect, from Casdo Labs GmbH, is an on-device AI firewall that detects prompt injection, PII/DLP, sensitive documents and agentic tool risk in text, public HTTPS webpages, documents and MCP servers before they are used by AI agents, RAG pipelines or LLM applications. It exposes a REST Scan API (control.patronus.studio/api/v1), first-party Rust, TypeScript and Python SDK clients, a local CLI with Codex, Claude Code and DeepSeek plugins, a remote OAuth-protected MCP server and a local stdio MCP server, and the open-source Patronus Ark scanning core.
json_schemas:
- name: Patronus local runtime v1 NDJSON frame
  property_count: 0
  slug: patronus-protect-runtime-v1.schema
layout: provider
mcp_servers:
- description: ''
  name: Patronus Protect MCP Server
  slug: patronus-protect-mcp-server
modified: '2026-09-20'
name: Patronus Protect
nav: Providers
network: true
overview: 'Patronus Protect publishes 1 API on the [APIs.io](https://apis.io/) network: Patronus Scan API. Tagged areas include AI Safety, Prompt Injection, Security, LLM, and agent-native.


  Patronus Protect''s developer surface includes getting-started guide, pricing, engineering blog, CLI, changelog, and 15 more developer resources.'
plans:
- name: Patronus Protect Plans Pricing
  plan_count: 4
  slug: patronus-protect-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Patronus Protect Rate Limits
  slug: patronus-protect-rate-limits
scopes:
- name: Patronus Protect Scopes
  scope_count: 0
  slug: patronus-protect-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 55.1
    developer_ergonomics: 73.8
    discoverability: 72.2
    operational_transparency: 31.6
  previous_composite: 49.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Patronus Protect Authentication
  slug: patronus-protect-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Patronus Protect Domain Security
  slug: patronus-protect-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Patronus Protect Vulnerability Disclosure
  slug: patronus-protect-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: patronus-protect
tags:
- AI Safety
- Prompt Injection
- Security
- LLM
- agent-native
- MCP
- DLP
- PII
- On-Device
- AI Firewall
website: https://patronus.studio/
---
