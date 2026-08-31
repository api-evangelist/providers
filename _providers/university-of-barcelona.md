---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: 'Public DSpace 7.6.6 REST API for the Dipòsit Digital de la Universitat de Barcelona, the institutional repository of teaching, research and institutional output. The API root advertises HAL links for '
  name: Dipòsit Digital REST API (DSpace 7)
  slug: diposit-rest
- description: OAI-PMH metadata-harvesting endpoint for the Dipòsit Digital de la Universitat de Barcelona. The Identify verb returns the repository name and OAI-PMH 2.0 metadata. Used for harvesting into aggregator
  name: Dipòsit Digital OAI-PMH
  slug: diposit-oai
- description: Universitat de Barcelona centralized single sign-on (Identificació UB) providing federated authentication for university web applications. Supports SAML 2.0 and CAS protocols. The SAML2 SSO service en
  name: UB Centralized SSO (SAML 2.0 / CAS)
  slug: sso-saml
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-barcelona-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ub.edu/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-barcelona/
- group: auth
  title: ''
  type: Authentication
  url: https://sso.ub.edu/SAML2/SSOService.php
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-barcelona-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-barcelona-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-barcelona-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-barcelona-context.jsonld
created: '2026-06-03'
description: 'The University of Barcelona (Universitat de Barcelona, UB) is a public research university founded in 1450 and based in Barcelona, Catalonia, Spain. It is ranked #165 in the QS World University Rankings 2025. Its publicly documented developer/API footprint is limited and primarily centered on library and scholarly infrastructure: the Dipòsit Digital de la Universitat de Barcelona runs DSpace 7.6.6, exposing a public REST API and an OAI-PMH metadata-harvesting endpoint. The university also operates centralized single sign-on (SSO) supporting SAML 2.0 / CAS, and publishes institutional open data through its transparency portal. No central, branded public developer portal or official organization-wide GitHub account was confirmed.'
finops:
- name: University Of Barcelona Finops
  service_category: Education
  slug: university-of-barcelona-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-barcelona.png
jsonld:
- class_count: 19
  name: University Of Barcelona Context
  property_count: 9
  slug: university-of-barcelona-context
layout: provider
modified: '2026-06-03'
name: University of Barcelona
nav: Providers
network: true
overview: 'University of Barcelona publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Spain, and Catalonia.


  The University of Barcelona catalog on APIs.io includes 1 JSON-LD context.


  University of Barcelona''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: University Of Barcelona Plans Pricing
  plan_count: 2
  slug: university-of-barcelona-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: University Of Barcelona Rate Limits
  slug: university-of-barcelona-rate-limits
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: University Of Barcelona Domain Security
  slug: university-of-barcelona-domain-security
  summary_line: TLSv1.2 · DMARC
slug: university-of-barcelona
tags:
- Education
- Higher Education
- University
- Spain
- Catalonia
- Open Data
- Library
- Scholarly
- Repository
- DSpace
- OAI-PMH
website: https://www.ub.edu/
---
