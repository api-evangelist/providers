---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 214
  human_in_the_loop: 0
  name: Impulse Dynamics Agentic Access
  operation_count: 379
  slug: impulse-dynamics-agentic-access
  summary_line: 379 operations · 214 acting
api_count: 5
apis:
- description: 'WordPress core content API of the corporate website (posts, pages, media, taxonomies, users, settings) plus this company''s own custom post types: the CCM clinic/provider locator, the Optimizer technic'
  name: Impulse Dynamics wp/v2 API
  slug: impulse-dynamics-wp-v2-api
- description: Two Model Context Protocol servers exposed by the WordPress MCP Adapter plugin on the corporate host. Both reject anonymous JSON-RPC with HTTP 401, and the host publishes no RFC 8414 or RFC 9728 metad
  name: Impulse Dynamics MCP API
  slug: impulse-dynamics-mcp-api
- description: 'WordPress Abilities API — the registry of named abilities the MCP adapter draws its tools from. Capability-gated: HTTP 401 rest_forbidden anonymously.'
  name: Impulse Dynamics wp-abilities/v1 API
  slug: impulse-dynamics-wp-abilities-v1-api
- description: oEmbed discovery and proxy endpoints.
  name: Impulse Dynamics oEmbed/1.0 API
  slug: impulse-dynamics-oembed-1-0-api
- description: REST API index / namespace discovery — the anonymous route-discovery document this whole profile was derived from.
  name: Impulse Dynamics Root API
  slug: impulse-dynamics-root-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://impulse-dynamics.com/
- group: company
  title: ''
  type: About
  url: https://impulse-dynamics.com/company/
- group: company
  title: ''
  type: Blog
  url: https://news.impulse-dynamics.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://impulse-dynamics.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://impulse-dynamics.com/company/careers/
- group: other
  title: ''
  type: Governance
  url: https://impulse-dynamics.com/company/governance/
- group: operate
  title: ''
  type: Contact
  url: https://impulse-dynamics.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://impulse-dynamics.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://impulse-dynamics.com/privacy-policy/
- group: other
  title: ''
  type: DataProtection
  url: https://impulse-dynamics.com/data-protection-statement/
- group: auth
  title: ''
  type: Security
  url: https://impulse-dynamics.com/vulnerability-disclosure-program/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/impulse-dynamics-stock
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/impulse-dynamics-wp-rest-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/impulse-dynamics-wp-rest-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/impulse-dynamics-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/impulse-dynamics-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/impulse-dynamics-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/impulse-dynamics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/impulse-dynamics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/impulse-dynamics-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/impulse-dynamics-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/impulse-dynamics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/impulse-dynamics-conformance.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/impulse-dynamics-agentic-access.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/impulse-dynamics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/impulse-dynamics-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/impulse-dynamics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/impulse-dynamics-domain-security.yml
created: '2026-08-23'
description: 'Impulse Dynamics is a medical-device company that created Cardiac Contractility Modulation (CCM) therapy, delivered by the implantable Optimizer Smart and Optimizer Smart Mini pulse generators for patients with moderate-to-severe chronic heart failure who remain symptomatic despite guideline-directed medical therapy. Incorporated in 1997, with US headquarters in Marlton, New Jersey, the company won the first-ever FDA Breakthrough Device designation and received FDA approval for the Optimizer Smart in March 2019; the device has been CE marked since October 2016 and is now approved in more than 30 countries plus China. Impulse Dynamics operates no developer programme: there is no developer portal, API documentation, API reference, SDK, CLI, sandbox, pricing or sign-up, and nothing clinical or device-related is exposed as an API. It is catalogued here because its corporate website runs a live, anonymous, self-describing WordPress REST API advertising 420 routes across 30 namespaces,
  because that same install exposes two Model Context Protocol servers, and because the company publishes a substantive vulnerability disclosure programme with two PGP-published security contacts covering its medical devices, health software and infrastructure.'
image: https://impulse-dynamics.com/wp-content/uploads/2023/05/Impulse-Dynamics_Logo_1.0.png
layout: provider
mcp_servers:
- description: ''
  name: Impulse Dynamics MCP Server
  slug: impulse-dynamics-mcp-server
modified: '2026-08-23'
name: Impulse Dynamics
nav: Providers
network: true
overview: 'Impulse Dynamics publishes 5 APIs on the [APIs.io](https://apis.io/) network, including wp/v2 API, MCP API, wp-abilities/v1 API, and 2 more. Tagged areas include Company, Medical Devices, Healthcare, Cardiology, and Heart Failure.


  Impulse Dynamics'' developer surface includes engineering blog, authentication, and 27 more developer resources.'
plans:
- name: Impulse Dynamics Plans Pricing
  plan_count: 0
  slug: impulse-dynamics-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Impulse Dynamics Rate Limits
  slug: impulse-dynamics-rate-limits
score:
  band: emerging
  composite: 18.2
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 13.2
    developer_ergonomics: 16.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 18.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Impulse Dynamics Authentication
  slug: impulse-dynamics-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Impulse Dynamics Domain Security
  slug: impulse-dynamics-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Impulse Dynamics Vulnerability Disclosure
  slug: impulse-dynamics-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: impulse-dynamics
tags:
- Company
- Medical Devices
- Healthcare
- Cardiology
- Heart Failure
- Implantable Devices
- Health Technology
- Life Sciences
- Clinical Trials
- MCP
- WordPress
website: https://impulse-dynamics.com/
---
