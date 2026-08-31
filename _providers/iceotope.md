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
  url: security/iceotope-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iceotope.com/
- group: company
  title: ''
  type: Blog
  url: https://www.iceotope.com/company/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Iceotope
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iceotope.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iceotope.com/terms-and-conditions
- group: operate
  title: ''
  type: Contact
  url: https://www.iceotope.com/contact-us
- group: operate
  title: ''
  type: FAQ
  url: https://www.iceotope.com/technology/faq
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iceotope-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Iceotope sells precision liquid-cooling hardware (KUL BOX and KUL AI chassis) and licenses thermal IP through OEM/ODM partners, so there is nothing to expose as an API - its Webflow site has no developer, docs or api path in its 108-URL sitemap, api./developer./docs. iceotope.com do not resolve, and its GitHub org holds only two 2019 forks of OpenBMC and a Xilinx firmware builder.
  evidence:
  - status: 404
    url: https://www.iceotope.com/developers
  - status: 404
    url: https://www.iceotope.com/openapi.json
  - status: 404
    url: https://www.iceotope.com/.well-known/api-catalog
  - status: 200
    url: https://api.github.com/orgs/Iceotope/repos
  - status: 200
    url: https://www.iceotope.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'Iceotope Technologies is a Sheffield, UK precision liquid cooling company founded in 2005 as a research-driven "green computing" venture, now supplying chassis-level liquid cooling for AI, HPC, data center and edge infrastructure. Its "direct to everything" single-phase immersion approach removes heat from every component rather than the processor alone, and ships as two product lines: KUL BOX for near-edge AI and HPC deployments, and KUL AI liquid-cooled server chassis for high-density rack environments. The company licenses its thermal IP (228 patents granted, allowed and pending) and works through OEM/ODM partnerships with vendors including HPE, Intel and nVent. Iceotope is a hardware and thermal-engineering business: it publishes no developer program, no public API, and no machine-readable API contract on any host it controls.'
image: https://cdn.prod.website-files.com/697467ed5b822a913931bc4b/699ab949d1369217910f1b93_Iceotope%20Open%20Graph%20Image.jpg
layout: provider
modified: '2026-08-22'
name: Iceotope
nav: Providers
network: true
overview: 'Iceotope is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Centers, Liquid Cooling, Thermal Management, and Infrastructure.


  Iceotope''s developer surface includes engineering blog, FAQ, and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.0
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Iceotope Domain Security
  slug: iceotope-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iceotope
tags:
- Company
- Data Centers
- Liquid Cooling
- Thermal Management
- Infrastructure
- Edge Computing
- High Performance Computing
- Sustainability
- Hardware
website: https://www.iceotope.com/
---
