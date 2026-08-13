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
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epic-cleantec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://epiccleantec.com/
- group: company
  title: ''
  type: About
  url: https://epiccleantec.com/about
- group: company
  title: ''
  type: Blog
  url: https://epiccleantec.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://epiccleantec.com/feed
- group: operate
  title: ''
  type: Support
  url: https://epiccleantec.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://epiccleantec.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://epiccleantec.com/privacy-policy
- group: company
  title: ''
  type: Newsletter
  url: https://epiccleantec.com/newsletter
- group: company
  title: ''
  type: Careers
  url: https://epiccleantec.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/epiccleantec/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/EpicCleantec
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@epiccleantec
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/epic-cleantec-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/epic-cleantec-plans-pricing.yml
coverage:
  checked: '2026-08-12'
  detail: Epic Cleantec ships a cloud-connected Eco-Insights reporting dashboard with every OneWater system, but that dashboard is an end-user product for building owners — the marketing site is the company's only public host, no api./app./portal./docs./developer subdomain resolves (all NXDOMAIN), and every OpenAPI, GraphQL, MCP, agent-card and /.well-known/ path probed on epiccleantec.com returned 404.
  evidence:
  - status: 404
    url: https://epiccleantec.com/openapi.json
  - status: 404
    url: https://epiccleantec.com/.well-known/agent-card.json
  - status: 404
    url: https://epiccleantec.com/llms.txt
  - status: 200
    url: https://epiccleantec.com/solutions/technology
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: Epic Cleantec is a San Francisco based water technology company that designs, builds and operates onsite water reuse systems for buildings. Its OneWater and OneWater Rain systems collect, treat and recycle a building's greywater, blackwater, rainwater and condensate onsite — recovering up to 95% of wastewater for non-potable uses such as toilet flushing, irrigation, cooling towers and laundry — alongside wastewater heat recovery and a soil amendment product line. The technology grew out of work on the Bill and Melinda Gates Foundation Reinvent the Toilet Challenge and is deployed in multifamily, commercial office, hospitality, stadium, data center, higher education and community-scale developments across North America. Systems ship with PLC/SCADA control and a cloud-connected Eco-Insights reporting dashboard for remote monitoring, alarms and utility savings reporting, but Epic Cleantec publishes no public developer program, API documentation or machine-readable API contract;
  the data surface is delivered to building owners and operators as a hosted dashboard rather than as a public API.
image: https://epiccleantec.com/wp-content/uploads/Epic_Cleantec_Logo_Stacked_Color-6.jpg
layout: provider
modified: '2026-08-12'
name: Epic CleanTec
nav: Providers
network: true
overview: 'Epic CleanTec is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Water, Water Reuse, Wastewater, and Cleantech.


  Epic CleanTec''s developer surface includes engineering blog, support, YouTube channel, and 12 more developer resources.'
plans:
- name: Epic Cleantec Plans Pricing
  plan_count: 0
  slug: epic-cleantec-plans-pricing
random_paper: 93
score:
  band: minimal
  composite: 11.3
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: domain-security
  name: Epic Cleantec Domain Security
  slug: epic-cleantec-domain-security
  summary_line: TLSv1.3 · DMARC
slug: epic-cleantec
tags:
- Company
- Water
- Water Reuse
- Wastewater
- Cleantech
- Sustainability
- Buildings
- Real Estate
- Climate Tech
- Internet of Things
website: https://epiccleantec.com/
---
