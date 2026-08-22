---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Cloudsight Agentic Access
  operation_count: 3
  slug: cloudsight-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: Submit images for recognition and retrieve the resulting annotation.
  name: CloudSight Images API
  slug: cloudsight-images-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CloudSight Images API
  slug: open-cloudsight-images-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/cloudsight-images-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudsight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudsight.ai
- group: docs
  title: ''
  type: Documentation
  url: https://cloudsight.docs.apiary.io
- group: operate
  title: ''
  type: Support
  url: https://cloudsight.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudsight
- group: start
  title: ''
  type: Login
  url: https://cloudsight.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloudsight.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudsight.ai/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudsight-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloudsight-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloudsight-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/cloudsight-images-examples.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cloudsight-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cloudsight-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloudsight-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cloudsight-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cloudsight-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/cloudsight-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cloudsight-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cloudsight-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudsight-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloudsight-llms.txt
created: '2026-08-09'
description: CloudSight Inc. is a computer-vision company that sells general-purpose image understanding as a single, simple REST API. A client POSTs an image — as a multipart upload, a base64 data URI, or a remote image URL — and receives a token; polling that token returns a natural-language caption describing what is in the picture, together with skip reasons (blurry, dark, bright, offensive, unsure) and content flags (adult) when the image cannot be described. The company grew out of the CamFind visual-search app, also ships an on-device SDK, and lists a whole-scene recognition model on Google Cloud Marketplace. The public API contract is published as an API Blueprint on Apiary and is backed by first-party client libraries for Ruby, Python, Go, Elixir and Objective-C.
image: https://cloudsight.ai/static/img/favicons/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: cloudsight-mcp.yml
  slug: cloudsight-mcpyml
modified: '2026-08-09'
name: CloudSight
nav: Providers
network: true
overview: 'CloudSight publishes 1 API on the [APIs.io](https://apis.io/) network: Images API. Tagged areas include Company, Artificial Intelligence, Machine Learning, Computer Vision, and Image Recognition.


  CloudSight''s developer surface includes documentation, support, authentication, code examples, changelog, sandbox, and 18 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 35.6
  delta: -7.9
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 16.7
    contract_quality: 58.7
    developer_ergonomics: 32.7
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudsight/refs/heads/main/screenshots/cloudsight-2026-08-17T080822.png
security:
- kind: authentication
  name: Cloudsight Authentication
  slug: cloudsight-authentication
  summary_line: apiKey/oauth1 · 2 schemes
- kind: domain-security
  name: Cloudsight Domain Security
  slug: cloudsight-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cloudsight
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Computer Vision
- Image Recognition
- Image Captioning
- Classification
- Media
website: https://cloudsight.ai
---
