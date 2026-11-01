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
- description: Free MCP server allowing AI agents to call drwho.me tools via Model Context Protocol.
  name: drwho.me MCP
  slug: drwho-me-mcp
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/drwho-me/well-known/drwho-me-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/drwho-me-www-security.txt
- group: agent
  href: https://artifacts.apis.io/drwho-me/well-known/drwho-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drwho-me-well-known.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.domainposture.com/trust
- group: auth
  href: https://artifacts.apis.io/drwho-me/security/drwho-me-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/drwho-me-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/drwho-me/llms/drwho-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drwho-me-llms.txt
- group: agent
  href: https://artifacts.apis.io/drwho-me/mcp/drwho-me-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/drwho-me-mcp.yml
- group: other
  href: https://artifacts.apis.io/drwho-me/hosts/drwho-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drwho-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/drwho-me/vendors/drwho-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/drwho-me-vendors.yml
- group: auth
  href: https://artifacts.apis.io/drwho-me/security/drwho-me-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/drwho-me-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/drwho-me/security/drwho-me-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/drwho-me-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/drwho-me/security/drwho-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drwho-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drwho.me/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drwho.me/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hikmahtech
created: '2026-10-30'
description: drwho.me provides free, browser‑based DNS, email, and web security tools, plus an MCP server for AI agents. Built by Hikmah Technologies, the team behind Domain Posture, it offers open‑source code on GitHub and runs checks without requiring accounts, storing no personal data. The service acts as a front‑door to the paid Domain Posture product, giving users a taste of comprehensive domain monitoring.
examples:
- key_count: 3
  name: Mcp Tools List
  slug: mcp-tools-list
image: https://drwho.me/icon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at drwho.me.
  name: drwho-me MCP Server
  slug: drwho-me-mcp-yml
modified: '2026-10-30'
name: drwho-me
nav: Providers
network: true
overview: drwho-me is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tools, Free, DNS, and Email.
random_paper: 11
scopes:
- name: Drwho Me Scopes
  scope_count: 0
  slug: drwho-me-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Drwho Me Authentication
  slug: drwho-me-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Drwho Me Domain Security
  slug: drwho-me-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Drwho Me Vulnerability Disclosure
  slug: drwho-me-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Drwho Me Trust Center
  slug: drwho-me-trust-center
  summary_line: SOC 2, ISO 27001
slug: drwho-me
tags:
- Company
- Tools
- Free
- DNS
- Email
- Browser
website: https://drwho.me/
---
