---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flytrex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flytrex.com/
- group: operate
  title: ''
  type: Support
  url: https://www.flytrex.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flytrex.com/legal/informational-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flytrex.com/legal/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://partners.flytrex.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Flytrex
- group: company
  title: ''
  type: Press
  url: https://www.flytrex.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.flytrex.com/careers
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flytrex-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flytrex-llms.txt
coverage:
  checked: '2026-08-16'
  detail: Flytrex's only public developer program, the OAuth2 Flytrex Live API at x.flytrex.com, has been decommissioned to the point that the host has no DNS record at all, and the current site offers merchants a sign-in portal and a contact form in its place with no API mentioned anywhere.
  evidence:
  - status: 0
    url: http://x.flytrex.com/developers/live-api/
  - status: 0
    url: https://api.flytrex.com/openapi.json
  - status: 404
    url: https://www.flytrex.com/.well-known/agent-card.json
  - status: 404
    url: https://www.flytrex.com/llms.txt
  - status: 200
    url: https://www.flytrex.com/merchants
  reason: no-developer-program
  state: none
created: '2026-08-16'
description: Flytrex is an autonomous drone delivery operator headquartered in Tel Aviv, Israel, with US operations centered on the Dallas-Fort Worth metroplex and North Carolina. The company runs an end-to-end backyard delivery service that flies food and small goods from partner restaurants and retailers to consumer homes in roughly five minutes, operating its own Sky-series multirotor aircraft, ground docks, and a remote-operations control center. Flytrex sells to consumers through its own iOS and Android ordering apps and to merchants through a partner portal, and routes demand from third-party marketplaces including DoorDash and Uber Eats. It does not currently publish a public developer program, API reference, or machine-readable specification.
image: https://www.flytrex.com/og-image.png
layout: provider
modified: '2026-08-16'
name: Flytrex
nav: Providers
network: true
overview: 'Flytrex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drone Delivery, Last Mile Delivery, Logistics, and Autonomous Systems.


  Flytrex''s developer surface includes support and 10 more developer resources.'
random_paper: 37
score:
  band: emerging
  composite: 15.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
security:
- kind: domain-security
  name: Flytrex Domain Security
  slug: flytrex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flytrex
tags:
- Company
- Drone Delivery
- Last Mile Delivery
- Logistics
- Autonomous Systems
- Unmanned Aerial Vehicles
- Aviation
- Food Delivery
website: https://www.flytrex.com/
---
