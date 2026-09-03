---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Adobe Photoshop API for automating image editing workflows, applying Photoshop actions, manipulating layers and smart objects, generating renditions and document manifests, and AI-powered image manipu
  name: Photoshop API
  slug: photoshop-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/photoshop-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/photoshop-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/adobe-creative-cloud
- group: start
  title: ''
  type: Portal
  url: https://developer.adobe.com/firefly-services/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.adobe.com/firefly-services/docs/photoshop/
- group: company
  title: ''
  type: Website
  url: https://www.adobe.com/products/photoshop.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/AdobeDocs/photoshop-api-docs
created: '2026-03-16'
description: Adobe Photoshop provides API capabilities through Adobe Firefly Services and the Photoshop API, allowing developers to automate photo editing, apply Photoshop actions, manipulate layers and smart objects, generate renditions, and leverage AI-powered image editing at scale.
finops:
- name: Photoshop Finops
  service_category: API
  slug: photoshop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/photoshop.png
layout: provider
modified: '2026-04-28'
name: Photoshop
nav: Providers
network: true
overview: 'Photoshop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Adobe, Artificial Intelligence, Image Editing, Photoshop, and Firefly Services.


  Photoshop''s developer surface includes developer portal, documentation, GitHub presence, and 4 more developer resources.'
plans:
- name: Photoshop Plans Pricing
  plan_count: 3
  slug: photoshop-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Photoshop Rate Limits
  slug: photoshop-rate-limits
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 21.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/photoshop/refs/heads/main/screenshots/photoshop-2026-06-20T191653.png
security:
- kind: domain-security
  name: Photoshop Domain Security
  slug: photoshop-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Photoshop Vulnerability Disclosure
  slug: photoshop-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: photoshop
tags:
- Adobe
- Artificial Intelligence
- Image Editing
- Photoshop
- Firefly Services
website: https://www.adobe.com/products/photoshop.html
---
