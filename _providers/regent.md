---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/regent-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.regentcraft.com
- group: operate
  title: ''
  type: Support
  url: https://www.regentcraft.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.regentcraft.com/newsroom
- group: operate
  title: ''
  type: FAQ
  url: https://www.regentcraft.com/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iubenda.com/privacy-policy/31330003
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/regent-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/regentcraft/
coverage:
  checked: '2026-08-26'
  detail: REGENT Craft manufactures physical Seaglider vessels, not software — its Webflow site has no developer, docs or API section anywhere in its 320-URL sitemap, and every OpenAPI, GraphQL and /.well-known/ probe on both www.regentcraft.com and defense.regentcraft.com 404s; the one machine-readable thing it publishes is a hand-authored llms.txt at the site root describing the company and its vessels.
  evidence:
  - status: 200
    url: https://www.regentcraft.com/llms.txt
  - status: 404
    url: https://www.regentcraft.com/openapi.json
  - status: 404
    url: https://www.regentcraft.com/.well-known/api-catalog
  - status: 404
    url: https://defense.regentcraft.com/openapi.json
  - status: 200
    url: https://www.regentcraft.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'REGENT Craft Inc. is a Rhode Island maritime mobility manufacturer building the Seaglider, an all-electric wing-in-ground-effect (WIG) vessel that floats on its hull, hydrofoils, and then flies within a wingspan of the water''s surface at up to 180 mph. The company builds the 12-passenger Viceroy, the larger Monarch, and the uncrewed Squire defense drone, and operates a defense product line for ISR, contested logistics and MEDEVAC missions. REGENT is a vehicle manufacturer rather than a software company: it publishes no developer program, no public API and no machine-readable API contract. It does serve a real, hand-authored llms.txt at its website root, which is the only machine-readable artifact on its public surface.'
image: https://cdn.prod.website-files.com/602ad05d28b6c66eb7baa871/69e7a8ff625bdd33565c703d_OG-min.jpg
layout: provider
modified: '2026-08-26'
name: REGENT Craft
nav: Providers
network: true
overview: 'REGENT Craft is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Transportation, Maritime, Aviation, and Electric Vehicles.


  REGENT Craft''s developer surface includes support, engineering blog, FAQ, and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/regent/refs/heads/main/screenshots/regent-2026-09-02T153241.png
security:
- kind: domain-security
  name: Regent Domain Security
  slug: regent-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: regent
tags:
- Company
- Transportation
- Maritime
- Aviation
- Electric Vehicles
- Defense
- Manufacturing
- Mobility
website: https://www.regentcraft.com
---
