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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: REST API for managing users, teams, on-call schedules, escalation policies, incidents, and routing keys in Splunk On-Call (VictorOps). Authentication uses X-VO-Api-Id and X-VO-Api-Key headers generate
  name: Splunk On-Call Public API
  slug: public-api
- description: Inbound REST endpoint for creating incidents from any monitoring system via HTTPS POST with a JSON payload and a routing-key segment in the URL.
  name: Splunk On-Call REST Endpoint
  slug: rest-endpoint
artifact_total: 6
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/splunk/
- group: auth
  title: ''
  type: TrustCenter
  url: security/victorops-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/victorops-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/victorops-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/victorops
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/victorops-inc-
- group: company
  title: ''
  type: Website
  url: https://www.splunk.com/en_us/products/on-call.html
- group: docs
  title: ''
  type: Documentation
  url: https://help.victorops.com/
- group: docs
  title: ''
  type: API Documentation
  url: https://help.victorops.com/knowledge-base/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.splunk.com/en_us/products/on-call.html
- group: start
  title: ''
  type: Signup
  url: https://portal.victorops.com/membership/#/
- group: start
  title: ''
  type: Login
  url: https://portal.victorops.com/auth/#/login
- group: operate
  title: ''
  type: Support
  url: https://www.splunk.com/en_us/support-and-services.html
created: '2026-05-11'
description: Splunk On-Call, formerly known as VictorOps, is an incident management and on-call alerting platform that helps DevOps and SRE teams reduce mean time to resolution by routing alerts, managing on-call schedules, and orchestrating incident response. The platform integrates with monitoring and observability tools to deliver context-rich alerts and supports collaborative chat-based remediation workflows. The VictorOps REST API enables programmatic management of users, teams, schedules, escalation policies, incidents, and integrations using API ID and API Key authentication headers.
graphqls:
- description: This conceptual GraphQL schema models the VictorOps (now Splunk On-Call) incident management platform. VictorOps provides REST APIs for programmatic control over incidents, on-call schedules, escalati
  name: VictorOps (Splunk On-Call) GraphQL Schema
  slug: victorops-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/victorops.png
layout: provider
modified: '2026-08-19'
name: Splunk On-Call (VictorOps)
nav: Providers
network: true
overview: 'Splunk On-Call (VictorOps) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Incident Management, On-Call, Alerting, DevOps, and SRE.


  Splunk On-Call (VictorOps)''s developer surface includes documentation, pricing, signup flow, support, and 9 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 4
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 26.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/victorops/refs/heads/main/screenshots/victorops-2026-06-20T201030.png
security:
- kind: domain-security
  name: Victorops Domain Security
  slug: victorops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Victorops Vulnerability Disclosure
  slug: victorops-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Victorops Trust Center
  slug: victorops-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: victorops
tags:
- Incident Management
- On-Call
- Alerting
- DevOps
- SRE
- Incident Response
- Observability
website: https://www.splunk.com/en_us/products/on-call.html
---
