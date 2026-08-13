---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: Helios is Cohesity's SaaS-based control plane that manages a fleet of Cohesity clusters from a single global pane of glass. The Helios REST API authenticates via an apiKey generated from the Helios UI
  name: Cohesity Helios REST API
  slug: helios-rest-api
- description: The DataProtect REST API is the per-cluster RESTful interface exposed by every Cohesity cluster, providing programmatic control over data management operations including backups, restores, replication
  name: Cohesity DataProtect REST API
  slug: dataprotect-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cohesity-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cohesity
- group: company
  title: ''
  type: Website
  url: https://www.cohesity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cohesity.com/
- group: other
  title: ''
  type: Developers Site
  url: https://developers.cohesity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cohesity.com/apidocs/versions/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cohesity
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cohesity.com/
- group: operate
  title: ''
  type: Support
  url: https://www.cohesity.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cohesity.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cohesity.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cohesity.com/agreements/website-terms-of-use/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.cohesity.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.cohesity.com/feed/
created: '2025-03-01'
description: Cohesity is a data security and management company providing backup, disaster recovery, archive, and cyber resilience capabilities across on-premises, cloud, and SaaS workloads. Following the merger with Veritas, the combined company protects enterprise data while powering automation, orchestration, and AI- driven recovery. The Cohesity developer surface centers on the Cohesity REST API, exposed both per-cluster (DataProtect/cluster API) and via the Helios global control plane, with versioned v1 and v2 endpoints, API-key authentication, and SDKs for Python, PowerShell, Ansible, Terraform, and ServiceNow.
finops:
- name: Cohesity Finops
  service_category: API
  slug: cohesity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cohesity.png
layout: provider
modified: '2026-04-28'
name: Cohesity
nav: Providers
network: true
overview: 'Cohesity publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Backup, Cyber Resilience, Data Management, and Data Protection.


  Cohesity''s developer surface includes API reference, GitHub presence, documentation, support, engineering blog, and 9 more developer resources.'
plans:
- name: Cohesity Plans Pricing
  plan_count: 3
  slug: cohesity-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 5
  name: Cohesity Rate Limits
  slug: cohesity-rate-limits
score:
  band: emerging
  composite: 23.9
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 23.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cohesity/refs/heads/main/screenshots/cohesity-2026-06-20T174720.png
security:
- kind: domain-security
  name: Cohesity Domain Security
  slug: cohesity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cohesity
tags:
- Automation
- Backup
- Cyber Resilience
- Data Management
- Data Protection
- Data Security
- DataProtect
- Disaster Recovery
- Helios
- Orchestration
website: https://www.cohesity.com/
---
