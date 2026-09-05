---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 4
apis:
- description: RESTful create, list, get, update, and delete access to Fluxx model records such as GrantRequest, Organization, and RequestTransaction under /api/rest/v2/{model}. Supports column selection (cols), rec
  name: Fluxx Records API
  slug: fluxx-grants-records-api
- description: OAuth 2.0 authorization for the Fluxx REST API. Administrators register an application at /oauth/applications on their instance to obtain a client ID and client secret, then exchange them for an acces
  name: Fluxx OAuth API
  slug: fluxx-grants-oauth-api
- description: Access to files and documents attached to grant records, exposed through Fluxx document models (such as ModelDocument) under /api/rest/v2/{model}. Used to list and retrieve attachments associated with
  name: Fluxx Documents API
  slug: fluxx-grants-documents-api
- description: RESTful access to Fluxx people and organization records - the User and Organization models under /api/rest/v2/{model} that represent grantees, grantseekers, staff, and funding organizations. Endpoints
  name: Fluxx Users and Organizations API
  slug: fluxx-grants-users-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/fluxx-grants-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fluxx-grants-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fluxx-grants-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fluxx
- group: company
  title: ''
  type: Website
  url: https://www.fluxx.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fluxxlabs
- group: docs
  title: ''
  type: Documentation
  url: https://www.fluxx.io/resource-center
created: '2026-07-05'
description: Fluxx is a cloud grants management platform for foundations, government agencies, corporations, and nonprofits, covering the full grant lifecycle from funding announcement through pre-award applications, post-award payments, and measurement and evaluation. Fluxx Grantmaker includes a RESTful API (REST API v2) available to customers for building custom integrations with financial, CRM, and business-intelligence systems. The API is exposed per-client on each customer's own Fluxx instance under https://{client}.fluxx.io/api/rest/v2, is authenticated with OAuth 2.0 credentials created in that instance, and is driven by a dynamic, instance-specific data model whose reference documentation is generated at /api/rest/v2/doc for each deployment. Because the surface is per-instance and gated behind an authenticated customer deployment, the endpoints below are honestly modeled from Fluxx's documented REST v2 conventions rather than pulled from a single public reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fluxx-grants.png
layout: provider
modified: '2026-07-05'
name: Fluxx
nav: Providers
network: true
overview: 'Fluxx publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Grants Management, Grantmaking, Non-Profit, Philanthropy, and Foundations.


  Fluxx''s developer surface includes documentation and 6 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 2
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fluxx-grants/refs/heads/main/screenshots/fluxx-grants-2026-07-25T214848.png
security:
- kind: domain-security
  name: Fluxx Grants Domain Security
  slug: fluxx-grants-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fluxx Grants Vulnerability Disclosure
  slug: fluxx-grants-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Fluxx Grants Trust Center
  slug: fluxx-grants-trust-center
  summary_line: SOC 2, ISO 27001
slug: fluxx-grants
tags:
- Grants Management
- Grantmaking
- Non-Profit
- Philanthropy
- Foundations
- REST API
website: https://www.fluxx.io/
---
