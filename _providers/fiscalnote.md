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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fiscalnote Agentic Access
  operation_count: 26
  slug: fiscalnote-agentic-access
  summary_line: 26 operations
api_count: 4
apis:
- description: Access legislation and bill data from federal, state, and international jurisdictions.
  name: FiscalNote Bills API
  slug: fiscalnote-bills-api
- description: Access legislative committee records including membership and jurisdiction information.
  name: FiscalNote Committees API
  slug: fiscalnote-committees-api
- description: Manage and retrieve organizational issues for tracking policy topics and legislative priorities.
  name: FiscalNote Issues API
  slug: fiscalnote-issues-api
- description: Manage and retrieve labels used to categorize and organize legislation and policy items.
  name: FiscalNote Labels API
  slug: fiscalnote-labels-api
- description: Access legislative data spanning Congress, all 50 U.S. states, and international jurisdictions.
  name: FiscalNote Legislation API
  slug: fiscalnote-legislation-api
- description: Access legislator-specific data including voting records, sponsored legislation, and committee memberships.
  name: FiscalNote Legislators API
  slug: fiscalnote-legislators-api
- description: Access government official profiles including legislators, executives, and appointees.
  name: FiscalNote Officials API
  slug: fiscalnote-officials-api
- description: Access government organization records including agencies, departments, and independent bodies.
  name: FiscalNote Organizations API
  slug: fiscalnote-organizations-api
- description: Access AI-powered policy analysis, impact summaries, and monitoring signals for policy changes.
  name: FiscalNote Policy Intelligence API
  slug: fiscalnote-policy-intelligence-api
- description: Access the real-time presidential transcript feed delivering primary-source transcripts of presidential communications.
  name: FiscalNote Presidential Transcripts API
  slug: fiscalnote-presidential-transcripts-api
- description: Access regulatory data including proposed and final rules across federal and state agencies.
  name: FiscalNote Regulations API
  slug: fiscalnote-regulations-api
- description: Access regulatory documents including proposed rules, final rules, and notices from government agencies.
  name: FiscalNote Regulatory Documents API
  slug: fiscalnote-regulatory-documents-api
- description: Access stakeholder intelligence including government officials and organizational relationships.
  name: FiscalNote Stakeholders API
  slug: fiscalnote-stakeholders-api
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FiscalNote AppData API
  slug: open-fiscalnote-appdata
- collection_type: open
  name: FiscalNote AppData Bills API
  slug: open-fiscalnote-bills-api
- collection_type: open
  name: FiscalNote AppData Bills Committees API
  slug: open-fiscalnote-committees-api
- collection_type: open
  name: FiscalNote AppData Bills Issues API
  slug: open-fiscalnote-issues-api
- collection_type: open
  name: FiscalNote AppData Bills Labels API
  slug: open-fiscalnote-labels-api
- collection_type: open
  name: FiscalNote AppData Bills Legislation API
  slug: open-fiscalnote-legislation-api
- collection_type: open
  name: FiscalNote AppData Bills Legislators API
  slug: open-fiscalnote-legislators-api
- collection_type: open
  name: FiscalNote AppData Bills Officials API
  slug: open-fiscalnote-officials-api
- collection_type: open
  name: FiscalNote Organization API
  slug: open-fiscalnote-organization
- collection_type: open
  name: FiscalNote AppData Bills Organizations API
  slug: open-fiscalnote-organizations-api
- collection_type: open
  name: FiscalNote People API
  slug: open-fiscalnote-people
- collection_type: open
  name: FiscalNote AppData Bills Policy Intelligence API
  slug: open-fiscalnote-policy-intelligence-api
- collection_type: open
  name: FiscalNote PolicyNote API
  slug: open-fiscalnote-policynote
- collection_type: open
  name: FiscalNote AppData Bills Presidential Transcripts API
  slug: open-fiscalnote-presidential-transcripts-api
- collection_type: open
  name: FiscalNote AppData Bills Regulations API
  slug: open-fiscalnote-regulations-api
- collection_type: open
  name: FiscalNote AppData Bills Regulatory Documents API
  slug: open-fiscalnote-regulatory-documents-api
- collection_type: open
  name: FiscalNote AppData Bills Stakeholders API
  slug: open-fiscalnote-stakeholders-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fiscalnote-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fiscalnote-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fiscalnote-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FiscalNote
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fiscalnote
- group: company
  title: ''
  type: Website
  url: https://fiscalnote.com/
- group: start
  title: ''
  type: Portal
  url: https://apidocs.fiscalnote.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.fiscalnote.com/apis
- group: company
  title: ''
  type: Blog
  url: https://fiscalnote.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fiscalnote.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fiscalnote.com/terms
- group: start
  title: ''
  type: Login
  url: https://app.fiscalnote.com/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/fiscalnote-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fiscalnote-legislation-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fiscalnote-official-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fiscalnote-transcript-schema.json
created: '2026-03-24'
description: FiscalNote is a policy intelligence platform that provides legislative, regulatory, and stakeholder data spanning Congress, all 50 U.S. states, and more than 100 countries. FiscalNote expanded its PolicyNote API to eliminate AI hallucinations in compliance workflows by providing primary-source verified policy data.
finops:
- name: Fiscalnote Finops
  service_category: Government / Policy Intelligence
  slug: fiscalnote-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fiscalnote.png
json_schemas:
- name: FiscalNote Legislation
  property_count: 19
  slug: fiscalnote-legislation
- name: FiscalNote Government Official
  property_count: 23
  slug: fiscalnote-official
- name: FiscalNote Presidential Transcript
  property_count: 14
  slug: fiscalnote-transcript
jsonld:
- class_count: 0
  name: Fiscalnote Context
  property_count: 5
  slug: fiscalnote-context
layout: provider
modified: '2026-05-19'
name: FiscalNote
nav: Providers
network: true
overview: 'FiscalNote publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Bills API, Committees API, Issues API, and 10 more. Tagged areas include Government, Legislation, Policy, Political Intelligence, and Regulations.


  The FiscalNote catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FiscalNote''s developer surface includes authentication, developer portal, documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Fiscalnote Plans Pricing
  plan_count: 4
  slug: fiscalnote-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Fiscalnote Rate Limits
  slug: fiscalnote-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: FiscalNote API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: fiscalnote-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 13
    catalog_gap: 58.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 9.8
    contract_quality: 58.2
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fiscalnote/refs/heads/main/screenshots/fiscalnote-2026-06-20T181249.png
security:
- kind: authentication
  name: Fiscalnote Authentication
  slug: fiscalnote-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fiscalnote Domain Security
  slug: fiscalnote-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fiscalnote
tags:
- Government
- Legislation
- Policy
- Political Intelligence
- Regulations
website: https://fiscalnote.com/
---
