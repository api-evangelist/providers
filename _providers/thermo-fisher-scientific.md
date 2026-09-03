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
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Thermo Fisher Scientific Agentic Access
  operation_count: 15
  slug: thermo-fisher-scientific-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 2
apis:
- description: The Thermo Fisher Connect Platform OData API provides standards-based interoperability for laboratory data management, enabling integration between instruments, LIMS, ELN, and enterprise systems throu
  name: Thermo Fisher Connect Platform OData API
  slug: connect-platform
- baseURL: https://{your-server}:{port}/smpwcfrestvgsm
  baseurl_source: declared
  description: Token-based authentication operations.
  name: Thermo Fisher Scientific Authentication API
  slug: thermo-fisher-scientific-authentication-api
- baseURL: https://{your-server}:{port}/smpwcfrestvgsm
  baseurl_source: declared
  description: Browse entity data from SampleManager.
  name: Thermo Fisher Scientific Entities API
  slug: thermo-fisher-scientific-entities-api
- baseURL: https://{your-server}:{port}/smpwcfrestvgsm
  baseurl_source: declared
  description: Data export operations.
  name: Thermo Fisher Scientific Export API
  slug: thermo-fisher-scientific-export-api
- baseURL: https://{your-server}:{port}/smpwcfrestvgsm
  baseurl_source: declared
  description: Instrument status and control.
  name: Thermo Fisher Scientific Instrument API
  slug: thermo-fisher-scientific-instrument-api
- baseURL: https://{your-server}:{port}/smpwcfrestvgsm
  baseurl_source: declared
  description: Sample measurements and spectra.
  name: Thermo Fisher Scientific Measurements API
  slug: thermo-fisher-scientific-measurements-api
- baseURL: https://{your-server}:{port}/smpwcfrestvgsm
  baseurl_source: declared
  description: Measurement method configuration.
  name: Thermo Fisher Scientific Methods API
  slug: thermo-fisher-scientific-methods-api
- baseURL: https://{your-server}:{port}/smpwcfrestvgsm
  baseurl_source: declared
  description: Access test results and measurements.
  name: Thermo Fisher Scientific Results API
  slug: thermo-fisher-scientific-results-api
- baseURL: https://{your-server}:{port}/smpwcfrestvgsm
  baseurl_source: declared
  description: Access and manage laboratory samples.
  name: Thermo Fisher Scientific Samples API
  slug: thermo-fisher-scientific-samples-api
- baseURL: https://{your-server}:{port}/smpwcfrestvgsm
  baseurl_source: declared
  description: Trigger and manage laboratory workflows.
  name: Thermo Fisher Scientific Workflows API
  slug: thermo-fisher-scientific-workflows-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Thermo Fisher NanoDrop Ultra Web API
  slug: open-thermo-fisher-nanodrop
- collection_type: open
  name: Thermo Fisher SampleManager LIMS REST API
  slug: open-thermo-fisher-samplemanager
- collection_type: open
  name: Thermo Fisher NanoDrop Ultra Web Authentication API
  slug: open-thermo-fisher-scientific-authentication-api
- collection_type: open
  name: Thermo Fisher NanoDrop Ultra Web Authentication Entities API
  slug: open-thermo-fisher-scientific-entities-api
- collection_type: open
  name: Thermo Fisher NanoDrop Ultra Web Authentication Export API
  slug: open-thermo-fisher-scientific-export-api
- collection_type: open
  name: Thermo Fisher NanoDrop Ultra Web Authentication Instrument API
  slug: open-thermo-fisher-scientific-instrument-api
- collection_type: open
  name: Thermo Fisher NanoDrop Ultra Web Authentication Measurements API
  slug: open-thermo-fisher-scientific-measurements-api
- collection_type: open
  name: Thermo Fisher NanoDrop Ultra Web Authentication Methods API
  slug: open-thermo-fisher-scientific-methods-api
- collection_type: open
  name: Thermo Fisher NanoDrop Ultra Web Authentication Results API
  slug: open-thermo-fisher-scientific-results-api
- collection_type: open
  name: Thermo Fisher NanoDrop Ultra Web Authentication Samples API
  slug: open-thermo-fisher-scientific-samples-api
- collection_type: open
  name: Thermo Fisher NanoDrop Ultra Web Authentication Workflows API
  slug: open-thermo-fisher-scientific-workflows-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/thermo-fisher-scientific-capability-edges.yml
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


  Thermo Fisher Scientific''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
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
random_paper: 7
rate_limits:
- limit_count: 1
  name: Thermo Fisher Scientific Rate Limits
  slug: thermo-fisher-scientific-rate-limits
rules:
- effective_rule_count: 9
  extends: []
  name: Thermo Fisher Scientific API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 6
  slug: thermo-fisher-rules
- effective_rule_count: 5
  extends: []
  name: Thermo Fisher Scientific API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: thermo-fisher-scientific-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 39.4
    contract_quality: 54.4
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 39.4
    operational_transparency: 10.5
  previous_composite: 34.3
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
