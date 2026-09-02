---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hubsync-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hubsync.com/
- group: company
  title: ''
  type: Blog
  url: https://hubsync.com/blog
- group: operate
  title: ''
  type: Support
  url: https://hubsync.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hubsync
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hubsync.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hubsync.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hubsync-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hubsync-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hubsync-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/hubsync-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hubsync-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hubsync-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hubsync-lifecycle.yml
coverage:
  checked: '2026-08-22'
  detail: 'HubSync markets an MCP server and bi-directional REST integrations with CCH Axcess, Thomson Reuters and SurePrep, but its only documentation host is a Docsie portal whose content API answers {"error": "Invalid token."} without a customer token, its Integrations and MCP shelves are absent from the public sitemap, and each CPA firm''s tenant at <firm>.hubsync.com refuses anonymous requests with HTTP 403 — so no contract, endpoint or tool list is reachable without an active firm subscription.'
  evidence:
  - status: 403
    url: https://api.docsie.io/api_v2/006/deployment/deployment_SEgpqVq42BLzmcNdl/
  - status: 403
    url: https://eisneramper.hubsync.com/
  - status: 404
    url: https://hubsync.com/openapi.json
  - status: 200
    url: https://docs.hubsync.com/?doc=release-notes/release-notes
  reason: customer-only-docs
  state: gated
created: '2026-08-22'
description: 'HubSync is an AI-powered, end-to-end tax and accounting workflow platform built for CPA firms, founded in 2019 by John McGowan and headquartered in Franklin, Tennessee. The SaaS platform unifies the engagement lifecycle in one interface: engagement letter generation and tracking, tax organizers and prepared-by-client data collection, document management, e-signature (including IRS Form 8879), batch federal and state extensions, tax return breakup and delivery, e-file status tracking, web-based tax workpapers, firm analytics dashboards, and integrated bill-and-pay. Its HubSync Halo layer adds agentic AI orchestration across those stages. HubSync publishes an llms.txt and states that it ships a Model Context Protocol (MCP) server and bi-directional API integrations with CCH Axcess/ProSystem fx, Thomson Reuters GoSystem/UltraTax and SurePrep, but it publishes no public developer portal, API reference, OpenAPI description or endpoint documentation — the entire integration surface
  is provisioned per customer firm.'
image: https://hubsync.com/hubfs/HubSync_primary-logo-white-color.svg
layout: provider
mcp_servers:
- description: ''
  name: HubSync MCP Server
  slug: hubsync-mcp-server
modified: '2026-08-22'
name: HubSync
nav: Providers
network: true
overview: 'HubSync is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tax, Accounting, Workflow-Automation, and Document-Management.


  HubSync''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Hubsync Plans Pricing
  plan_count: 0
  slug: hubsync-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Hubsync Rate Limits
  slug: hubsync-rate-limits
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 15.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Hubsync Domain Security
  slug: hubsync-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hubsync
tags:
- Company
- Tax
- Accounting
- Workflow-Automation
- Document-Management
- Electronic Signature
- Professional Services
- Artificial Intelligence
- MCP
- Software-as-a-Service
website: https://hubsync.com/
---
