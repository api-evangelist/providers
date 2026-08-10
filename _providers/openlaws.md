---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Openlaws Agentic Access
  operation_count: 28
  slug: openlaws-agentic-access
  summary_line: 28 operations
api_count: 5
apis:
- description: Courts issue Opinions and belong to a Jurisdiction.
  name: OpenLaws Courts API
  slug: openlaws-courts-api
- description: All data (statutes, regulations, caselaw opinions) in OpenLaws are organized into jurisdictions. This allows you to scope searches and lookups to a specific state or federal jurisdiction (or both).
  name: OpenLaws Jurisdictions API
  slug: openlaws-jurisdictions-api
- description: Divisions represent the hierarchical documents that make up statutes, regulations, and constitutions. Each document has a 'path' which uniquely identifies the document and where it resides in the hier
  name: OpenLaws Law Divisions API
  slug: openlaws-law-divisions-api
- description: 'Laws represent a specific law type in a Jurisdiction. For example, Code of Federal Regulations belongs to the FED Jurisdiction and is represented by the law_key `FED-CFR`. Florida Statutes belongs to '
  name: OpenLaws Laws API
  slug: openlaws-laws-api
- description: Opinions represent published and unpublished case law opinions. Opinions belong to a Court and Jurisdiction.
  name: OpenLaws Opinions API
  slug: openlaws-opinions-api
artifact_total: 12
collections:
- collection_type: open
  name: OpenLaws API Documentation
  slug: open-openlaws
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openlaws-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openlaws-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openlaws-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://openlaws.us/
- group: docs
  title: ''
  type: Documentation
  url: https://openlaws.apidocumentation.com
- group: start
  title: ''
  type: GettingStarted
  url: https://openlaws.apidocumentation.com/guide/openlaws-legal-data-api
- group: start
  title: ''
  type: Signup
  url: https://1be187uhimk.typeform.com/to/PwYQaCu4
- group: operate
  title: ''
  type: ChangeLog
  url: https://openlaws.apidocumentation.com/guide/release-notes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openlaws.us/terms
- group: operate
  title: ''
  type: ContactEmail
  url: mailto:team@openlaws.us
- group: commercial
  title: ''
  type: Plans
  url: plans/openlaws-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openlaws-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openlaws-finops.yml
created: '2025-03-01'
description: OpenLaws is a Public Benefit Corporation that provides programmatic access to U.S. law text — federal and state statutes, regulations, constitutions, and case law — through a unified Legal Data API. The platform exposes keyword and citation search, hierarchical division retrieval, historical versions with redline comparisons, citation parsing and validation, and deep links to authoritative government sources. Coverage spans 53 U.S. jurisdictions (50 states + D.C. + Puerto Rico + Federal) with more than 4.3 million law sections under a single data model, targeted at RegTech, LegalTech, GRC / IRM, generative AI / RAG, and legal research workloads.
finops:
- name: Openlaws Finops
  service_category: API
  slug: openlaws-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openlaws.png
layout: provider
modified: '2026-05-21'
name: OpenLaws
nav: Providers
network: true
overview: 'OpenLaws publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Courts API, Jurisdictions API, Law Divisions API, and 2 more. Tagged areas include Legal, Law, Statutes, Regulations, and Constitutions.


  OpenLaws'' developer surface includes authentication, documentation, getting-started guide, signup flow, changelog, and 8 more developer resources.'
plans:
- name: Openlaws Plans Pricing
  plan_count: 3
  slug: openlaws-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 5
  name: Openlaws Rate Limits
  slug: openlaws-rate-limits
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 62.3
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openlaws/refs/heads/main/screenshots/openlaws-2026-06-20T191009.png
security:
- kind: authentication
  name: Openlaws Authentication
  slug: openlaws-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openlaws Domain Security
  slug: openlaws-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openlaws
tags:
- Legal
- Law
- Statutes
- Regulations
- Constitutions
- Case Law
- Citations
- Search
- RAG
- LegalTech
- RegTech
- Compliance
- GRC
- Government Data
website: https://openlaws.us/
---
