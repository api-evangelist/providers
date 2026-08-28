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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: EU-hosted email API for transactional and marketing email, with contacts, broadcasts, and analytics
  name: PostStack
  slug: poststack
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/poststack-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/poststack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/poststack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://poststack.dev/docs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: EU-hosted email API for transactional and marketing email, with contacts, broadcasts, and analytics
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/poststack.png
layout: provider
modified: '2026-05-28'
name: PostStack
nav: Providers
network: true
overview: PostStack publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email and Public APIs.
random_paper: 1
score:
  band: minimal
  composite: 9.2
  delta: 1.9
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/poststack/refs/heads/main/screenshots/poststack-2026-06-20T192019.png
security:
- kind: domain-security
  name: Poststack Domain Security
  slug: poststack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Poststack Vulnerability Disclosure
  slug: poststack-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Poststack Trust Center
  slug: poststack-trust-center
  summary_line: ISO 27001, GDPR
slug: poststack
tags:
- Email
- Public APIs
website: https://poststack.dev/docs
---
