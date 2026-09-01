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
  url: https://ocsial.com/
- group: other
  title: ''
  type: ProductSite
  url: https://tuball.com/
- group: company
  title: ''
  type: About
  url: https://ocsial.com/about/
- group: company
  title: ''
  type: Blog
  url: https://ocsial.com/press-room/
- group: operate
  title: ''
  type: Contact
  url: https://ocsial.com/contacts/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ocsial.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ocsial.com/terms-of-use/
- group: commercial
  title: ''
  type: LegalNotice
  url: https://ocsial.com/legal-notice/
- group: company
  title: ''
  type: Careers
  url: https://ocsial.com/careers/
- group: company
  title: ''
  type: Partners
  url: https://ocsial.com/partners/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ocsial-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ocsial-llms.txt
coverage:
  checked: '2026-08-26'
  detail: OCSiAl manufactures and sells physical single wall carbon nanotube powder, concentrates and dispersions (TUBALL); its only non-marketing web system is docs.ocsial.com, which redirects to a Flexbby CRM/document-flow login rather than to any developer reference, and every OpenAPI, GraphQL, MCP, agent-card and /.well-known path probed on ocsial.com, tuball.com and docs.ocsial.com returned a hard 404.
  evidence:
  - status: 404
    url: https://ocsial.com/openapi.json
  - status: 404
    url: https://ocsial.com/.well-known/api-catalog
  - status: 404
    url: https://tuball.com/openapi.json
  - status: 200
    url: https://docs.ocsial.com/
  - status: 200
    url: https://api.github.com/orgs/OCSiAl/repos
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: OCSiAl is a Luxembourg-headquartered advanced-materials manufacturer and the world's largest industrial producer of single wall carbon nanotubes (graphene nanotubes), sold under the TUBALL brand. Founded in 2010, the company industrialised nanotube synthesis with its Graphetron reactors and now supplies TUBALL nanotubes, TUBALL MATRIX concentrates and TUBALL BATT dispersions as conductive and reinforcing additives to lithium-ion battery electrode, elastomer, thermoplastic, coating, composite and ESD-flooring producers. TUBALL was the first single wall carbon nanotube registered under EU REACH and covered by a US EPA consent order. OCSiAl operates production and dispersion facilities in Luxembourg and Serbia plus laboratories and TUBALL CENTERs in Europe and Asia, with commercial representation in more than 20 countries. It is a materials producer, not a software vendor, and publishes no public API, developer portal or SDK.
image: https://ocsial.com/static/assets/images/share/fb-share.jpg
layout: provider
modified: '2026-08-26'
name: OCSiAl
nav: Providers
network: true
overview: 'OCSiAl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advanced Materials, Nanotechnology, Carbon Nanotubes, and Chemicals.


  OCSiAl''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.7
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
    operational_transparency: 0.0
  previous_composite: 9.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Ocsial Domain Security
  slug: ocsial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ocsial
tags:
- Company
- Advanced Materials
- Nanotechnology
- Carbon Nanotubes
- Chemicals
- Manufacturing
- Batteries
- Coatings
- Luxembourg
website: https://ocsial.com/
---
