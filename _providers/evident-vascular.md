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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evident-vascular-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evident-vascular-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/evident-vascular-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/evident-vascular-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://evidentvascular.com/
- group: company
  title: ''
  type: Blog
  url: https://evidentvascular.com/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://evidentvascular.com/newsroom/feed/
- group: operate
  title: ''
  type: Support
  url: https://evidentvascular.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://evidentvascular.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evidentvascular.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/evident-vascular/
coverage:
  checked: '2026-08-12'
  detail: Evident Vascular is a pre-commercial medical device maker whose product is an IVUS catheter and console awaiting FDA 510(k) clearance, so its five-page WordPress marketing site has no developer section at all and every API host an integrator would try (api., developer., docs., app., portal.evidentvascular.com) is NXDOMAIN.
  evidence:
  - status: 404
    url: https://evidentvascular.com/developers
  - status: 404
    url: https://evidentvascular.com/openapi.json
  - status: 404
    url: https://evidentvascular.com/llms.txt
  - status: 404
    url: https://evidentvascular.com/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: Evident Vascular, Inc. is a San Jose, California medical device company developing the Evident Vascular Guidance System, an AI-powered intravascular ultrasound (IVUS) platform purpose-built for peripheral vascular image-guided therapy, with future capability intended for coronary procedures. The company came out of stealth in 2023 with a $35M Series A led by Vensana Capital and closed a Series B in March 2025 with Shangbay Capital and strategic investors, funding work toward FDA 510(k) clearance and a U.S. launch. The platform pairs an IVUS catheter and console with machine-learning image interpretation intended to improve vessel assessment and streamline the interventional workflow. Evident Vascular is pre-commercial and publishes no developer program, API, SDK, or machine-readable interface on its public web surface.
image: https://evidentvascular.com/wp-content/uploads/Evident_Vascular_Logo_White.png
layout: provider
modified: '2026-08-12'
name: Evident Vascular
nav: Providers
network: true
overview: 'Evident Vascular is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health, Imaging, and Artificial Intelligence.


  Evident Vascular''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Evident Vascular Plans Pricing
  plan_count: 0
  slug: evident-vascular-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Evident Vascular Rate Limits
  slug: evident-vascular-rate-limits
score:
  band: emerging
  composite: 11.2
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Evident Vascular Domain Security
  slug: evident-vascular-domain-security
  summary_line: TLSv1.3
slug: evident-vascular
tags:
- Company
- Medical Devices
- Health
- Imaging
- Artificial Intelligence
- Cardiovascular
- Ultrasound
- Medical Imaging
website: https://evidentvascular.com/
---
