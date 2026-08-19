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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 7
apis:
- description: Modeled logical service area for the people and organizations attached to a file - buyers, sellers, lenders, agents, and vendors - and their roles and mappings to partner-side identifiers. Delivered o
  name: ResWare Contacts API
  slug: resware-contacts-api
- description: Modeled logical service area for creating and managing title/escrow files (orders) - the core transaction records that carry file number, property, parties, and status through the closing lifecycle. D
  name: ResWare Files & Orders API
  slug: resware-files-orders-api
- description: Modeled logical service area for retrieving, uploading, and generating documents attached to a file - closing packages, executed documents, and auto-generated forms. In partner integrations this is th
  name: ResWare Documents API
  slug: resware-documents-api
- description: Modeled logical service area for ResWare's action-based tasks and multi-directional workflow steps that drive a file through its lifecycle - creating, completing, and querying tasks. Delivered over Re
  name: ResWare Tasks API
  slug: resware-tasks-api
- description: Modeled logical service area for escrow accounting - trust ledgers, receipts and disbursements, reconciliation, and remittance data tied to a file. Delivered over ResWare's gated SOAP/XML (WCF) partne
  name: ResWare Accounting API
  slug: resware-accounting-api
- description: Modeled logical service area for reading and writing notes and activity entries on a file, used by partners to post status updates and messages back into ResWare. Delivered over ResWare's gated SOAP/X
  name: ResWare Notes API
  slug: resware-notes-api
- description: Modeled logical service area for ResWare's partner-integration framework - the proxy/partner web-service messages that exchange orders, documents, and status with external vendors (signing/RON, record
  name: ResWare Partners API
  slug: resware-partners-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/resware-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qualia-labs
- group: company
  title: ''
  type: Website
  url: https://resware.com
- group: company
  title: ''
  type: Website
  url: https://www.qualia.com/resware/
- group: docs
  title: ''
  type: Documentation
  url: https://www.qualia.com/resware-integrations/
- group: start
  title: ''
  type: SupportPortal
  url: https://knowledge.resware.com
- group: operate
  title: ''
  type: Contact
  url: mailto:sales@adeptivesw.com
created: '2026-07-04'
description: ResWare is customizable title and escrow production software for real estate closings, originally built by Adeptive Software Corporation and acquired by Qualia Labs in December 2020 (now shipping as ResWare 10 within the Qualia ecosystem). It is an on-premises, workflow-driven platform covering title and escrow production, document management and auto-generation, secure communications, and escrow accounting. ResWare exposes an integration API to partners and customers that is historically a SOAP/XML web-service API (built on Windows Communication Foundation / WCF, Microsoft binary protocol by default with Basic Authentication available on request), complemented by newer REST APIs for document handling. There is no public, self-serve developer portal - API access is gated behind a partner/integration program and an "API assistance" package (developer support hours, REST/WCF code samples, and documentation), with pricing on request via sales@adeptivesw.com. The logical service
  areas below are modeled from partner-integration behavior; ResWare publishes no public API reference or OpenAPI, so no REST surface is fabricated here.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/resware.png
layout: provider
modified: '2026-07-25'
name: ResWare
nav: Providers
network: true
overview: 'ResWare publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Title, Escrow, Real Estate, Closing, and Title Production.


  ResWare''s developer surface includes documentation and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 8.4
  delta: 0.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Resware Domain Security
  slug: resware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: resware
tags:
- Title
- Escrow
- Real Estate
- Closing
- Title Production
- SOAP
- XML
- WCF
- Partner API
- Gated
- Qualia
website: https://resware.com
---
