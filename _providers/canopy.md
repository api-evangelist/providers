---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: The Canopy Connect API returns structured property and casualty insurance data directly from 400+ carriers in real time. Applications can verify coverage, retrieve policy documents, pull driver and ve
  name: Canopy Connect API
  slug: canopy-connect-api
artifact_total: 11
asyncapis:
- description: ''
  name: Canopy Webhooks
  slug: canopy-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/canopy-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/canopy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/canopy-packages.yml
- group: design
  title: ''
  type: Components
  url: components/canopy-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/canopy-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/canopy-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/canopy-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/canopy-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://docs.usecanopy.com/.well-known/api-catalog
- group: commercial
  title: ''
  type: Plans
  url: plans/canopy-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/canopy-finops.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/canopy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.usecanopy.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/canopy-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.usecanopy.com/company/is-canopy-connect-safe
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canopy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usecanopy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.usecanopy.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usecanopy.com/reference/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usecanopy.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usecanopy.com/reference/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.usecanopy.com/api/developer-account
- group: start
  title: ''
  type: Login
  url: https://dashboard.usecanopy.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usecanopy.com/api/api-plans
- group: operate
  title: ''
  type: Support
  url: https://help.usecanopy.com/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usecanopy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canopy-connect
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usecanopy.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usecanopy.com/terms
- group: company
  title: ''
  type: Blog
  url: https://www.usecanopy.com/blog
- group: company
  title: ''
  type: About
  url: https://www.usecanopy.com/company/about
- group: company
  title: ''
  type: Careers
  url: https://www.usecanopy.com/company/careers
created: '2024-07-02'
description: Canopy Connect is an insurance infrastructure platform that lets consumers and businesses quickly and securely share property and casualty insurance information through integrations with 400+ carriers covering 95%+ of the U.S. auto and homeowners markets. The API returns structured policy, driver, vehicle, claims, and property data in seconds, replacing manual verification workflows used across mortgage lending, auto finance, insurance carriers, and embedded insurance products.
finops:
- name: Canopy Finops
  service_category: API
  slug: canopy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canopy.png
layout: provider
mcp_servers:
- description: 'Canopy Connect runs a hosted, remote MCP server on its documentation host. The docs platform advertises it in its own configuration (`mcp_server_card: true`, `webmcp: true`) and the endpoint answers a'
  name: Canopy Connect Documentation MCP Server
  slug: canopy-connect-documentation-mcp-server
modified: '2026-09-05'
name: Canopy Connect
nav: Providers
network: true
overview: 'Canopy Connect publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Auto Insurance, Casualty, Financial-Services, Homeowners Insurance, and Insurance.


  The Canopy Connect catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Canopy Connect''s developer surface includes sandbox, documentation, API reference, getting-started guide, signup flow, pricing, support, and 26 more developer resources.'
plans:
- name: Canopy Plans Pricing
  plan_count: 3
  slug: canopy-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Canopy Rate Limits
  slug: canopy-rate-limits
scopes:
- name: Canopy Scopes
  scope_count: 0
  slug: canopy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 71.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 55.5
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 61.9
    developer_ergonomics: 73.2
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 16.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 80.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/screenshots/canopy-2026-06-20T173925.png
security:
- kind: authentication
  name: Canopy Authentication
  slug: canopy-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Canopy Domain Security
  slug: canopy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Canopy Vulnerability Disclosure
  slug: canopy-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Canopy Trust Center
  slug: canopy-trust-center
  summary_line: SOC 2 Type 2
slug: canopy
tags:
- Auto Insurance
- Casualty
- Financial-Services
- Homeowners Insurance
- Insurance
- Insurance Verification
- Property
website: https://www.usecanopy.com/
---
