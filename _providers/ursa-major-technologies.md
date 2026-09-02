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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ursa-major-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ursamajor.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/ursa-major-technologies_stock/
- group: company
  title: ''
  type: About
  url: https://ursamajor.com/about/
- group: other
  title: ''
  type: Leadership
  url: https://ursamajor.com/leadership/
- group: other
  title: ''
  type: Capabilities
  url: https://ursamajor.com/capabilities/
- group: other
  title: ''
  type: Products
  url: https://ursamajor.com/hypersonics/
- group: other
  title: ''
  type: Products
  url: https://ursamajor.com/solid-rocket-motors/
- group: other
  title: ''
  type: Products
  url: https://ursamajor.com/space/
- group: company
  title: ''
  type: Blog
  url: https://ursamajor.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://ursamajor.com/feed/
- group: company
  title: ''
  type: Press
  url: https://ursamajor.com/news/
- group: company
  title: ''
  type: Careers
  url: https://ursamajor.com/careers/
- group: other
  title: ''
  type: Media
  url: https://ursamajor.com/downloadable-assets/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ursamajor.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ursamajor.com/privacy/
- group: other
  title: ''
  type: CopyrightPolicy
  url: https://ursamajor.com/copyright-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ursa-major-technologies/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ursamajortech
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ursamajortech
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/ursamajortech/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ursa-major-technologies-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://ursamajor.com/llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ursa-major-technologies-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ursa-major-technologies-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/ursa-major-technologies-conformance.yml
coverage:
  checked: '2026-08-05'
  detail: Ursa Major builds rocket engines and solid rocket motors as physical hardware for defense and space-launch customers, so there is nothing to expose as an API — ursamajor.com is a WordPress marketing site whose only machine-readable output is a Yoast-generated llms.txt with empty link targets, and no api., developer., docs. or portal. subdomain resolves at all.
  evidence:
  - status: 404
    url: https://ursamajor.com/openapi.json
  - status: 404
    url: https://ursamajor.com/.well-known/agent-card.json
  - status: 403
    url: https://ursamajor.com/wp-json/wp/v2/
  - status: 200
    url: https://ursamajor.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Ursa Major Technologies Inc. is an American aerospace and defense propulsion manufacturer founded in 2015 by Joe Laurienti, a former SpaceX and Blue Origin propulsion engineer, and headquartered at 19750 Co Rd 7 in Berthoud, Colorado, with additive manufacturing operations in Youngstown, Ohio. The company designs, builds and hot-fire tests liquid rocket engines, solid rocket motors and in-space propulsion systems for space launch, hypersonics and U.S. and allied defense customers. Its product line includes the 5,000 lbf Hadley oxygen-rich staged-combustion liquid engine — the first Ursa Major engine to reach flight qualification for hypersonic missions — and Draper, a storable, throttleable, restartable engine for tactical hypersonic strike, missile defense and rapid in-space maneuver, alongside a solid rocket motor line validated through static fire and a chemical propulsion capability for tactical satellite bus systems. Ursa Major was the first American company to successfully
  fire an oxygen-rich staged combustion engine; it states it has delivered more than 100 engines and logged over 100,000 seconds of hotfire testing, with engines and motors more than 80 percent 3D printed by mass. The company is AS9100D, ISO 9001 and CMMC Level 2 certified. Ursa Major is a hardware manufacturer selling to government and prime-contractor customers: it publishes no public developer API, SDK, CLI, developer portal or machine-readable API contract of any kind.'
image: https://ursamajor.com/wp-content/uploads/2025/08/logo.svg
layout: provider
modified: '2026-08-05'
name: Ursa Major Technologies
nav: Providers
network: true
overview: 'Ursa Major Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Defense, Propulsion, and Rocket Engines.


  Ursa Major Technologies'' developer surface includes engineering blog, YouTube channel, and 24 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 14.2
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Ursa Major Technologies Domain Security
  slug: ursa-major-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ursa-major-technologies
tags:
- Company
- Aerospace
- Defense
- Propulsion
- Rocket Engines
- Solid Rocket Motors
- Hypersonics
- Space
- Satellites
- Missile Defense
- Additive Manufacturing
- Manufacturing
- National Security
- Colorado
website: https://ursamajor.com/
---
