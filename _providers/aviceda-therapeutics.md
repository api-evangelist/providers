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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aviceda-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avicedarx.com/
- group: company
  title: ''
  type: About
  url: https://www.avicedarx.com/about-us
- group: operate
  title: ''
  type: Contact
  url: https://www.avicedarx.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.avicedarx.com/careers
- group: company
  title: ''
  type: News
  url: https://www.avicedarx.com/company-updates
- group: company
  title: ''
  type: Investors
  url: https://www.avicedarx.com/investors
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aviceda-therapeutics/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/avicedarx
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/aviceda-therapeutics_stock/
coverage:
  checked: '2026-08-06'
  detail: Aviceda is a clinical-stage biotech developing the AVD-104 nanoparticle for geographic atrophy; its entire web presence is a ten-page corporate brochure at avicedarx.com (sitemap.xml lists only home, technology-platform, lead-asset, pipeline, publications, company-updates, about-us, investors, careers, contact) with no developer section, and api./developer./docs.avicedarx.com do not resolve in DNS.
  evidence:
  - status: 200
    url: https://www.avicedarx.com/sitemap.xml
  - status: 404
    url: https://www.avicedarx.com/openapi.json
  - status: 404
    url: https://www.avicedarx.com/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Aviceda Therapeutics is a private, late-stage clinical biotechnology company based in Cambridge, Massachusetts that describes itself as the world leader in glyco-immune checkpoint therapeutics. It develops immune-mediated therapies built on a glyco-mimetic nanoparticle platform that targets the interaction between sialic acids on cell surfaces and Siglec immune receptors in order to modulate aberrant inflammation. Its lead asset, AVD-104, is an intravitreally administered sialic-acid-coated nanoparticle being evaluated in the Phase 2/3 SIGLEC trial for geographic atrophy secondary to age-related macular degeneration. Aviceda is a therapeutics developer, not a software vendor: it publishes no developer program, no public API, and no machine-readable API artifacts.'
image: https://www.avicedarx.com/media/logo/aviceda.svg
layout: provider
modified: '2026-08-06'
name: Aviceda Therapeutics
nav: Providers
network: true
overview: 'Aviceda Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Therapeutics, and Ophthalmology.


  Aviceda Therapeutics'' developer surface includes product news and 9 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 3.3
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aviceda-therapeutics/refs/heads/main/screenshots/aviceda-therapeutics-2026-08-07T162022.png
security:
- kind: domain-security
  name: Aviceda Therapeutics Domain Security
  slug: aviceda-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: aviceda-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Therapeutics
- Ophthalmology
- Clinical Trials
- Life Sciences
website: https://www.avicedarx.com/
---
