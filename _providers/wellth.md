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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The production GraphQL API behind the Wellth member mobile app and the Wellth internal dashboard. Confirmed live at https://api.wellthapp.com/graphql: the endpoint is an Apollo Server deployment (stac'
  name: Wellth GraphQL API
  slug: graphql
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wellth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wellthapp.com/
- group: company
  title: ''
  type: Blog
  url: https://www.wellthapp.com/resources
- group: operate
  title: ''
  type: Support
  url: https://www.wellthapp.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wellth-app
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wellthapp.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wellthapp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wellthapp.com/privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/wellth_stock/
- group: build
  title: ''
  type: Packages
  url: packages/wellth-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wellth-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.wellthapp.com/privacy-policy
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wellth-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wellth-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wellth-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wellth-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Wellth runs a real production GraphQL API at api.wellthapp.com/graphql — its own status page lists a "Wellth API" component — but Apollo Server introspection is disabled in production (INTROSPECTION_DISABLED), there is no developer portal or reference documentation anywhere on wellthapp.com, and every other path on the API host answers 200 with the plain-text stub "Please use the /graphql route for access to useful data", so no schema, operation list or auth model can be read by any anonymous machine.
  evidence:
  - status: 200
    url: https://api.wellthapp.com/graphql
  - status: 404
    url: https://www.wellthapp.com/openapi.json
  - status: 404
    url: https://www.wellthapp.com/llms.txt
  - status: 200
    url: https://status.wellthapp.com/api/v2/summary.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-08-05'
description: Wellth is a digital health company that applies behavioral economics to care-plan adherence for health plans and providers. Members use the Wellth mobile app to complete daily check-ins — photographing medications, logging blood pressure or glucose readings, confirming appointments and screenings — and earn financial rewards for staying on plan. Wellth sells into Medicare Advantage and D-SNP, Medicaid, ACA marketplace, employer and provider lines of business, and reports reductions in high-cost utilization, emergency department visits and readmissions. The company operates a production GraphQL API at api.wellthapp.com/graphql (Apollo Server, internally versioned apiv4) that backs the member mobile app and its internal dashboard, and publishes an Atlassian status page whose components include "Wellth API". The API is not accompanied by a public developer portal, reference documentation or machine-readable contract, and GraphQL introspection is disabled in production.
image: https://www.wellthapp.com/images/uploads/brand/wellth-social-image.png
layout: provider
modified: '2026-08-05'
name: Wellth
nav: Providers
network: true
overview: 'Wellth publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Digital Health, and Medication Adherence.


  Wellth''s developer surface includes engineering blog, support, and 14 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 20.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Wellth Domain Security
  slug: wellth-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wellth
tags:
- Company
- Health
- Healthcare
- Digital Health
- Medication Adherence
- Behavioral Health
- Health Plans
- Medicare
- Medicaid
- Patient Engagement
- Rewards
- GraphQL
- Mobile
website: https://www.wellthapp.com/
---
