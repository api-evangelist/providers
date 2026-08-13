---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-12'
api_count: 6
apis:
- description: The Digital LTL Council's electronic bill of lading standard, version 2.1.0 — the council's first and most adopted contract. This is the standard's own specification, not any carrier's implementation.
  name: DSDC LTL eBOL API
  slug: nmfta-dsdc-ltl-ebol-api
- description: Gives shippers, carriers and 3PLs visibility into freight charges as they evolve — reclassifications, reweighs and accessorial changes mid-shipment rather than weeks later on the invoice. The only LTL
  name: DSDC LTL Preliminary Freight Charges API
  slug: nmfta-dsdc-ltl-preliminary-freight-charges-api
- description: The Digital FTL Council's electronic bill of lading standard. Published in the public repository as 1.0.0-public-preview while the DSDC website advertises 1.1.0 as released.
  name: DSDC FTL eBOL API
  slug: nmfta-dsdc-ftl-ebol-api
- description: Full truckload rate and quote exchange between shippers, carriers and intermediaries. Published as 1.0.0-public-preview.
  name: DSDC FTL Rate/Quote API
  slug: nmfta-dsdc-ftl-rate-quote-api
- description: Invoicing and supporting document exchange for full truckload movements. Published as 1.0.0-public-preview.
  name: DSDC FTL Invoice and Documents API
  slug: nmfta-dsdc-ftl-invoice-and-documents-api
- description: Shipment status and location events while a full truckload movement is under way. Published as 1.0.0-public-preview; the LTL council's equivalent is still in development.
  name: DSDC FTL In-Transit Visibility API
  slug: nmfta-dsdc-ftl-in-transit-visibility-api
artifact_total: 16
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/dsdcapis/less-than-truckload/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/dsdcapis/less-than-truckload/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/dsdcapis/less-than-truckload/blob/main/CONTRIBUTING.md
- group: start
  title: ''
  type: Portal
  url: https://nmfta.org/
- group: docs
  title: ''
  type: Specification
  url: https://dsdc.nmfta.org/apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dsdcapis
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/dsdcapis
- group: other
  title: ''
  type: WorkingGroups
  url: https://dsdc.nmfta.org/digital-ltl-council
- group: other
  title: ''
  type: Contributing
  url: https://dsdc.nmfta.org/contributor-agreement-form
- group: company
  title: ''
  type: News
  url: https://dsdc.nmfta.org/news
- group: other
  title: ''
  type: Events
  url: https://nmfta.org/nmfta-event/2026-dsdc-membership-meeting/
- group: operate
  title: ''
  type: Contact
  url: mailto:dsdc@nmfta.org
- group: other
  title: ''
  type: Governance
  url: governance/nmfta-governance.yml
- group: other
  title: ''
  type: Taxonomy
  url: taxonomy/nmfta-taxonomy.yml
- group: other
  title: ''
  type: Companies
  url: companies/nmfta-companies.yml
- group: other
  title: ''
  type: Adoption
  url: adoption/nmfta-adoption.yml
- group: other
  title: ''
  type: Leads
  url: leads/nmfta-new-company-leads.yml
- group: other
  title: ''
  type: Repositories
  url: repositories/nmfta-repositories.yml
- group: other
  title: ''
  type: Contributors
  url: contributors/nmfta-contributors.yml
created: '2026-08-03'
description: 'The National Motor Freight Traffic Association (NMFTA) is the nonprofit membership body that has set the standards for North American freight since 1956, and through its Digital Standards Development Council (DSDC) it publishes that industry agreement as open OpenAPI contracts. Two councils sit under the DSDC — the Digital LTL Council, founded November 2020, and the Digital FTL Council, which absorbed the Scheduling Standards Consortium — and between them they turn the paper artifacts of trucking into machine-readable APIs: the electronic bill of lading, the rate quote, the invoice and supporting documents, in-transit visibility, appointment scheduling, book and tender, and preliminary freight charges. For most of NMFTA''s history its standards were classification and coding — the NMFC freight classification, ClassIT+, SCAC carrier codes, SPLC location codes — and the DSDC is the same institution doing the same job for the API layer. It is one of the clearest examples of an
  old, mandate-free trade association choosing specifications-as-code over another PDF behind a membership wall, and the gap between what its website advertises as released and what its public repositories actually contain is the most interesting thing about it.'
features:
- 'Host: NMFTA, founded 1956; DSDC is a division, not a separate entity'
- 'Councils: Digital LTL (November 2020) and Digital FTL (absorbed the Scheduling Standards Consortium)'
- 'APIs advertised: 10 across the two councils'
- 'Specifications in public repositories: 5 of 10'
- 'GitHub repositories: 6, two of which are named test repositories'
- 'Contributors: 5 humans, 123 total contributions'
- 'Participating companies published as logos: 32'
- 'Participants already in the API Evangelist network: 15'
- 'Regulatory mandate: none — adoption earned on cost and friction'
- 'Server declarations across all six harvested specifications: zero'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nmfta.png
layout: provider
modified: '2026-08-03'
name: NMFTA
nav: Providers
network: true
overview: 'NMFTA publishes 6 APIs on the [APIs.io](https://apis.io/) network, including DSDC LTL eBOL API, DSDC LTL Preliminary Freight Charges API, DSDC FTL eBOL API, and 3 more. Tagged areas include API Standards, DSDC, Digital FTL Council, Digital LTL Council, and Freight.


  NMFTA''s developer surface includes developer portal, product news, and 17 more developer resources.'
random_paper: 54
score:
  band: emerging
  composite: 20.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 47.8
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 20.9
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nmfta/refs/heads/main/screenshots/nmfta-2026-08-07T185355.png
slug: nmfta
tags:
- API Standards
- DSDC
- Digital FTL Council
- Digital LTL Council
- Freight
- Full Truckload
- LTL
- Less-Than-Truckload
- Logistics
- NMFTA
- OpenAPI
- Standards
- Standards Body
- Supply Chain
- Transportation
- Trucking
website: https://nmfta.org/
---
