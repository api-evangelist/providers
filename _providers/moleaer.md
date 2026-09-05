---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.moleaer.com/
- group: company
  title: ''
  type: Blog
  url: https://www.moleaer.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.moleaer.com/contact/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://faq.moleaer.com/en/knowledge
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moleaer.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moleaer.com/en-us/terms-of-service
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moleaer
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moleaer-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moleaer-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Moleaer sells nanobubble generators and pairs them with an AMI Global-built remote monitoring service whose entire surface is a login-gated ASP.NET portal — www.monitoring-moleaer.com 302s every non-login path to /login.aspx — and the company publishes no developer portal, API reference, SDK or spec anywhere on moleaer.com, faq.moleaer.com or its GitHub org (4 public repos, all internal Netlify/Notion program hubs).
  evidence:
  - status: 302
    url: https://www.monitoring-moleaer.com/api-docs
  - status: 404
    url: https://www.moleaer.com/openapi.json
  - status: 404
    url: https://www.moleaer.com/.well-known/agent-card.json
  - status: 0
    url: https://api.moleaer.com/
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Moleaer Inc. is a Hawthorne, California nanobubble technology company that designs and manufactures nanobubble generators — Clear, Bloom, Lotus, Neo, Nexus, Trinity, Freya, Indalo, Titan and XTB, plus the NanoShield service — used to raise dissolved oxygen, act as a chemical-free oxidant, and control algae and biofilm in aquaculture, horticulture and irrigation water, lakes and ponds, wastewater treatment, food and beverage, car washes, mining, and oil and gas. Its only digital surface is a customer-only remote monitoring service, launched in 2020 with industrial IoT provider AMI Global, that reports equipment status and water-quality readings (DO, pH, ORP, temperature, conductivity) into a login-gated portal at www.monitoring-moleaer.com. Moleaer publishes no public API, SDK, developer portal or machine-readable specification; equipment-level integration is offered through industrial control protocols (SCADA/Modbus/EtherNet-IP) on the generators themselves, not through a web
  API.
image: https://www.moleaer.com/hubfs/Logo-2.png
layout: provider
modified: '2026-08-26'
name: Moleaer
nav: Providers
network: true
overview: 'Moleaer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nanobubbles, Water Treatment, Water Quality, and Aquaculture.


  Moleaer''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Moleaer Plans Pricing
  plan_count: 0
  slug: moleaer-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Moleaer Rate Limits
  slug: moleaer-rate-limits
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moleaer/refs/heads/main/screenshots/moleaer-2026-09-02T150652.png
security:
- kind: domain-security
  name: Moleaer Domain Security
  slug: moleaer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moleaer
tags:
- Company
- Nanobubbles
- Water Treatment
- Water Quality
- Aquaculture
- Agriculture
- Wastewater
- Industrial Equipment
- Remote Monitoring
- Internet of Things
- Manufacturing
website: https://www.moleaer.com/
---
