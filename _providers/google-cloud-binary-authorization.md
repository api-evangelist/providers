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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Binary Authorization Agentic Access
  operation_count: 8
  slug: google-cloud-binary-authorization-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 1
apis:
- baseURL: https://binaryauthorization.googleapis.com
  baseurl_source: declared
  description: Operations for validating attestations
  name: Google Cloud Binary Authorization Attestations API
  slug: google-cloud-binary-authorization-attestations-api
- baseURL: https://binaryauthorization.googleapis.com
  baseurl_source: declared
  description: Operations for managing attestors
  name: Google Cloud Binary Authorization Attestors API
  slug: google-cloud-binary-authorization-attestors-api
- baseURL: https://binaryauthorization.googleapis.com
  baseurl_source: declared
  description: Operations for managing the Binary Authorization policy
  name: Google Cloud Binary Authorization Policy API
  slug: google-cloud-binary-authorization-policy-api
artifact_total: 22
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
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Binary Authorization API
  slug: open-binary-authorization-api
- collection_type: open
  name: Google Cloud Binary Authorization Attestations API
  slug: open-google-cloud-binary-authorization-attestations-api
- collection_type: open
  name: Google Cloud Binary Authorization Attestations Attestors API
  slug: open-google-cloud-binary-authorization-attestors-api
- collection_type: open
  name: Google Cloud Binary Authorization Attestations Policy API
  slug: open-google-cloud-binary-authorization-policy-api
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
random_paper: 17
rate_limits:
- limit_count: 5
  name: Google Cloud Binary Authorization Rate Limits
  slug: google-cloud-binary-authorization-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Binary Authorization API Rules
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
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 60.3
    catalog_earned_first_party: 0.0
    catalog_gap: 54.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 61.9
    developer_ergonomics: 51.2
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 72.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
