---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: REST API for programmatic access to Logikcull's eDiscovery platform, enabling document upload, project management, tagging, redactions, and production set generation for legal review workflows.
  name: Logikcull API
  slug: logikcull-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/logikcull-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/logikcull-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/logikcull-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/logikcull-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/logikcull-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/logikcull-finops.yml
- group: operate
  title: ''
  type: Status
  url: https://status.logikcull.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.logikcull.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.logikcull.com/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.revealdata.com/logikcull
- group: operate
  title: ''
  type: Contact
  url: https://www.logikcull.com/company/contact-us
created: '2026-06-13'
description: Cloud eDiscovery platform with a REST API for uploading case documents, managing review projects, applying tags and redactions, and generating production sets. Logikcull enables legal teams to process, review, and produce data in a self-service model with integrations for Slack, Microsoft 365, Google Workspace, Box, and Dropbox.
finops:
- name: Logikcull Finops
  service_category: ''
  slug: logikcull-finops
graphqls:
- description: Logikcull is a cloud-based e-discovery platform. The API covers upload management, processing status, project management, search queries, document review workflows, tag management, production, and ana
  name: Logikcull GraphQL API
  slug: logikcull-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logikcull.png
jsonld:
- class_count: 28
  name: Logikcull Context
  property_count: 4
  slug: logikcull-context
layout: provider
modified: '2026-06-13'
name: Logikcull
nav: Providers
network: true
overview: 'Logikcull publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include eDiscovery, Legal, Document Management, Legal Holds, and Redaction.


  The Logikcull catalog on APIs.io includes 1 JSON-LD context.


  Logikcull''s developer surface includes status page, pricing, engineering blog, support, and 7 more developer resources.'
plans:
- name: Logikcull Plans Pricing
  plan_count: 2
  slug: logikcull-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Logikcull Rate Limits
  slug: logikcull-rate-limits
score:
  band: thin
  composite: 35.0
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 53.1
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/logikcull/refs/heads/main/screenshots/logikcull-2026-06-20T184702.png
security:
- kind: domain-security
  name: Logikcull Domain Security
  slug: logikcull-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Logikcull Vulnerability Disclosure
  slug: logikcull-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Logikcull Trust Center
  slug: logikcull-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: logikcull
tags:
- eDiscovery
- Legal
- Document Management
- Legal Holds
- Redaction
- Production Sets
- Cloud
---
