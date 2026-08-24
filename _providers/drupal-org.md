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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Drupal.org
  name: Drupal.org
  slug: drupalorg
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/drupal-org-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drupal-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.drupal.org/drupalorg/docs/api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.drupal.org/planet/rss.xml
created: '2026-05-28'
description: Drupal.org
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drupal-org.png
layout: provider
modified: '2026-05-28'
name: Drupal.org
nav: Providers
network: true
overview: 'Drupal.org publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Source Projects and Public APIs.


  Drupal.org''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 6.2
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/drupal-org/refs/heads/main/screenshots/drupal-org-2026-06-20T180251.png
security:
- kind: domain-security
  name: Drupal Org Domain Security
  slug: drupal-org-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Drupal Org Vulnerability Disclosure
  slug: drupal-org-vulnerability-disclosure
  summary_line: disclosure policy published
slug: drupal-org
tags:
- Open Source Projects
- Public APIs
website: https://www.drupal.org/drupalorg/docs/api
---
