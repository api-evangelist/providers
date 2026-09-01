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
api_count: 1
apis:
- description: Intersection's AI-powered Order Management System for out-of-home advertising. Announced 2026-05-11, it is a single API over Intersection's digital screen inventory (LinkNYC and other street, transit,
  name: Intersection Order Management System (OMS) API
  slug: intersection-order-management-system-oms-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.intersection.com/
- group: company
  title: ''
  type: Blog
  url: https://www.intersection.com/insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.intersection.com/insights/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.intersection.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.intersection.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.intersection.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Intersection
- group: company
  title: ''
  type: Press
  url: https://www.intersection.com/press/
- group: company
  title: ''
  type: Careers
  url: https://www.intersection.com/join-our-team/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/10016248
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/intersection_co
- group: build
  title: ''
  type: Packages
  url: packages/intersection-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/intersection-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intersection-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/intersection-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/intersection-rate-limits.yml
coverage:
  checked: '2026-08-23'
  detail: Intersection's only API - the AI-powered OOH Order Management System it announced on 2026-05-11 as an MCP server built on IAB Tech Lab OpenDirect 2.0 - is published as a press release with no endpoint, no reference and no spec, ending in "contact Intersection directly for access and integration", and every candidate API host either NXDOMAINs or (ixn.intersection.com) resolves to twelve EC2 addresses that accept no connection.
  evidence:
  - status: 200
    url: https://www.intersection.com/announcement/intersection-opens-extensive-street-level-ooh-network-to-ai-agents-for-planning-and-booking/
  - status: 404
    url: https://www.intersection.com/openapi.json
  - status: 404
    url: https://www.intersection.com/.well-known/agent-card.json
  - status: 200
    url: https://registry.modelcontextprotocol.io/v0/servers?search=intersection
  - status: 0
    url: https://ixn.intersection.com/
  reason: sales-gate
  state: gated
created: '2026-08-23'
description: 'Intersection is a New York-based, experience-driven out-of-home (OOH) media and technology company formed from the merger of Titan, a municipal out-of-home advertising operator, and Control Group, a technology and design studio. It operates street-level, transit, airport, bikeshare and place-based advertising networks across 13 major U.S. markets - including LinkNYC, the largest street-level digital network in New York City - and it builds the software behind them: the IxNConnect display-management and communications platform used by cities, transit agencies and airports, and an AI-powered Order Management System (OMS) that exposes inventory discovery, availability, pricing and campaign reservation to AI agents through an MCP server built on the IAB Tech Lab OpenDirect 2.0 specification.'
image: https://www.intersection.com/wp-content/themes/intersection/dist/images/favicons/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Intersection Order Management System (OMS) MCP Server
  slug: intersection-order-management-system-oms-mcp-server
modified: '2026-08-23'
name: Intersection
nav: Providers
network: true
overview: 'Intersection publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Out-of-Home, Digital Signage, Media, and Smart Cities.


  Intersection''s developer surface includes engineering blog, support, and 14 more developer resources.'
plans:
- name: Intersection Plans Pricing
  plan_count: 0
  slug: intersection-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Intersection Rate Limits
  slug: intersection-rate-limits
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 14.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Intersection Domain Security
  slug: intersection-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: intersection
tags:
- Advertising
- Out-of-Home
- Digital Signage
- Media
- Smart Cities
- Transit
- Programmatic
- Agents
- MCP
website: https://www.intersection.com/
---
