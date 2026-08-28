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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/osaro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.osaro.com/
- group: company
  title: ''
  type: About
  url: https://www.osaro.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.osaro.com/media
- group: operate
  title: ''
  type: FAQ
  url: https://www.osaro.com/resources/faq
- group: operate
  title: ''
  type: ContactUs
  url: https://www.osaro.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.osaro.com/legal/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.osaro.com/legal/terms-of-use
- group: company
  title: ''
  type: Careers
  url: https://jobs.lever.co/osaro
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/osaroinc/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@OsaroAI
- group: auth
  title: ''
  type: Compliance
  url: conformance/osaro-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/osaro-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/osaro-plans-pricing.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/osaro-well-known.yml
- group: auth
  title: ''
  type: SecurityProbe
  url: security/osaro-vulnerability-disclosure.yml
coverage:
  checked: '2026-08-26'
  detail: OSARO ships its SightWorks perception software only as part of an integrated robotic work cell delivered by its own field team and integrator partners, so its complete 74-URL sitemap contains no developer, docs or API page and no api./docs./developer.osaro.com host exists in DNS.
  evidence:
  - status: 200
    url: https://www.osaro.com/sitemap.xml
  - status: 404
    url: https://www.osaro.com/developers
  - status: 404
    url: https://www.osaro.com/api
  - status: 404
    url: https://www.osaro.com/openapi.json
  - status: 0
    url: https://api.osaro.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: OSARO is a San Francisco-based industrial AI company that builds machine-learning software for warehouse and fulfillment robotics. Its SightWorks perception platform and AutoModel learning system let industrial robot arms perceive, grasp and place highly variable goods without per-SKU pre-training, 3D object models or fixed programming, powering piece picking, robotic bagging, kitting and mixed-case depalletizing in production deployments across five countries. OSARO sells complete robotic work cells and licenses its perception software to robot makers and system integrators, wrapping deployments in its HyperCare support program. The company publishes no public developer program, API documentation or machine-readable API contract; integration with customer estates (WMS/WCS, conveyors, ASRS, AMRs) is delivered as a professional-services engagement through OSARO and its integrator partners rather than through a self-serve API.
image: https://cdn.prod.website-files.com/68701c86565deda53fa2f1b0/68702c4aefcbf3192f452701_OSARO%20-%20Logo%20-%20Gradient.svg
layout: provider
modified: '2026-08-26'
name: OSARO
nav: Providers
network: true
overview: 'OSARO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Artificial Intelligence, Machine Learning, and Warehouse Automation.


  OSARO''s developer surface includes engineering blog, FAQ, YouTube channel, and 13 more developer resources.'
plans:
- name: Osaro Plans Pricing
  plan_count: 0
  slug: osaro-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 13.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Osaro Domain Security
  slug: osaro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Osaro Vulnerability Disclosure
  slug: osaro-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Osaro Trust Center
  slug: osaro-trust-center
  summary_line: SOC 2 Type II
slug: osaro
tags:
- Company
- Robotics
- Artificial Intelligence
- Machine Learning
- Warehouse Automation
- Logistics
- Supply Chain
- Computer Vision
- Manufacturing
website: https://www.osaro.com/
---
