---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The Concentriq REST API exposes whole-slide images, annotations, regions of interest, users, and clinical/case data on Proscia's open, API-first digital pathology platform. Authentication is via a Con
  name: Concentriq Platform API
  slug: concentriq-platform-api
- description: 'Concentriq Embeddings is Proscia''s foundation-model API. It extracts rich visual feature vectors (embeddings) at any magnification from whole-slide images in Concentriq LS using widely used pathology '
  name: Concentriq Embeddings API
  slug: concentriq-embeddings-api
artifact_total: 5
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://proscia.com/build-on-concentriq/
- group: docs
  title: ''
  type: Documentation
  url: https://proscia.com/build-on-concentriq/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Proscia
- group: company
  title: ''
  type: Blog
  url: https://proscia.com/blog/
- group: start
  title: ''
  type: Login
  url: https://cloud.proscia.com/
- group: start
  title: ''
  type: SignUp
  url: https://proscia.com/demo
- group: operate
  title: ''
  type: Support
  url: https://supportteam.concentriq.proscia.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://proscia.com/whats-new-in-concentriq-ap/
- group: auth
  title: ''
  type: Compliance
  url: https://proscia.com/press-releases/proscia-achieves-soc-2-type-ii-certification-strengthening-enterprise-trust/
- group: auth
  title: ''
  type: Authentication
  url: authentication/proscia-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/proscia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/proscia-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/proscia-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/proscia-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/proscia-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/proscia-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/proscia-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/proscia-llms.txt
created: '2026-07-17'
description: 'Proscia is a digital pathology software company whose Concentriq platform powers AI-driven precision medicine and diagnostic pathology for clinical laboratories, pharmaceutical and biotech R&D, CROs, and academic research organizations. Concentriq is an open, API-first platform: its REST API, Custom APIs, SDK, Model Context Protocol (MCP) data backbone, Concentriq Embeddings foundation-model API, Compute service, and Analysis API let developers and data scientists manage whole-slide images, annotations, and clinical data and build next-generation pathology AI. Proscia is SOC 2 Type II, ISO 27001, and ISO 13485 certified, HIPAA- and GDPR-aligned, and ships FDA 510(k)-cleared and CE-IVDR-marked diagnostic products (Concentriq AP-Dx).'
image: https://avatars.githubusercontent.com/u/6182466?v=4
layout: provider
mcp_servers:
- description: ''
  name: proscia-mcp.yml
  slug: proscia-mcpyml
modified: '2026-07-20'
name: Proscia
nav: Providers
network: true
overview: 'Proscia publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Digital Pathology, Pathology, and Life Sciences.


  Proscia''s developer surface includes documentation, engineering blog, signup flow, support, changelog, authentication, and 12 more developer resources.'
random_paper: 42
score:
  band: emerging
  composite: 27.8
  delta: -1.7
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 29.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Proscia Authentication
  slug: proscia-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Proscia Domain Security
  slug: proscia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: proscia
tags:
- Company
- Healthcare
- Digital Pathology
- Pathology
- Life Sciences
- Precision Medicine
- Artificial Intelligence
- Medical Imaging
- Whole Slide Imaging
- Foundation Models
- Diagnostics
website: https://proscia.com/build-on-concentriq/
---
