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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Used to retrieve and apply transformations to images
  name: Contentful Images
  slug: contentful-images
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/contentful-images-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/contentful-images-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contentful-images-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.contentful.com/developers/docs/references/images-api/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.contentful.com/blog/
created: '2026-05-28'
description: Used to retrieve and apply transformations to images
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contentful-images.png
layout: provider
modified: '2026-05-28'
name: Contentful Images
nav: Providers
network: true
overview: 'Contentful Images publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Development and Public APIs.


  Contentful Images'' developer surface includes engineering blog and 5 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contentful-images/refs/heads/main/screenshots/contentful-images-2026-06-20T174926.png
security:
- kind: domain-security
  name: Contentful Images Domain Security
  slug: contentful-images-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Contentful Images Vulnerability Disclosure
  slug: contentful-images-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Contentful Images Trust Center
  slug: contentful-images-trust-center
  summary_line: SOC 2, ISO 27001
slug: contentful-images
tags:
- Development
- Public APIs
website: https://www.contentful.com/developers/docs/references/images-api/
---
