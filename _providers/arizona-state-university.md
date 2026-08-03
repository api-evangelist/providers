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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-03'
api_count: 4
apis:
- description: The ASU Library Research Data Repository runs on the open-source Dataverse platform (verified version 6.10.1) and exposes Dataverse's native REST API for searching, retrieving, and depositing research
  name: ASU Library Research Data Repository API
  slug: dataverse-api
- description: The ASU Library Research Data Repository Dataverse OAI Archive exposes an OAI-PMH 2.0 metadata harvesting endpoint. The Identify verb responds publicly, allowing harvesting of dataset metadata records
  name: ASU Research Data Repository OAI-PMH
  slug: dataverse-oai
- description: ASU publishes a public course catalog and class search at catalog.apps.asu.edu (with a legacy interface at webapp4.asu.edu). It provides searchable real-time course and section data through a web inte
  name: ASU Course Catalog & Class Search
  slug: course-catalog
- description: ASU operates an enterprise single sign-on service using the Central Authentication Service (CAS) protocol with Shibboleth/SAML federation for authenticating ASURITE accounts across university web appl
  name: ASU WebAuth (CAS / Shibboleth SSO)
  slug: sso-cas
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arizona-state-university-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arizona-state-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.asu.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ASU
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/arizona-state-university/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ASU
- group: auth
  title: ''
  type: Authentication
  url: https://getprotected.asu.edu/services/identity-and-access-management/authentication-services
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/asulibraries
- group: commercial
  title: ''
  type: Plans
  url: plans/arizona-state-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/arizona-state-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/arizona-state-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Arizona State University (ASU) is a large public research university based in Tempe, Arizona, United States, ranked #200 in the QS World University Rankings 2025. ASU''s confirmed public developer footprint centers on its Library Research Data Repository, a Dataverse instance that exposes a documented native REST API and an OAI-PMH metadata interface. ASU also operates a public course catalog and class search, a CAS/Shibboleth single sign-on identity service, and an official GitHub organization hosting its Unity design system and Drupal-based web infrastructure. Most administrative and student-facing APIs are gated behind ASURITE authentication and are not publicly documented.'
finops:
- name: Arizona State University Finops
  service_category: Education
  slug: arizona-state-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arizona-state-university.png
jsonld:
- class_count: 11
  name: Arizona State University Context
  property_count: 2
  slug: arizona-state-university-context
layout: provider
modified: '2026-06-03'
name: Arizona State University
nav: Providers
network: true
overview: 'Arizona State University publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research Data, and Open Data.


  The Arizona State University catalog on APIs.io includes 1 JSON-LD context.


  Arizona State University''s developer surface includes GitHub presence, authentication, and 10 more developer resources.'
plans:
- name: Arizona State University Plans Pricing
  plan_count: 2
  slug: arizona-state-university-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 1
  name: Arizona State University Rate Limits
  slug: arizona-state-university-rate-limits
score:
  band: emerging
  composite: 24.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 42.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arizona-state-university/refs/heads/main/screenshots/arizona-state-university-2026-06-20T172431.png
security:
- kind: domain-security
  name: Arizona State University Domain Security
  slug: arizona-state-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arizona State University Vulnerability Disclosure
  slug: arizona-state-university-vulnerability-disclosure
  summary_line: disclosure policy published
slug: arizona-state-university
tags:
- Education
- Higher Education
- University
- Research Data
- Open Data
- United States
- Arizona
website: https://www.asu.edu/
---
