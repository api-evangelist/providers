---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    mcp_server: platform
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.1
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://robodialer-service-api-9nc4t1p9.uc.gateway.dev
  baseurl_source: declared
  description: 'SuperDial employs Bearer Authentication. Fetch a bearer token using your API Key and API Secret, then pass it as `Authorization: Bearer <token>` on subsequent calls.'
  name: SuperDial Authentication API
  slug: superdial-authentication-api
- baseURL: https://robodialer-service-api-9nc4t1p9.uc.gateway.dev
  baseurl_source: declared
  description: Endpoints for creating and reading requests (structured data extraction jobs). All non-2xx responses use the uniform `{error, message, [details]}` envelope (see the `ApiError` schema).
  name: SuperDial Requests API
  slug: superdial-requests-api
- baseURL: https://robodialer-service-api-9nc4t1p9.uc.gateway.dev
  baseurl_source: declared
  description: Discover the schemas provisioned for your account and the required input keys for each. All non-2xx responses use the uniform `{error, message, [details]}` envelope (see the `ApiError` schema).
  name: SuperDial Schemas API
  slug: superdial-schemas-api
artifact_total: 10
asyncapis:
- description: ''
  name: Superdial Requests Webhooks
  slug: superdial-requests-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/overlays/superdial-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/superdial-api-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/security/superdial-trust-center.yml
  title: ''
  type: Compliance
  url: security/superdial-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/authentication/superdial-authentication.yml
  title: ''
  type: Authentication
  url: authentication/superdial-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/conventions/superdial-conventions.yml
  title: ''
  type: Conventions
  url: conventions/superdial-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/conventions/superdial-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/superdial-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/errors/superdial-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/superdial-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/errors/superdial-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/superdial-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/lifecycle/superdial-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/superdial-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/sandbox/superdial-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/superdial-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/plans/superdial-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/superdial-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/rate-limits/superdial-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/superdial-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/packages/superdial-packages.yml
  title: ''
  type: Packages
  url: packages/superdial-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/conformance/superdial-conformance.yml
  title: ''
  type: Conformance
  url: conformance/superdial-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/security/superdial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/superdial-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/well-known/superdial-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/superdial-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/llms/superdial-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/superdial-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/mcp/superdial-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/superdial-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/mcp/superdial-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/superdial-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/a2a/superdial-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/superdial-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/skills/_index.yml
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
overview: 'SuperDial publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Requests API, and Schemas API. Tagged areas include Company, Healthcare, Revenue Cycle Management, Voice AI, and Insurance.


  The SuperDial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SuperDial''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, sandbox, and 23 more developer resources.'
plans:
- name: Superdial Plans Pricing
  plan_count: 0
  slug: superdial-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Superdial Rate Limits
  slug: superdial-rate-limits
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 64.4
    developer_ergonomics: 66.7
    discoverability: 75.9
    operational_transparency: 7.9
  previous_composite: 46.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/superdial/refs/heads/main/screenshots/superdial-2026-09-02T161224.png
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
