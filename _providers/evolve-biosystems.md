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
  url: security/evolve-biosystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.infinanthealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.infinanthealth.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.infinanthealth.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.infinanthealth.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.infinanthealth.com/privacy
- group: company
  title: ''
  type: Newsletter
  url: https://www.infinanthealth.com/newsletter-subscribe
- group: company
  title: ''
  type: Press
  url: https://www.infinanthealth.com/press
- group: company
  title: ''
  type: Investors
  url: https://www.infinanthealth.com/for-investors
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/evolve-biosystems_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evolve-biosystems-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/evolve-biosystems-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/evolve-biosystems-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: Infinant Health is a UC Davis infant-microbiome biotech that sells the Evivo probiotic and develops the INF108 drug candidate; its only web properties are a HubSpot marketing site and a WordPress consumer store, and api./developer./docs. infinanthealth.com do not resolve in DNS at all.
  evidence:
  - status: 404
    url: https://www.infinanthealth.com/openapi.json
  - status: 404
    url: https://www.infinanthealth.com/.well-known/agent-card.json
  - status: 404
    url: https://www.infinanthealth.com/llms.txt
  - status: 404
    url: https://www.evivo.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/infinanthealth
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: 'Infinant Health (formerly Evolve Biosystems) is a privately held life-sciences company in Sacramento, California, spun out of the Foods for Health Institute at the University of California, Davis after more than a decade of research into the infant gut microbiome. Its foundational discovery is B. infantis EVC001, a strain of Bifidobacterium longum subsp. infantis that metabolizes human milk oligosaccharides and has largely disappeared from infants in industrialized countries. The company commercializes that strain as Evivo, a consumer infant probiotic sold direct-to-consumer and through retail, and is developing INF108 as a drug candidate intended to reduce necrotizing enterocolitis in premature infants. Infinant Health is a biotechnology and consumer-health manufacturer rather than a software company: it publishes clinical trials, peer-reviewed publications and investor material, but no developer program, public API, SDK or machine-readable API contract could be found on any
  of its hosts.'
image: https://www.infinanthealth.com/hs-fs/hubfs/Infinant_logo_K_no_mark_new.png?width=500&height=250&name=Infinant_logo_K_no_mark_new.png
layout: provider
modified: '2026-08-12'
name: Infinant Health
nav: Providers
network: true
overview: 'Infinant Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Health, and Infant Nutrition.


  Infinant Health''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Evolve Biosystems Plans Pricing
  plan_count: 0
  slug: evolve-biosystems-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Evolve Biosystems Rate Limits
  slug: evolve-biosystems-rate-limits
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
  name: Evolve Biosystems Domain Security
  slug: evolve-biosystems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: evolve-biosystems
tags:
- Company
- Biotechnology
- Life Sciences
- Health
- Infant Nutrition
- Microbiome
- Probiotics
- Consumer Health
- Pharmaceuticals
- Clinical Research
website: https://www.infinanthealth.com/
---
