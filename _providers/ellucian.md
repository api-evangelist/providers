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
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.ellucian.com/security
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ellucian/refs/heads/main/hosts/ellucian-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ellucian-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ellucian/refs/heads/main/vendors/ellucian-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ellucian-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.ellucian.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ellucian.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.ellucian.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.ellucian.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ellucian/refs/heads/main/security/ellucian-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ellucian-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ellucian/refs/heads/main/security/ellucian-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ellucian-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ellucian/refs/heads/main/security/ellucian-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ellucian-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ellucian.com
coverage:
  checked: '2026-10-13'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found at the API host api.ellucian.com.
  evidence:
  - status: failed
    url: https://api.ellucian.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Ellucian provides cloud‑based software and services for higher education institutions, delivering comprehensive solutions for student information systems, finance, human resources, and campus analytics. Their platform enables colleges and universities to streamline operations, improve student experiences, and leverage data‑driven insights across the entire campus ecosystem.
image: https://www.ellucian.com/files/2025-09/social-image-ellucian.jpg
layout: provider
modified: '2026-10-12'
name: Ellucian
nav: Providers
network: true
overview: 'Ellucian is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Software, Cloud, HigherEducation, and StudentInformationSystems.


  Ellucian''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ellucian Domain Security
  slug: ellucian-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ellucian Vulnerability Disclosure
  slug: ellucian-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Ellucian Trust Center
  slug: ellucian-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: ellucian
tags:
- Education
- Software
- Cloud
- HigherEducation
- StudentInformationSystems
website: https://www.ellucian.com
---
