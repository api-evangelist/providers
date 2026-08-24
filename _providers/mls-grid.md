---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'MLS Grid''s RESO Web API — a replication-oriented OData v4 surface over listing data normalized to the RESO Data Dictionary and pooled from the participating MLSs. Documented entity sets are Property, '
  name: MLS Grid Web API v2
  slug: mls-grid-web-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mls-grid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mlsgrid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mlsgrid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mlsgrid.com/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mlsgrid.com/sitemap.md
- group: start
  title: ''
  type: Portal
  url: https://app.mlsgrid.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.mlsgrid.com/interest-form
- group: commercial
  title: ''
  type: LicenseAgreement
  url: https://www.mlsgrid.com/s/MLS-GRID-Data-License-Agreement.pdf
- group: operate
  title: ''
  type: FAQ
  url: https://www.mlsgrid.com/faq
- group: other
  title: ''
  type: Resources
  url: https://www.mlsgrid.com/resources
- group: other
  title: ''
  type: Overview
  url: https://www.mlsgrid.com/overview
- group: company
  title: ''
  type: About
  url: https://www.mlsgrid.com/whoisthemlsgrid
- group: other
  title: ''
  type: Customers
  url: https://www.mlsgrid.com/vendors
- group: company
  title: ''
  type: Blog
  url: https://www.mlsgrid.com/news
- group: operate
  title: ''
  type: Contact
  url: https://www.mlsgrid.com/contact-us
- group: operate
  title: ''
  type: Support
  url: mailto:support@mlsgrid.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mlsgrid
- group: auth
  title: ''
  type: Certification
  url: https://certification.reso.org/summary/T00000045
- group: auth
  title: ''
  type: Certification
  url: https://www.reso.org/certificates/
- group: docs
  title: ''
  type: Documentation
  url: https://www.reso.org/reso-web-api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.reso.org/data-dictionary/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.mlsgrid.com/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.mlsgrid.com/privacypolicy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.mlsgrid.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mls-grid-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://certification.reso.org/summary/T00000045
- group: design
  title: ''
  type: Conformance
  url: conformance/mls-grid-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mls-grid-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mls-grid-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mls-grid-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mls-grid-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mls-grid-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mls-grid-rate-limits.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mls-grid-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/mls-grid-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mls-grid-llms.txt
created: '2026-07-26'
description: 'The MLS Grid is a United States MLS data-distribution cooperative created by a network of Multiple Listing Services to give brokers, MLSs and technology vendors ONE normalized data feed, ONE license agreement and ONE compliance process instead of dozens of per-MLS RETS and Web API feeds. It ingests listing data from participating MLSs, converts it to the RESO Data Dictionary, and republishes it as a single RESO Web API (OData v4) replication surface at https://api.mlsgrid.com/v2/. It sits in the middle of the residential real estate value chain, between the MLSs that own the data and the IDX/VOW sites, portals and proptech applications that display it. Its API posture is the sector archetype: the documentation is genuinely public and complete, and MLS Grid is RESO-certified for Data Dictionary 2.0 and Web API Server Core 2.0.0 in the RESO certification directory (UOI T00000045) — but nothing is reachable without credentials. Every anonymous call to the service root, to /Property
  and to the OData $metadata document returns HTTP 401. Access requires the MLS Grid Master Data License Agreement plus approval by each originating MLS before a long-lived OAuth 2.0 bearer token is issued in the MLS Grid web application. Certified, documented, and closed.'
examples:
- key_count: 8
  name: Mls Grid Lookup Example
  slug: mls-grid-lookup-example
- key_count: 138
  name: Mls Grid Property Example
  slug: mls-grid-property-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mls-grid.png
layout: provider
modified: '2026-07-26'
name: MLS Grid
nav: Providers
network: true
overview: 'MLS Grid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, United States, MLS, RESO, and Property Listings.


  MLS Grid''s developer surface includes documentation, developer portal, signup flow, FAQ, engineering blog, support, changelog, and 30 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 6
  name: Mls Grid Rate Limits
  slug: mls-grid-rate-limits
score:
  band: thin
  composite: 32.4
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 33.3
    contract_quality: 1.4
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 50.0
  previous_composite: 32.4
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mls-grid/refs/heads/main/screenshots/mls-grid-2026-08-07T183841.png
security:
- kind: authentication
  name: Mls Grid Authentication
  slug: mls-grid-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mls Grid Domain Security
  slug: mls-grid-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: mls-grid
tags:
- Real-Estate
- United States
- MLS
- RESO
- Property Listings
- IDX
- PropTech
- OData
- Data Licensing
website: https://www.mlsgrid.com/
---
