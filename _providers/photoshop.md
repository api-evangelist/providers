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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
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
overview: 'Photoshop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Adobe, AI, Image Editing, Photoshop, and Firefly Services.


  Photoshop''s developer surface includes developer portal, documentation, GitHub presence, and 4 more developer resources.'
plans:
- name: Photoshop Plans Pricing
  plan_count: 3
  slug: photoshop-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 5
  name: Photoshop Rate Limits
  slug: photoshop-rate-limits
score:
  band: emerging
  composite: 23.0
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 25.4
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- AI
- Image Editing
- Photoshop
- Firefly Services
website: https://www.adobe.com/products/photoshop.html
---
