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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Binary Authorization Agentic Access
  operation_count: 8
  slug: google-cloud-binary-authorization-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 3
apis:
- description: Operations for validating attestations
  name: Google Cloud Binary Authorization Attestations API
  slug: google-cloud-binary-authorization-attestations-api
- description: Operations for managing attestors
  name: Google Cloud Binary Authorization Attestors API
  slug: google-cloud-binary-authorization-attestors-api
- description: Operations for managing the Binary Authorization policy
  name: Google Cloud Binary Authorization Policy API
  slug: google-cloud-binary-authorization-policy-api
artifact_total: 18
collections:
- collection_type: postman
  name: Google Cloud Binary Authorization Attestations API
  slug: postman-google-cloud-binary-authorization-attestations-api
- collection_type: postman
  name: Google Cloud Binary Authorization Attestations Attestors API
  slug: postman-google-cloud-binary-authorization-attestors-api
- collection_type: postman
  name: Google Cloud Binary Authorization Attestations Policy API
  slug: postman-google-cloud-binary-authorization-policy-api
- collection_type: open
  name: Google Cloud Binary Authorization API
  slug: open-binary-authorization-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-binary-authorization/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-binary-authorization-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-binary-authorization-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-binary-authorization-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-binary-authorization-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-binary-authorization-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/binary-authorization
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/binary-authorization/docs/getting-started-cli
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/binary-authorization/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/binary-authorization/docs/reference/rest#authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/binary-authorization/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/binary-authorization/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-binary-authorization-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/binary-authorization-release-notes.xml
created: '2026-03-13'
description: Google Cloud Binary Authorization is a deploy-time security control that ensures only trusted container images are deployed on Google Kubernetes Engine (GKE), Cloud Run, and Anthos clusters. It uses attestation-based policies to validate that container images have been signed by trusted authorities before allowing deployment, helping enforce software supply chain security.
finops:
- name: Google Cloud Binary Authorization Finops
  service_category: API
  slug: google-cloud-binary-authorization-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-binary-authorization.png
json_schemas:
- name: Google Cloud Binary Authorization Policy
  property_count: 8
  slug: google-cloud-binary-authorization-policy
jsonld:
- class_count: 0
  name: Google Cloud Binary Authorization Context
  property_count: 3
  slug: google-cloud-binary-authorization-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Binary Authorization
nav: Providers
network: true
overview: 'Google Cloud Binary Authorization publishes 3 APIs on the [APIs.io](https://apis.io/) network: Attestations API, Attestors API, and Policy API. Tagged areas include Attestation, Container Security, DevSecOps, Kubernetes, and Policy Enforcement.


  The Google Cloud Binary Authorization catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Binary Authorization''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Google Cloud Binary Authorization Plans Pricing
  plan_count: 3
  slug: google-cloud-binary-authorization-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 5
  name: Google Cloud Binary Authorization Rate Limits
  slug: google-cloud-binary-authorization-rate-limits
rules:
- name: Google Cloud Binary Authorization API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: google-cloud-binary-authorization-jsonschema-spectral-rules
scopes:
- name: Google Cloud Binary Authorization Scopes
  scope_count: 1
  slug: google-cloud-binary-authorization-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 62.4
  delta: -3.2
  facets:
    commercial_clarity: 71.1
    contract_quality: 67.8
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 65.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-binary-authorization/refs/heads/main/screenshots/google-cloud-binary-authorization-2026-06-20T182045.png
security:
- kind: authentication
  name: Google Cloud Binary Authorization Authentication
  slug: google-cloud-binary-authorization-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Binary Authorization Domain Security
  slug: google-cloud-binary-authorization-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Binary Authorization Vulnerability Disclosure
  slug: google-cloud-binary-authorization-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-binary-authorization
tags:
- Attestation
- Container Security
- DevSecOps
- Kubernetes
- Policy Enforcement
- Supply Chain Security
website: https://cloud.google.com/binary-authorization
---
