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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.sasgroup.net/contact/vulnerability-disclosure-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sas-scandinavian-airlines/refs/heads/main/well-known/sas-scandinavian-airlines-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sas-scandinavian-airlines-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sas-scandinavian-airlines/refs/heads/main/well-known/sas-scandinavian-airlines-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sas-scandinavian-airlines-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sas-scandinavian-airlines/refs/heads/main/hosts/sas-scandinavian-airlines-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sas-scandinavian-airlines-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sas-scandinavian-airlines/refs/heads/main/vendors/sas-scandinavian-airlines-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sas-scandinavian-airlines-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sas-scandinavian-airlines/refs/heads/main/security/sas-scandinavian-airlines-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sas-scandinavian-airlines-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sas-scandinavian-airlines/refs/heads/main/security/sas-scandinavian-airlines-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sas-scandinavian-airlines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flysas.com/
created: '2026-10-15'
description: Scandinavian Airlines (SAS) is the largest airline in Scandinavia, operating a network of flights across Europe, North America, and Asia. Founded in 1946, SAS provides passenger and cargo services, loyalty programs, and a range of travel solutions. The airline is a member of the Star Alliance and focuses on sustainability, digital innovation, and customer experience.
image: https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f6/SE-RSE%40PEK_%2820220221140316%29.jpg/330px-SE-RSE%40PEK_%2820220221140316%29.jpg
layout: provider
modified: '2026-10-15'
name: SAS
nav: Providers
network: true
overview: SAS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Airlines, Travel, Europe, NorthAmerica, and Asia.
random_paper: 5
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sas Scandinavian Airlines Domain Security
  slug: sas-scandinavian-airlines-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sas Scandinavian Airlines Vulnerability Disclosure
  slug: sas-scandinavian-airlines-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sas-scandinavian-airlines
tags:
- Airlines
- Travel
- Europe
- NorthAmerica
- Asia
- Company
website: https://flysas.com/
---
