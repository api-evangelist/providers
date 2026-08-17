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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Cloud Interconnect Agentic Access
  operation_count: 6
  slug: google-cloud-interconnect-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 3
apis:
- description: Manage VLAN attachments for interconnects
  name: Google Cloud Interconnect InterconnectAttachments API
  slug: google-cloud-interconnect-interconnectattachments-api
- description: Query available interconnect locations
  name: Google Cloud Interconnect InterconnectLocations API
  slug: google-cloud-interconnect-interconnectlocations-api
- description: Manage interconnect connections
  name: Google Cloud Interconnect Interconnects API
  slug: google-cloud-interconnect-interconnects-api
artifact_total: 20
collections:
- collection_type: postman
  name: Google Cloud Interconnect InterconnectAttachments API
  slug: postman-google-cloud-interconnect-interconnectattachments-api
- collection_type: postman
  name: Google Cloud Interconnect InterconnectAttachments InterconnectLocations API
  slug: postman-google-cloud-interconnect-interconnectlocations-api
- collection_type: postman
  name: Google Cloud Interconnect InterconnectAttachments Interconnects API
  slug: postman-google-cloud-interconnect-interconnects-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Interconnect InterconnectAttachments API
  slug: open-google-cloud-interconnect-interconnectattachments-api
- collection_type: open
  name: Google Cloud Interconnect InterconnectAttachments InterconnectLocations API
  slug: open-google-cloud-interconnect-interconnectlocations-api
- collection_type: open
  name: Google Cloud Interconnect InterconnectAttachments Interconnects API
  slug: open-google-cloud-interconnect-interconnects-api
- collection_type: open
  name: Google Cloud Interconnect API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-interconnect/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-interconnect-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-interconnect-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-interconnect-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-interconnect-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-interconnect-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/network-connectivity/docs/interconnect
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/network-connectivity/docs/interconnect/how-to
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/network-connectivity/docs/interconnect
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/network-connectivity/docs/interconnect/pricing
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
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/network-connectivity/docs/interconnect/support
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: Google Cloud Interconnect provides high-bandwidth, low-latency connections between your on-premises network and Google Cloud, enabling hybrid cloud architectures through dedicated or partner interconnect options.
finops:
- name: Google Cloud Interconnect Finops
  service_category: API
  slug: google-cloud-interconnect-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-interconnect.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Interconnect
nav: Providers
network: true
overview: 'Google Cloud Interconnect publishes 3 APIs on the [APIs.io](https://apis.io/) network: InterconnectAttachments API, InterconnectLocations API, and Interconnects API. Tagged areas include Dedicated Connectivity, Google Cloud, Hybrid Cloud, Interconnect, and Networking.


  The Google Cloud Interconnect catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Interconnect''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Interconnect Plans Pricing
  plan_count: 3
  slug: google-cloud-interconnect-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Google Cloud Interconnect Rate Limits
  slug: google-cloud-interconnect-rate-limits
rules:
- name: Google Cloud Interconnect API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-interconnect-jsonschema-spectral-rules
scopes:
- name: Google Cloud Interconnect Scopes
  scope_count: 2
  slug: google-cloud-interconnect-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 53.3
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 64.2
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-interconnect/refs/heads/main/screenshots/google-cloud-interconnect-2026-06-20T182115.png
security:
- kind: authentication
  name: Google Cloud Interconnect Authentication
  slug: google-cloud-interconnect-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Interconnect Domain Security
  slug: google-cloud-interconnect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Interconnect Vulnerability Disclosure
  slug: google-cloud-interconnect-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-interconnect
tags:
- Dedicated Connectivity
- Google Cloud
- Hybrid Cloud
- Interconnect
- Networking
website: https://cloud.google.com/network-connectivity/docs/interconnect
---
