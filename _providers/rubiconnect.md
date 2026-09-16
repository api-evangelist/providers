---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-09-15'
api_count: 2
apis:
- baseURL: https://console.rubiconnect.com/api/v1
  baseurl_source: declared
  description: REST API for sending messages, managing campaigns, RCS capability checks, and webhook callbacks. Auth via API key (X-API-Key) or Bearer token.
  name: RubiConnect Messaging Platform
  slug: rubiconnect-messaging-platform
- description: Hosted MCP server exposing 18 tools for messaging, templates, campaigns, agents, analytics, and media. Auth via OAuth 2.0/PKCE or API key.
  name: RubiConnect MCP Server
  slug: rubiconnect-mcp-server
artifact_total: 9
asyncapis:
- description: ''
  name: Rubiconnect Webhooks
  slug: rubiconnect-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.rubiconnect.com/en
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rubiconnect/refs/heads/main/security/rubiconnect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rubiconnect-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rubiconnect/refs/heads/main/authentication/rubiconnect-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rubiconnect-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rubiconnect/refs/heads/main/well-known/rubiconnect-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rubiconnect-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rubiconnect/refs/heads/main/llms/rubiconnect-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rubiconnect-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rubiconnect/refs/heads/main/packages/rubiconnect-packages.yml
  title: ''
  type: Packages
  url: packages/rubiconnect-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rubiconnect/refs/heads/main/scopes/rubiconnect-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/rubiconnect-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rubiconnect/refs/heads/main/conformance/rubiconnect-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rubiconnect-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rubiconnect/refs/heads/main/errors/rubiconnect-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rubiconnect-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rubiconnect/refs/heads/main/data-model/rubiconnect-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rubiconnect-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rubiconnect/refs/heads/main/conventions/rubiconnect-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rubiconnect-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rubiconnect/refs/heads/main/lifecycle/rubiconnect-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rubiconnect-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rubiconnect/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/rubiconnect/refs/heads/main/plans/rubiconnect-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rubiconnect-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/rubiconnect/refs/heads/main/rate-limits/rubiconnect-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rubiconnect-rate-limits.yml
- group: start
  title: ''
  type: SignUp
  url: https://console.rubiconnect.com/en?view=signUp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rubiconnect.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rubiconnect.com/en/privacy
- group: company
  title: ''
  type: Blog
  url: https://rubiconnect.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zarelan/rubiconnect-mcp
created: '2026-09-15'
description: Enterprise business-messaging (CPaaS) platform for RCS Business Messaging and WhatsApp Business, exposing a REST API with a public OpenAPI contract and a hosted MCP server with 18 tools for messaging, campaigns, templates, and analytics.
layout: provider
mcp_servers:
- description: Official first-party MCP server for the RubiConnect RCS Business Messaging and WhatsApp Business platform. Exposes 18 tools spanning capability checks, rich messaging, inbox, templates, campaigns, age
  name: RubiConnect MCP Server
  slug: rubiconnect-mcp-server
modified: '2026-09-15'
name: RubiConnect
nav: Providers
network: true
overview: 'RubiConnect publishes 1 API on the [APIs.io](https://apis.io/) network: Messaging Platform. Tagged areas include CPaaS, Communications APIs, Business Messaging, RCS, and WhatsApp Business.


  The RubiConnect catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  RubiConnect''s developer surface includes authentication, signup flow, engineering blog, and 17 more developer resources.'
plans:
- name: Rubiconnect Plans Pricing
  plan_count: 0
  slug: rubiconnect-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Rubiconnect Rate Limits
  slug: rubiconnect-rate-limits
scopes:
- name: Rubiconnect Scopes
  scope_count: 0
  slug: rubiconnect-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 57.0
    developer_ergonomics: 25.6
    discoverability: 64.8
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 66.7
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Rubiconnect Authentication
  slug: rubiconnect-authentication
  summary_line: apiKey/http/oauth2 · 2 schemes
- kind: domain-security
  name: Rubiconnect Domain Security
  slug: rubiconnect-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rubiconnect
tags:
- CPaaS
- Communications APIs
- Business Messaging
- RCS
- WhatsApp Business
- SMS
- Marketing & Campaigns
- Conversational AI
- MCP
- AI Agents
website: https://www.rubiconnect.com/en
---
