---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Gene, variant and trait pages and the genome search as JSON. Public and read‑only, no key required.
  name: Dante Labs Genome Data
  slug: dante-labs-genome-data
- baseURL: https://dantelabs.com
  baseurl_source: declared
  description: 'Gene, variant and trait pages and the genome search as JSON: the facts each page shows, every link an absolute `url`. Public and read-only, with no key; any origin may read it.'
  name: Dante Labs genome data Api API
  slug: dante-labs-genome-data-api-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/dantelabs/rules/dantelabs-rules.yml
  title: ''
  type: Spectral
  url: rules/dantelabs-rules.yml
- group: design
  href: https://artifacts.apis.io/dantelabs/json-ld/dantelabs-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dantelabs-context.jsonld
- group: design
  href: https://artifacts.apis.io/dantelabs/vocabulary/dantelabs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dantelabs-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dantelabs/data-model/dantelabs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dantelabs-data-model.yml
- group: design
  href: https://artifacts.apis.io/dantelabs/errors/dantelabs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dantelabs-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dantelabs/conformance/dantelabs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dantelabs-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dantelabs/llms/dantelabs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dantelabs-llms.txt
- group: agent
  href: https://artifacts.apis.io/dantelabs/well-known/dantelabs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dantelabs-well-known.yml
- group: other
  href: https://artifacts.apis.io/dantelabs/hosts/dantelabs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dantelabs-hosts.yml
- group: other
  href: https://artifacts.apis.io/dantelabs/vendors/dantelabs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dantelabs-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dantelabs.com/terms
- group: auth
  title: ''
  type: Security
  url: https://support.dantelabs.com/enquiries/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dantelabs.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://dantelabs.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/dantelabs/security/dantelabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dantelabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dantelabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://dantelabs.com/about
- group: company
  title: ''
  type: Blog
  url: https://dantelabs.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.dantelabs.com
created: '2026-10-22'
description: Dante Labs (operating as Dantelabs) provides clinical‑grade whole genome sequencing and multi‑omics testing services. Customers can order comprehensive genomic analyses, receive detailed health reports, and access their raw data for research or clinical use. The company emphasizes privacy, HIPAA/GDPR compliance, and integrates AI‑driven insights to support proactive health management and hereditary risk assessment.
image: https://cdn.sanity.io/images/k5ybuy00/production/a1eae9fd2821fae2d259dbf16f3c5e253ae00f21-1200x630.jpg?w=1200&q=80&fm=jpg&fit=crop&h=630
json_schemas:
- name: Gene
  property_count: 3
  slug: dantelabs-gene
- name: SearchResults
  property_count: 6
  slug: dantelabs-search-results
- name: Trait
  property_count: 2
  slug: dantelabs-trait
- name: Variant
  property_count: 4
  slug: dantelabs-variant
jsonld:
- class_count: 6
  name: Dantelabs Context
  property_count: 12
  slug: dantelabs-context
layout: provider
modified: '2026-10-22'
name: Dantelabs
nav: Providers
network: true
overview: 'Dantelabs publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dante Labs genome data Api API, and 1 more. Tagged areas include Genomics, Health, DNA, Clinical Testing, and Artificial Intelligence.


  The Dantelabs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dantelabs'' developer surface includes API reference, documentation, engineering blog, support, and 15 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Dantelabs API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: dantelabs-rules
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 54.0
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dantelabs Domain Security
  slug: dantelabs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dantelabs
tags:
- Genomics
- Health
- DNA
- Clinical Testing
- Artificial Intelligence
website: https://dantelabs.com
---
