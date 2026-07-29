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
- acting_count: 6
  human_in_the_loop: 0
  name: Google Beyondcorp Agentic Access
  operation_count: 11
  slug: google-beyondcorp-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 3
apis:
- description: Operations for managing BeyondCorp app connections
  name: Google BeyondCorp AppConnections API
  slug: google-beyondcorp-appconnections-api
- description: Operations for managing BeyondCorp app connectors
  name: Google BeyondCorp AppConnectors API
  slug: google-beyondcorp-appconnectors-api
- description: Operations for managing BeyondCorp security gateways
  name: Google BeyondCorp SecurityGateways API
  slug: google-beyondcorp-securitygateways-api
artifact_total: 15
collections:
- collection_type: open
  name: Google BeyondCorp API
  slug: open-beyondcorp-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-beyondcorp-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-beyondcorp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-beyondcorp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-beyondcorp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-beyondcorp-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/beyondcorp-enterprise/docs/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/beyondcorp-enterprise/pricing
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-beyondcorp-context.jsonld
created: '2026-03-13'
description: Google BeyondCorp Enterprise is a zero-trust security platform that enables secure access to applications and resources without requiring a traditional VPN. It provides identity and context-aware access controls for enterprise resources, enabling organizations to implement zero-trust access policies across multi-cloud and on-premises environments using app connectors and client connectors.
finops:
- name: Google Beyondcorp Finops
  service_category: API
  slug: google-beyondcorp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-beyondcorp.png
json_schemas:
- name: Google BeyondCorp App Connection
  property_count: 11
  slug: google-beyondcorp-app-connection
jsonld:
- class_count: 0
  name: Google Beyondcorp Context
  property_count: 4
  slug: google-beyondcorp-context
layout: provider
modified: '2026-05-19'
name: Google BeyondCorp
nav: Providers
network: true
overview: 'Google BeyondCorp publishes 3 APIs on the [APIs.io](https://apis.io/) network: AppConnections API, AppConnectors API, and SecurityGateways API. Tagged areas include Access Control, Enterprise Security, Identity, Security, and VPN Alternative.


  The Google BeyondCorp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google BeyondCorp''s developer surface includes authentication, getting-started guide, pricing, and 6 more developer resources.'
plans:
- name: Google Beyondcorp Plans Pricing
  plan_count: 3
  slug: google-beyondcorp-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Google Beyondcorp Rate Limits
  slug: google-beyondcorp-rate-limits
rules:
- name: Google BeyondCorp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-beyondcorp-jsonschema-spectral-rules
scopes:
- name: Google Beyondcorp Scopes
  scope_count: 1
  slug: google-beyondcorp-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 50.5
  delta: -4.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 54.6
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
screenshot: https://raw.githubusercontent.com/api-evangelist/google-beyondcorp/refs/heads/main/screenshots/google-beyondcorp-2026-06-20T182023.png
security:
- kind: authentication
  name: Google Beyondcorp Authentication
  slug: google-beyondcorp-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Beyondcorp Domain Security
  slug: google-beyondcorp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Beyondcorp Vulnerability Disclosure
  slug: google-beyondcorp-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-beyondcorp
tags:
- Access Control
- Enterprise Security
- Identity
- Security
- VPN Alternative
- Zero Trust
---
