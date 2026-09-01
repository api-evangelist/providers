---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Asynchronous REST API for submitting structured data extraction requests against insurance payers and retrieving the results. Submit a request (single or batch) against an account-provisioned schema, '
  name: SuperDial API
  slug: superdial-api
artifact_total: 8
asyncapis:
- description: ''
  name: Superdial Requests Webhooks
  slug: superdial-requests-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.superdial.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.superdial.com/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.superdial.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.superdial.com/api-reference/requests/create-a-request
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.superdial.com/guides/creating-a-request
- group: company
  title: ''
  type: Blog
  url: https://www.superdial.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.thesuperbill.com/super-dial-sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.superdial.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.superdial.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/thesuperbill.com/trust/yxpg5guedf5rle15cka4ab
- group: auth
  title: ''
  type: Compliance
  url: security/superdial-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/superdial-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/superdial-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/superdial-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/superdial-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/superdial-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/superdial-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/superdial-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/superdial-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/superdial-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/superdial-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/superdial-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superdial-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/superdial-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/superdial-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/superdial-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/superdial-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/superdial-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-29'
description: 'SuperDial builds voice AI agents that automate high-friction administrative phone calls in healthcare revenue cycle management. Its agents place outbound calls from providers, billing teams and RCM companies to insurance payers — navigating IVR phone trees, holding, and conducting live conversations with payer representatives — and return structured, auditable results. Common workflows include benefits verification, prior authorization, claim status, provider data validation, and credentialing and enrollment outreach. The SuperDial API exposes this as an asynchronous job API: a client submits a "request" against an account-provisioned schema, SuperDial fulfills it across digital and phone modalities, and delivers the structured result by signed webhook or polling. Founded in 2021 in San Francisco as SuperBill by Stanford classmates Sam Schwager and Harrison Caruthers, the company raised a $15M Series A led by SignalFire in 2025.'
image: https://cdn.prod.website-files.com/6a295c5ee7351e54c6d2a237/6a66f67df4c11ba71463b5e3_OG%20Superdial%20v2.png
layout: provider
mcp_servers:
- description: 'SuperDial publishes a hosted, remote MCP server on its documentation host. It answers an anonymous `tools/list` and exposes three tools. IMPORTANT: this is a DOCUMENTATION MCP server (Mintlify-hosted)'
  name: SuperDial API Documentation MCP Server
  slug: superdial-api-documentation-mcp-server
modified: '2026-08-29'
name: SuperDial
nav: Providers
network: true
overview: 'SuperDial publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Revenue Cycle Management, Voice AI, and Insurance.


  The SuperDial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SuperDial''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, sandbox, and 22 more developer resources.'
plans:
- name: Superdial Plans Pricing
  plan_count: 0
  slug: superdial-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Superdial Rate Limits
  slug: superdial-rate-limits
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 59.9
    developer_ergonomics: 66.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 46.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Superdial Authentication
  slug: superdial-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Superdial Domain Security
  slug: superdial-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Superdial Trust Center
  slug: superdial-trust-center
  summary_line: trust center published
slug: superdial
tags:
- Company
- Healthcare
- Revenue Cycle Management
- Voice AI
- Insurance
- Artificial Intelligence
- Claims
- Prior Authorization
- Benefits Verification
- Automation
website: https://www.superdial.com/
---
