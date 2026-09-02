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
- group: company
  title: ''
  type: Website
  url: https://www.manusbio.com/
- group: company
  title: ''
  type: About
  url: https://www.manusbio.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.manusbio.com/insights-and-news
- group: operate
  title: ''
  type: Contact
  url: https://www.manusbio.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.manusbio.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.manusbio.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.manusbio.com/cookie-and-privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ManusBio
- group: auth
  title: ''
  type: DomainSecurity
  url: security/manus-bio-domain-security.yml
coverage:
  checked: '2026-08-04'
  detail: Manus sells fermentation-produced ingredients and contract biomanufacturing services, not software; its Webflow marketing site returns 404 for every contract-discovery path, no api./docs./developer. subdomain resolves, and the github.com/ManusBio organization has zero public repositories.
  evidence:
  - status: 404
    url: https://www.manusbio.com/openapi.json
  - status: 404
    url: https://www.manusbio.com/llms.txt
  - status: 404
    url: https://www.manusbio.com/.well-known/security.txt
  - status: 404
    url: https://www.manusbio.com/.well-known/agent-card.json
  - status: 404
    url: https://www.manusbio.com/.well-known/agent.json
  - status: 200
    url: https://www.manusbio.com/sitemap.xml
  - status: 200
    url: https://www.inscripta.com/
  - status: 200
    url: https://api.github.com/orgs/manusbio
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: Manus Bio Inc. (trading as "Manus", the BioAlternatives Company) is a Cambridge, Massachusetts industrial biotechnology company founded in 2011 out of MIT by Dr. Aji Parayil and Dr. Greg Stephanopoulos. Manus engineers microbial cell factories and precision-fermentation processes so that complex molecules normally obtained through petrochemical synthesis, agricultural extraction, or animal husbandry can be produced by fermentation instead - what the company calls bioalternatives. Its commercialized products include the first U.S. commercial-scale monk fruit sweetener (produced at its Augusta, Georgia BioFacility), the Yume M stevia Reb M sweetener co-developed with Tate & Lyle, citrus-derived aroma ingredients (Nootkatone 70, Valencene 80, BioNootkatone) for Givaudan, and an artemisinin antimalarial program funded by HHS/ASPR. It sells scale-up services through its BioAccelerator and BioManufacturing programs (protein engineering, strain development, bioprocess development from
  250 ml to 3,000 L, pilot-scale and biomanufacturing). In April 2025 Manus merged with genome-engineering company Inscripta, adding whole-genome editing technology and the MAD7 CRISPR nuclease licensing program; inscripta.com is now a redirect notice. Manus is a manufacturer of physical ingredients and a contract development and manufacturing organization - it sells molecules and services, not software. It publishes no public API, developer portal, SDK, webhook surface, or machine-readable specification of any kind, and its computational and AI-driven enzyme-engineering tools are internal capabilities that support its services rather than a customer-facing platform.
image: https://cdn.prod.website-files.com/6536fe08e98c41581598326f/6682ee89aa355ed6e2dca105_Manus%20Social%20Image.png
layout: provider
modified: '2026-08-04'
name: Manus Bio
nav: Providers
network: true
overview: 'Manus Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Synthetic Biology, Biomanufacturing, and Industrial Biotechnology.


  Manus Bio''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 3
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/manus-bio/refs/heads/main/screenshots/manus-bio-2026-08-07T172005.png
security:
- kind: domain-security
  name: Manus Bio Domain Security
  slug: manus-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: manus-bio
tags:
- Company
- Biotechnology
- Synthetic Biology
- Biomanufacturing
- Industrial Biotechnology
- Precision Fermentation
- Ingredients
- Food and Beverage
- Sustainability
- Life Sciences
website: https://www.manusbio.com/
---
