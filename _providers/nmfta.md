---
agent_readiness:
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
api_count: 6
apis:
- description: Standards for Carrier APIs
  name: NMFTA Carrier API Standards API
  slug: nmfta-carrier-api-standards-api
- description: Endpoints for uploading, and managing supporting documents.
  name: NMFTA Document Management API
  slug: nmfta-document-management-api
- description: Pull shipment events
  name: NMFTA Events API
  slug: nmfta-events-api
- description: The In Transit Visibility API API from NMFTA — 0 operation(s) for in transit visibility api.
  name: NMFTA In Transit Visibility API
  slug: nmfta-in-transit-visibility-api-api
- description: Endpoints for creating, retrieving, and managing invoices.
  name: NMFTA Invoice Management API
  slug: nmfta-invoice-management-api
- description: Access freight charges information
  name: NMFTA Preliminary Freight Charges API
  slug: nmfta-preliminary-freight-charges-api
- description: Standards for the FTL Rate Quote API
  name: NMFTA Rate Quote API Standards API
  slug: nmfta-rate-quote-api-standards-api
- description: Manage webhook subscriptions
  name: NMFTA Subscriptions API
  slug: nmfta-subscriptions-api
- description: Webhook management and testing
  name: NMFTA Webhooks API
  slug: nmfta-webhooks-api
artifact_total: 25
collections:
- collection_type: open
  name: Electronic Bill Of Lading API
  slug: open-nmfta-dsdc-ftl-ebol
- collection_type: open
  name: In-Transit Visibility API
  slug: open-nmfta-dsdc-ftl-in-transit-visibility
- collection_type: open
  name: Invoice & Document API
  slug: open-nmfta-dsdc-ftl-invoice-and-documents
- collection_type: open
  name: Rate Quote API
  slug: open-nmfta-dsdc-ftl-rate-quote
- collection_type: open
  name: Electronic Bill Of Lading Service
  slug: open-nmfta-dsdc-ltl-ebol-2.1
- collection_type: open
  name: Preliminary Freight Charges (PFC) API
  slug: open-nmfta-dsdc-ltl-preliminary-freight-charges
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/nmfta-capability-edges.yml
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
overview: 'NMFTA publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Carrier API Standards API, Document Management API, Events API, and 6 more. Tagged areas include API Standards, DSDC, Digital FTL Council, Digital LTL Council, and Freight.


  NMFTA''s developer surface includes developer portal, product news, and 18 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 48.0
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 22.6
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
