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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 5
apis:
- description: Modeled logical API for the eBinders investigator site file (eISF) and participant binder structure - creating and organizing binders, folders, and placeholders, and inbound/outbound exchange of regul
  name: Florence Documents and Binders API
  slug: florence-documents-binders-api
- description: Modeled logical API for compliant electronic signature and audit-trail workflows on regulatory documents (21 CFR Part 11 / GxP), including signature requests, signing, and document status/compliance r
  name: Florence Signatures and Compliance API
  slug: florence-signatures-api
- description: Modeled logical API over the SiteLink network for managing studies, investigator sites, and cross-site document status reporting for regulatory and source documents involved in clinical research. Endp
  name: Florence Studies and Sites API
  slug: florence-studies-sites-api
- description: Modeled logical API for connected management of users, roles, and permissions across the eBinders/SiteLink platform - the "connected management of roles and permissions" Florence cites for its open AP
  name: Florence Users and Permissions API
  slug: florence-users-permissions-api
- description: Modeled logical API for operational tasks and workflow automation (site startup, monitoring, source data verification) that SiteLink orchestrates across sites, sponsors, and CROs. Endpoints are modele
  name: Florence Tasks and Workflows API
  slug: florence-tasks-workflows-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/florence-ebinder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.florencehc.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/florence-healthcare
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FlorenceHC
- group: docs
  title: ''
  type: Documentation
  url: https://www.florencehc.com/products/sitelink/
- group: start
  title: ''
  type: SignUp
  url: https://www.florencehc.com/sign-in-4/
- group: operate
  title: ''
  type: Contact
  url: https://www.florencehc.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.florencehc.com/products/ebinders/
created: '2026-07-05'
description: Florence Healthcare provides eRegulatory and clinical-trial site enablement software for research sites, sponsors, and CROs. Its eBinders product is an electronic investigator site file (eISF) and participant binder platform that replaces paper regulatory binders with structured, compliant, 21 CFR Part 11 workflows; eTMF manages the sponsor-side trial master file; and SiteLink connects a network of 10,000+ investigator sites across 44+ countries to sponsors and CROs for remote site access, monitoring, document exchange, and source data verification. Florence describes an "open API" for eBinders, eTMF, and SiteLink that supports connected management of roles and permissions, inbound and outbound document exchange, and document status reporting across regulatory and source documents. Access to the API is partner- and customer-gated - it is granted through Florence's integration and partnership programs rather than a self-service public developer portal, and no public API reference,
  OpenAPI description, or base URL is published as of this writing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/florence-ebinder.png
layout: provider
modified: '2026-07-05'
name: Florence Healthcare
nav: Providers
network: true
overview: 'Florence Healthcare publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Clinical Trials, eRegulatory, eISF, eBinders, and eTMF.


  Florence Healthcare''s developer surface includes documentation, signup flow, pricing, and 5 more developer resources.'
random_paper: 39
score:
  band: emerging
  composite: 15.5
  delta: -0.4
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.9
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Florence Ebinder Domain Security
  slug: florence-ebinder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: florence-ebinder
tags:
- Clinical Trials
- eRegulatory
- eISF
- eBinders
- eTMF
- Clinical Research
- Healthcare
- Life Sciences
- Document Management
- Partner API
website: https://www.florencehc.com/
---
