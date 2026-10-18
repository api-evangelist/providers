---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Quietstance Agentic Access
  operation_count: 1
  slug: quietstance-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://quietstance.com
  baseurl_source: spec
  description: The Inquiries API from Quiet Stance — 1 operation(s) for inquiries.
  name: Quiet Stance Inquiries API
  slug: quietstance-inquiries-api
artifact_total: 6
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quietstance/refs/heads/main/agentic-access/quietstance-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/quietstance-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quietstance/refs/heads/main/rules/quietstance-rules.yml
  title: ''
  type: Spectral
  url: rules/quietstance-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quietstance/refs/heads/main/vocabulary/quietstance-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/quietstance-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://quietstance.com/terms
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quietstance/refs/heads/main/conformance/quietstance-conformance.yml
  title: ''
  type: Conformance
  url: conformance/quietstance-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/quietstance/refs/heads/main/overlays/quietstance-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/quietstance-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quietstance/refs/heads/main/llms/quietstance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quietstance-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/quietstance/refs/heads/main/a2a/quietstance-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/quietstance-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quietstance/refs/heads/main/mcp/quietstance-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/quietstance-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quietstance/refs/heads/main/well-known/quietstance-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/quietstance-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quietstance/refs/heads/main/well-known/quietstance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/quietstance-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/quietstance/refs/heads/main/hosts/quietstance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quietstance-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/quietstance/refs/heads/main/vendors/quietstance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quietstance-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quietstance/refs/heads/main/security/quietstance-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/quietstance-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quietstance/refs/heads/main/security/quietstance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quietstance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quietstance.com
- group: docs
  title: ''
  type: Documentation
  url: https://quietstance.com/for-agents
- group: docs
  title: ''
  type: APIReference
  url: https://quietstance.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://quietstance.com/for-agents
- group: commercial
  title: ''
  type: TermsOfService
  url: https://quietstance.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://quietstance.com/privacy
created: '2026-10-05'
description: Quiet Stance provides a platform for infrastructure project development and co-development, enabling owners, sponsors, and partners to submit sanitized, permission‑aware productive opportunities. The service records initial opportunity states, ensuring that only authorized parties can engage, and facilitates transparent collaboration without creating mandates or financial commitments.
image: https://quietstance.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at quietstance.com.
  name: Quiet Stance MCP Server
  slug: quietstance-mcp-yml
modified: '2026-10-05'
name: Quiet Stance
nav: Providers
network: true
overview: 'Quiet Stance publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Inquiries API. Tagged areas include Company, Infrastructure, Project Development, and Collaboration.


  The Quiet Stance catalog on APIs.io includes 1 Spectral governance ruleset.


  Quiet Stance''s developer surface includes documentation, API reference, getting-started guide, and 18 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Quiet Stance API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: quietstance-rules
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.8
    catalog_earned_first_party: 0.0
    catalog_gap: 82.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 47.1
    developer_ergonomics: 28.6
    discoverability: 58.3
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Quietstance Domain Security
  slug: quietstance-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Quietstance Vulnerability Disclosure
  slug: quietstance-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: quietstance
tags:
- Company
- Infrastructure
- Project Development
- Collaboration
website: https://quietstance.com
---
