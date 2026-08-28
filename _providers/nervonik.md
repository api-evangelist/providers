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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nervonik-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nervonik.com/
- group: company
  title: ''
  type: Blog
  url: https://nervonik.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://nervonik.com/blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://nervonik.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nervonik.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nervonik-inc/
- group: other
  title: ''
  type: Team
  url: https://nervonik.com/team/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nervonik-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/nervonik-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nervonik-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: Nervonik's product is a physical implantable peripheral nerve stimulation device that its own site states is still under development and not FDA-cleared; the only host it operates, nervonik.com, is a five-page WordPress marketing site whose sole machine-readable output is a Yoast-generated llms.txt indexing team and news pages.
  evidence:
  - status: 200
    url: https://nervonik.com/llms.txt
  - status: 404
    url: https://nervonik.com/openapi.json
  - status: 404
    url: https://nervonik.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/nervonik
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Nervonik, Inc. is a clinical-stage medical device company in Los Angeles, California, founded in 2020 by CEO Aydin Babakhani, developing miniaturized peripheral nerve stimulation (PNS) neuromodulation implants for chronic neuropathic pain in high-motion anatomy. Its platform pairs proprietary wireless power delivery and miniaturized implantable leads with integrated sensing circuitry that records evoked compound action potentials (ECAPs) and other biomarkers, enabling closed-loop, patient-specific stimulation as an opioid-free alternative to spinal cord stimulators and pharmacological therapy. The company completed a first-in-human feasibility study and closed an oversubscribed $52.5M Series B in April 2026 led by Amzak Health, after a $13M Series A in March 2025. Nervonik publishes no developer program, public API, SDK, or machine-readable API contract; its public web surface is a WordPress marketing and investor-relations site.
image: https://nervonik.com/wp-content/uploads/2026/01/Nervonik-Featured-1-80.jpg
layout: provider
modified: '2026-08-26'
name: Nervonik
nav: Providers
network: true
overview: 'Nervonik is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Neuromodulation, Neurotechnology, and Health.


  Nervonik''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Nervonik Plans Pricing
  plan_count: 0
  slug: nervonik-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Nervonik Rate Limits
  slug: nervonik-rate-limits
score:
  band: minimal
  composite: 8.3
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Nervonik Domain Security
  slug: nervonik-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: nervonik
tags:
- Company
- Medical Devices
- Neuromodulation
- Neurotechnology
- Health
- Chronic Pain
- Implantable Devices
- Clinical Stage
- Medical Technology
website: https://nervonik.com/
---
