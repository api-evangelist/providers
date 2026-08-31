---
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helmai-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/helmai-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/helmai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/helmai-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://helm.ai/
- group: company
  title: ''
  type: Blog
  url: https://helm.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://helm.ai/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/helm-ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://helm.ai/privacy-policy
- group: company
  title: ''
  type: Press
  url: https://helm.ai/news
- group: company
  title: ''
  type: PressKit
  url: https://helm.ai/press-kit
coverage:
  checked: '2026-08-22'
  detail: Helm.ai licenses embedded perception and autonomy software into OEM vehicle programs (Honda, Volkswagen) and runs no developer surface whatsoever — api./docs./developer./ app./console./status.helm.ai are all NXDOMAIN, /developers /api /sdk /documentation /pricing and every /.well-known/ path return 404 from its Webflow marketing site, and the strings "SDK", "developer" and "docs" appear ZERO times across its seven product and technology pages, which all end at a "BOOK A DEMO" contact form.
  evidence:
  - status: 404
    url: https://helm.ai/openapi.json
  - status: 404
    url: https://helm.ai/developers
  - status: 404
    url: https://helm.ai/.well-known/agent-card.json
  - status: 404
    url: https://helm.ai/.well-known/api-catalog
  - status: 404
    url: https://helm.ai/graphql
  - status: 200
    url: https://api.github.com/orgs/helm-ai/repos
  - status: 200
    url: https://helm.ai/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Helm.ai is an AI software company for autonomous driving and robotics, founded in 2016 and headquartered in Redwood City, California. It develops camera-first perception, path prediction and end-to-end autonomy stacks — Helm.ai Vision and Helm.ai Driver — alongside the generative AI development and validation tools VidGen-3, GenSim-3 and WorldGen-1, all trained with its proprietary Deep Teaching unsupervised learning method. The software is licensed to automotive OEMs and Tier 1 suppliers (Honda, Volkswagen, Ambarella, NVIDIA, Qualcomm, Texas Instruments) as embedded, hardware-agnostic components for production vehicle programs rather than as a public developer API. As of 2026-08-22 the company publishes no developer portal, API reference, SDK, or machine-readable specification on any host it controls.
image: https://cdn.prod.website-files.com/65f47b0c0401bc4c08dd802a/6664edcabcd4c93b85b3c222_256x256.png
layout: provider
modified: '2026-08-22'
name: Helm.ai
nav: Providers
network: true
overview: 'Helm.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Autonomous Driving, Automotive, and ADAS.


  Helm.ai''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Helmai Plans Pricing
  plan_count: 0
  slug: helmai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Helmai Rate Limits
  slug: helmai-rate-limits
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 12.6
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Helmai Domain Security
  slug: helmai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: helmai
tags:
- Company
- Artificial Intelligence
- Autonomous Driving
- Automotive
- ADAS
- Computer-Vision
- Machine-Learning
- Generative AI
- Simulation
- Robotics
website: https://helm.ai/
---
