---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://api.conveyor.com
  baseurl_source: declared
  description: The Single Question API from Conveyor — 1 operation(s) for single question.
  name: Conveyor Single Question API
  slug: conveyor-single-question-api
artifact_total: 8
asyncapis:
- description: ''
  name: Conveyor Webhooks
  slug: conveyor-webhooks
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/conveyor/refs/heads/main/plans/conveyor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/conveyor-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/conveyor/refs/heads/main/rules/conveyor-rules.yml
  title: ''
  type: Spectral
  url: rules/conveyor-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/conveyor/refs/heads/main/asyncapi/conveyor-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/conveyor-webhooks.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.conveyor.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/conveyor/refs/heads/main/authentication/conveyor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/conveyor-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/conveyor/refs/heads/main/conformance/conveyor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/conveyor-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/conveyor/refs/heads/main/llms/conveyor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/conveyor-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/conveyor/refs/heads/main/mcp/conveyor-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/conveyor-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/conveyor/refs/heads/main/well-known/conveyor-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/conveyor-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/conveyor/refs/heads/main/well-known/conveyor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/conveyor-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/conveyor/refs/heads/main/hosts/conveyor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/conveyor-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/conveyor/refs/heads/main/vendors/conveyor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/conveyor-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.conveyor.com/legal/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.conveyor.com
- group: auth
  title: ''
  type: Security
  url: https://www.conveyor.com/legal/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.conveyor.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.conveyor.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.conveyor.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/conveyor
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/conveyor/refs/heads/main/security/conveyor-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/conveyor-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/conveyor/refs/heads/main/security/conveyor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conveyor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.conveyor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.conveyor.com/
- group: company
  title: ''
  type: Blog
  url: https://www.conveyor.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.conveyor.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.conveyor.com/legal/privacy
coverage:
  checked: '2026-10-10'
  detail: Docs site returns HTTP 429 and HTML shells, no machine‑readable OpenAPI spec found.
  evidence:
  - status: 429
    url: https://docs.conveyor.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-10'
description: Conveyor provides an AI‑powered platform that automates security questionnaire responses, trust‑center management, and RFP workflows for enterprise teams. By combining large‑language models with a curated knowledge base, Conveyor helps security, compliance, and sales organizations accelerate reviews, improve accuracy, and reduce manual effort. The solution includes a Trust Center, AI‑driven questionnaire automation, analytics, and integrations with popular SaaS tools, delivering a secure, scalable, and customizable experience for high‑stakes customer interactions.
image: https://cdn.prod.website-files.com/696e25579726c96825c6d025/699c0c6c8d3725bc4a835181_conveyor-og.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.conveyor.com.
  name: Conveyor MCP Server
  slug: conveyor-mcp-yml
modified: '2026-10-10'
name: Conveyor
nav: Providers
network: true
overview: 'Conveyor is listed with 1 API on the [APIs.io](https://apis.io/) network: Single Question API. Tagged areas include Artificial Intelligence, Security Questionnaire Automation, RFP Automation, Trust Center, and Customer Trust.


  The Conveyor catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Conveyor''s developer surface includes authentication, changelog, API reference, getting-started guide, documentation, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Conveyor Plans Pricing
  plan_count: 3
  slug: conveyor-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Conveyor API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: conveyor-rules
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 19.8
    developer_ergonomics: 42.9
    discoverability: 75.0
    operational_transparency: 55.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Conveyor Authentication
  slug: conveyor-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Conveyor Domain Security
  slug: conveyor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Conveyor Trust Center
  slug: conveyor-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: conveyor
tags:
- Artificial Intelligence
- Security Questionnaire Automation
- RFP Automation
- Trust Center
- Customer Trust
- Compliance
- Knowledge Management
website: https://www.conveyor.com/
---
