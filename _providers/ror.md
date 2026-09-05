---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
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
  score: 15.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The ROR REST API provides programmatic access to the Research Organization Registry, enabling users to retrieve, search, filter, and match organization records by name, identifier, affiliation text, o
  name: ROR REST API
  slug: ror-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ror-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ror.org/
- group: docs
  title: ''
  type: Documentation
  url: https://ror.readme.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ror-community
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ror-research-organization-registry
- group: company
  title: ''
  type: Blog
  url: https://ror.org/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://ror.org/api-client-id
- group: operate
  title: ''
  type: StatusPage
  url: https://ror1.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/ResearchOrgs
- group: commercial
  title: ''
  type: Plans
  url: plans/ror-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ror-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ror-finops.yml
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/ror-context.jsonld
created: '2026-06-12'
description: ROR (Research Organization Registry) is a global, community-led, curated registry of open persistent identifiers for research organizations. It provides unique, stable identifiers (ROR IDs) for over 120,000 universities, companies, government labs, nonprofits, and other organizations involved in scholarly research. The registry is maintained collaboratively by California Digital Library, Crossref, and DataCite, with all data available under the CC0 license. ROR offers a free REST API for querying, searching, and retrieving organization records, and is integrated as the preferred organization identifier across Crossref, DataCite, and ORCID platforms.
finops:
- name: Ror Finops
  service_category: ''
  slug: ror-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ror.png
jsonld:
- class_count: 8
  name: Ror Context
  property_count: 19
  slug: ror-context
layout: provider
modified: '2026-06-12'
name: ROR
nav: Providers
network: true
overview: 'ROR publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Research, Organization, Identifiers, Registry, and Scholarly.


  The ROR catalog on APIs.io includes 1 JSON-LD context.


  ROR''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Ror Plans Pricing
  plan_count: 2
  slug: ror-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Ror Rate Limits
  slug: ror-rate-limits
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 71.0
    catalog_earned_first_party: 0.0
    catalog_gap: 44.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 41.3
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 65.8
  previous_composite: 34.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ror/refs/heads/main/screenshots/ror-2026-06-20T193222.png
security:
- kind: domain-security
  name: Ror Domain Security
  slug: ror-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ror
tags:
- Research
- Organization
- Identifiers
- Registry
- Scholarly
- Open Data
- Persistent Identifiers
website: https://ror.org/
---
