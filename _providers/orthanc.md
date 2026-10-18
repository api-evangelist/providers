---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Orthanc provides a RESTful DICOM API for storing, retrieving and managing medical imaging data.
  name: Orthanc API
  slug: orthanc-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/orthanc/refs/heads/main/conformance/orthanc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/orthanc-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/orthanc/refs/heads/main/hosts/orthanc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orthanc-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/orthanc/refs/heads/main/security/orthanc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orthanc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.orthanc-server.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.orthanc-server.com/static.php?page=documentation
- group: docs
  title: ''
  type: APIReference
  url: https://orthanc.uclouvain.be/api/
- group: company
  title: ''
  type: Blog
  url: https://www.orthanc-server.com/static.php?page=blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orthanc-server.com/static.php?page=privacy
coverage:
  checked: '2026-10-14'
  detail: The provider's documentation links to an OpenAPI spec hosted at dataverse.uclouvain.be, which describes the Dataverse platform, not Orthanc.
  evidence:
  - status: 302
    url: https://opendata.uclouvain.be/openapi
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Orthanc is an open-source, lightweight DICOM server for medical imaging. It provides a RESTful API to store, retrieve, and manage DICOM studies, series, and instances. Orthanc is widely used in hospitals, research labs, and imaging workflows to simplify integration with PACS, viewers, and analysis tools. The platform offers a web interface, extensive documentation, and a vibrant community supporting extensions and plugins.
layout: provider
modified: '2026-10-14'
name: Orthanc
nav: Providers
network: true
overview: 'Orthanc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DICOM, Medical Imaging, Open Source, and REST API.


  Orthanc''s developer surface includes documentation, API reference, engineering blog, and 5 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Orthanc Domain Security
  slug: orthanc-domain-security
  summary_line: TLSv1.3
slug: orthanc
tags:
- Company
- DICOM
- Medical Imaging
- Open Source
- REST API
website: https://www.orthanc-server.com
---
