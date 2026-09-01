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
modified: '2026-07-25'
name: Florence Healthcare
nav: Providers
network: true
overview: 'Florence Healthcare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Clinical Trials, eRegulatory, eISF, eBinders, and eTMF.


  Florence Healthcare''s developer surface includes documentation, signup flow, pricing, and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/florence-ebinder/refs/heads/main/screenshots/florence-ebinder-2026-07-25T214822.png
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
- Document-Management
- Partner API
website: https://www.florencehc.com/
---
