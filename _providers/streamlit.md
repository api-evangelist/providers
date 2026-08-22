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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Streamlit Agentic Access
  operation_count: 8
  slug: streamlit-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 4
apis:
- description: 'The Streamlit Python library API provides a rich set of functions for building interactive data applications. Organized by activity type: display data (st.write, st.dataframe, st.table), input widgets'
  name: Streamlit Python API
  slug: streamlit-python-api
- description: Manage Streamlit applications deployed on Community Cloud. Deploy, list, restart, and delete apps connected to GitHub repositories.
  name: Streamlit Apps API
  slug: streamlit-apps-api
- description: Manage secrets for Streamlit applications. Secrets are environment variables securely injected into the application at runtime via st.secrets.
  name: Streamlit Secrets API
  slug: streamlit-secrets-api
- description: Manage Streamlit Community Cloud workspaces and their settings.
  name: Streamlit Workspaces API
  slug: streamlit-workspaces-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Streamlit Community Cloud Apps API
  slug: open-streamlit-apps-api
- collection_type: open
  name: Streamlit Community Cloud API
  slug: open-streamlit-cloud
- collection_type: open
  name: Streamlit Community Cloud Apps Secrets API
  slug: open-streamlit-secrets-api
- collection_type: open
  name: Streamlit Community Cloud Apps Workspaces API
  slug: open-streamlit-workspaces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/streamlit-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/streamlit-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/streamlit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/streamlit-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/streamlit
- group: company
  title: ''
  type: Website
  url: https://streamlit.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.streamlit.io
- group: build
  title: ''
  type: GitHub
  url: https://github.com/streamlit/streamlit
- group: operate
  title: ''
  type: Forums
  url: https://discuss.streamlit.io
- group: company
  title: ''
  type: Blog
  url: https://blog.streamlit.io
- group: other
  title: ''
  type: Gallery
  url: https://streamlit.io/gallery
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.streamlit.io/develop/quick-reference/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://streamlit.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://streamlit.io/privacy-policy
- group: start
  title: ''
  type: Signup
  url: https://share.streamlit.io/signup
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/streamlit/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/streamlit/refs/heads/main/openapi/streamlit-cloud-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/streamlit/refs/heads/main/json-schema/streamlit-app-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/streamlit/refs/heads/main/json-ld/streamlit-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.streamlit.io/llms.txt
created: '2025-02-12'
description: Streamlit is an open-source Python framework that makes it easy to build and share beautiful, custom web apps for machine learning and data science. With Streamlit, you can turn data scripts into shareable web applications in minutes without needing front-end experience. Streamlit Community Cloud provides free hosting for Streamlit apps directly from GitHub repositories. The framework offers a Python API for displaying data, creating interactive widgets, caching computation, and connecting to databases and APIs.
examples:
- key_count: 2
  name: Streamlit Deploy App Example
  slug: streamlit-deploy-app-example
- key_count: 2
  name: Streamlit List Apps Example
  slug: streamlit-list-apps-example
finops:
- name: Streamlit Finops
  service_category: API
  slug: streamlit-finops
image: https://streamlit.io/images/brand/streamlit-mark-color.png
json_schemas:
- name: Streamlit Community Cloud App
  property_count: 10
  slug: streamlit-app
json_structures:
- name: Streamlit App Structure
  property_count: 0
  slug: streamlit-app-structure
jsonld:
- class_count: 0
  name: Streamlit Context
  property_count: 2
  slug: streamlit-context
layout: provider
modified: '2026-05-19'
name: Streamlit
nav: Providers
network: true
overview: 'Streamlit publishes 3 APIs on the [APIs.io](https://apis.io/) network: Apps API, Secrets API, and Workspaces API. Tagged areas include Data Science, Machine Learning, Open Source, Python, and Web Applications.


  The Streamlit catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Streamlit''s developer surface includes authentication, documentation, GitHub presence, engineering blog, changelog, signup flow, and 14 more developer resources.'
plans:
- name: Streamlit Plans Pricing
  plan_count: 3
  slug: streamlit-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Streamlit Rate Limits
  slug: streamlit-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Streamlit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: streamlit-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Streamlit API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: streamlit-rules
score:
  band: developing
  composite: 45.0
  delta: -6.4
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 62.2
    developer_ergonomics: 28.6
    discoverability: 72.2
    governance: 9.8
    operational_transparency: 28.9
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/streamlit/refs/heads/main/screenshots/streamlit-2026-06-20T194618.png
security:
- kind: authentication
  name: Streamlit Authentication
  slug: streamlit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Streamlit Domain Security
  slug: streamlit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Streamlit Trust Center
  slug: streamlit-trust-center
  summary_line: SOC 2, ISO 27001
slug: streamlit
tags:
- Data Science
- Machine Learning
- Open Source
- Python
- Web Applications
website: https://streamlit.io
---
