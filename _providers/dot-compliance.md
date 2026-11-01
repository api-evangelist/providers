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
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Dot Compliance, as described on the company website.
  name: Dot Compliance API
  slug: dot-compliance-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dot-compliance/llms/dot-compliance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dot-compliance-llms.txt
- group: other
  href: https://artifacts.apis.io/dot-compliance/hosts/dot-compliance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dot-compliance-hosts.yml
- group: other
  href: https://artifacts.apis.io/dot-compliance/vendors/dot-compliance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dot-compliance-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dotcompliance.com/terms-conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.dotcompliance.com/help-center/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dotcompliance.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.dotcompliance.com/blog/
- group: auth
  href: https://artifacts.apis.io/dot-compliance/security/dot-compliance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dot-compliance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dotcompliance.com/
coverage:
  checked: '2026-10-24'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's documented hosts.
  evidence:
  - status: error
    url: https://api.dotcompliance.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: Dot Compliance provides an AI‑powered electronic quality management system (eQMS) built on the Salesforce platform for life sciences organizations. The solution includes modules for document control, CAPA, training, audit, supplier quality, risk and equipment management, and supports regulatory standards such as 21 CFR Part 11, ISO 9001 and ISO 13485.
image: https://www.dotcompliance.com/wp-content/uploads/2025/03/Group-607-1024x691.png
layout: provider
modified: '2026-10-24'
name: Dot Compliance
nav: Providers
network: true
overview: 'Dot Compliance is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include eQMS, Quality Management, Life Sciences, Pharmaceutical, and Biotechnology.


  Dot Compliance''s developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.2
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
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dot Compliance Domain Security
  slug: dot-compliance-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dot-compliance
tags:
- eQMS
- Quality Management
- Life Sciences
- Pharmaceutical
- Biotechnology
- Medical Device
- Compliance
- Salesforce
website: https://www.dotcompliance.com/
---
