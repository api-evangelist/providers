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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Colab Agentic Access
  operation_count: 8
  slug: google-colab-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 1
apis:
- description: Google Colab provides internal APIs for managing notebook runtimes and kernels, including connecting to hosted runtimes, local runtimes, and custom GCE VM backends. The runtime API handles kernel life
  name: Colab Runtime and Kernel Management
  slug: colab-runtime-and-kernel-management
- description: The Colab Enterprise API on Google Cloud provides managed notebook runtimes integrated with Vertex AI. It enables creating and managing notebook execution schedules, runtime templates, and managed run
  name: Colab Enterprise API
  slug: colab-enterprise-api
- description: Notebook file operations
  name: Google Colab Files API
  slug: google-colab-files-api
- description: Sharing and access control
  name: Google Colab Permissions API
  slug: google-colab-permissions-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Colab Notebooks via Drive API
  slug: open-colab-drive
- collection_type: open
  name: Google Colab Notebooks via Drive Files API
  slug: open-google-colab-files-api
- collection_type: open
  name: Google Colab Notebooks via Drive Files Permissions API
  slug: open-google-colab-permissions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-colab-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-colab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-colab-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-colab-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-colab-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googlecolab
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/google-colab
- group: start
  title: ''
  type: GettingStarted
  url: https://colab.research.google.com/notebooks/welcome.ipynb
- group: commercial
  title: ''
  type: Pricing
  url: https://colab.research.google.com/signup
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/drive/api/guides/about-auth
- group: operate
  title: ''
  type: Support
  url: https://research.google.com/colaboratory/faq.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-colab-context.jsonld
created: '2026-03-13'
description: Google Colab (Colaboratory) is a hosted Jupyter notebook environment that provides free access to computing resources including GPUs and TPUs, with APIs for managing notebooks, runtimes, and integration with Google Drive for collaborative data science and machine learning workflows.
finops:
- name: Google Colab Finops
  service_category: Notebook / ML Compute
  slug: google-colab-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-colab.png
json_schemas:
- name: Google Colab Notebook
  property_count: 4
  slug: google-colab-notebook
jsonld:
- class_count: 0
  name: Google Colab Context
  property_count: 4
  slug: google-colab-context
layout: provider
modified: '2026-05-19'
name: Google Colab
nav: Providers
network: true
overview: 'Google Colab publishes 2 APIs on the [APIs.io](https://apis.io/) network: Files API and Permissions API. Tagged areas include Collaboration, Data Science, Google Cloud, Jupyter, and Machine-Learning.


  The Google Colab catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Colab''s developer surface includes authentication, getting-started guide, pricing, support, and 9 more developer resources.'
plans:
- name: Google Colab Plans Pricing
  plan_count: 5
  slug: google-colab-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 7
  name: Google Colab Rate Limits
  slug: google-colab-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Colab API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: google-colab-jsonschema-spectral-rules
scopes:
- name: Google Colab Scopes
  scope_count: 2
  slug: google-colab-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 66.7
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-colab/refs/heads/main/screenshots/google-colab-2026-06-20T182152.png
security:
- kind: authentication
  name: Google Colab Authentication
  slug: google-colab-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Colab Domain Security
  slug: google-colab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Colab Vulnerability Disclosure
  slug: google-colab-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-colab
tags:
- Collaboration
- Data Science
- Google Cloud
- Jupyter
- Machine-Learning
- Notebooks
- Python
---
