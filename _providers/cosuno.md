---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 60
  human_in_the_loop: 0
  name: Cosuno Agentic Access
  operation_count: 107
  slug: cosuno-agentic-access
  summary_line: 107 operations · 60 acting
api_count: 1
apis:
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Awarded Bids API from Cosuno — 1 operation(s) for awarded bids.
  name: Cosuno Awarded Bids API
  slug: cosuno-awarded-bids-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Bid Package Custom Fields API from Cosuno — 2 operation(s) for bid package custom fields.
  name: Cosuno Bid Package Custom Fields API
  slug: cosuno-bid-package-custom-fields-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Bid Packages API from Cosuno — 14 operation(s) for bid packages.
  name: Cosuno Bid Packages API
  slug: cosuno-bid-packages-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Bid Requests API from Cosuno — 10 operation(s) for bid requests.
  name: Cosuno Bid Requests API
  slug: cosuno-bid-requests-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Bids API from Cosuno — 9 operation(s) for bids.
  name: Cosuno Bids API
  slug: cosuno-bids-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Company API from Cosuno — 7 operation(s) for company.
  name: Cosuno Company API
  slug: cosuno-company-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Current User API from Cosuno — 1 operation(s) for current user.
  name: Cosuno Current User API
  slug: cosuno-current-user-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Offices API from Cosuno — 2 operation(s) for offices.
  name: Cosuno Offices API
  slug: cosuno-offices-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Project Costs API from Cosuno — 2 operation(s) for project costs.
  name: Cosuno Project Costs API
  slug: cosuno-project-costs-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Project Custom Fields API from Cosuno — 2 operation(s) for project custom fields.
  name: Cosuno Project Custom Fields API
  slug: cosuno-project-custom-fields-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Projects API from Cosuno — 13 operation(s) for projects.
  name: Cosuno Projects API
  slug: cosuno-projects-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Subcontractor Custom Fields API from Cosuno — 2 operation(s) for subcontractor custom fields.
  name: Cosuno Subcontractor Custom Fields API
  slug: cosuno-subcontractor-custom-fields-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Subcontractor Reviews API from Cosuno — 2 operation(s) for subcontractor reviews.
  name: Cosuno Subcontractor Reviews API
  slug: cosuno-subcontractor-reviews-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Subcontractors API from Cosuno — 4 operation(s) for subcontractors.
  name: Cosuno Subcontractors API
  slug: cosuno-subcontractors-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Users API from Cosuno — 3 operation(s) for users.
  name: Cosuno Users API
  slug: cosuno-users-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Webhooks API from Cosuno — 2 operation(s) for webhooks.
  name: Cosuno Webhooks API
  slug: cosuno-webhooks-api
- baseURL: https://api.cosuno.com/v1
  baseurl_source: declared
  description: The Work Categories API from Cosuno — 1 operation(s) for work categories.
  name: Cosuno Work Categories API
  slug: cosuno-work-categories-api
artifact_total: 28
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/vendors/cosuno-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cosuno-vendors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/agentic-access/cosuno-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cosuno-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/rules/cosuno-rules.yml
  title: ''
  type: Spectral
  url: rules/cosuno-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/json-ld/cosuno-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cosuno-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/vocabulary/cosuno-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cosuno-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/data-model/cosuno-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cosuno-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/errors/cosuno-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cosuno-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/conformance/cosuno-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cosuno-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/llms/cosuno-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cosuno-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/well-known/cosuno-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cosuno-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/well-known/cosuno-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cosuno-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/hosts/cosuno-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cosuno-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cosuno.com/web/en/legal-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.cosuno.com/web/en/press
- group: docs
  title: ''
  type: Documentation
  url: https://help.cosuno.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/authentication/cosuno-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cosuno-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cosuno/refs/heads/main/security/cosuno-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cosuno-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cosuno.com/en
created: '2026-10-11'
description: Cosuno is an AI‑based tendering platform for the construction industry in Germany, Austria and Switzerland. It connects clients and subcontractors, offering over 4,000 private/commercial tenders per month from 600+ clients, helping contractors win jobs with AI‑assisted bid creation and delivering average cost savings of 5‑7%.
image: https://www.cosuno.com/assets/brand-logo-C5d0Dbh5.svg
json_schemas:
- name: BidPackageResponse
  property_count: 23
  slug: cosuno-bid-package-response
- name: CreateSubcontractorInput
  property_count: 25
  slug: cosuno-create-subcontractor-input
- name: ProjectResponse
  property_count: 22
  slug: cosuno-project-response
- name: SubcontractorResponse
  property_count: 29
  slug: cosuno-subcontractor-response
- name: UpdateSubcontractorInput
  property_count: 25
  slug: cosuno-update-subcontractor-input
- name: UpsertSubcontractorInput
  property_count: 27
  slug: cosuno-upsert-subcontractor-input
jsonld:
- class_count: 120
  name: Cosuno Context
  property_count: 205
  slug: cosuno-context
layout: provider
modified: '2026-10-11'
name: Cosuno
nav: Providers
network: true
overview: 'Cosuno publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Awarded Bids API, Bid Package Custom Fields API, Bid Packages API, and 14 more. Tagged areas include Construction, Marketplace, Artificial Intelligence, Tendering, and Germany.


  The Cosuno catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cosuno''s developer surface includes documentation, authentication, and 17 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Cosuno API Rules
  rule_count: 16
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 0
  slug: cosuno-rules
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 19.7
    contract_quality: 66.5
    developer_ergonomics: 23.2
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Cosuno Authentication
  slug: cosuno-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cosuno Domain Security
  slug: cosuno-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cosuno
tags:
- Construction
- Marketplace
- Artificial Intelligence
- Tendering
- Germany
website: https://www.cosuno.com/en
---
