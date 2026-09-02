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
  url: security/shine-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shinefusion.com/
- group: company
  title: ''
  type: Blog
  url: https://www.shinefusion.com/insights-updates
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shinefusion.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shinefusion.com/terms-and-conditions
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shine-technologies-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/shine-technologies-stock
coverage:
  checked: '2026-08-27'
  detail: SHINE Technologies manufactures fusion neutron systems and radiopharmaceuticals (lutetium-177, molybdenum-99) — its 273-URL sitemap has no developer, API, docs or integration section at all, and neither candidate GitHub org holds a single public repo, so there is no software product for an API to sit on.
  evidence:
  - status: 200
    url: https://www.shinefusion.com/sitemap.xml
  - status: 404
    url: https://www.shinefusion.com/openapi.json
  - status: 404
    url: https://www.shinefusion.com/llms.txt
  - status: 404
    url: https://www.shinefusion.com/developers
  - status: 404
    url: https://www.shinefusion.com/.well-known/agent-card.json
  - status: 404
    url: https://www.phoenixneutronimaging.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/users/shine-technologies/repos
  reason: not-a-software-company
  state: none
created: '2026-08-27'
description: 'SHINE Technologies is a privately held fusion technology company founded in 2010 and headquartered in Janesville, Wisconsin, that operates fusion neutron generators at industrial scale. High-current particle beams strike a tritium gas target to produce an intense neutron flux, which SHINE applies across four staged business phases: neutron imaging and radiation-effects testing (the Phoenix Imaging Center, the FLARE 14 MeV radiation-effects service, and a nuclear fuel scanner), medical isotope production (Cassiopeia, which makes the non-carrier-added lutetium-177 product Ilumira, and Chrysalis, a molybdenum-99 facility backed by a conditional $263M U.S. Department of Energy loan), used nuclear fuel recycling (the REDUCE process, with partners including Orano and Deep Isolation), and ultimately fusion energy. SHINE designs and manufactures its own particle accelerators, fusion targets and radiochemical processing systems, and merged with Phoenix LLC in 2022. It is a manufacturer
  of hardware and radiopharmaceuticals rather than a software company, and publishes no public API, SDK, developer portal or machine-readable contract of any kind.'
image: https://cdn.prod.website-files.com/63bc8628e53c0011f41ce702/6425da2ac24561fe6ff4a9e6_ST-Open-Graph-Image.jpg
layout: provider
modified: '2026-08-27'
name: SHINE Technologies
nav: Providers
network: true
overview: 'SHINE Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fusion, Nuclear, Medical Isotopes, and Radiopharmaceuticals.


  SHINE Technologies'' developer surface includes engineering blog and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Shine Technologies Domain Security
  slug: shine-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shine-technologies
tags:
- Company
- Fusion
- Nuclear
- Medical Isotopes
- Radiopharmaceuticals
- Neutron Imaging
- Energy
- Advanced Manufacturing
- Healthcare
- Non-Destructive Testing
website: https://www.shinefusion.com/
---
