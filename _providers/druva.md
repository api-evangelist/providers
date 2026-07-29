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
- acting_count: 11
  human_in_the_loop: 0
  name: Druva Agentic Access
  operation_count: 21
  slug: druva-agentic-access
  summary_line: 21 operations · 11 acting
api_count: 14
apis:
- description: The Druva Cyber Resilience REST API provides programmatic access to reports and events across the Druva Data Resiliency Cloud, supporting ransomware recovery, anomaly detection, and security posture m
  name: Druva Cyber Resilience API
  slug: cyber-resilience
- description: The Druva Endpoints and Data Governance API exposes Reports and Events endpoints for visibility into endpoint backups, user activity, and governance posture across managed devices and SaaS workloads.
  name: Druva Endpoints and Data Governance API
  slug: endpoints-data-governance
- description: 'The Druva Enterprise Workloads Events API provides programmatic access to events generated across protected enterprise workloads such as servers, virtual machines, and databases inside the Druva Data '
  name: Druva Enterprise Workloads API
  slug: enterprise-workloads
- description: The Druva CloudRanger Native Workloads API provides automated backup, disaster recovery, and lifecycle management for AWS-native workloads including EC2, EBS, RDS, Redshift, and DynamoDB.
  name: Druva CloudRanger Native Workloads API
  slug: cloudranger
- description: The Druva MSP API enables managed service providers to programmatically manage tenants, customers, and reporting across the Druva platform from a single MSP console integration.
  name: Druva MSP API
  slug: msp
- description: The Druva Legal Hold Targeted Download API supports legal and compliance teams in initiating targeted downloads of preserved data from devices placed under legal hold within Druva.
  name: Druva Legal Hold Targeted Download API
  slug: legal-hold
- description: The Accounts API from Druva — 2 operation(s) for accounts.
  name: Druva Accounts API
  slug: druva-accounts-api
- description: The Authentication API from Druva — 1 operation(s) for authentication.
  name: Druva Authentication API
  slug: druva-authentication-api
- description: The Backups API from Druva — 1 operation(s) for backups.
  name: Druva Backups API
  slug: druva-backups-api
- description: The Cyber Resilience API from Druva — 2 operation(s) for cyber resilience.
  name: Druva Cyber Resilience API
  slug: druva-cyber-resilience-api
- description: The Policies API from Druva — 2 operation(s) for policies.
  name: Druva Policies API
  slug: druva-policies-api
- description: The Reports API from Druva — 1 operation(s) for reports.
  name: Druva Reports API
  slug: druva-reports-api
- description: The Schedules API from Druva — 1 operation(s) for schedules.
  name: Druva Schedules API
  slug: druva-schedules-api
- description: The Servers API from Druva — 1 operation(s) for servers.
  name: Druva Servers API
  slug: druva-servers-api
artifact_total: 22
collections:
- collection_type: open
  name: Druva REST API
  slug: open-druva
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/druva-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/druva-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/druva-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/druva-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/druva
- group: company
  title: ''
  type: Website
  url: https://www.druva.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.druva.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.druva.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.druva.com/reference
- group: operate
  title: ''
  type: Support
  url: https://support.druva.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/druvainc
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.druva.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.druva.com/blog
created: '2026-03-27'
description: Druva is a cloud data protection and management platform providing SaaS backup, disaster recovery, and data governance for endpoints, data centers, and SaaS applications. Druva exposes a public REST API across its Cyber Resilience, Endpoint Data Governance, Enterprise Workloads, CloudRanger, MSP, and Legal Hold products, using token-based authentication and JSON over HTTPS.
finops:
- name: Druva Finops
  service_category: API
  slug: druva-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/druva.png
layout: provider
modified: '2026-04-28'
name: Druva
nav: Providers
network: true
overview: 'Druva publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Backups API, and 5 more. Tagged areas include Backup, Cyber Resilience, Data Protection, Disaster Recovery, and SaaS Backup.


  Druva''s developer surface includes authentication, documentation, API reference, support, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Druva Plans Pricing
  plan_count: 3
  slug: druva-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 5
  name: Druva Rate Limits
  slug: druva-rate-limits
score:
  band: developing
  composite: 43.3
  delta: -2.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 53.4
    developer_ergonomics: 41.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/druva/refs/heads/main/screenshots/druva-2026-06-20T180253.png
security:
- kind: authentication
  name: Druva Authentication
  slug: druva-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Druva Domain Security
  slug: druva-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Druva Trust Center
  slug: druva-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR, FIPS 140
slug: druva
tags:
- Backup
- Cyber Resilience
- Data Protection
- Disaster Recovery
- SaaS Backup
website: https://www.druva.com
---
