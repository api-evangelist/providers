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
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coco-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coco-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.cocodelivery.com/
- group: company
  title: ''
  type: About
  url: https://www.cocodelivery.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.cocodelivery.com/blog
- group: company
  title: ''
  type: Press
  url: https://www.cocodelivery.com/press
- group: operate
  title: ''
  type: Support
  url: https://www.cocodelivery.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cocodelivery.com/merchant-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cocodelivery.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cocorobotics
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/cocodelivery
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cocodelivery/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/CocoRobotics
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/coco.robot/
coverage:
  checked: '2026-08-09'
  detail: Coco has no developer surface at all — the 39-page Framer marketing site 404s on /developers and /api, no docs/developer/api subdomain resolves, and the only API host in its own code (api.cyanbot.com, hard-coded in the track.cocodelivery.com order-tracker bundle) is now NXDOMAIN; merchants reach Coco through Uber Eats, DoorDash, Wolt and Olo Dispatch rather than through a Coco API.
  evidence:
  - status: 404
    url: https://www.cocodelivery.com/developers
  - status: 404
    url: https://www.cocodelivery.com/api
  - status: 404
    url: https://www.cocodelivery.com/.well-known/api-catalog
  - status: 404
    url: https://www.cocodelivery.com/llms.txt
  - status: 0
    url: https://api.cyanbot.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: 'Coco Robotics is a Santa Monica, California urban robotics company operating a fleet of zero-emission, remotely-supervised sidewalk delivery robots ("Cocobots") for last-mile food, grocery and retail delivery. Merchants do not integrate with Coco directly: Coco is consumed as a delivery service provider through Uber Eats, DoorDash, Wolt and Olo Dispatch, and the company publishes no developer portal, API documentation, SDKs or webhooks of its own. Its public software surface is limited to a marketing site, a customer order-tracking web app, and a GitHub organization of forked ROS and infrastructure tooling.'
image: https://framerusercontent.com/assets/7ibf2PeV3erFTPA5Cn1q9XrTE.jpg
layout: provider
modified: '2026-08-09'
name: Coco Robotics
nav: Providers
network: true
overview: 'Coco Robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Delivery, Logistics, and Last Mile.


  Coco Robotics'' developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 60
score:
  band: minimal
  composite: 11.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Coco Domain Security
  slug: coco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coco
tags:
- Company
- Robotics
- Delivery
- Logistics
- Last Mile
- Autonomous Vehicles
- Urban Mobility
- Food Delivery
website: https://www.cocodelivery.com/
---
