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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: V7 Labs Agentic Access
  operation_count: 25
  slug: v7-labs-agentic-access
  summary_line: 25 operations · 14 acting
api_count: 6
apis:
- description: Read and import item annotations.
  name: V7 Annotations API
  slug: v7-labs-annotations-api
- description: Manage annotation classes (labeling taxonomy).
  name: V7 Classes API
  slug: v7-labs-classes-api
- description: Create and manage datasets.
  name: V7 Datasets API
  slug: v7-labs-datasets-api
- description: Request and manage dataset exports (releases).
  name: V7 Exports API
  slug: v7-labs-exports-api
- description: Register, upload, list, and manage dataset items.
  name: V7 Items API
  slug: v7-labs-items-api
- description: Manage multi-stage annotation workflows and stages.
  name: V7 Workflows API
  slug: v7-labs-workflows-api
artifact_total: 15
collections:
- collection_type: open
  name: V7 Darwin API
  slug: open-v7-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/v7-labs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/v7-labs-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/v7-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/v7-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/v7-labs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/v7labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/v7labs
- group: company
  title: ''
  type: Website
  url: https://www.v7labs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.v7labs.com
- group: commercial
  title: ''
  type: Plans
  url: plans/v7-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/v7-labs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/v7-labs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.v7labs.com/blog
created: '2026-06-21'
description: V7 is an AI training-data and document-automation company. V7 Darwin is a training-data platform for labeling images, video, and documents and orchestrating human-in-the-loop annotation workflows; V7 Go automates document-intensive knowledge work with agentic AI. The Darwin REST API at https://darwin.v7labs.com/api manages datasets, items, annotations, classes, workflow stages, and exports using ApiKey authentication.
finops:
- name: V7 Labs Finops
  service_category: AI and Machine Learning
  slug: v7-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/v7-labs.png
layout: provider
modified: '2026-06-21'
name: V7
nav: Providers
network: true
overview: 'V7 publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Annotations API, Classes API, Datasets API, and 3 more. Tagged areas include AI, Training Data, Data Labeling, Annotation, and Document AI.


  V7''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: V7 Labs Plans Pricing
  plan_count: 3
  slug: v7-labs-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 4
  name: V7 Labs Rate Limits
  slug: v7-labs-rate-limits
score:
  band: thin
  composite: 39.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 55.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: V7 Labs Authentication
  slug: v7-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: V7 Labs Domain Security
  slug: v7-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: V7 Labs Vulnerability Disclosure
  slug: v7-labs-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: V7 Labs Trust Center
  slug: v7-labs-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: v7-labs
tags:
- AI
- Training Data
- Data Labeling
- Annotation
- Document AI
- Computer Vision
website: https://www.v7labs.com
---
