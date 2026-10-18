---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Provides access to Cortechs AI medical imaging solutions and related data. Documentation is available at the resources page.
  name: Cortechs AI Solutions API
  slug: cortechs-ai-solutions-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cortechslabs/refs/heads/main/well-known/cortechslabs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cortechslabs-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cortechslabs/refs/heads/main/hosts/cortechslabs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cortechslabs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cortechslabs/refs/heads/main/vendors/cortechslabs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cortechslabs-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cortechs.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cortechs.ai/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://www.cortechs.ai/about/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cortechslabs/refs/heads/main/security/cortechslabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cortechslabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cortechs.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.cortechs.ai/resources/
- group: company
  title: ''
  type: Blog
  url: https://www.cortechs.ai/category/blogs/
- group: operate
  title: ''
  type: Support
  url: https://www.cortechs.ai/customer-support/
- group: operate
  title: ''
  type: Contact
  url: https://www.cortechs.ai/contact/
coverage:
  checked: '2026-10-11'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on any discovered host.
  evidence:
  - status: 404
    url: https://api.cortechs.ai/openapi.json
  - status: 404
    url: https://api.cortechs.ai/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Cortechslabs is a technology-focused company that appears in the API Evangelist harvest backlog as a secondary-market stub. While detailed public information is limited, the company is presumed to develop software solutions and APIs. Further investigation is required to uncover its product offerings, documentation, and API endpoints. This placeholder description will be refined as more evidence becomes available.
image: https://www.cortechs.ai/wp-content/uploads/2024/08/Website-Featured-Image.png
layout: provider
modified: '2026-10-11'
name: Cortechslabs
nav: Providers
network: true
overview: 'Cortechslabs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Medical Imaging, Brain Segmentation, and Healthcare.


  Cortechslabs'' developer surface includes documentation, engineering blog, support, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cortechslabs Domain Security
  slug: cortechslabs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cortechslabs
tags:
- Company
- Artificial Intelligence
- Medical Imaging
- Brain Segmentation
- Healthcare
website: https://www.cortechs.ai
---
