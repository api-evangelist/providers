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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Orakl Agentic Access
  operation_count: 11
  slug: orakl-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 9
apis:
- description: Resource 'CommonContent' operations.
  name: Orakl CommonContent API
  slug: orakl-commoncontent-api
- description: CustomForms describe each node structure family, They are mandatory before creating any Node.
  name: Orakl CustomForm API
  slug: orakl-customform-api
- description: Folders entity represent a directory on server with datetime and naming.
  name: Orakl Folder API
  slug: orakl-folder-api
- description: The Login Check API from Orakl — 1 operation(s) for login check.
  name: Orakl Login Check API
  slug: orakl-login-check-api
- description: NodesSources store Node content according to a translation and a NodeType.
  name: Orakl NodesSources API
  slug: orakl-nodessources-api
- description: Page node-source entity.
  name: Orakl Page API
  slug: orakl-page-api
- description: Tags are hierarchical entities used to qualify Nodes.
  name: Orakl Tag API
  slug: orakl-tag-api
- description: Translations describe language locales to be used by Nodes, Tags, UrlAliases and Documents.
  name: Orakl Translation API
  slug: orakl-translation-api
- description: Resource 'WebResponse' operations.
  name: Orakl WebResponse API
  slug: orakl-webresponse-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orakl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.orakl-oncology.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.orakl-oncology.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.orakl-oncology.com/api/docs.jsonld
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orakl-oncology.com/legals
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orakl-oncology.com/legals
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orakloncology/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orakl-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orakl-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/orakl-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/orakl-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orakl-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Orakl Oncology is a Paris-based TechBio company, a spin-off from the Gustave Roussy cancer institute, building an AI-powered drug-development platform that combines one of the largest biobanks of patient tumor avatars (organoids) with deep clinical and omics data and machine learning to predict how individual patients will respond to new cancer drug candidates. Its commercial products O-Predict and O-Validate deliver actionable response predictions to drug developers across clinical trials. This API Evangelist profile documents the public website API (an API Platform / Roadiz headless-CMS Hydra + JSON-LD surface with JWT authentication) that powers orakl-oncology.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orakl.png
layout: provider
mcp_servers:
- description: ''
  name: orakl-mcp.yml
  slug: orakl-mcpyml
modified: '2026-07-20'
name: Orakl
nav: Providers
network: true
overview: 'Orakl publishes 9 APIs on the [APIs.io](https://apis.io/) network, including CommonContent API, CustomForm API, Folder API, and 6 more. Tagged areas include Company, TechBio, Oncology, Drug Development, and Artificial Intelligence.


  Orakl''s developer surface includes documentation, API reference, authentication, and 10 more developer resources.'
random_paper: 51
score:
  band: thin
  composite: 33.4
  delta: -4.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 56.4
    developer_ergonomics: 29.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Orakl Authentication
  slug: orakl-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Orakl Domain Security
  slug: orakl-domain-security
  summary_line: TLSv1.3 · HSTS
slug: orakl
tags:
- Company
- TechBio
- Oncology
- Drug Development
- Artificial Intelligence
- Machine Learning
- Healthcare
- Biotechnology
- Precision Medicine
- Cancer Research
- Content Management
- JSON-LD
website: https://www.orakl-oncology.com/
---
