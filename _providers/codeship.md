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
- description: Codeship is a Continuous Integration Platform in the cloud
  name: Codeship
  slug: codeship
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/codeship-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/codeship-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codeship-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.cloudbees.com/docs/cloudbees-codeship/latest/api-overview/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Codeship is a Continuous Integration Platform in the cloud
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codeship.png
layout: provider
modified: '2026-05-28'
name: Codeship
nav: Providers
network: true
overview: Codeship publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Continuous Integration and Public APIs.
random_paper: 7
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codeship/refs/heads/main/screenshots/codeship-2026-06-20T174706.png
security:
- kind: domain-security
  name: Codeship Domain Security
  slug: codeship-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Codeship Vulnerability Disclosure
  slug: codeship-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Codeship Trust Center
  slug: codeship-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: codeship
tags:
- Continuous Integration
- Public APIs
website: https://docs.cloudbees.com/docs/cloudbees-codeship/latest/api-overview/
---
