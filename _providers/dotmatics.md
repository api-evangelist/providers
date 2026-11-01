---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-10-31'
api_count: 4
apis:
- description: REST, GraphQL, and JDBC APIs for the Luma Scientific Intelligence Platform, enabling data access, workflow automation, instrument integration, and scientific data management for pharma and biotech R&D
  name: Dotmatics Luma API
  slug: dotmatics-luma-api
- description: Open REST API for the Dotmatics Electronic Lab Notebook (ELN), enabling data routing to data warehouses, LIMS, BI tools, and external systems via the Integration Framework using Apache NiFi.
  name: Dotmatics ELN API
  slug: dotmatics-eln-api
- description: RESTful API layer for Dotmatics Studies, which organizes acquired screening data from HTS, HCS, and DMPK studies, enabling protocol definition, assay execution, and integration with external systems a
  name: Dotmatics Studies API
  slug: dotmatics-studies-api
- description: REST API for compound, sample, and entity registration management in Dotmatics, supporting single and batch registration, stereochemistry handling, uniqueness rules, and crosscheck workflows for chemi
  name: Dotmatics Registration API
  slug: dotmatics-registration-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/dotmatics/llms/dotmatics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dotmatics-llms.txt
- group: agent
  href: https://artifacts.apis.io/dotmatics/well-known/dotmatics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dotmatics-well-known.yml
- group: other
  href: https://artifacts.apis.io/dotmatics/hosts/dotmatics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dotmatics-hosts.yml
- group: other
  href: https://artifacts.apis.io/dotmatics/vendors/dotmatics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dotmatics-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.dotmatics.com/news
- group: auth
  href: https://artifacts.apis.io/dotmatics/security/dotmatics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dotmatics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dotmatics.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.dotmatics.com/whats-new
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/dotmatics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dotmatics/
- group: company
  title: ''
  type: Blog
  url: https://www.dotmatics.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dotmatics.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dotmatics.com
- group: other
  title: ''
  type: X
  url: https://x.com/dotmatics
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.dotmatics.com/whats-new
- group: operate
  title: ''
  type: Support
  url: https://community.dotmatics.com/Support/s/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dotmatics.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dotmatics.com/privacy-policy
- group: commercial
  href: https://artifacts.apis.io/dotmatics/plans/dotmatics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dotmatics-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/dotmatics/finops/dotmatics-finops.yml
  title: ''
  type: FinOps
  url: finops/dotmatics-finops.yml
coverage:
  checked: '2026-10-20'
  detail: docs.dotmatics.com answers with an "Unauthorized" page redirecting to a customer support site, its /mcp path is 403 and community.dotmatics.com/mcp/v1 is 401, and the previously recorded api.dotmatics.com host does not resolve in DNS.
  evidence:
  - status: 200
    url: https://docs.dotmatics.com/index.html
  - status: 401
    url: https://community.dotmatics.com/mcp/v1
  - status: 403
    url: https://docs.dotmatics.com/mcp
  reason: customer-only-docs
  state: gated
created: '2026-06-13'
description: Dotmatics is a scientific informatics platform for R&D organizations in pharma and biotech, whose API documentation is customer-only, for managing experimental data, compound and sample registrations, study definitions, screening workflows, ELN data, and instrument integration through its Luma scientific intelligence platform.
finops:
- has_sources: false
  method: generated
  name: Dotmatics Finops
  primary_unit: ''
  service_category: ''
  slug: dotmatics-finops
  template: true
graphqls:
- description: Dotmatics provides a GraphQL API as part of its Luma Scientific Intelligence Platform, alongside REST and JDBC interfaces. The GraphQL layer enables flexible, query-driven access to scientific data ma
  name: Dotmatics GraphQL API
  slug: dotmatics-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dotmatics.png
layout: provider
modified: '2026-06-13'
name: Dotmatics
nav: Providers
network: true
overview: 'Dotmatics is listed with 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Scientific Informatics, Pharma, Biotechnology, Drug Discovery, and ELN.


  Dotmatics'' developer surface includes documentation, engineering blog, pricing, changelog, support, and 15 more developer resources.'
plans:
- name: Dotmatics Plans Pricing
  plan_count: 4
  slug: dotmatics-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Dotmatics Rate Limits
  slug: dotmatics-rate-limits
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 64.3
    operational_transparency: 36.8
  previous_composite: 23.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dotmatics/dotmatics-2026-06-20T180201.png
security:
- kind: domain-security
  name: Dotmatics Domain Security
  slug: dotmatics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dotmatics
tags:
- Scientific Informatics
- Pharma
- Biotechnology
- Drug Discovery
- ELN
- LIMS
- Compound Registration
- Experimental Data
- R&D
website: https://www.dotmatics.com
---
