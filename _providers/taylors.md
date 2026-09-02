---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Taylors Agentic Access
  operation_count: 11
  slug: taylors-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- description: REST API of the Taylor's University Library catalog, served under /api/v1 by a Koha integrated library system that Taylor's self-hosts (librarycatalogue.taylors.edu.my resolves through librarycatalogu
  name: Taylor's Library Koha REST API
  slug: library-rest
- description: OAI-PMH 2.0 data provider exposed by the Koha-powered Taylor's Library catalog for harvesting bibliographic metadata. The Identify response returns repositoryName "Taylor's Library", protocolVersion 2
  name: Taylor's Library OAI-PMH
  slug: library-oai
- description: The Taylor's e-Repository runs DSpace CRIS 2022.01.01 self-hosted at irepo.taylors.edu.my (resolving through irepo.wip.taylors.edu.my to 103.145.155.17 — again Taylor's own infrastructure, no vendor C
  name: Taylor's e-Repository DSpace CRIS REST API
  slug: irepo-rest
- description: OAI-PMH 2.0 data provider for the DSpace CRIS e-Repository, Identifying as repositoryName "Taylor's University Library", repositoryIdentifier irepo.taylors.edu.my, protocolVersion 2.0, earliestDatesta
  name: Taylor's e-Repository OAI-PMH
  slug: irepo-oai
- description: Taylor's operates a Microsoft Entra ID tenant, 0a39ee13-5c27-420c-b0af-8e65c6929055, branded "Taylor's Education Group", as the identity provider behind taylors.edu.my. The realm is NameSpaceType "Man
  name: Taylor's University Identity Federation (Microsoft Entra ID)
  slug: entra-identity-federation
- description: Taylor's University Press is Crossref member 37785, registered at Subang Jaya, Selangor, Malaysia, holding DOI prefix 10.58946 with 70 deposited DOIs. This is a membership fact about the institution —
  name: Taylor's University Crossref Membership
  slug: crossref-membership
- description: Taylor's University is registered in the Research Organization Registry as ror.org/0498pcx51, located Subang Jaya, Malaysia, cross-walked to Crossref Funder ID 501100011915, GRID grid.452879.5, ISNI 0
  name: Taylor's University ROR Registration
  slug: ror-registration
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Taylor's Library Koha REST checkouts API
  slug: open-taylors-checkouts-api
- collection_type: open
  name: Taylor's Library Koha REST checkouts holds API
  slug: open-taylors-holds-api
- collection_type: open
  name: Taylor's Library Koha REST checkouts item_types API
  slug: open-taylors-item-types-api
- collection_type: open
  name: Taylor's Library Koha REST checkouts items API
  slug: open-taylors-items-api
- collection_type: open
  name: Taylor's Library Koha REST checkouts libraries API
  slug: open-taylors-libraries-api
- collection_type: open
  name: Taylor's Library Koha REST checkouts patrons API
  slug: open-taylors-patrons-api
common:
- group: company
  title: ''
  type: Website
  url: https://university.taylors.edu.my/en.html
- group: docs
  title: ''
  type: APIReference
  url: https://librarycatalogue.taylors.edu.my/api/v1/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://librarycatalogue.taylors.edu.my/
- group: other
  title: ''
  type: ResearchRepository
  url: https://irepo.taylors.edu.my/
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.microsoftonline.com/taylors.edu.my/v2.0/.well-known/openid-configuration
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://university.taylors.edu.my/en/privacy-policy.html
- group: operate
  title: ''
  type: Support
  url: https://university.taylors.edu.my/en/get-in-touch/contact-information.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Taylors-University
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/taylor's-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/taylors-conformance.yml
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/taylors-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/taylors-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taylors-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/taylors-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/taylors-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/taylors-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/taylors-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/taylors-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Taylor''s University is a private research university in Subang Jaya, Selangor, Malaysia, ranked #251 in the QS World University Rankings 2025. It operates no developer portal, no public API programme and no public code: the Taylors-University GitHub organisation has existed since 2020 and still holds zero public repositories. What it does operate, on its own infrastructure under taylors.edu.my, are four live machine-readable surfaces — a self-hosted Koha library system exposing a REST API at /api/v1 and an OAI-PMH 2.0 data provider, and a self-hosted DSpace CRIS e-Repository exposing a HAL+JSON REST API at /server/api and a second OAI-PMH 2.0 provider. Both REST contracts are the upstream products'' own documents (Koha Development Team; DSpace CRIS 2022.01.01) running on Taylor''s servers: the deployment, the data and the DOIs are the institution''s, the contract is not. Identity runs through a Microsoft Entra ID tenant whose SAML 2.0 and OpenID Connect metadata are publicly
  retrievable, and the institution is registered with ROR and holds a Crossref membership through Taylor''s University Press. No open data portal, no course-catalog or timetable API, and no institution-operated developer documentation were found.'
examples:
- key_count: 16
  name: Taylors Getcheckout Example
  slug: taylors-getCheckout-example
- key_count: 24
  name: Taylors Getitem Example
  slug: taylors-getItem-example
- key_count: 23
  name: Taylors Getpatron Example
  slug: taylors-getPatron-example
finops:
- name: Taylors Finops
  service_category: Education
  slug: taylors-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/taylors.png
json_schemas:
- name: Koha Checkout
  property_count: 16
  slug: taylors-checkout
- name: Koha Hold
  property_count: 20
  slug: taylors-hold
- name: Koha Item
  property_count: 24
  slug: taylors-item
- name: Koha Patron
  property_count: 23
  slug: taylors-patron
json_structures:
- name: Taylors Item Structure
  property_count: 20
  slug: taylors-item-structure
- name: Taylors Patron Structure
  property_count: 18
  slug: taylors-patron-structure
jsonld:
- class_count: 6
  name: Taylors Context
  property_count: 6
  slug: taylors-context
layout: provider
modified: '2026-09-01'
name: Taylor's University
nav: Providers
network: true
overview: 'Taylor''s University publishes 1 API on the [APIs.io](https://apis.io/) network: Taylor''s Library Koha REST API. Tagged areas include Education, Higher Education, University, Private University, and Malaysia.


  The Taylor''s University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Taylor''s University''s developer surface includes API reference, support, GitHub presence, authentication, and 15 more developer resources.'
plans:
- name: Taylors Plans Pricing
  plan_count: 2
  slug: taylors-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Taylors Rate Limits
  slug: taylors-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Taylor's University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: taylors-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: Taylor's University API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 4
  slug: taylors-rules
scopes:
- name: Taylors Scopes
  scope_count: 0
  slug: taylors-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 32.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 8.6
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 25.0
    contract_quality: 66.0
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/taylors/refs/heads/main/screenshots/taylors-2026-06-20T194940.png
security:
- kind: authentication
  name: Taylors Authentication
  slug: taylors-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Taylors Domain Security
  slug: taylors-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: taylors
tags:
- Education
- Higher Education
- University
- Private University
- Malaysia
- Asia
- Library
- Library Catalog
- Institutional Repository
- Research Data
- OAI-PMH
- Identity Federation
- Koha
- DSpace
website: https://university.taylors.edu.my/en.html
---
