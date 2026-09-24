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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.aessensegrows.com/en/
- group: operate
  title: ''
  type: Support
  url: https://www.aessensegrows.com/en/contact-us-cultivation
- group: company
  title: ''
  type: Blog
  url: https://www.aessensegrows.com/en/resources/plant-science-test-kitchen-blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aessensegrows.com/en/corporate/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aessensegrows.com/en/corporate/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aessenseholding/refs/heads/main/security/aessenseholding-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aessenseholding-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aessenseholding/refs/heads/main/conformance/aessenseholding-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aessenseholding-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aessenseholding/refs/heads/main/packages/aessenseholding-packages.yml
  title: ''
  type: Packages
  url: packages/aessenseholding-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aessenseholding/refs/heads/main/plans/aessenseholding-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aessenseholding-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aessenseholding/refs/heads/main/rate-limits/aessenseholding-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aessenseholding-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aessenseholding/refs/heads/main/llms/aessenseholding-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aessenseholding-llms.txt
coverage:
  checked: '2026-09-12'
  detail: AEssenseGrows sells aeroponic SmartFarm hardware whose Guardian Grow Manager control software ships bundled with the machines as an operator web application reached by demo request — there is no developer portal, no API reference and no GitHub organization, the public Technical Document Library is product brochures and UL/CE datasheets in PDF, and the one regulated machine interface the company is on record as touching (California Metrc seed-to-sale) is one Guardian consumes, not one it publishes.
  evidence:
  - status: 200
    url: https://www.aessensegrows.com/en/
  - status: 200
    url: https://www.aessensegrows.com/sitemap.xml
  - status: 404
    url: https://www.aessensegrows.com/openapi.json
  - status: 404
    url: https://www.aessensegrows.com/.well-known/agent-card.json
  - status: 404
    url: https://www.aessensegrows.com/llms.txt
  - status: 200
    url: https://api.github.com/search/users?q=aessense
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: 'AEssenseGrows is the operating brand of AEssense Corporation (held as AEssense Holding), a precision agtech manufacturer founded in Silicon Valley in 2014 by Robert Chen and headquartered at 205 E Alma Ave, San Jose, California, with a second facility in Jiading, Shanghai. It designs and builds fully automated zero-soil aeroponic SmartFarms for commercial indoor growers — the modular, stackable AEtrium-2.1 cloning and vegging system, the AEtrium-4 and Double Deck AEtrium-4 bloom systems, the compact Nursery-6, and the AEtrium Automated Dosing Unit — together with the AExcel, Aerix, AEdge and Blaze LED and horticultural lighting lines and a design-build-test-train-transfer consulting practice. The hardware is wired with a blanket of precision sensors and driven by Guardian Grow Manager, the company''s own control software, which automates nutrient dosing, irrigation, photoperiod, pH, CO2, humidity and temperature against customer-authored Grow Plan recipes, logs and analyzes
  the resulting grow data, and offers remote access and alerting from any browser. A second brand, AEssenseFresh (aessensefresh.com), takes the same platform to leafy greens and fresh produce; the cannabis line has been licensed to integrate California''s Metrc seed-to-sale system, which makes Guardian a consumer of a third-party regulatory API rather than a producer of one. AEssenseGrows operates no public developer program: there is no developer portal, no API reference, no OpenAPI, AsyncAPI, GraphQL SDL or Postman collection, no first-party SDK on any package registry, and no GitHub organization. Guardian ships only as an end-user product bundled with the hardware it controls, and the public Technical Document Library is product brochures and UL/CE datasheets in PDF. Customer documentation beyond that sits behind a Grow Partner Portal private-access request form.'
image: https://www.aessensegrows.com/hubfs/AEssense%20Grows%20Logo%20V00%20MIXED%202.png
layout: provider
modified: '2026-09-12'
name: AEssenseGrows
nav: Providers
network: true
overview: 'AEssenseGrows is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Aeroponics, and Hydroponics.


  AEssenseGrows'' developer surface includes support, engineering blog, and 9 more developer resources.'
plans:
- name: Aessenseholding Plans Pricing
  plan_count: 0
  slug: aessenseholding-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Aessenseholding Rate Limits
  slug: aessenseholding-rate-limits
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 12.8
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aessenseholding Domain Security
  slug: aessenseholding-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aessenseholding
tags:
- Company
- Agriculture
- AgTech
- Aeroponics
- Hydroponics
- Vertical Farming
- Controlled Environment Agriculture
- Indoor Farming
- Automation
- Industrial IoT
- LED Lighting
- Cannabis
- Hardware
- Manufacturing
website: https://www.aessensegrows.com/en/
---
