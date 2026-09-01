---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
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
  score: 30.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Formassembly Agentic Access
  operation_count: 25
  slug: formassembly-agentic-access
  summary_line: 25 operations · 14 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Manage aggregated statistics and counters for forms
  name: FormAssembly Aggregates API
  slug: formassembly-aggregates-api
- description: Manage integrations (Salesforce, etc.) attached to forms
  name: FormAssembly Connectors API
  slug: formassembly-connectors-api
- description: Manage custom reusable form element types
  name: FormAssembly Form Elements API
  slug: formassembly-form-elements-api
- description: Create, read, update, and delete form definitions
  name: FormAssembly Forms API
  slug: formassembly-forms-api
- description: OAuth2 authorization code flow for obtaining access tokens
  name: FormAssembly OAuth2 API
  slug: formassembly-oauth2-api
- description: Export and manage form submission responses
  name: FormAssembly Responses API
  slug: formassembly-responses-api
- description: Manage CSS themes applied to forms
  name: FormAssembly Themes API
  slug: formassembly-themes-api
artifact_total: 41
collections:
- collection_type: postman
  name: FormAssembly REST Admin API
  slug: postman-formassembly-admin-api
- collection_type: postman
  name: FormAssembly REST Admin Aggregates API
  slug: postman-formassembly-aggregates-api
- collection_type: postman
  name: FormAssembly REST Admin Connectors API
  slug: postman-formassembly-connectors-api
- collection_type: postman
  name: FormAssembly REST Admin Form Elements API
  slug: postman-formassembly-form-elements-api
- collection_type: postman
  name: FormAssembly REST Admin Forms API
  slug: postman-formassembly-forms-api
- collection_type: postman
  name: FormAssembly REST Admin OAuth2 API
  slug: postman-formassembly-oauth2-api
- collection_type: postman
  name: FormAssembly REST Admin Responses API
  slug: postman-formassembly-responses-api
- collection_type: postman
  name: FormAssembly REST Admin Themes API
  slug: postman-formassembly-themes-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FormAssembly REST Admin API
  slug: open-formassembly-admin-api
- collection_type: open
  name: FormAssembly REST Admin Aggregates API
  slug: open-formassembly-aggregates-api
- collection_type: open
  name: FormAssembly REST Admin Connectors API
  slug: open-formassembly-connectors-api
- collection_type: open
  name: FormAssembly REST Admin Form Elements API
  slug: open-formassembly-form-elements-api
- collection_type: open
  name: FormAssembly REST Admin Forms API
  slug: open-formassembly-forms-api
- collection_type: open
  name: FormAssembly REST Admin OAuth2 API
  slug: open-formassembly-oauth2-api
- collection_type: open
  name: FormAssembly REST Admin Responses API
  slug: open-formassembly-responses-api
- collection_type: open
  name: FormAssembly REST Admin Themes API
  slug: open-formassembly-themes-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/formassembly/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/formassembly-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/formassembly-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/formassembly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/formassembly-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/formassembly-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.formassembly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.formassembly.com/help/working-with-the-formassembly-api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/formassembly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/formassembly
- group: company
  title: ''
  type: Blog
  url: https://www.formassembly.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.formassembly.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.formassembly.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/FormAssembly
- group: commercial
  title: ''
  type: Plans
  url: plans/formassembly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/formassembly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/formassembly-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/formassembly-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/formassembly-context.jsonld
created: 2026-06-13
description: FormAssembly is an enterprise form and data collection platform with a REST API for managing forms, exporting submission data, handling Salesforce integrations, and building compliant data collection workflows. The API supports OAuth2 authentication and enables programmatic access to forms, responses, themes, connectors, and account components across cloud, enterprise, and government deployment environments.
examples:
- key_count: 7
  name: Formassembly Connector Example
  slug: formassembly-connector-example
- key_count: 5
  name: Formassembly Form Example
  slug: formassembly-form-example
- key_count: 1
  name: Formassembly Response Export Example
  slug: formassembly-response-export-example
finops:
- name: Formassembly Finops
  service_category: ''
  slug: formassembly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/formassembly.png
json_schemas:
- name: FormAssembly Connector
  property_count: 7
  slug: formassembly-connector
- name: FormAssembly Form
  property_count: 5
  slug: formassembly-form
- name: FormAssembly Response
  property_count: 4
  slug: formassembly-response
- name: FormAssembly Theme
  property_count: 3
  slug: formassembly-theme
jsonld:
- class_count: 10
  name: Formassembly Context
  property_count: 34
  slug: formassembly-context
layout: provider
modified: 2026-06-13
name: FormAssembly
nav: Providers
network: true
overview: 'FormAssembly publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Aggregates API, Connectors API, Form Elements API, and 4 more. Tagged areas include Forms, Data Collection, Salesforce, Enterprise, and HIPAA.


  The FormAssembly catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FormAssembly''s developer surface includes authentication, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Formassembly Plans Pricing
  plan_count: 4
  slug: formassembly-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Formassembly Rate Limits
  slug: formassembly-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: FormAssembly API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: formassembly-jsonschema-spectral-rules
scopes:
- name: Formassembly Scopes
  scope_count: 0
  slug: formassembly-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 31.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 60.1
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 52.6
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 59.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/formassembly/refs/heads/main/screenshots/formassembly-2026-06-20T181430.png
security:
- kind: authentication
  name: Formassembly Authentication
  slug: formassembly-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Formassembly Domain Security
  slug: formassembly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Formassembly Trust Center
  slug: formassembly-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP, GDPR
slug: formassembly
tags:
- Forms
- Data Collection
- Salesforce
- Enterprise
- HIPAA
- Compliance
- Government
- FedRAMP
- Workflows
- E-Signatures
website: https://www.formassembly.com/
---
