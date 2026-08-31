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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bioconsortia-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bioconsortia-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.bioconsortia.com/
- group: company
  title: ''
  type: About
  url: https://www.bioconsortia.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.bioconsortia.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.bioconsortia.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.bioconsortia.com/resources/faq
- group: company
  title: ''
  type: Careers
  url: https://www.bioconsortia.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bioconsortia-inc-
coverage:
  checked: '2026-08-07'
  detail: BioConsortia sells microbial seed treatments and biofertilizers as physical crop inputs; its RhizoViz and GenePro "platforms" are internal laboratory R&D instruments, and the entire 68-URL sitemap covers products, pipeline, news and careers with no developer, docs or API page.
  evidence:
  - status: 200
    url: https://www.bioconsortia.com/sitemap.xml
  - status: 404
    url: https://www.bioconsortia.com/openapi.json
  - status: 404
    url: https://www.bioconsortia.com/.well-known/agent-card.json
  - status: 404
    url: https://www.bioconsortia.com/llms.txt
  - status: 0
    url: https://api.bioconsortia.com/
  reason: not-a-software-company
  state: none
created: '2026-08-07'
description: BioConsortia, Inc. is an agricultural biotechnology company headquartered in Davis, California, with additional laboratories in New Zealand, that discovers and commercializes microbial biologicals for row crops and specialty agriculture. Its patented Advanced Microbial Selection (AMS) process, RhizoViz microbe-visualization tool and GenePro genomics and gene-engineering platform are used to screen a collection of more than 60,000 characterized microorganisms — including roughly 9,000 endophytes — into nitrogen-fixation biofertilizers, biocontrol products (bionematicides and biofungicides) and biostimulants, largely delivered as seed treatments. The company sells physical crop inputs through partners such as Mosaic, Nichino America and Envu; its platform technologies are internal R&D instruments rather than commercial software, and BioConsortia publishes no public API, developer portal, SDK or machine-readable specification.
image: https://www.bioconsortia.com/hubfs/Bio%20Consortia/Logos/bioconsortia%20logo%202026%20full%20color%20lrg%20(R)%20MASTER.svg
layout: provider
modified: '2026-08-07'
name: BioConsortia
nav: Providers
network: true
overview: 'BioConsortia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Biotechnology, and Agricultural Biologicals.


  BioConsortia''s developer surface includes engineering blog, support, FAQ, and 6 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bioconsortia/refs/heads/main/screenshots/bioconsortia-2026-08-07T162449.png
security:
- kind: domain-security
  name: Bioconsortia Domain Security
  slug: bioconsortia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bioconsortia
tags:
- Company
- Agriculture
- AgTech
- Biotechnology
- Agricultural Biologicals
- Microbials
- Crop Science
- Biofertilizers
- Nitrogen Fixation
- Genomics
website: https://www.bioconsortia.com/
---
