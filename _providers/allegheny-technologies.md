---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.atimaterials.com
- group: company
  title: ''
  type: Blog
  url: https://www.atimaterials.com/newsroom/Pages/default.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atimaterials.com/Pages/atitermsandconditions.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atimaterials.com/Pages/atiprivacypolicy.aspx
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.atimaterials.com
- group: start
  title: ''
  type: CustomerPortal
  url: https://myati.atimaterials.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allegheny-technologies-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allegheny-technologies-domain-security.yml
coverage:
  checked: '2026-09-01'
  detail: ATI melts and forges titanium and superalloys for jet engines; its whole public web estate is a SharePoint 2013 marketing site whose only machine-shaped surfaces are alloy-grade pages, safety data sheets and raw-material surcharge schedules, and the one host actually named api — api.atimaterials.com — resolves but serves the stock Apache "It works!" page dated 2007 with Tomcat 404s on every path under it.
  evidence:
  - status: 404
    url: https://api.atimaterials.com/openapi.json
  - status: 200
    url: https://api.atimaterials.com/
  - status: 404
    url: https://www.atimaterials.com/llms.txt
  - status: 200
    url: https://www.atimaterials.com/.well-known/allegheny-technologies-negative-control-7f3ab91c.json
  - status: 200
    url: https://myati.atimaterials.com/
  - status: 500
    url: https://www.atimaterials.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'Allegheny Technologies Incorporated, which trades and brands itself as ATI Inc., is an American producer of specialty materials and components headquartered in Dallas, Texas and listed on the NYSE under the ticker ATI. ATI melts, forges, rolls, machines and additively manufactures titanium and titanium alloys, nickel-based alloys and superalloys, stainless and specialty steels, zirconium, hafnium, niobium and tungsten materials, plus forgings and castings. It serves aerospace and defense — over half of sales — along with oil and gas, chemical and hydrocarbon processing, power generation, medical and electronics markets, on roughly $4.6 billion in annual revenue. ATI is a materials manufacturer rather than a software company and publishes no public API: as of 2026-09-01 probing found no developer portal, no API reference, no OpenAPI, AsyncAPI, GraphQL or WSDL contract, no SDK on any public package registry and no GitHub organization. The only credentialed digital surfaces are
  My ATI, a customer and supplier extranet behind a logon form, and a third-party sourcing platform linked from the supplier self-service page; customer onboarding itself is documented as PDF forms emailed to a sales contact.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/allegheny-technologies.png
layout: provider
modified: '2026-09-01'
name: Allegheny Technologies Incorporated
nav: Providers
network: true
overview: 'Allegheny Technologies Incorporated is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Specialty Materials, Aerospace, Defense, Titanium, and Manufacturing.


  Allegheny Technologies Incorporated''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 5.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/allegheny-technologies/refs/heads/main/screenshots/allegheny-technologies-2026-07-25T195653.png
security:
- kind: domain-security
  name: Allegheny Technologies Domain Security
  slug: allegheny-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: allegheny-technologies
tags:
- Specialty Materials
- Aerospace
- Defense
- Titanium
- Manufacturing
- Metals
- Fortune 500
website: https://www.atimaterials.com
---
