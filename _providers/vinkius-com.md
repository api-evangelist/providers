---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: templated
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.3
  scored_at: '2026-09-23'
api_count: 2
apis:
- description: 'REST API behind the AI Connect SDK: application users, connector connections, write-only credentials, connection tokens, catalog and marketplace search, plus the execution plane for capabilities. Auth'
  name: Vinkius API
  slug: vinkius-api
- description: 'The hosted MCP data plane. Every connector is a remote MCP server at https://edge.vinkius.com/{connection_token}/mcp; the host also serves OAuth 2 authorization-server and protected-resource metadata '
  name: Vinkius Edge MCP
  slug: vinkius-edge-mcp
artifact_total: 9
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vinkius-com/refs/heads/main/security/vinkius-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vinkius-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vinkius.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://vinkius.com/en/build-with-vinkius
- group: docs
  title: ''
  type: Documentation
  url: https://vinkius.com/learn/en
- group: commercial
  title: ''
  type: Pricing
  url: https://vinkius.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.vinkius.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vinkius.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vinkius.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vinkius-labs
- group: operate
  title: ''
  type: Support
  url: https://github.com/vinkius-labs/vinkius-issues
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://vinkius.com/legal/service-level-agreement
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vinkius-com/refs/heads/main/llms/vinkius-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vinkius-com-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vinkius-com/refs/heads/main/packages/vinkius-com-packages.yml
  title: ''
  type: Packages
  url: packages/vinkius-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vinkius-com/refs/heads/main/packages/vinkius-com-packages.yml
  title: ''
  type: SDKs
  url: packages/vinkius-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vinkius-com/refs/heads/main/cli/vinkius-com-cli.yml
  title: ''
  type: CLI
  url: cli/vinkius-com-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vinkius-com/refs/heads/main/well-known/vinkius-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vinkius-com-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vinkius-com/refs/heads/main/conformance/vinkius-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vinkius-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vinkius-com/refs/heads/main/lifecycle/vinkius-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vinkius-com-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/vinkius-com/refs/heads/main/plans/vinkius-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vinkius-com-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vinkius-com/refs/heads/main/security/vinkius-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vinkius-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vinkius-com/refs/heads/main/security/vinkius-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/vinkius-com-vulnerability-disclosure.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://vinkius.com/legal/subprocessors
- group: operate
  title: ''
  type: IncidentNotification
  url: https://vinkius.com/legal/security
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://vinkius.com/legal/privacy-policy
- group: other
  title: ''
  type: DataResidency
  url: https://vinkius.com/legal/subprocessors
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vinkius-com/refs/heads/main/regulatory/vinkius-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/vinkius-com-regulatory-posture.yml
created: '2026-09-20'
description: 'Vinkius is an AI connectivity cloud: a managed catalog of thousands of hosted Model Context Protocol (MCP) Connectors that AI agents call through one URL per connector, working in ChatGPT, Claude, Gemini, Cursor and other MCP clients. Connectors run in a sealed sandbox on the Vinkius Edge (edge.vinkius.com) with credential encryption, governance policies, audit trails, spend controls and log streaming. Developers build on it with the AI Connect SDK (@vinkius/connect) over the Vinkius API (api.vinkius.com), and publish their own connectors with the open source MCP Fusion TypeScript framework.'
image: https://vinkius.com/og/logo-512.png
layout: provider
mcp_servers:
- description: 'Vinkius IS an MCP platform - every Connector in its catalog (9,258 connectors / 63,093 capabilities per llms.txt on 2026-09-20) is a hosted remote MCP server on the Vinkius Edge, addressed by one URL '
  name: Vinkius MCP Server
  slug: vinkius-mcp-server
modified: '2026-09-20'
name: Vinkius
nav: Providers
network: true
overview: 'Vinkius publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, AI Agents, Integration, and Connectors.


  Vinkius'' developer surface includes documentation, pricing, signup flow, support, CLI, and 21 more developer resources.'
plans:
- name: Vinkius Com Plans Pricing
  plan_count: 5
  slug: vinkius-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Vinkius Com Rate Limits
  slug: vinkius-com-rate-limits
scopes:
- name: Vinkius Com Scopes
  scope_count: 0
  slug: vinkius-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 75.9
    operational_transparency: 31.6
  previous_composite: 42.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Vinkius Com Authentication
  slug: vinkius-com-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Vinkius Com Domain Security
  slug: vinkius-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vinkius Com Vulnerability Disclosure
  slug: vinkius-com-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: vinkius-com
tags:
- Company
- MCP
- AI Agents
- Integration
- Connectors
- AI Governance
- Developer Tools
- Agent-Native
website: https://vinkius.com/
---
