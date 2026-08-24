---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Crossref Agentic Access
  operation_count: 18
  slug: crossref-agentic-access
  summary_line: 18 operations
api_count: 8
apis:
- description: The Agency API from Crossref — 1 operation(s) for agency.
  name: Crossref Agency API
  slug: crossref-agency-api
- description: Endpoints that expose funder related data
  name: Crossref Funders API
  slug: crossref-funders-api
- description: Endpoints that expose journal related data
  name: Crossref Journals API
  slug: crossref-journals-api
- description: Endpoints that expose license related data
  name: Crossref Licenses API
  slug: crossref-licenses-api
- description: Endpoints that expose member related data
  name: Crossref Members API
  slug: crossref-members-api
- description: Endpoints that expose prefix related data
  name: Crossref Prefixes API
  slug: crossref-prefixes-api
- description: Endpoints that expose type related data
  name: Crossref Types API
  slug: crossref-types-api
- description: Endpoints that expose works related data
  name: Crossref Works API
  slug: crossref-works-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Crossref Agency API
  slug: open-crossref-agency-api
- collection_type: open
  name: Crossref Agency Funders API
  slug: open-crossref-funders-api
- collection_type: open
  name: Crossref Agency Journals API
  slug: open-crossref-journals-api
- collection_type: open
  name: Crossref Agency Licenses API
  slug: open-crossref-licenses-api
- collection_type: open
  name: Crossref Agency Members API
  slug: open-crossref-members-api
- collection_type: open
  name: Crossref Agency Prefixes API
  slug: open-crossref-prefixes-api
- collection_type: open
  name: Crossref Agency Types API
  slug: open-crossref-types-api
- collection_type: open
  name: Crossref Agency Works API
  slug: open-crossref-works-api
- collection_type: open
  name: Crossref
  slug: open-crossref
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crossref-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crossref-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crossref-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crossref
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/crossref-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/crossref-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/crossref-work-schema.json
- group: company
  title: ''
  type: Website
  url: https://www.crossref.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.crossref.org/documentation/
- group: docs
  title: ''
  type: APIDocumentation
  url: https://www.crossref.org/documentation/retrieve-metadata/rest-api/
- group: company
  title: ''
  type: Blog
  url: https://www.crossref.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CrossRef
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crossref.org/
- group: operate
  title: ''
  type: Community
  url: https://community.crossref.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crossref.org/operations-and-sustainability/terms/
created: '2024-07-02'
description: Crossref is a non-profit organization that provides digital infrastructure for scholarly communications. Best known for Digital Object Identifier (DOI) registration, Crossref also operates a public REST API offering searchable, filterable access to metadata for tens of millions of scholarly works, journals, members, funders, prefixes, types, licenses, and DOI registration agency information. The Crossref REST API supports free-form queries, field queries, filters, facets, deep-paging cursors, and selection of specific elements, and is used by reference managers, repositories, discovery layers, and analytics platforms.
finops:
- name: Crossref Finops
  service_category: API
  slug: crossref-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crossref.png
json_schemas:
- name: Crossref Work
  property_count: 38
  slug: crossref-work
jsonld:
- class_count: 36
  name: Crossref Context
  property_count: 12
  slug: crossref-context
layout: provider
modified: '2026-05-19'
name: Crossref
nav: Providers
network: true
overview: 'Crossref publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Agency API, Funders API, Journals API, and 5 more. Tagged areas include Citations, DOI, Funders, Identifiers, and Journals.


  The Crossref catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Crossref''s developer surface includes documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Crossref Plans Pricing
  plan_count: 3
  slug: crossref-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Crossref Rate Limits
  slug: crossref-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Crossref API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: crossref-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Crossref API Rules
  rule_count: 6
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 1
  slug: crossref-rules
score:
  band: thin
  composite: 32.5
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 53.3
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crossref/refs/heads/main/screenshots/crossref-2026-06-20T175248.png
security:
- kind: domain-security
  name: Crossref Domain Security
  slug: crossref-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Crossref Vulnerability Disclosure
  slug: crossref-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crossref
tags:
- Citations
- DOI
- Funders
- Identifiers
- Journals
- Licenses
- Members
- Metadata
- Open Access
- ORCID
- Prefixes
- Publishers
- Reference Linking
- ROR
- Scholarly
website: https://www.crossref.org/
---
