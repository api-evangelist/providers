---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 38
  human_in_the_loop: 2
  name: Soiloptix Agentic Access
  operation_count: 85
  slug: soiloptix-agentic-access
  summary_line: 85 operations · 38 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.soiloptix.com
  baseurl_source: declared
  description: 'Create a new analysis for a field, make changes to an existing Analysis, or view Messages and Files related to an Analysis. To submit a new Analysis, you would generally follow these steps: - **Create'
  name: SoilOptix Analyses - Billable API
  slug: soiloptix-analyses-billable-api
- baseURL: https://api.soiloptix.com
  baseurl_source: declared
  description: View general information about an Analysis and the available Models. A Model represents a soil property, such as Sand, Silt, or Clay. Exports provides a number of standard export formats for your conv
  name: SoilOptix Analyses - Read API
  slug: soiloptix-analyses-read-api
- baseURL: https://api.soiloptix.com
  baseurl_source: declared
  description: 'Follows the OAuth 2.0 Specification and adds additional forgot password functionality. New users can only be registered with a valid business invitation key. (**Tip:** Create a new Business Invite to '
  name: SoilOptix Authentication API
  slug: soiloptix-authentication-api
- baseURL: https://api.soiloptix.com
  baseurl_source: declared
  description: Distributors, Providers, and Clients are all Businesses. If you have admin access to a Business you will be able to view and modify Invitations and Customers for that business, as well as have admin a
  name: SoilOptix Businesses API
  slug: soiloptix-businesses-api
- baseURL: https://api.soiloptix.com
  baseurl_source: declared
  description: Businesses, Farms, and Fields accept a CountryId to help you filter and find your data.
  name: SoilOptix Countries API
  slug: soiloptix-countries-api
- baseURL: https://api.soiloptix.com
  baseurl_source: declared
  description: Farms are attached directly to a Business and provide a level of organization within a Business.
  name: SoilOptix Farms API
  slug: soiloptix-farms-api
- baseURL: https://api.soiloptix.com
  baseurl_source: declared
  description: 'Fields are attached directly to a Farm and provide a level of organization within a Farm. When requesting the Boundary of a Field, the Boundary of the active Analysis for this Field will be returned. '
  name: SoilOptix Fields API
  slug: soiloptix-fields-api
- baseURL: https://api.soiloptix.com
  baseurl_source: declared
  description: View and make changes to your customer profile. Businesses will show what businesses you have been granted access to along with your level of permission. Invites show the active invitations you've rec
  name: SoilOptix My Account API
  slug: soiloptix-my-account-api
- baseURL: https://api.soiloptix.com
  baseurl_source: declared
  description: The v3 - Boundaries API from SoilOptix — 2 operation(s) for v3 - boundaries.
  name: SoilOptix v3 - Boundaries API
  slug: soiloptix-v3-boundaries-api
- baseURL: https://api.soiloptix.com
  baseurl_source: declared
  description: The v3 - Customers API from SoilOptix — 3 operation(s) for v3 - customers.
  name: SoilOptix v3 - Customers API
  slug: soiloptix-v3-customers-api
- baseURL: https://api.soiloptix.com
  baseurl_source: declared
  description: The v3 - Farms API from SoilOptix — 3 operation(s) for v3 - farms.
  name: SoilOptix v3 - Farms API
  slug: soiloptix-v3-farms-api
- baseURL: https://api.soiloptix.com
  baseurl_source: declared
  description: The v3 - Fields API from SoilOptix — 3 operation(s) for v3 - fields.
  name: SoilOptix v3 - Fields API
  slug: soiloptix-v3-fields-api
- baseURL: https://api.soiloptix.com
  baseurl_source: declared
  description: The v3 - Identity API from SoilOptix — 2 operation(s) for v3 - identity.
  name: SoilOptix v3 - Identity API
  slug: soiloptix-v3-identity-api
- baseURL: https://api.soiloptix.com
  baseurl_source: declared
  description: The v3 - Sets API from SoilOptix — 6 operation(s) for v3 - sets.
  name: SoilOptix v3 - Sets API
  slug: soiloptix-v3-sets-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/soiloptix/agentic-access/soiloptix-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/soiloptix-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/soiloptix/rules/soiloptix-rules.yml
  title: ''
  type: Spectral
  url: rules/soiloptix-rules.yml
- group: design
  href: https://artifacts.apis.io/soiloptix/json-ld/soiloptix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/soiloptix-context.jsonld
- group: design
  href: https://artifacts.apis.io/soiloptix/vocabulary/soiloptix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/soiloptix-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/soiloptix/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/soiloptix/data-model/soiloptix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/soiloptix-data-model.yml
- group: design
  href: https://artifacts.apis.io/soiloptix/errors/soiloptix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/soiloptix-problem-types.yml
- group: design
  href: https://artifacts.apis.io/soiloptix/conformance/soiloptix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/soiloptix-conformance.yml
- group: other
  href: https://artifacts.apis.io/soiloptix/overlays/soiloptix-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/soiloptix-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/soiloptix/hosts/soiloptix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/soiloptix-hosts.yml
- group: other
  href: https://artifacts.apis.io/soiloptix/vendors/soiloptix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/soiloptix-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://soiloptix.com/terms-of-use/
- group: start
  title: ''
  type: SignUp
  url: https://soiloptix.com/registered/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://soiloptix.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://soiloptix.com/resources/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/soiloptix
- group: auth
  href: https://artifacts.apis.io/soiloptix/security/soiloptix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/soiloptix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://soiloptix.com/
created: '2026-10-28'
description: SoilOptix® has been working for decades on soil analysis, setting the standard for accuracy and precision in soil and field mapping for agriculture. Research began in Europe in 2003 on gamma radiation in agriculture, leading to the founding of Practical Precision Inc. in 2009 and the introduction of SoilOptix® technology to North America in 2010. Today the company provides advanced soil mapping solutions that help growers optimize inputs, improve yields, and promote sustainable farming practices.
image: https://soiloptix.com/wp-content/uploads/2024/04/SO_2024_whitetext_682x202.png
json_schemas:
- name: Analysis
  property_count: 17
  slug: soiloptix-analysis
- name: BusinessCreate
  property_count: 10
  slug: soiloptix-business-create
- name: Business
  property_count: 21
  slug: soiloptix-business
- name: BusinessUpdate
  property_count: 10
  slug: soiloptix-business-update
- name: Farm
  property_count: 10
  slug: soiloptix-farm
- name: Field
  property_count: 12
  slug: soiloptix-field
jsonld:
- class_count: 54
  name: Soiloptix Context
  property_count: 73
  slug: soiloptix-context
layout: provider
modified: '2026-10-28'
name: SoilOptix
nav: Providers
network: true
overview: 'SoilOptix publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analyses - Billable API, Analyses - Read API, Authentication API, and 11 more. Tagged areas include Agriculture, Soil-Analysis, Precision Agriculture, Mapping, and Technology.


  The SoilOptix catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SoilOptix''s developer surface includes signup flow and 17 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: SoilOptix API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: soiloptix-rules
scopes:
- name: Soiloptix Scopes
  scope_count: 0
  slug: soiloptix-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 59.8
    developer_ergonomics: 6.5
    discoverability: 67.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/soiloptix/soiloptix-2026-11-03T143456.png
security:
- kind: authentication
  name: Soiloptix Authentication
  slug: soiloptix-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Soiloptix Domain Security
  slug: soiloptix-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: get-account-info
  slug: soiloptix-get-account-info
slug: soiloptix
tags:
- Agriculture
- Soil-Analysis
- Precision Agriculture
- Mapping
- Technology
website: https://soiloptix.com/
---
