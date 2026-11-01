---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Integration APIs for Singpass Login and MyInfo services as documented in the Singpass Developer Portal.
  name: Singpass API
  slug: singpass-api
artifact_total: 3
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developer.singpass.gov.sg/docs/getting-started/readme
- group: auth
  href: https://artifacts.apis.io/singpass/authentication/singpass-authentication.yml
  title: ''
  type: Authentication
  url: authentication/singpass-authentication.yml
- group: agent
  href: https://artifacts.apis.io/singpass/llms/singpass-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/singpass-llms.txt
- group: agent
  href: https://artifacts.apis.io/singpass/well-known/singpass-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/singpass-well-known.yml
- group: other
  href: https://artifacts.apis.io/singpass/hosts/singpass-hosts.yml
  title: ''
  type: Hosts
  url: hosts/singpass-hosts.yml
- group: other
  href: https://artifacts.apis.io/singpass/vendors/singpass-vendors.yml
  title: ''
  type: Vendors
  url: vendors/singpass-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.singpass.gov.sg/main/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/singpass
- group: auth
  href: https://artifacts.apis.io/singpass/security/singpass-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/singpass-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://singpass.gov.sg/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.singpass.gov.sg
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.singpass.gov.sg
- group: docs
  title: ''
  type: APIReference
  url: https://developer.singpass.gov.sg/docs
- group: operate
  title: ''
  type: Support
  url: https://partnersupport.singpass.gov.sg
- group: company
  title: ''
  type: Blog
  url: https://www.singpass.gov.sg/main/newsroom/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://portal.singpass.gov.sg/home/ui/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://portal.singpass.gov.sg/home/ui/privacy-statement
coverage:
  checked: '2026-10-27'
  detail: The Singpass developer portal provides documentation only in markdown pages without any OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://docs.developer.singpass.gov.sg/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Singpass is Singapore’s national digital identity platform that enables residents to securely access government services, sign documents, and share verified personal data with businesses. It provides authentication, MyInfo data pre-fill, and digital signing capabilities, supporting over 2,700 services across more than 800 agencies, and aims to simplify and secure everyday transactions for citizens and residents.
image: https://www.singpass.gov.sg/main/images/common/400 x 400.webp
layout: provider
modified: '2026-10-27'
name: Singpass
nav: Providers
network: true
overview: 'Singpass is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Authentication, Government, and Singapore.


  Singpass'' developer surface includes getting-started guide, authentication, documentation, API reference, support, engineering blog, and 11 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Singpass Authentication
  slug: singpass-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Singpass Domain Security
  slug: singpass-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: singpass
tags:
- Company
- Identity
- Authentication
- Government
- Singapore
website: https://singpass.gov.sg/
---
