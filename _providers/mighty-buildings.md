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
  url: security/mighty-buildings-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mightybuildings.com
- group: company
  title: ''
  type: About
  url: https://www.mightybuildings.com/about-us
- group: other
  title: ''
  type: Technology
  url: https://www.mightybuildings.com/mighty-kit-system
- group: other
  title: ''
  type: Resources
  url: https://www.mightybuildings.com/resources
- group: company
  title: ''
  type: Press
  url: https://www.mightybuildings.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.mightybuildings.com/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mightybuildings.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MightyBuildings
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mightybuildings
coverage:
  checked: '2026-08-04'
  detail: Mighty Buildings sells physical 3D-printed wall panels and factory-built housing, not software - its whole site is a 17-page Webflow marketing brochure (about-us, projects, mighty-kit-system, press, careers) with no developers, docs, or API section anywhere in it, and no api./docs./developer. subdomain resolves in DNS.
  evidence:
  - status: 200
    url: https://www.mightybuildings.com/
  - status: 404
    url: https://www.mightybuildings.com/openapi.json
  - status: 404
    url: https://www.mightybuildings.com/llms.txt
  - status: 404
    url: https://www.mightybuildings.com/.well-known/api-catalog
  - status: 404
    url: https://www.mightybuildings.com/.well-known/agent-card.json
  - status: 404
    url: https://www.lumuscorp.com/
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: Mighty Buildings is a construction-technology and advanced-manufacturing company that industrializes homebuilding using large-format 3D printing, proprietary polymer-composite materials and robotic automation. Founded in 2019 and originally based in Oakland, California, it raised more than $150 million from investors including Khosla Ventures, Bold Capital and Aramco's Wa'ed Ventures, and was the first company certified under the UL 3401 standard for evaluating building structures and assemblies, as well as being certified under California's Factory Built Housing program. Its current product is the Mighty Kit System / Mighty Wall System - factory-made complete wall panels that arrive on site with integrated structure, insulation, waterproofing and exterior finish, so builders assemble a building envelope with conventional methods and fewer on-site steps. After a January 2025 restructuring and sale process, the full suite of Mighty Buildings technologies was acquired by LUMUS
  Inc., and Mighty Buildings now operates as a LUMUS brand headquartered in Beaverton, Oregon. The company sells physical building systems to developers and builders; it operates no public API, developer portal, SDK, or machine-readable specification of any kind.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mighty-buildings.png
layout: provider
modified: '2026-08-04'
name: Mighty Buildings
nav: Providers
network: true
overview: Mighty Buildings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Construction Technology, Contech, and 3D Printing.
random_paper: 5
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mighty-buildings/refs/heads/main/screenshots/mighty-buildings-2026-08-07T172857.png
security:
- kind: domain-security
  name: Mighty Buildings Domain Security
  slug: mighty-buildings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mighty-buildings
tags:
- Company
- Construction
- Construction Technology
- Contech
- 3D Printing
- Additive Manufacturing
- Advanced Manufacturing
- Prefabrication
- Modular Housing
- Housing
- Real-Estate
- Building Materials
- Robotics
- Sustainability
- Acquired
website: https://www.mightybuildings.com
---
