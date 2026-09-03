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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: GraphQL API for querying and managing cloud security inventory, issues, vulnerabilities, misconfigurations, identities, controls, and reports across the Wiz security graph. Authentication uses OAuth 2
  name: Wiz GraphQL API
  slug: graphql-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/wiz-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wiz-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wiz-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wizsecurity
- group: company
  title: ''
  type: Website
  url: https://www.wiz.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wiz.io
- group: start
  title: ''
  type: Signup
  url: https://www.wiz.io/demo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wiz.io/pricing
- group: learn
  title: ''
  type: Academy
  url: https://www.wiz.io/academy
- group: company
  title: ''
  type: Blog
  url: https://www.wiz.io/blog/rss.xml
created: '2026-05-11'
description: Wiz is a cloud-native application protection platform (CNAPP) that provides agentless security across AWS, Azure, GCP, Kubernetes, and containers, covering CSPM, CWPP, CIEM, vulnerability management, DSPM, and threat detection in a unified security graph. The Wiz GraphQL API exposes inventory, issues, vulnerabilities, configurations, and reporting using OAuth 2.0 client credentials authentication.
graphqls:
- description: GraphQL API for querying and managing cloud security inventory, issues, vulnerabilities, misconfigurations, identities, controls, and reports across the Wiz security graph. Authentication uses OAuth 2
  name: Wiz GraphQL API
  slug: wiz-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wiz.png
layout: provider
modified: '2026-05-11'
name: Wiz
nav: Providers
network: true
overview: 'Wiz publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Security, CNAPP, CSPM, Vulnerability Management, and Cloud-Native.


  Wiz''s developer surface includes documentation, signup flow, pricing, academy / training, engineering blog, and 5 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wiz/refs/heads/main/screenshots/wiz-2026-06-20T201539.png
security:
- kind: domain-security
  name: Wiz Domain Security
  slug: wiz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Wiz Vulnerability Disclosure
  slug: wiz-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Wiz Trust Center
  slug: wiz-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, CSA STAR
slug: wiz
tags:
- Cloud Security
- CNAPP
- CSPM
- Vulnerability Management
- Cloud-Native
- DevSecOps
- Security
website: https://www.wiz.io
---
