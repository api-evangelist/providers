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
  score: 8.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xage-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/xage-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/xage-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xage-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/xage-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/xage-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/xage-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/xage-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xage-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://xage.com/
- group: company
  title: ''
  type: Blog
  url: https://xage.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://xage.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://xage.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xage.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://xage.com/careers/
- group: operate
  title: ''
  type: PressReleases
  url: https://xage.com/press/
- group: other
  title: ''
  type: CaseStudies
  url: https://xage.com/case-studies/
- group: company
  title: ''
  type: Partners
  url: https://xage.com/partners/
coverage:
  checked: '2026-09-04'
  detail: Xage's own support page tells you the documentation library lives inside the Xage support portal, and that portal's Zendesk Help Center API answers anonymously with HTTP 401 "Couldn't authenticate you" — so the Fabric Manager REST API that partners such as Axonius integrate against has no readable public reference, base URL or spec; docs.xage.com resolves in DNS but has no listener on 80 or 443.
  evidence:
  - status: 401
    url: https://xage.zendesk.com/api/v2/help_center/en-us/articles.json
  - status: 200
    url: https://xage.com/support/
  - status: 0
    url: https://docs.xage.com/
  reason: customer-only-docs
  state: gated
created: '2026-09-04'
description: Xage Security is a Palo Alto, California zero trust access and protection company whose Xage Fabric Platform enforces identity-based access control across operational technology (OT), IT, cloud and edge environments — covering privileged access management, secure remote access, VPN replacement, zero trust segmentation, critical asset protection and zero trust data exchange for critical infrastructure operators in energy, utilities, manufacturing, oil and gas, transportation, defense, government and space. Xage also markets a control layer that governs how AI agents reach resources over MCP, A2A and REST APIs. The Fabric Manager exposes a REST API that third-party platforms integrate against, but its reference documentation is published only inside the customer-authenticated Xage support portal.
image: https://xage.com/wp-content/uploads/2023/07/cropped-Xage-Favicon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: Xage Security Website MCP Server
  slug: xage-security-website-mcp-server
modified: '2026-09-04'
name: Xage
nav: Providers
network: true
overview: 'Xage is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Zero Trust, and Identity and Access Management.


  Xage''s developer surface includes authentication, engineering blog, support, and 15 more developer resources.'
plans:
- name: Xage Plans Pricing
  plan_count: 0
  slug: xage-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Xage Rate Limits
  slug: xage-rate-limits
scopes:
- name: Xage Scopes
  scope_count: 0
  slug: xage-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Xage Authentication
  slug: xage-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Xage Domain Security
  slug: xage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xage
tags:
- Company
- Security
- Cybersecurity
- Zero Trust
- Identity and Access Management
- Privileged Access Management
- Operational Technology
- Critical Infrastructure
- Industrial
- Agent Security
website: https://xage.com/
---
