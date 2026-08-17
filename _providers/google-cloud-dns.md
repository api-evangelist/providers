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
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Dns Agentic Access
  operation_count: 10
  slug: google-cloud-dns-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 4
apis:
- description: Manage DNS changes
  name: Google Cloud DNS Changes API
  slug: google-cloud-dns-changes-api
- description: Manage DNS zones
  name: Google Cloud DNS ManagedZones API
  slug: google-cloud-dns-managedzones-api
- description: Manage DNS policies
  name: Google Cloud DNS Policies API
  slug: google-cloud-dns-policies-api
- description: Manage DNS resource record sets
  name: Google Cloud DNS ResourceRecordSets API
  slug: google-cloud-dns-resourcerecordsets-api
artifact_total: 25
collections:
- collection_type: postman
  name: Google Cloud DNS Changes API
  slug: postman-google-cloud-dns-changes-api
- collection_type: postman
  name: Google Cloud DNS Changes ManagedZones API
  slug: postman-google-cloud-dns-managedzones-api
- collection_type: postman
  name: Google Cloud DNS Changes Policies API
  slug: postman-google-cloud-dns-policies-api
- collection_type: postman
  name: Google Cloud DNS Changes ResourceRecordSets API
  slug: postman-google-cloud-dns-resourcerecordsets-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud DNS API
  slug: open-dns
- collection_type: open
  name: Google Cloud DNS Changes API
  slug: open-google-cloud-dns-changes-api
- collection_type: open
  name: Google Cloud DNS Changes ManagedZones API
  slug: open-google-cloud-dns-managedzones-api
- collection_type: open
  name: Google Cloud DNS Changes Policies API
  slug: open-google-cloud-dns-policies-api
- collection_type: open
  name: Google Cloud DNS Changes ResourceRecordSets API
  slug: open-google-cloud-dns-resourcerecordsets-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-dns/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-dns-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-dns-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-dns-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-dns-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-dns-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/dns
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/dns/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/dns/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/dns/pricing
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
  url: https://cloud.google.com/dns/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dns-context.jsonld
created: '2026-03-13'
description: Google Cloud DNS is a scalable, reliable, and managed authoritative Domain Name System (DNS) service running on the same infrastructure as Google. It provides low-latency, high-availability DNS serving with 100% uptime SLA, supporting both public and private DNS zones for domain name resolution.
finops:
- name: Google Cloud Dns Finops
  service_category: API
  slug: google-cloud-dns-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-dns.png
json_schemas:
- name: Google Cloud DNS Managed Zone
  property_count: 8
  slug: dns-managedzone
jsonld:
- class_count: 11
  name: Dns Context
  property_count: 3
  slug: dns-context
layout: provider
modified: '2026-05-19'
name: Google Cloud DNS
nav: Providers
network: true
overview: 'Google Cloud DNS publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Changes API, ManagedZones API, Policies API, and 1 more. Tagged areas include DNS, Domain Names, Google Cloud, Name Resolution, and Networking.


  The Google Cloud DNS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud DNS''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Dns Plans Pricing
  plan_count: 3
  slug: google-cloud-dns-plans-pricing
random_paper: 97
rate_limits:
- limit_count: 5
  name: Google Cloud Dns Rate Limits
  slug: google-cloud-dns-rate-limits
rules:
- name: Google Cloud DNS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-dns-jsonschema-spectral-rules
scopes:
- name: Google Cloud Dns Scopes
  scope_count: 2
  slug: google-cloud-dns-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 54.7
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 70.1
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-dns/refs/heads/main/screenshots/google-cloud-dns-2026-06-20T182106.png
security:
- kind: authentication
  name: Google Cloud Dns Authentication
  slug: google-cloud-dns-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Dns Domain Security
  slug: google-cloud-dns-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Dns Vulnerability Disclosure
  slug: google-cloud-dns-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-dns
tags:
- DNS
- Domain Names
- Google Cloud
- Name Resolution
- Networking
website: https://cloud.google.com/dns
---
