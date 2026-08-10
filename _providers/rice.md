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
  scored_at: '2026-08-10'
api_count: 4
apis:
- description: 'DSpace 9.x REST API for the Rice Research Repository (R-3), Fondren Library''s institutional repository. The API root advertises HAL links to communities, collections, items, bitstreams, and discovery '
  name: Rice Research Repository REST API
  slug: repository-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for the Rice Research Repository. The Identify verb returns repositoryName "Rice Research Repository" with an earliest datestamp of 2005. Supports standard OAI
  name: Rice Research Repository OAI-PMH
  slug: repository-oai
- description: Rice University Shibboleth/SAML 2.0 identity provider used for federated single sign-on. The IdP publishes SAML metadata (EntityDescriptor with IDPSSODescriptor) at its shibboleth metadata URL. Access
  name: Rice Shibboleth SAML Identity Provider
  slug: sso-shibboleth
- description: Public course catalog and schedule search at courses.rice.edu, exposing term, subject, and catalog query parameters via the SWKSCAT endpoint. It is a web query interface rather than a formally documen
  name: Rice University Course Schedule
  slug: course-schedule
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rice-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rice.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/RiceUniversity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/rice-university/
- group: operate
  title: ''
  type: Status
  url: https://status.rice.edu/
- group: auth
  title: ''
  type: Authentication
  url: https://idp.rice.edu/idp/shibboleth
- group: commercial
  title: ''
  type: Plans
  url: plans/rice-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rice-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rice-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Rice University is a private research university in Houston, Texas, ranked #141 in the QS World University Rankings 2025. Its public developer/API footprint is modest and centered on the library''s Rice Research Repository (R-3), a DSpace 9.x platform that exposes both a REST API and an OAI-PMH metadata interface for harvesting theses, dissertations, and scholarship. Rice also operates a Shibboleth/SAML identity provider for federated single sign-on and publishes a public course schedule. There is an official "RiceUniversity" GitHub organization, but it currently has no public repositories. No general-purpose, publicly documented developer portal was found.'
finops:
- name: Rice Finops
  service_category: Education
  slug: rice-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rice.png
jsonld:
- class_count: 13
  name: Rice Context
  property_count: 5
  slug: rice-context
layout: provider
modified: '2026-06-03'
name: Rice University
nav: Providers
network: true
overview: 'Rice University publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Library.


  The Rice University catalog on APIs.io includes 1 JSON-LD context.


  Rice University''s developer surface includes GitHub presence, status page, authentication, and 7 more developer resources.'
plans:
- name: Rice Plans Pricing
  plan_count: 2
  slug: rice-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 1
  name: Rice Rate Limits
  slug: rice-rate-limits
score:
  band: emerging
  composite: 21.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rice/refs/heads/main/screenshots/rice-2026-06-20T193109.png
security:
- kind: domain-security
  name: Rice Domain Security
  slug: rice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rice
tags:
- Education
- Higher Education
- University
- Research
- Library
- Open Repository
- United States
website: https://www.rice.edu/
---
