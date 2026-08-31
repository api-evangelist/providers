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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Google Cloud Certificate Manager Agentic Access
  operation_count: 4
  slug: google-cloud-certificate-manager-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: Operations for managing certificate maps
  name: Google Cloud Certificate Manager CertificateMaps API
  slug: google-cloud-certificate-manager-certificatemaps-api
- description: Operations for managing TLS certificates
  name: Google Cloud Certificate Manager Certificates API
  slug: google-cloud-certificate-manager-certificates-api
- description: Operations for managing DNS authorizations
  name: Google Cloud Certificate Manager DnsAuthorizations API
  slug: google-cloud-certificate-manager-dnsauthorizations-api
artifact_total: 22
collections:
- collection_type: postman
  name: Google Cloud Certificate Manager CertificateMaps API
  slug: postman-google-cloud-certificate-manager-certificatemaps-api
- collection_type: postman
  name: Google Cloud Certificate Manager CertificateMaps Certificates API
  slug: postman-google-cloud-certificate-manager-certificates-api
- collection_type: postman
  name: Google Cloud Certificate Manager CertificateMaps DnsAuthorizations API
  slug: postman-google-cloud-certificate-manager-dnsauthorizations-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Certificate Manager API
  slug: open-certificate-manager-api
- collection_type: open
  name: Google Cloud Certificate Manager CertificateMaps API
  slug: open-google-cloud-certificate-manager-certificatemaps-api
- collection_type: open
  name: Google Cloud Certificate Manager CertificateMaps Certificates API
  slug: open-google-cloud-certificate-manager-certificates-api
- collection_type: open
  name: Google Cloud Certificate Manager CertificateMaps DnsAuthorizations API
  slug: open-google-cloud-certificate-manager-dnsauthorizations-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-certificate-manager/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-certificate-manager-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-certificate-manager-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-certificate-manager-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-certificate-manager-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-certificate-manager-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/certificate-manager
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/certificate-manager/docs/overview
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/certificate-manager/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/certificate-manager/docs/reference/rest#authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/certificate-manager/pricing
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
  url: https://cloud.google.com/certificate-manager/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-certificate-manager-context.jsonld
created: '2026-03-13'
description: Google Cloud Certificate Manager is a service that lets you acquire and manage TLS (SSL) certificates for use with Google Cloud load balancers and other Google Cloud services. It supports provisioning, renewing, and deploying both Google-managed and self-managed certificates, simplifying certificate lifecycle management at scale.
finops:
- name: Google Cloud Certificate Manager Finops
  service_category: API
  slug: google-cloud-certificate-manager-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-certificate-manager.png
json_schemas:
- name: Google Cloud Certificate Manager Certificate
  property_count: 11
  slug: google-cloud-certificate-manager-certificate
jsonld:
- class_count: 0
  name: Google Cloud Certificate Manager Context
  property_count: 3
  slug: google-cloud-certificate-manager-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Certificate Manager
nav: Providers
network: true
overview: 'Google Cloud Certificate Manager publishes 3 APIs on the [APIs.io](https://apis.io/) network: CertificateMaps API, Certificates API, and DnsAuthorizations API. Tagged areas include Certificate Management, Certificates, Load Balancing, Security, and SSL.


  The Google Cloud Certificate Manager catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Certificate Manager''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Certificate Manager Plans Pricing
  plan_count: 3
  slug: google-cloud-certificate-manager-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Google Cloud Certificate Manager Rate Limits
  slug: google-cloud-certificate-manager-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Certificate Manager API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-certificate-manager-jsonschema-spectral-rules
scopes:
- name: Google Cloud Certificate Manager Scopes
  scope_count: 1
  slug: google-cloud-certificate-manager-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 61.9
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-certificate-manager/refs/heads/main/screenshots/google-cloud-certificate-manager-2026-06-20T182052.png
security:
- kind: authentication
  name: Google Cloud Certificate Manager Authentication
  slug: google-cloud-certificate-manager-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Certificate Manager Domain Security
  slug: google-cloud-certificate-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Certificate Manager Vulnerability Disclosure
  slug: google-cloud-certificate-manager-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-certificate-manager
tags:
- Certificate Management
- Certificates
- Load Balancing
- Security
- SSL
- TLS
website: https://cloud.google.com/certificate-manager
---
