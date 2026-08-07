---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Thermo Fisher Scientific Agentic Access
  operation_count: 15
  slug: thermo-fisher-scientific-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 10
apis:
- description: The Thermo Fisher Connect Platform OData API provides standards-based interoperability for laboratory data management, enabling integration between instruments, LIMS, ELN, and enterprise systems throu
  name: Thermo Fisher Connect Platform OData API
  slug: connect-platform
- description: Token-based authentication operations.
  name: Thermo Fisher Scientific Authentication API
  slug: thermo-fisher-scientific-authentication-api
- description: Browse entity data from SampleManager.
  name: Thermo Fisher Scientific Entities API
  slug: thermo-fisher-scientific-entities-api
- description: Data export operations.
  name: Thermo Fisher Scientific Export API
  slug: thermo-fisher-scientific-export-api
- description: Instrument status and control.
  name: Thermo Fisher Scientific Instrument API
  slug: thermo-fisher-scientific-instrument-api
- description: Sample measurements and spectra.
  name: Thermo Fisher Scientific Measurements API
  slug: thermo-fisher-scientific-measurements-api
- description: Measurement method configuration.
  name: Thermo Fisher Scientific Methods API
  slug: thermo-fisher-scientific-methods-api
- description: Access test results and measurements.
  name: Thermo Fisher Scientific Results API
  slug: thermo-fisher-scientific-results-api
- description: Access and manage laboratory samples.
  name: Thermo Fisher Scientific Samples API
  slug: thermo-fisher-scientific-samples-api
- description: Trigger and manage laboratory workflows.
  name: Thermo Fisher Scientific Workflows API
  slug: thermo-fisher-scientific-workflows-api
artifact_total: 26
collections:
- collection_type: open
  name: Thermo Fisher NanoDrop Ultra Web API
  slug: open-thermo-fisher-nanodrop
- collection_type: open
  name: Thermo Fisher SampleManager LIMS REST API
  slug: open-thermo-fisher-samplemanager
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thermo-fisher-scientific-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thermo-fisher-scientific-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thermo-fisher-scientific-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thermo-fisher-scientific
- group: company
  title: ''
  type: Website
  url: https://www.thermofisher.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.thermofisher.com/us/en/home/digital-science/thermo-fisher-connect.html
- group: company
  title: ''
  type: Blog
  url: https://www.thermofisher.com/blog/connectedlab/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thermofisher.com/blog/connectedlab/platform-for-science-developer-portal-beta/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/thermofisherlsms/iapi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thermofisherlsms
created: '2026-03-21'
description: Thermo Fisher Scientific is the world leader in serving science, providing analytical instruments, life sciences solutions, specialty diagnostics, laboratory products, and biopharma services. Developer APIs enable laboratory automation, instrument control, LIMS integration, and data management across life science workflows.
examples:
- key_count: 2
  name: Thermo Fisher Get Samples Example
  slug: thermo-fisher-get-samples-example
- key_count: 2
  name: Thermo Fisher Nanodrop Measurement Example
  slug: thermo-fisher-nanodrop-measurement-example
finops:
- name: Thermo Fisher Scientific Finops
  service_category: Life Sciences
  slug: thermo-fisher-scientific-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thermo-fisher-scientific.png
json_schemas:
- name: Thermo Fisher NanoDrop Measurement
  property_count: 13
  slug: thermo-fisher-measurement
- name: Thermo Fisher SampleManager Sample
  property_count: 10
  slug: thermo-fisher-sample
json_structures:
- name: Thermo Fisher Lims Structure
  property_count: 0
  slug: thermo-fisher-lims-structure
jsonld:
- class_count: 0
  name: Thermo Fisher Context
  property_count: 3
  slug: thermo-fisher-context
layout: provider
modified: '2026-05-19'
name: Thermo Fisher Scientific
nav: Providers
network: true
overview: 'Thermo Fisher Scientific publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Entities API, Export API, and 6 more. Tagged areas include Life Sciences, Laboratory, Scientific Instruments, LIMS, and Diagnostics.


  The Thermo Fisher Scientific catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Thermo Fisher Scientific''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Thermo Fisher Scientific Plans Pricing
  plan_count: 1
  slug: thermo-fisher-scientific-plans-pricing
press:
- date: '2026-05-25'
  title: Thermo Fisher, Lundbeck Announce New OpenAI ...
  url: https://www.appliedclinicaltrialsonline.com/view/thermo-fisher-lundbeck-announce-new-openai-partnerships-advancing-ai-drug-development
- date: '2026-05-25'
  title: Thermo Fisher's approach to AI is built on readiness ...
  url: https://www.facebook.com/thermofisher/posts/thermo-fishers-approach-to-ai-is-built-on-readiness-that-stems-from-years-of-del/873593251728102/
- date: '2026-05-25'
  title: Thermo Fisher's growing AI ecosystem aims to transform how ...
  url: https://corporate.thermofisher.com/content/tfcorpsite/us/en/index/newsroom/Our-stories/AI-ecosystem.html
- date: '2026-05-25'
  title: News Details - Investors - Thermo Fisher Scientific
  url: https://ir.thermofisher.com/investors/news-events/news/news-details/2025/Thermo-Fisher-Scientific-to-Accelerate-Life-Science-Breakthroughs-with-OpenAI/default.aspx
- date: '2026-05-25'
  title: Thermo Fisher and NVIDIA Partner to Expand AI Driven ...
  url: https://www.chromatographyonline.com/view/thermo-fisher-and-nvidia-partner-to-expand-ai-driven-laboratory-automation
random_paper: 70
rate_limits:
- limit_count: 1
  name: Thermo Fisher Scientific Rate Limits
  slug: thermo-fisher-scientific-rate-limits
rules:
- name: Thermo Fisher Scientific API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 6
  slug: thermo-fisher-rules
- name: Thermo Fisher Scientific API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: thermo-fisher-scientific-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 59.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 27.1
    operational_transparency: 26.3
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thermo-fisher-scientific/refs/heads/main/screenshots/thermo-fisher-scientific-2026-06-20T195253.png
security:
- kind: authentication
  name: Thermo Fisher Scientific Authentication
  slug: thermo-fisher-scientific-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Thermo Fisher Scientific Domain Security
  slug: thermo-fisher-scientific-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thermo-fisher-scientific
tags:
- Life Sciences
- Laboratory
- Scientific Instruments
- LIMS
- Diagnostics
- Biosciences
- Fortune 500
website: https://www.thermofisher.com
---
